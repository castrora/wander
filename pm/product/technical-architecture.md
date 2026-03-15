# Pierway — Technical Architecture
**Version 1.0 · March 2026**

---

## Overview

Pierway is three systems that work together:

| System | What It Does | Who Uses It |
|---|---|---|
| **Consumer App** | Route generation, map, navigation, voice narration | Passengers / walkers |
| **Verified Visit Engine** | Merchant QR scan → timestamped visit record → billable event | Passengers at merchant location |
| **Back Office** | Merchant onboarding, visit log, invoicing, Stripe billing, Ray's dashboard | Ray + enrolled merchants |

These systems share a single backend and database. They are not three separate products — they are three surfaces of one product.

---

## Stack Decision

### Why This Stack

Built for a solo founder building with AI assistance. Priorities: fast to ship, easy to reason about, minimal infrastructure, no ops burden.

| Layer | Choice | Why |
|---|---|---|
| Frontend | **React + Vite** | Component-based, fast dev server, large ecosystem, AI tooling works well with it |
| Styling | **Tailwind CSS** | Utility-first, no design system overhead, mobile-first by default |
| Maps | **Mapbox GL JS** | Best mobile performance, offline tile support, route drawing, free tier sufficient for MVP |
| Voice | **Web Speech API** (browser native) | Zero cost, no API key, works offline after page load. Upgrade to ElevenLabs v2 after validation |
| AI (routes) | **Claude API** (`claude-sonnet-4-6`) | Route generation + narrative content |
| Backend | **Supabase** | Postgres database + REST/realtime API + auth + storage, all in one. No separate server to manage |
| Serverless functions | **Supabase Edge Functions** (Deno) | Runs close to Supabase DB, holds API keys securely, handles Claude API calls |
| Payments | **Stripe** | Industry standard, handles invoicing and recurring billing |
| Hosting | **Vercel** | Free tier for frontend, automatic HTTPS, GitHub deploy integration |
| Domain | **pierway.io** | Already selected |

### What We're Not Using (and Why)

| Skipped | Reason |
|---|---|
| Next.js | Server-side rendering not needed for this product in v1 |
| Firebase | Vendor lock-in, pricing surprises at scale |
| Custom backend (Node/Express) | Supabase replaces it — less to manage |
| Google Maps | Mapbox is better for custom route rendering and offline |
| ElevenLabs (v1) | $0.30/min adds up fast before revenue. Browser TTS is good enough to validate the concept |
| React Native / Expo | Web-first is correct for scan-from-QR-code use case. No install friction. |

---

## System 1: Consumer App

### What It Delivers

A mobile-web experience that:
1. Accepts time + interest preferences (no account required)
2. Generates a personalized walking route via Claude API
3. Displays the route on a Mapbox map with sequential waymarkers
4. Reads stop narratives aloud via voice narration
5. Accepts merchant QR scans to record verified visits

### Screen Flow

```
QR Code Scan
     ↓
Landing (pierway.io)
     ↓
Preferences (time / interests / starting point)
     ↓
Generating... (Claude API call, 3–5 sec)
     ↓
Route Map — all stops visible, Mapbox
     ↓
Stop Detail — narrative + voice + "I'm Here" + merchant QR
     ↓
Verified Visit Confirmation (if at merchant stop)
     ↓
Next Stop →
```

### Route Generation (Claude API Call)

One structured API call per route request. Inputs:
- `starting_point`: "Pier 91" | "Pier 66" | "Hotel X" | lat/lng
- `available_time`: 2 | 3 | 4 | 5+ hours
- `interests`: array of tags (History, Food, Waterfront, Shopping, Arts, Coffee)
- `current_date`: for seasonal context
- `city`: "Seattle" (expandable)

Output — strict JSON:
```json
{
  "route_id": "uuid",
  "route_title": "A Waterfront Morning",
  "total_time": "3 hours",
  "total_distance": "1.8 miles",
  "return_note": "Back at Pier 91 by 3:00 PM",
  "stops": [
    {
      "order": 1,
      "name": "Pike Place Market",
      "type": "landmark",
      "distance_from_prev": "0.3 mi from pier",
      "walk_time_from_prev": "6 min",
      "suggested_time": "45 minutes",
      "narrative": "...",
      "insider_tip": "The original farmers' stalls are on the lower level — most visitors never find them.",
      "merchant_hook": null,
      "lat": 47.6085,
      "lng": -122.3402,
      "merchant_id": null
    },
    {
      "order": 2,
      "name": "Café Bengodi",
      "type": "merchant",
      "distance_from_prev": "0.2 mi",
      "walk_time_from_prev": "4 min",
      "suggested_time": "20 minutes",
      "narrative": "...",
      "insider_tip": "Ask for the cortado — it's not on the menu.",
      "merchant_hook": "Show your Pierway route for 10% off",
      "lat": 47.6099,
      "lng": -122.3415,
      "merchant_id": "merchant_abc123"
    }
  ]
}
```

**Stop types:**
- `landmark` — public attraction, no merchant billing
- `merchant` — enrolled merchant, CPV billable on verified visit

