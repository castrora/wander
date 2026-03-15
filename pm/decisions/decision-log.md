# Decision Log

Append-only. Each entry records what was decided, why, what alternatives were considered, and who made the call. Revisit decisions here before changing direction.

---

## D-001 — Bootstrap to MVP
**Date:** 2026-03-12
**Status:** Active
**Decision:** Wander will be bootstrapped to MVP. No external funding sought at this stage.
**Rationale:** The thesis needs validation before a capital raise is warranted. A bootstrapped MVP in a single cruise corridor is the fastest path to real data. Funding conversations can open after proof of behavior.
**Alternatives Considered:** Seed raise (referenced in manifesto — $5M GV pitch). Rejected for now as premature before any user or merchant validation.
**Owner:** Ray Castro

---

## D-002 — Seattle / Port of Seattle as Pilot Market
**Date:** 2026-03-12
**Status:** Active
**Decision:** Seattle is the pilot city. Specifically the Port of Seattle cruise disembarkation corridor.
**Rationale:** High foot traffic from cruise passengers with defined time windows and no cars. Ray is based in Seattle. Local network and operational presence is an advantage.
**Alternatives Considered:** Boston (Freedom Trail), NYC. Both are in the manifesto but require remote market entry without local presence.
**Owner:** Ray Castro

---

## D-003 — Data-First Sequencing (Months 1-2)
**Date:** 2026-03-12
**Status:** Active
**Decision:** First 1-2 months of operation prioritize foot traffic data capture over revenue generation. Merchant pitch happens after data exists.
**Rationale:** "15,000 people walked past your door" is a fundamentally stronger merchant pitch than a hypothetical. Sequencing data before revenue avoids the classic marketplace cold-start trap.
**Alternatives Considered:** Simultaneous merchant + user acquisition. Rejected as too complex with no proof points on either side.
**Owner:** Ray Castro

---

## D-005 — MVP Scope: Full Product Lifecycle
**Date:** 2026-03-12
**Status:** Active
**Decision:** The MVP covers the complete product lifecycle — consumer app (route + map + voice), verified visit engine (merchant QR scan → visit record), and back office (merchant onboarding + Stripe billing). Not a cruise-season-only demo.
**Rationale:** The waterfront corridor is walkable year-round. Hotels and local merchants can be piloted before cruise season begins. Limiting MVP scope to cruise-season UX would delay the commercial validation of the CPV model. The full lifecycle needs to be tested together to prove the business works.
**Alternatives Considered:** Lean v1 (UI only, no merchant billing). Rejected — a demo with no billing mechanism is not a business, it's a prototype.
**Owner:** Ray Castro

---

## D-006 — Tech Stack (Full Product)
**Date:** 2026-03-12
**Status:** Active
**Decision:** React + Vite / Tailwind CSS / Mapbox GL JS / Web Speech API / Claude API / Supabase / Stripe / Vercel.
**Rationale:** Solo founder building with AI assistance. Stack priorities: fast to ship, minimal ops burden, all free tiers sufficient for MVP, clear upgrade paths. Supabase replaces a custom backend. Mapbox is the best mobile map SDK for route rendering and offline tile support. Web Speech API eliminates ElevenLabs cost before revenue validation.
**Alternatives Considered:** Next.js (unnecessary SSR overhead), Firebase (vendor lock-in), custom Node/Express backend (more to manage), Google Maps (worse for custom route rendering), ElevenLabs v1 (cost before revenue).
**Owner:** Ray Castro

---

## D-007 — Build With Claude (AI-Assisted Development)
**Date:** 2026-03-12
**Status:** Active
**Decision:** Pierway is built by Ray Castro with Claude as AI development partner. No separate developer.
**Rationale:** The 1-Person Enterprise thesis. AI-assisted development is sufficient for this product at this stage. Hiring a developer before product-market fit is premature.
**Alternatives Considered:** Hiring a contract developer. Rejected — adds cost and coordination overhead before validation.
**Owner:** Ray Castro

