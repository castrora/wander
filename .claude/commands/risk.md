Log a new risk or action item to the Wander risk log.

Gather from conversation context:
- Is this a Risk (R-###) or Action Item (A-###)?
- Description of the risk or action
- For risks: likelihood (H/M/L), impact (H/M/L), mitigation options
- For actions: owner, due date, linked risk or decision if applicable

Then append the entry to pm/risks/risk-log.md using the next sequential number.

For risks, format:
---
### R-### — [Short Title]
**Date Raised:** YYYY-MM-DD
**Likelihood:** H/M/L | **Impact:** H/M/L | **Status:** Open
**Description:** [What the risk is]
**Mitigation Options:** [How to address it]
**Owner:** [Who is tracking this]
**Action:** [Linked A-### if applicable]
---

For actions, format:
---
### A-### — [Short Title]
**Date:** YYYY-MM-DD | **Owner:** [Name] | **Status:** Open | **Due:** [Date or "Next session"]
**Description:** [What needs to happen]
---

Confirm to the user that the item has been logged and give the ID.
