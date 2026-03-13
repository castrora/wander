# Pierway — Passenger-Facing MVP Spec
**Version 1.0 · March 2026 · Closes A-002**

---

## What This Is

The passenger-facing MVP is the web experience a cruise passenger lands on after scanning a Pierway QR code. It must work in a mobile browser, require no app download, no account, and deliver a useful walking route in under 60 seconds.

**Success condition:** A passenger scans at Pier 91, answers two questions, and walks out of the terminal with a personalized route they actually follow.

**Partner demo condition:** When a partner asks "can I see what a passenger experiences?" — we open this on our phone and show them.

---

## What the MVP Does (and Does Not Do)

### In scope for v1
- Mobile web experience (responsive, browser-native, no install)
- Time + interest input → AI-generated walking route
- Route displayed as sequential stops with narrative content at each
- Loop structure — returns passenger to pier before their deadline
- "I'm here" check-in at each stop (geolocation, browser-native)
- Works from Pier 66 and Pier 91 starting points

### Explicitly out of scope for v1
- Merchant recommendations (requires merchant sign-ups — Phase 2)
- Payment processing / CPV billing (no merchants yet)
- User accounts or profiles
- Push notifications
- Native app / app store
- Multiple cities (Seattle only)
- Real-time map with animated position
- Backend database (no persistence required in v1)

---

## User Flow

### Screen 1 — Landing
**What the passenger sees when they scan the QR code.**

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

**Key message:** Free. No download. Personal.

---

### Screen 2 — Preferences
**Two questions. No more.**

```
┌─────────────────────────────────┐
│  ← Back     Your Route          │
│                                 │
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
│  [Pier 91]  [Pier 66]           │
│                                 │
│  [  Build My Route  ]           │
└─────────────────────────────────┘
```

**Design principle:** Fast, friendly, zero friction. No free-text input. Selections should feel like a preference, not a form.

---

### Screen 3 — Generating
**Show motion. This is the "magic moment."**

```
┌─────────────────────────────────┐
│                                 │
│      [Pierway logo mark]        │
│      [animated pulse]           │
│                                 │
│  Building your route...         │
│                                 │
│  ✓ Time: 3 hours                │
│  ✓ Interests: History, Food     │
│  ✓ Start: Pier 91               │
│  ⟳ Generating route...          │
│                                 │
└─────────────────────────────────┘
```

Target: 3–5 seconds. This is the Claude API call.

---

### Screen 4 — Route Overview
**The output. This screen has to earn trust immediately.**

```
┌─────────────────────────────────┐
│  Your Seattle Route             │
│  3 hrs · 4 stops · ~1.8 miles  │
│  Back at Pier 91 by 3:00 PM    │
│                                 │
│  ┌──────────────────────────┐  │
│  │ STOP 1 · 0.3 mi          │  │
│  │ Pike Place Market        │  │
│  │ "Seattle's oldest public │  │
│  │ market has been here     │  │
│  │ since 1907..."           │  │
│  │           [I'm Here →]   │  │
│  └──────────────────────────┘  │
│                                 │
│  ┌──────────────────────────┐  │
│  │ STOP 2 · 0.4 mi          │  │
│  │ Seattle Art Museum ...   │  │
│  └──────────────────────────┘  │
│                                 │
│  ┌──────────────────────────┐  │
│  │ STOP 3 · ...             │  │
│  └──────────────────────────┘  │
│                                 │
│  ┌──────────────────────────┐  │
│  │ RETURN · back to pier    │  │
│  └──────────────────────────┘  │
└─────────────────────────────────┘
```

Each stop card expands to show full narrative when tapped.

---

### Screen 5 — Stop Detail (expanded stop card)
**The narrative experience. This is the product.**

```
┌─────────────────────────────────┐
│  ← Route     Stop 1 of 4       │
│                                 │
│  Pike Place Market              │
│  ★ 0.3 miles from pier         │
│  ⏱ Suggest 45 minutes here     │
│                                 │
│  Seattle's oldest public market │
│  has operated continuously      │
│  since 1907. What started as a  │
│  farmers' market to cut out     │
│  middlemen has become the       │
│  beating heart of the city...   │
│                                 │
│  Look for the original farmer   │
│  stalls on the lower level —    │
│  most tourists never find them. │
│                                 │
│  [  I'm Here  ]  ← check-in   │
│                                 │
│  [ Next Stop → ]               │
└─────────────────────────────────┘
```