---

## D-008 — Accounting Software: Wave (Pre-Revenue)
**Date:** 2026-03-12
**Status:** Active
**Decision:** Use Wave (free) for bookkeeping pre-revenue. Switch to QuickBooks Online when revenue begins.
**Rationale:** Pre-revenue means there's nothing material to report except expenses. Wave handles Stripe sync, expense tracking, and P&L at zero cost. QuickBooks is what CPAs work in — switching when there's an actual tax situation makes more sense than paying $30/mo now.
**Alternatives Considered:** QuickBooks Online Simple Start ($30/mo), Xero ($15/mo). Rejected as premature overhead before first invoice.
**Owner:** Ray Castro

---

## D-009 — LLC Formation: Defer Until Product Is Usable
**Date:** 2026-03-12
**Status:** Active
**Decision:** Defer forming a Washington LLC until the product is functional and Ray can use it himself.
**Rationale:** No revenue, no contracts, no employees — the liability exposure of operating as a sole proprietor at this stage is minimal. Formation costs (~$200 WA filing fee + registered agent) are better spent after the product exists.
**Alternatives Considered:** Form LLC immediately. Rejected as premature overhead before product validation.
**Owner:** Ray Castro

---

## D-010 — Build Sequence: Personal Test First
**Date:** 2026-03-12
**Status:** Active
**Decision:** Phase 1 of the build produces something Ray can personally walk around Seattle with — not a demo for others, but a real test of the product. Direct URL access (no QR required) is a Phase 1 requirement.
**Rationale:** The founder needs to experience the product as a user before showing it to anyone. A "Plan My Walk" starting-point selector (Pier 91 / Pier 66 / Current Location) covers both the QR-scan use case and the direct-URL test case.
**Alternatives Considered:** Build for demo first, test later. Rejected — you can't demo something you haven't walked yourself.
**Owner:** Ray Castro

---

## D-004 — Weekly Status Cadence
**Date:** 2026-03-12
**Status:** Active
**Decision:** Weekly status meetings and reports. Claude produces the report; Ray reviews and confirms priorities.
**Rationale:** 10-12 week timeline to cruise season requires tight cadence to catch slippage early.
**Alternatives Considered:** Bi-weekly. Rejected given the compressed timeline.
**Owner:** Ray Castro / Claude

---

## D-016 — Web Presence: App-First, No Separate Marketing Site Until Merchant Traction
**Date:** 2026-03-13
**Status:** Active
**Decision:** No separate consumer marketing site or B2B merchant site at launch. The app at `pierway.io` is the consumer presence — the landing screen does that job. Merchant outreach in Phase 1 is founder-led (cold email + in-person), supported by a PDF one-pager, not a website. A `/merchants` page is added only after the first 2–3 merchants are signed and there's something real to say. The merchant portal (login, dashboard, billing) is Phase 3 back office.
**Rationale:** A polished B2B site before any merchant data actively undermines sales credibility. First merchants need to hear the story from Ray directly. Building a site before the product is validated is distraction.
**Sequence:** (1) App + PDF one-pager now → (2) `/merchants` page after first signed merchants → (3) Full merchant portal in Phase 3.
**Alternatives Considered:** Separate B2B site at launch. Rejected — premature, no proof points to put on it, distraction from product.
**Owner:** Ray Castro

---

## D-014 — Voice Narration: Web Speech API Now, ElevenLabs Post-Validation
**Date:** 2026-03-12
**Status:** Active
**Decision:** Keep Web Speech API (browser-native TTS) through the first real walk test. Upgrade to ElevenLabs only after confirming walkers actually use the Listen feature. Kurt Cobain voice likeness specifically is off the table — estate controls the rights and Washington right-of-publicity law applies commercially.
**Rationale:** ElevenLabs adds $5–22/mo in cost and an API call per stop. That cost is justified only if narration is a feature people actually use. The first walk test will tell us whether Listen gets tapped. No point paying for audio polish before that data exists.
**Alternatives Considered:** ElevenLabs immediately (premature cost before validation); Kurt Cobain voice clone (legal exposure — estate controls likeness rights).
**Owner:** Ray Castro

