# Pierway — MVP Spec
**Version 2.0 · March 2026 · Supersedes v1.0**

---

## What This Is

The Pierway MVP is the complete working product — not a cruise-season demo, not a prototype. It covers the full lifecycle:

1. A passenger walks a personalized AI route with map and voice narration
2. A merchant's QR code is scanned, creating a verified visit record
3. Ray invoices the merchant and gets paid

The MVP is pilot-ready. It can onboard a real merchant, record real visits, and generate a real invoice. The cruise season is one distribution channel — not the scope boundary.

**Pilot target:** Any walkable tourist corridor in Seattle. Hotels and waterfront merchants are the first cohort. Cruise passengers are the first high-volume moment.

---

## The Three Systems

| System | MVP Scope |
|---|---|
| Consumer App | Route gen, Mapbox map, voice narration, geolocation check-in, merchant QR scan |
| Verified Visit Engine | QR validation, visit record, confidence scoring |
| Back Office | Merchant onboarding, merchant dashboard, Ray's admin, Stripe billing |

See [technical-architecture.md](./technical-architecture.md) for full design.

---

## Consumer App — User Flow

### Screen 1 — Landing
```
┌─────────────────────────────────┐
│  [Pierway logo]                 │
│                                 │
│  Your next few hours            │
│  in Seattle, figured out.       │
│                                 │
│  A free walking route built     │
│  around your time and           │
│  interests. No app required.    │
│                                 │
│  [  Plan My Walk  ]  ← CTA     │
└─────────────────────────────────┘
```

### Screen 2 — Preferences
```
┌─────────────────────────────────┐
│  How much time do you have?     │
│                                 │
│  [2 hrs] [3 hrs] [4 hrs] [5+]  │
│                                 │
│  What sounds good today?        │
│  (pick any)                     │
│                                 │
│  [🏛 History]  [🍽 Food]        │
│  [🌊 Waterfront] [🛍 Shopping]  │
│  [🎨 Arts]  [☕ Coffee & Cafes] │
│                                 │
│  Starting from:                 │
│  [Pier 91] [Pier 66] [Downtown] │
│                                 │
│  [  Build My Route  ]           │
└─────────────────────────────────┘
```

No free-text input. No account. No friction.

### Screen 3 — Generating
3–5 second Claude API call. Animated feedback:
```
✓ Time: 3 hours
✓ Interests: History, Food
✓ Start: Pier 91
⟳ Building your route...
```

### Screen 4 — Route Map
**Primary view: the Mapbox map.**
```
┌─────────────────────────────────┐
│  Your Seattle Route             │
│  3 hrs · 4 stops · ~1.8 miles  │
│                                 │
│  [MAP — full width]             │
│  numbered markers on route      │
│  polyline connecting stops      │
│  your position dot              │
│                                 │
│  ┌─────────────────────────┐   │
│  │ STOP 1 — Pike Place     │   │
│  │ 0.3 mi · 45 min         │   │
│  │ [tap to expand]     →   │   │
│  └─────────────────────────┘   │
│  [STOP 2] [STOP 3] [RETURN]    │
└─────────────────────────────────┘
```

Stops are swipeable cards below the map. Tapping a card opens Stop Detail and centers map on that stop.

### Screen 5 — Stop Detail
```
┌─────────────────────────────────┐
│  ← Route     Stop 1 of 4       │
│                                 │
│  Pike Place Market              │
│  ★ 0.3 miles from pier         │
│  ⏱ Suggest 45 minutes here     │
│                                 │
│  [▶ Listen]                     │
│                                 │
│  Seattle's oldest public market │
│  has operated continuously      │
│  since 1907...                  │
│                                 │
│  The original farmers' stalls   │
│  are on the lower level — most  │
│  visitors never find them.      │
│                                 │
│  [  I'm Here  ]  ← check-in   │
│  [ Next Stop → ]               │
└─────────────────────────────────┘
```

**[▶ Listen]** triggers Web Speech API narration of the narrative + insider tip.

### Screen 6 — Merchant Stop Detail
Same as Screen 5, with an added merchant layer:
```
│  ──────────────────────────────  │
│  🏷 Pierway Offer               │
│  Show this screen for 10% off  │
│                                 │
│  [  Scan to Check In  ]        │
│  (scans merchant QR code)      │
```

**[Scan to Check In]** opens the device camera to scan the merchant's QR code. This is the verified visit trigger.

### Screen 7 — Visit Confirmed
```
┌─────────────────────────────────┐
│                                 │
│         ✓                       │
│                                 │
│  Checked in at                  │
│  Café Bengodi                   │
│  12:34 PM                       │
│                                 │
│  Enjoy your visit.              │
│                                 │
│  [ Continue Route → ]          │
└─────────────────────────────────┘
```

