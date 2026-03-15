# Risk & Action Log

**Format:** Risks are tracked with likelihood (H/M/L), impact (H/M/L), status, and mitigation. Action items are linked to risks or decisions where applicable.

---

## Open Risks

### R-001 — Cruise Line Partnership Not Secured
**Date Raised:** 2026-03-12
**Likelihood:** H | **Impact:** H | **Status:** Open
**Description:** The primary distribution strategy (QR code at disembarkation, cruise operator rev share) depends on a partnership with a cruise line or the Port of Seattle. No contact has been established. This is the critical path item — without it, user acquisition for the pilot has no clear mechanism.
**Mitigation Options:**
- Identify smallest possible operator (local ferry, small cruise line) vs. going direct to Carnival/Royal Caribbean
- Explore Port of Seattle's existing vendor/partner programs
- Consider guerrilla alternative: street team at disembarkation without operator partnership (lower conversion but zero dependency)
**Owner:** Ray Castro
**Action:** A-001

---

### R-002 — Timeline Compression (10-12 Weeks to Cruise Season)
**Date Raised:** 2026-03-12
**Likelihood:** H | **Impact:** H | **Status:** Open
**Description:** Cruise season opens May/June 2026. MVP must be functional, tested, and deployed at the port by then. 10-12 weeks is feasible but leaves no buffer for scope creep, technical blockers, or partnership delays.
**Mitigation:** Define and lock MVP scope in next session. Any feature not in MVP scope gets cut ruthlessly.
**Owner:** Ray Castro
**Action:** A-002

---

### R-003 — Demographic Fit of Cruise Passengers
**Date Raised:** 2026-03-12
**Likelihood:** M | **Impact:** M | **Status:** Open
**Description:** Alaska cruise passengers (Port of Seattle primary route) skew 55+. May be less likely to download an unfamiliar app from a QR code. App adoption behavior in this demographic is unvalidated.
**Mitigation:** Research demographic data on Alaska cruise passengers. Consider whether the product UX and onboarding can accommodate lower-tech-comfort users (e.g., no account required, instant route on open).
**Owner:** Claude (research), Ray Castro (decision)
**Action:** A-003

---

### R-004 — GPS Accuracy in Urban Canyons
**Date Raised:** 2026-03-12 (from manifesto)
**Likelihood:** M | **Impact:** M | **Status:** Open
**Description:** Seattle's downtown corridor has buildings that can degrade GPS accuracy. Verified visit tracking depends on location precision.
**Mitigation:** Multi-sensor fusion + QR verification fallback (as noted in manifesto). For MVP, QR-only verification may be sufficient.
**Owner:** Claude (technical scoping)

---

### R-005 — Build Complexity vs. Solo Founder Bandwidth
**Date Raised:** 2026-03-12
**Likelihood:** M | **Impact:** H | **Status:** Open
**Description:** The full-lifecycle MVP (consumer app + verified visit engine + back office) is a materially larger build than a simple UI prototype. React, Supabase, Mapbox, Stripe Connect, and Claude API integration all in parallel — with no prior development background — carries real risk of scope creep, technical debt, and missed deadlines.
**Mitigation:** Strict phased build sequence. Phase 1 (consumer app only) is the partner demo gate. Don't start Phase 2 until Phase 1 ships. Claude manages architecture and code; Ray drives requirements and testing. Weekly checkpoints on build velocity.
**Owner:** Ray Castro

---

### R-006 — Accounts and Services Not Set Up
**Date Raised:** 2026-03-12
**Likelihood:** M | **Impact:** M | **Status:** Open
**Description:** Build cannot start until Supabase, Mapbox, Stripe, Vercel, and pierway.io domain are set up. These are blocking dependencies.
**Mitigation:** Set up all accounts before first line of code is written.
**Owner:** Ray Castro
**Action:** A-005

---

## Open Action Items

### A-005 — Set Up Build Infrastructure Accounts
**Date:** 2026-03-12 | **Owner:** Ray Castro | **Status:** Open | **Due:** Before build starts
**Description:** Set up: (1) Node.js LTS — install via `winget install OpenJS.NodeJS.LTS` (required before any code runs); (2) pierway.io domain purchase — Namecheap or Cloudflare Registrar, ~$35/yr; (3) Supabase account — free tier; (4) Mapbox account — free tier; (5) Stripe account — no monthly cost; (6) Vercel account — free tier; (7) Anthropic API account — pay-per-use; (8) GitHub repo for pierway codebase. Total monthly cost before revenue: ~$0.

---

### A-001 — Map Network Into Cruise / Port Ecosystem
**Date:** 2026-03-12 | **Owner:** Ray Castro | **Status:** Open | **Due:** Before next session
**Description:** Audit your existing network for any connection into Port of Seattle, cruise operators (Alaska Cruise lines, Carnival, Royal Caribbean, Norwegian, etc.), shore excursion vendors, or local tourism boards. Even a second-degree connection matters.
**Follow-up:** ray.s.castro@outlook.com (to be sent when email capability is available)

---

### A-002 — Define MVP Scope
**Date:** 2026-03-12 | **Owner:** Ray Castro + Claude | **Status:** Closed 2026-03-12
**Description:** Define exactly what ships before May/June. Features in, features out. What is the smallest thing that proves the core behavior (pedestrian → route → merchant visit)?
**Resolution:** MVP spec v2.0 written (pm/product/mvp-spec.md). Full-lifecycle scope confirmed: consumer app + verified visit engine + back office. Technical architecture documented (pm/product/technical-architecture.md).

---

### A-003 — Research Alaska Cruise Passenger Demographics
**Date:** 2026-03-12 | **Owner:** Claude | **Status:** Open | **Due:** Next session
**Description:** Pull data on Alaska cruise passenger age distribution, smartphone adoption, shore excursion behavior, and average dwell time at Port of Seattle. Assess demographic fit for app adoption.

---

### A-004 — Research Port of Seattle Cruise Operators & Shore Excursion Programs
**Date:** 2026-03-12 | **Owner:** Claude | **Status:** Open | **Due:** Next session
**Description:** Identify which cruise lines dock at Port of Seattle, their shore excursion vendor programs, and any existing partnership pathways for startups or local businesses.

---

## Closed Actions

### A-002 — Define MVP Scope
**Closed:** 2026-03-12 — MVP spec v2.0 and technical architecture written. Scope confirmed as full lifecycle.