---

## D-015 — Analytics: PostHog (Product Behavior) + Supabase Events (Business Data)
**Date:** 2026-03-12
**Status:** Active
**Decision:** Two-layer analytics from day one. PostHog handles product behavior — session replay, funnels, screen time, abandonment — added as a script tag at Vercel deploy. Supabase handles business-critical events (route_sessions, check-ins, visits) that feed CPV billing and eventual merchant/city reporting. No separate analytics app needed.
**Key metrics to capture:** Route preferences selected, stop engagement + dwell time, Listen button usage, check-in attempts + outcomes, abandonment point, interest popularity, route completion rate.
**Rationale:** PostHog is free up to 1M events/mo and gives session replay with zero build time — understanding how real walkers navigate the app is worth more than any assumption. Supabase events stay owned, feed billing, and become the proprietary dataset for data licensing. Both layers should be live from the first walk.
**Alternatives Considered:** Build custom analytics dashboard (Phase 3 only — not worth building before traffic exists); Google Analytics (limited for custom product events); single tool for both layers (PostHog alone doesn't feed CPV billing).
**Owner:** Ray Castro

---

## D-012 — Merchant Integration: Editorial Voice, No Explicit Sponsorship
**Date:** 2026-03-12
**Status:** Active
**Decision:** Merchant stops will never be labeled as "sponsored." They appear in the route as editorial recommendations in Claude's local voice — e.g., "One of the oldest bars in Seattle, known for its back-bar whiskey collection. You're right nearby — worth a stop." The commercial relationship is invisible to the walker. The check-in mechanism is the same; the presentation is curation, not advertising.
**Rationale:** Explicit sponsorship labels destroy the trust and authenticity that make the product work. A walker who feels like they're being pushed through a paid tour stops trusting the narrative. The value to the merchant is identical — attributed foot traffic + check-ins — but the value to the user is preserved because it reads as a genuine local tip, not an ad.
**Alternatives Considered:** Labeled sponsored stops ("Sponsored by Tavern X"). Rejected — erodes editorial credibility and makes the product feel like a mall directory.
**Owner:** Ray Castro

---

## D-013 — Multi-City Architecture: One Backend, City-Parameterized Frontend
**Date:** 2026-03-12
**Status:** Active (Future Phase)
**Decision:** When Pierway expands beyond Seattle, it will use a single Supabase backend with a `city_id` column on all tables (routes, merchants, visits). The React frontend will resolve city from the URL path (e.g., `/seattle`, `/nyc`, `/london`) and load a city-specific config: SVG background illustration, starting points, and neighborhood/landmark context injected into the Claude prompt. No separate deployments per city.
**Rationale:** One codebase, one database, one deployment. Adding a city is a config file + SVG illustration, not a new repo. City-specific Claude prompts ensure the local voice and context feel native to each place.
**Alternatives Considered:** Separate frontend deployments per city. Rejected — operational overhead scales linearly with cities, defeating the 1-Person Enterprise model.
**Owner:** Ray Castro

---

## D-011 — Navigation: Map + Position Dot, Not Turn-by-Turn
**Date:** 2026-03-12
**Status:** Active
**Decision:** Pierway will show a Mapbox map with the passenger's moving position dot and route drawn between stops. No turn-by-turn street directions.
**Rationale:** Turn-by-turn makes Pierway a worse Google Maps. The product differentiator is narrative and discovery, not routing. "Walk 0.3 miles to Pike Place" + a map showing where you are is sufficient for navigation. If real walkers get lost in testing, add turn-by-turn later via Mapbox Directions API.
**Alternatives Considered:** Full turn-by-turn via Mapbox Directions API. Rejected — competes on Google Maps' strongest feature, dilutes the discovery/narrative identity.
**Owner:** Ray Castro