---

## Voice Narration

- Engine: Web Speech API (`window.speechSynthesis`) — browser native, zero cost
- Triggered on: stop detail open (auto) OR play button tap (manual)
- Content: stop name → narrative → insider tip
- UI: play/pause button, visual waveform or simple progress bar
- Fallback: if browser doesn't support speechSynthesis, hide the button gracefully
- Upgrade path: ElevenLabs custom voice after revenue validation

---

## Merchant QR Scan — Verified Visit

1. Passenger taps "Scan to Check In" on a merchant stop card
2. Browser camera opens (via `<input type="file" accept="image/*" capture="environment">` or jsQR library)
3. QR code decoded: `https://pierway.io/visit?m=MERCHANT_ID&t=TOKEN`
4. Edge Function validates the HMAC token (prevents spoofing)
5. If valid: creates visit record in `visits` table with `method = 'qr_scan'`
6. Returns confirmation → Screen 7 displayed
7. Merchant sees the visit appear in their dashboard within seconds

---

## Merchant Back Office

### Onboarding (pierway.io/merchants)
Self-serve, 5 minutes:
1. Business name, type, address
2. Accept CPV terms
3. Stripe Connect (bank account for billing)
4. Download QR code PDF

### Merchant Dashboard (pierway.io/dashboard)
- Visits this month (count + daily chart)
- This month's bill (running total)
- Download QR code

### Ray's Admin (pierway.io/admin)
- All merchants table (name, active, visits this month, revenue)
- Visits log
- Invoice history
- Trigger billing run manually (before cron is set up)

---

## Billing

- CPV rates: $3–6 per visit depending on merchant category
- Merchant sets daily cap (default: 20 visits/day)
- Monthly invoicing via Stripe
- Stripe Checkout or hosted invoice page handles payment
- Ray gets notified on payment

---

## Technical Decisions — Locked

| Decision | Choice |
|---|---|
| Frontend | React + Vite |
| Styling | Tailwind CSS |
| Maps | Mapbox GL JS |
| Voice | Web Speech API (browser native) |
| AI | Claude API (`claude-sonnet-4-6`) |
| Backend | Supabase (Postgres + Edge Functions) |
| Payments | Stripe + Stripe Connect |
| Hosting | Vercel |

---

## Phase 1.5 Features (After End-to-End Works)

These are confirmed additions — deferred until the preset-based flow is validated end-to-end.

| Feature | Description | Why Deferred |
|---|---|---|
| **Custom theme input** | Free-text or voice field on Preferences: "haunted buildings," "street art," "best views" — fed directly into the Claude prompt | Need to validate baseline Claude output quality on preset inputs first before opening to arbitrary free-form |
| **Voice input (SpeechRecognition)** | Mic button on the custom theme field — Web Speech API, browser native, zero cost | Dependent on custom theme field; Safari support inconsistency needs testing |
| **GPS starting point** | "Use My Location" option on Preferences — calls `navigator.geolocation`, passes actual lat/lng to Claude. Unlocks testing from anywhere in Seattle and non-pier distribution (hotels, waterfront merchants) | Deferred until preset flow is validated end-to-end |

---

## What Is Still Out of Scope

- Native app / app store
- Multiple cities (Seattle only in MVP)
- Real-time animated position tracking (battery drain)
- Review or rating system
- User accounts for passengers (anonymous by design)
- Push notifications
- Analytics beyond visit counts

---

## Build Sequence

| Phase | Weeks | Gate |
|---|---|---|
| Consumer App (no merchants) | 1–3 | Partner demo: scan → route → map → voice |
| Verified Visit Engine | 4 | First QR scan records a visit in DB |
| Back Office | 5–6 | First merchant invoiced via Stripe |
| Pilot | 7 | First real merchant, first real walk, first real invoice |

---

## Accounts to Set Up Before Build Starts

| Service | Why | Cost |
|---|---|---|
| Supabase | Database + backend | Free tier sufficient |
| Mapbox | Map tiles + routing | Free tier (50K loads/mo) |
| Stripe | Payment processing | No monthly fee, 2.9% + 30¢ per transaction |
| Vercel | Frontend hosting | Free tier sufficient |
| Anthropic API | Route generation | Pay-per-use (claude-sonnet-4-6) |
| GitHub | Code repo | Free |

Total monthly cost before revenue: ~$0 (all free tiers).

---

*Spec owner: Ray Castro · Replaces v1.0 (cruise-season scope)*
*Architecture detail: see [technical-architecture.md](./technical-architecture.md)*