**The narrative is the differentiator.** Not directions. Not star ratings. A story that makes the passenger feel like they're getting insider knowledge.

---

## What Happens When "I'm Here" Is Tapped

v1 behavior:
1. Browser requests geolocation permission
2. If within ~150m of stop: confirms with a visual "✓ Checked in" and timestamps
3. If not within range: shows message "Looks like you're not quite there yet — keep walking!"
4. This data is logged for later (even if not yet monetized)

This is the foundation of the verified-visit infrastructure. No merchant billing yet — just proving we can confirm physical presence at a location.

---

## AI Prompt Design (the Claude call)

The route is generated by a single structured call to Claude. Input:
- Starting pier (Pier 91 / Pier 66)
- Available time (2h / 3h / 4h / 5h+)
- Interest tags (History, Food, Waterfront, Shopping, Arts, Coffee)

Output format (JSON):
```json
{
  "route_title": "A Waterfront Morning",
  "total_time": "3 hours",
  "total_distance": "1.8 miles",
  "return_note": "Back at Pier 91 by 3:00 PM",
  "stops": [
    {
      "order": 1,
      "name": "Pike Place Market",
      "distance_from_prev": "0.3 mi from pier",
      "suggested_time": "45 minutes",
      "narrative": "...",
      "lat": 47.6085,
      "lng": -122.3402
    }
  ]
}
```

**Prompt principles:**
- Narrative voice: local, specific, story-first — not Wikipedia
- Loop logic: routes must end near the starting pier
- Time honesty: don't overpromise how much fits in 2 hours
- Merchant layer hook: each stop should have a natural "while you're here" moment (ready for when merchants are enrolled)

---

## Technical Architecture (v1)

| Layer | Choice | Rationale |
|---|---|---|
| Frontend | Vanilla HTML/CSS/JS or React | No framework overhead needed for v1 |
| AI | Claude API (claude-sonnet-4-6) | Route generation + narrative |
| Backend | Single serverless function (Vercel/Netlify) | Just to hold the API key securely |
| Geolocation | Browser native (`navigator.geolocation`) | No maps SDK needed |
| Database | None in v1 | Log check-ins to a simple JSON endpoint or Airtable |
| Hosting | Vercel or GitHub Pages + serverless | Free tier sufficient |
| Domain | pierway.io | Once purchased |

**No auth. No database. No native app.** The entire product is a mobile web page that calls Claude and displays structured output.

---

## The Minimum Bar for a Partner Demo

A partner asks: "Can I see what a passenger would experience?"

You pull out your phone, navigate to `pierway.io`, select:
- 4 hours
- History + Food
- Pier 91

And in 5 seconds you show them a route with 4 stops, real narrative about Seattle, and a clean UI that works on mobile.

That's the demo. That's what we need before outreach calls convert.

---

## Build Sequence

| Phase | What | Why |
|---|---|---|
| **Week 1** | UI shell — screens 1–3, no AI yet | Get the UX right before wiring AI |
| **Week 2** | Claude API integration — route generation | Core product working end-to-end |
| **Week 3** | Route display + stop detail screens | The experience passengers actually walk through |
| **Week 4** | Geolocation check-in ("I'm Here") | Proves the verification model |
| **Buffer** | Polish, mobile testing, edge cases | Before season demo meetings |

**Hard deadline:** Working demo before first partner meeting converts to a product question.

---

## Open Questions Before Build Starts

1. **Pier 91 vs Pier 66 routes:** Do we build separate route pools per pier, or does the AI handle this through the prompt? (Recommend: prompt-driven, with pier as a context variable)

2. **Offline behavior:** Passengers may lose signal mid-walk. Does the route need to work offline after initial load? (Recommend: yes — cache the generated route in localStorage)

3. **Group dynamics:** Most cruise passengers travel in groups of 2–4. Does the UI need to account for this? (Recommend: ignore in v1 — the route works for any group size)

4. **What if the route is wrong?** What happens if Claude generates a stop that doesn't exist or gives wrong directions? (Recommend: human review of the top 10 most common route combinations before launch)

---

*Spec owner: Ray Castro · Closes action item A-002 from risk log*
*Next step: Confirm build approach and start Week 1 UI shell*