### Map Implementation

- Mapbox GL JS renders the route
- Polyline drawn between stops in sequence
- Custom markers: numbered circles (navy fill, teal border)
- Active stop marker enlarges when passenger is at/near location
- Route is cached in `localStorage` after generation — works offline after first load
- Geolocation updates position dot continuously (battery-friendly interval: every 15 sec)

### Voice Narration

- Web Speech API (`speechSynthesis`) — zero cost, browser native
- Triggered automatically when stop detail opens, or manually via play button
- Reads: stop name + narrative + insider tip
- UI: play/pause button, progress bar
- Upgrade path: ElevenLabs API for a custom "Pierway guide" voice after revenue validation

---

## System 2: Verified Visit Engine

### The Core Loop

```
Passenger arrives at merchant location
     ↓
Taps "I'm Here" on stop card
     ↓
Two-track verification:
  Track A: Geolocation check (~150m radius)
  Track B: Scan merchant QR code (optional — stronger signal)
     ↓
Backend records: merchant_id, route_id, passenger_session_id,
                 timestamp, lat/lng, verification_method
     ↓
Billable event created in visits table
     ↓
Merchant sees visit in their dashboard (near-realtime)
```

### Merchant QR Code

Each enrolled merchant gets a unique QR code that encodes:
```
https://pierway.io/visit?m=merchant_abc123&t=TOKEN
```

- Token is a short-lived HMAC (prevents spoofing)
- Passenger scans → backend validates token → records visit
- Merchant places QR at point of entry (counter, door, sign)

This is the **higher-confidence verification** signal. Geolocation alone has ~10–15m accuracy in dense urban environments and can be fooled. QR scan requires physical presence.

### Visit Record Schema

```sql
CREATE TABLE visits (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  merchant_id   UUID REFERENCES merchants(id),
  route_id      TEXT,
  session_id    TEXT,               -- anonymous passenger session
  stop_order    INTEGER,
  verified_at   TIMESTAMPTZ DEFAULT now(),
  lat           DECIMAL(9,6),
  lng           DECIMAL(9,6),
  accuracy_m    INTEGER,            -- geolocation accuracy in meters
  method        TEXT,               -- 'geolocation' | 'qr_scan' | 'both'
  billed        BOOLEAN DEFAULT false,
  bill_amount   DECIMAL(10,2),
  invoice_id    UUID REFERENCES invoices(id)
);
```

### Verification Logic

```
IF method = 'qr_scan'
  → High confidence. Record as verified visit. Bill.

ELSE IF method = 'geolocation' AND accuracy_m < 200
  → Medium confidence. Record as verified visit. Bill.

ELSE IF method = 'geolocation' AND accuracy_m >= 200
  → Low confidence. Record as attempted. Do not bill.
  → Show passenger: "Looks like you're not quite there yet — keep walking!"
```

---

## System 3: Back Office

### Merchant Onboarding

Self-serve flow at `pierway.io/merchants`:
1. Name, business type, address
2. Accept CPV pricing terms
3. Stripe Connect onboarding (bank account for billing)
4. Download QR code
5. Set daily visit cap (e.g., max 20 billed visits/day)

### Merchant Dashboard

What merchants see at `pierway.io/dashboard`:
- Visits this month (total + chart by day)
- Pending invoice / next billing date
- Route appearances (how many generated routes included their stop)
- Simple conversion data: appearances → visits
- QR code download / reprint

### Ray's Admin Dashboard

