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

## Open Action Items

### A-001 — Map Network Into Cruise / Port Ecosystem
**Date:** 2026-03-12 | **Owner:** Ray Castro | **Status:** Open | **Due:** Before next session
**Description:** Audit your existing network for any connection into Port of Seattle, cruise operators (Alaska Cruise lines, Carnival, Royal Caribbean, Norwegian, etc.), shore excursion vendors, or local tourism boards. Even a second-degree connection matters.
**Follow-up:** ray.s.castro@outlook.com (to be sent when email capability is available)

---

### A-002 — Define MVP Scope
**Date:** 2026-03-12 | **Owner:** Ray Castro + Claude | **Status:** Open | **Due:** Next session
**Description:** Define exactly what ships before May/June. Features in, features out. What is the smallest thing that proves the core behavior (pedestrian → route → merchant visit)?

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
*(none yet)*
