# Pierway — Cruise Terminal Flyer

## Design Spec

**Size:** 5.5" x 8.5" (half-letter) — easy to hand out, fits in a back pocket
**Paper:** 100lb gloss cardstock — holds up in rain, feels premium
**Print:** Two-sided, full color

---

## FRONT

```
┌─────────────────────────────────────────────┐
│                                             │
│            [Seattle skyline silhouette]      │
│                                             │
│                                             │
│         YOU HAVE 8 HOURS IN SEATTLE.        │
│            MAKE THEM COUNT.                 │
│                                             │
│                                             │
│    ┌─────────────────────────────────┐       │
│    │         [QR CODE]              │       │
│    │                                │       │
│    │    pierway.vercel.app          │       │
│    │    ?utm_source=cruise_flyer    │       │
│    │    &utm_terminal=pier91        │       │
│    └─────────────────────────────────┘       │
│                                             │
│                                             │
│      Free AI-powered walking routes         │
│      built around YOUR interests.           │
│                                             │
│      No app download. No signup.            │
│      Just scan and walk.                    │
│                                             │
│                                             │
│              ⟡ Pierway                      │
│                                             │
└─────────────────────────────────────────────┘
```

### Front Copy (exact text)

**Headline (large, display font):**
YOU HAVE 8 HOURS IN SEATTLE.
MAKE THEM COUNT.

**Below QR code (medium):**
Free AI-powered walking routes
built around YOUR interests.

**Subtext (small):**
No app download. No signup.
Just scan and walk.

**Logo:** Pierway mark + wordmark, bottom center

---

## BACK

```
┌─────────────────────────────────────────────┐
│                                             │
│     HOW IT WORKS                            │
│                                             │
│     1. Scan the QR code                     │
│                                             │
│     2. Pick your time and interests         │
│        (history, food, art, waterfront...)  │
│                                             │
│     3. Get a personalized walking route     │
│        with hidden gems and local stories   │
│                                             │
│     4. Walk at your own pace — your phone   │
│        buzzes when something cool is nearby │
│                                             │
│                                             │
│     ─────────────────────────────           │
│                                             │
│     "Nirvana played their first Seattle     │
│      show two blocks from where you're      │
│      standing right now."                   │
│                                             │
│     — The kind of thing Pierway tells you   │
│                                             │
│     ─────────────────────────────           │
│                                             │
│                                             │
│     Works on any phone. No download needed. │
│     pierway.vercel.app                      │
│                                             │
└─────────────────────────────────────────────┘
```

### Back Copy (exact text)

**Header:** HOW IT WORKS

**Steps:**
1. Scan the QR code
2. Pick your time and interests (history, food, art, waterfront...)
3. Get a personalized walking route with hidden gems and local stories
4. Walk at your own pace — your phone buzzes when something cool is nearby

**Pull quote (italic, larger font):**
"Nirvana played their first Seattle show two blocks from where you're standing right now."
— The kind of thing Pierway tells you

**Footer:**
Works on any phone. No download needed.
pierway.vercel.app

---

## QR Code Tracking

Two versions of the flyer — identical design, different QR codes:

**Pier 91 (Smith Cove) version:**
`https://pierway.vercel.app/?utm_source=cruise_flyer&utm_terminal=pier91`

**Pier 66 (Bell Street) version:**
`https://pierway.vercel.app/?utm_source=cruise_flyer&utm_terminal=pier66`

PostHog will capture the UTM parameters automatically so you can see:
- Total scans per terminal per day
- Conversion from scan → route built → route completed
- Which terminal produces more engaged walkers

---

## Distribution Plan

**Where:**
- Pier 91 (Smith Cove) — Carnival, Royal Caribbean, Princess, Holland America, Celebrity
- Pier 66 (Bell Street) — Norwegian, Oceania

**When:**
- Disembarkation window: 8:30 AM – 10:00 AM (passengers leaving ship)
- Embarkation window: 11:00 AM – 2:00 PM (passengers arriving, less useful but still walking the area)

**Season:** Mid-April through mid-October 2026 (~330 ship calls, ~2M passengers)

**Permit note:** Cruise terminals are Port of Seattle property. Stand on the public sidewalk adjacent to the terminal — protected First Amendment activity, no permit needed. Contact Port of Seattle (206-787-3000) if you want to explore on-property access.

**Volume:** Start with 500 flyers for the first 2-3 ships. Measure scan rate before scaling up.

**Cost estimate:** 500 half-letter gloss cardstock flyers ≈ $60-80 at FedEx Office or Vistaprint.

---

## Design Notes for Print Production

- Use the seattle-bg.svg skyline silhouette from the app as the header graphic
- Color palette: navy (#1B2A4A) background, teal (#2DD4BF) accents, white text
- Display font for headline (same as app)
- QR code: white background square with navy QR pattern, high error correction (L25)
- Keep the back mostly white/light for legibility and contrast with the dark front