What Ray sees at `pierway.io/admin`:
- All merchants (active / inactive / onboarding)
- Visits log (all verified visits, raw)
- Monthly recurring revenue (MRR)
- Invoices (pending / paid / failed)
- Route generation logs (what's being generated, common patterns)

### Billing Cycle

- Visits accumulate throughout the month
- On the 1st of each month, Edge Function runs:
  1. Aggregates unbilled visits per merchant
  2. Creates invoice record in DB
  3. Stripe creates and sends invoice via email
  4. Merchant pays via Stripe-hosted invoice page
  5. On payment: marks visits as `billed = true`, updates merchant account

### CPV Pricing

| Merchant Type | CPV Rate |
|---|---|
| Food & Coffee | $4 |
| Retail / Shopping | $5 |
| Arts / Attractions | $3 |
| Hotels (referrals) | $6 |

Ray can override per-merchant in admin.

---

## Database Schema (Supabase / Postgres)

```sql
-- Merchants
CREATE TABLE merchants (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name            TEXT NOT NULL,
  category        TEXT,              -- 'food' | 'retail' | 'arts' | 'hotel'
  address         TEXT,
  lat             DECIMAL(9,6),
  lng             DECIMAL(9,6),
  cpv_rate        DECIMAL(6,2) DEFAULT 4.00,
  daily_cap       INTEGER DEFAULT 20,
  stripe_customer_id TEXT,
  qr_token        TEXT UNIQUE,
  active          BOOLEAN DEFAULT true,
  onboarded_at    TIMESTAMPTZ DEFAULT now()
);

-- Visits (see System 2 above)
CREATE TABLE visits ( ... );

-- Invoices
CREATE TABLE invoices (
  id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  merchant_id     UUID REFERENCES merchants(id),
  period_start    DATE,
  period_end      DATE,
  visit_count     INTEGER,
  total_amount    DECIMAL(10,2),
  stripe_invoice_id TEXT,
  status          TEXT DEFAULT 'pending',  -- 'pending' | 'sent' | 'paid' | 'failed'
  created_at      TIMESTAMPTZ DEFAULT now(),
  paid_at         TIMESTAMPTZ
);

-- Route sessions (anonymous, no PII)
CREATE TABLE route_sessions (
  id              TEXT PRIMARY KEY,   -- client-generated UUID stored in localStorage
  starting_point  TEXT,
  available_time  INTEGER,            -- hours
  interests       TEXT[],
  generated_at    TIMESTAMPTZ DEFAULT now(),
  stop_count      INTEGER,
  city            TEXT DEFAULT 'seattle'
);
```

**No user accounts.** Passengers are anonymous. `session_id` is generated client-side and stored in `localStorage`.

---

## Edge Functions (Supabase)

| Function | Trigger | Does |
|---|---|---|
| `generate-route` | POST from consumer app | Calls Claude API, returns route JSON, logs to route_sessions |
| `record-visit` | POST on "I'm Here" tap or QR scan | Validates, creates visit record |
| `validate-qr` | GET on QR scan URL | Validates HMAC token, redirects to app |
| `run-billing` | Cron: 1st of month | Aggregates visits, creates invoices, triggers Stripe |
| `merchant-dashboard-data` | GET from merchant dashboard | Returns visit summary for authenticated merchant |

---

## Repository Structure

```
pierway/
├── src/
│   ├── app/               # Consumer app (React)
│   │   ├── Landing.jsx
│   │   ├── Preferences.jsx
│   │   ├── Generating.jsx
│   │   ├── RouteMap.jsx
│   │   ├── StopDetail.jsx
│   │   └── VisitConfirm.jsx
│   ├── merchant/          # Merchant portal (React)
│   │   ├── Onboarding.jsx
│   │   └── Dashboard.jsx
│   ├── admin/             # Ray's admin (React)
│   │   └── AdminDashboard.jsx
│   ├── components/        # Shared UI components
│   └── lib/               # API clients, utilities
│       ├── claude.js       # Route generation client
│       ├── supabase.js     # Supabase client
│       └── geolocation.js  # Location utilities
├── supabase/
│   ├── functions/         # Edge functions
│   │   ├── generate-route/
│   │   ├── record-visit/
│   │   ├── validate-qr/
│   │   └── run-billing/
│   └── migrations/        # SQL schema migrations
├── public/
│   └── logo.svg
├── index.html
└── vite.config.js
```

---

## Build Sequence

### Phase 1 — Consumer App (Weeks 1–3)
Goal: passenger can scan, get a route, see it on a map, hear narration

| Week | Deliverable |
|---|---|
| 1 | React app scaffolded (Vite), Tailwind configured, Landing + Preferences screens, brand tokens |
| 2 | Claude API integration via Supabase Edge Function — route generation works end-to-end |
| 3 | Mapbox map with waymarkers, Stop Detail with voice narration, geolocation check-in |

**Partner demo possible after Week 3.**

### Phase 2 — Verified Visit Engine (Week 4)
Goal: merchant QR scan creates a verified visit record in the database

| Week | Deliverable |
|---|---|
| 4 | Supabase DB setup, Edge Function for visit recording, QR code generation for test merchant, visit confirmation UI |

### Phase 3 — Back Office (Weeks 5–6)
Goal: Ray can see visits, generate invoices, get paid

| Week | Deliverable |
|---|---|
| 5 | Merchant onboarding flow, simple merchant dashboard, Stripe Connect setup |
| 6 | Ray's admin dashboard, billing Edge Function, invoice generation + Stripe invoices |

### Phase 4 — Pilot Prep (Week 7)
Goal: first real merchant enrolled, first real walk tested

| Week | Deliverable |
|---|---|
| 7 | End-to-end test with a real merchant, QR placed, walk performed, visit recorded and billed |

---

## Open Questions (Decision Required)

1. **Offline support:** After route generation, cache stop data and map tiles in `localStorage` + Service Worker? Recommended yes — passengers lose signal mid-walk.

2. **Mapbox tier:** Free tier = 50,000 map loads/month. More than enough for MVP. Switch to paid at scale. No decision needed now.

3. **Merchant QR placement:** Physical printed QR or digital (displayed on screen)? Physical is more reliable. Ray sources and delivers for first cohort.

4. **Admin auth:** Supabase Auth with email magic link for Ray's admin. Merchant dashboard uses Supabase Auth too. No passwords.

5. **Route quality:** Before pilot launch, manually review the top 20 most common route combinations (pier + time + interests). Human approval before going live.

---

*Spec owner: Ray Castro · Architecture v1.0*
*Dependencies: pierway.io domain purchase, Supabase account, Mapbox account, Stripe account*
