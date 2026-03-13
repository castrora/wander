"""
Wander — Port of Seattle Prospect List Builder
Generates research/port-of-seattle-prospects.xlsx

Sheets:
  1. Priority Contacts  — Port of Seattle + Tourism orgs (most actionable)
  2. Cruise Lines       — 11 operators with named contacts
  3. Hotels             — 13 hotels with named contacts
  4. How To Use
"""

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = Workbook()

# ── Colour palette ───────────────────────────────────────────────────────────
DARK_BLUE  = "1F3864"
MID_BLUE   = "2E75B6"
TEAL       = "1A7A6E"
PURPLE     = "5C3D8F"
ORANGE_BG  = "FFF2CC"
LIGHT_BLUE = "D6E4F0"
LIGHT_TEAL = "D6EFEC"
LIGHT_PURP = "EAE0F5"
WHITE      = "FFFFFF"
LIGHT_GREY = "F2F2F2"
GREEN      = "375623"
GREEN_BG   = "E2EFDA"
RED_BG     = "FCE4D6"

def fill(hex_color):
    return PatternFill("solid", fgColor=hex_color)

def border():
    s = Side(style="thin", color="CCCCCC")
    return Border(left=s, right=s, top=s, bottom=s)

def style_header(ws, row_num, bg, fg=WHITE):
    for cell in ws[row_num]:
        cell.font      = Font(bold=True, color=fg, name="Calibri", size=10)
        cell.fill      = fill(bg)
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border    = border()
    ws.row_dimensions[row_num].height = 36

def style_row(ws, row_num, bg=WHITE):
    for cell in ws[row_num]:
        cell.fill      = fill(bg)
        cell.alignment = Alignment(vertical="center", wrap_text=True)
        cell.border    = border()
        cell.font      = Font(name="Calibri", size=10)
    ws.row_dimensions[row_num].height = 18

def style_section_label(ws, row_num, bg, fg=WHITE, label=""):
    cell = ws.cell(row=row_num, column=1, value=label)
    ws.merge_cells(start_row=row_num, start_column=1, end_row=row_num, end_column=ws.max_column or 12)
    cell.font      = Font(bold=True, color=fg, name="Calibri", size=11)
    cell.fill      = fill(bg)
    cell.alignment = Alignment(vertical="center")
    cell.border    = border()
    ws.row_dimensions[row_num].height = 22

def set_widths(ws, widths):
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w

def freeze(ws, ref="A2"):
    ws.freeze_panes = ref
    ws.auto_filter.ref = ws.dimensions


# ════════════════════════════════════════════════════════════════════════════
# SHEET 1 — PRIORITY CONTACTS
# ════════════════════════════════════════════════════════════════════════════
ws1 = wb.active
ws1.title = "Priority Contacts"

hdrs = ["Organization", "Category", "Contact Name", "Title",
        "Email", "Phone", "GTM Relevance", "LinkedIn Search", "Notes"]
ws1.append(hdrs)
style_header(ws1, 1, DARK_BLUE)

sections = [
    # ── PORT OF SEATTLE ──────────────────────────────────────────────────
    ("_SECTION", "PORT OF SEATTLE", TEAL),
    ("Port of Seattle", "Port — Cruise Ops",
     "Marie Ellingson", "Manager, Cruise Services & Business Development",
     "mellingson@portseattle.org", "(206) 787-3529",
     "Direct vendor/partner intake for cruise terminals. PRIMARY contact for QR code placement at Pier 91 & Pier 66.",
     '"Port of Seattle" "Cruise" "Business Development"',
     "Best first call. Manages vendor relationships at both terminals."),
    ("Port of Seattle", "Port — Public Affairs",
     "Rosie Courtney", "Senior Manager, Cruise Public Affairs & Community Engagement",
     "", "",
     "Community/brand angle. Useful if Wander pitches as a visitor experience rather than a vendor.",
     '"Port of Seattle" "Cruise" "Public Affairs" OR "Community"',
     "Good secondary contact after initial outreach to Ellingson."),
    ("Port of Seattle", "Port — General",
     "Cruise Terminal Manager (general)", "Cruise Terminal Operations",
     "cruiseterminal@portseattle.org", "(206) 644-1355",
     "General operations line. Use if direct contacts don't respond.",
     "", "Fallback contact — portseattle.org/contacts/cruise-terminal-manager"),

    # ── VISIT SEATTLE ─────────────────────────────────────────────────────
    ("_SECTION", "VISIT SEATTLE  (Official DMO — Seattle/King County)", MID_BLUE),
    ("Visit Seattle", "Tourism — Executive",
     "Tammy Canavan", "President & CEO",
     "tcanavan@visitseattle.org", "206.461.5833",
     "Top-level champion. If Wander fits Visit Seattle's mission (visitor experience, local commerce), she can open doors to hotels and cruise lines simultaneously.",
     '"Visit Seattle" "CEO" OR "President"',
     "Manages STIA (71 downtown hotels). Strong QR code distribution leverage."),
    ("Visit Seattle", "Tourism — Sales & Marketing",
     "Kelly Saling", "EVP Sales & Marketing & Chief Business Officer",
     "ksaling@visitseattle.org", "206.461.5802",
     "Controls co-marketing and partnership budget. Key for Wander distribution deals.",
     '"Visit Seattle" "Sales" OR "Chief Business Officer"',
     ""),
    ("Visit Seattle", "Tourism — Destination Dev",
     "Marco Leal", "Vice President, Destination Development",
     "mleal@visitseattle.org", "206.461.5816",
     "Destination development = exactly Wander's pitch. Most aligned role in the org.",
     '"Visit Seattle" "Destination Development"',
     "Strong alignment with Wander's value prop. High priority outreach."),
    ("Visit Seattle", "Tourism — Marketing",
     "Stephanie Byington", "Chief Marketing Officer",
     "sbyington@visitseattle.org", "206.461.5809",
     "Brand/content angle. Useful if pitching media layer (build in public) as co-marketing.",
     '"Visit Seattle" "Chief Marketing Officer"',
     ""),
    ("Visit Seattle", "Tourism — Engagement",
     "Michael Woody", "Chief Engagement Officer",
     "mwoody@visitseattle.org", "206.461.5808",
     "Community/experience programs. Secondary contact.",
     '"Visit Seattle" "Engagement"',
     ""),

    # ── STATE OF WASHINGTON TOURISM ───────────────────────────────────────
    ("_SECTION", "STATE OF WASHINGTON TOURISM  (Statewide DMO)", PURPLE),
    ("State of Washington Tourism", "Tourism — Executive",
     "David Blandford", "CEO",
     "tourisminfo@stateofwatourism.com", "",
     "Statewide scope — valuable for multi-city expansion, less critical for Seattle pilot.",
     '"State of Washington Tourism" "CEO"',
     "Former SVP Public Affairs at Visit Seattle. Knows the ecosystem well."),
    ("State of Washington Tourism", "Tourism — Partnerships",
     "Mike Moe", "Director of Strategic Partnerships & Tourism Development",
     "tourisminfo@stateofwatourism.com", "",
     "Partnerships role — directly relevant. Good contact for statewide distribution conversations.",
     '"State of Washington Tourism" "Partnerships" OR "Tourism Development"',
     "Use org email as direct emails not publicly listed."),
    ("State of Washington Tourism", "Tourism — Marketing",
     "Michelle Thana", "Director of Marketing",
     "tourisminfo@stateofwatourism.com", "",
     "Marketing director — relevant if pitching media/content angle.",
     '"State of Washington Tourism" "Marketing"',
     ""),
]

row_num = 2
for item in sections:
    if item[0] == "_SECTION":
        ws1.append([""] * len(hdrs))
        style_section_label(ws1, row_num, item[2], label=f"  {item[1]}")
        row_num += 1
    else:
        ws1.append(list(item))
        bg = LIGHT_TEAL if "Port" in item[1] else (LIGHT_BLUE if "Visit" in item[1] else LIGHT_PURP)
        style_row(ws1, row_num, bg=bg)
        row_num += 1

set_widths(ws1, [26, 22, 24, 36, 34, 18, 52, 44, 44])
ws1.freeze_panes = "A2"


# ════════════════════════════════════════════════════════════════════════════
# SHEET 2 — CRUISE LINES
# ════════════════════════════════════════════════════════════════════════════
ws2 = wb.create_sheet("Cruise Lines")

hdrs2 = ["Company", "Parent", "Website", "Terminal",
         "Cruise Type", "Segment", "Est. Annual Pax (Seattle)",
         "New 2026?", "GTM Priority",
         "Contact Name", "Title", "Email", "Phone",
         "LinkedIn Search", "Notes"]
ws2.append(hdrs2)
style_header(ws2, 1, DARK_BLUE)

cruise_data = [
    ("Holland America Line", "Carnival Corporation", "hollandamerica.com",
     "Pier 91 — Smith Cove", "Alaska 7-night / Cruisetours", "Premium", "~350,000+", "No", "HIGH",
     "Jessica Ashe", "Sr. Director, Shore Excursions & Future Cruises", "", "",
     '"Holland America Line" "Jessica Ashe" OR "Shore Excursions" Seattle',
     "Seattle-based. Most directly relevant role for Wander partnership."),

    ("Holland America Line", "Carnival Corporation", "hollandamerica.com",
     "Pier 91 — Smith Cove", "Alaska 7-night / Cruisetours", "Premium", "~350,000+", "No", "HIGH",
     "Robert Morgenstern", "SVP, Alaska Operations", "", "",
     '"Holland America Line" "Robert Morgenstern" OR "Alaska Operations"',
     "Senior Alaska ops lead. Good escalation contact after Shore Excursions."),

    ("Princess Cruises", "Carnival Corporation", "princess.com",
     "Pier 91 — Smith Cove", "Alaska 7-night / Cruisetours", "Premium", "~300,000+", "No", "HIGH",
     "", "Shore Excursions / Destination Team", "", "",
     '"Princess Cruises" "Shore Excursions" OR "Destination" Alaska Seattle',
     "No named contact found publicly. Use LinkedIn search to identify."),

    ("Norwegian Cruise Line", "Norwegian Cruise Line Holdings", "ncl.com",
     "Pier 66 — Bell Street", "Alaska 7-night Inside Passage", "Contemporary", "~250,000+", "No", "HIGH",
     "Milos Cicic", "Manager, Destination Services, Shore Excursions", "", "",
     '"Norwegian Cruise Line" "Milos Cicic" OR "Destination Services"',
     "NCL Holdings manages Oceania and Regent Seven Seas too."),

    ("Virgin Voyages", "Virgin Group / Bain Capital", "virginvoyages.com",
     "Pier 91 — Smith Cove", "Alaska 7-night", "Premium / Millennial", "TBD", "YES — 2026", "HIGH",
     "Michelle Bentubo", "COO", "", "",
     '"Virgin Voyages" "Partnerships" OR "Destination" OR "Shore" Seattle 2026',
     "NEW to Seattle 2026. Team actively standing up. High receptivity to innovative experiences. Best cold-start opportunity."),

    ("MSC Cruises", "MSC Group (Private)", "msccruises.com",
     "Pier 91 — Smith Cove", "Alaska 7-night", "Contemporary / Family", "TBD", "YES — 2026", "HIGH",
     "", "US Partnerships / Destination Team", "", "",
     '"MSC Cruises" "Partnerships" OR "Destination" OR "Shore Excursions" Seattle 2026',
     "NEW to Seattle 2026. No named US contact found. Use LinkedIn search."),

    ("Royal Caribbean International", "Royal Caribbean Group", "royalcaribbean.com",
     "Pier 91 — Smith Cove", "Alaska 5–13-night", "Contemporary / Family", "~200,000+", "No", "MEDIUM",
     "", "Destination Experiences Team", "", "",
     '"Royal Caribbean" "Destination Experiences" OR "Shore Excursions" Alaska Seattle',
     ""),

    ("Celebrity Cruises", "Royal Caribbean Group", "celebritycruises.com",
     "Pier 91 — Smith Cove", "Alaska 7-night", "Premium / Modern Luxury", "~150,000+", "No", "MEDIUM",
     "", "Shore Excursions / Partnerships", "", "",
     '"Celebrity Cruises" "Shore Excursions" OR "Partnerships" Seattle',
     "Same parent as Royal Caribbean — one contact may cover both."),

    ("Carnival Cruise Line", "Carnival Corporation", "carnival.com",
     "Pier 91 — Smith Cove", "Alaska 7-night", "Value / Family", "~150,000+", "No", "MEDIUM",
     "", "Shore Excursions / Destination", "", "",
     '"Carnival Cruise Line" "Shore Excursions" OR "Destination" Alaska Seattle',
     ""),

    ("Oceania Cruises", "Norwegian Cruise Line Holdings", "oceaniacruises.com",
     "Pier 66 — Bell Street", "Alaska 10-night (small ship)", "Premium / Upscale", "~30,000", "No", "LOW",
     "", "Destination Services", "", "",
     '"Oceania Cruises" "Destination" OR "Shore Excursions"',
     "Same NCL Holdings umbrella as NCL — Cicic contact may apply."),

    ("Silversea Cruises", "Royal Caribbean Group", "silversea.com",
     "Pier 66 — Bell Street", "Alaska (luxury/expedition)", "Ultra-Luxury", "~15,000", "No", "LOW",
     "", "Destination / Expedition Team", "", "",
     '"Silversea" "Destination" OR "Expedition" OR "Shore Excursions"',
     ""),

    ("Cunard", "Carnival Corporation", "cunard.com",
     "Pier 91 — Smith Cove", "Alaska 7-night (luxury/classic)", "Luxury", "~50,000", "No", "LOW",
     "", "Shore Excursions / Destination", "", "",
     '"Cunard" "Shore Excursions" OR "Destination" OR "Partnerships" Seattle',
     ""),
]

for i, row in enumerate(cruise_data):
    ws2.append(list(row))
    alt = i % 2 == 1
    style_row(ws2, i + 2, bg=LIGHT_GREY if alt else WHITE)

set_widths(ws2, [26, 24, 24, 22, 32, 20, 20, 12, 12, 24, 34, 32, 16, 48, 44])
freeze(ws2)


# ════════════════════════════════════════════════════════════════════════════
# SHEET 3 — HOTELS
# ════════════════════════════════════════════════════════════════════════════
ws3 = wb.create_sheet("Hotels")

hdrs3 = ["Hotel", "Address", "Terminal", "Distance",
         "Stars", "Website", "Cruise Pkg?", "Shuttle?",
         "GTM Priority", "Contact Name", "Title",
         "Email", "Phone", "LinkedIn Search", "Notes"]
ws3.append(hdrs3)
style_header(ws3, 1, MID_BLUE)

hotel_data = [
    # ── PIER 66 HOTELS ───────────────────────────────────────────────────
    ("The Edgewater Hotel", "2411 Alaskan Way (Pier 67), Seattle WA 98121",
     "Pier 66", "~0.14 mi / 2-min walk", "4★", "edgewaterhotel.com",
     "Yes", "Walk-in", "HIGH",
     "Ian McClendon", "General Manager", "", "",
     '"Edgewater Hotel Seattle" "Ian McClendon" OR "General Manager"',
     "Directly adjacent to terminal. Noble House Hotels & Resorts property. Highest priority hotel contact."),

    ("Seattle Marriott Waterfront", "2100 Alaskan Way, Seattle WA 98121",
     "Pier 66", "~0.1 mi", "4★", "marriott.com",
     "Yes — Park & Cruise", "Yes", "HIGH",
     "Amrit Sandhu", "General Manager", "", "",
     '"Seattle Marriott Waterfront" "Amrit Sandhu" OR "General Manager"',
     "Directly across from terminal. Also contact Haley Connors (Destination Sales Executive) for partnership conversations."),

    ("Seattle Marriott Waterfront", "2100 Alaskan Way, Seattle WA 98121",
     "Pier 66", "~0.1 mi", "4★", "marriott.com",
     "Yes — Park & Cruise", "Yes", "HIGH",
     "Haley Connors", "Destination Sales Executive", "", "",
     '"Seattle Marriott Waterfront" "Haley Connors" OR "Destination Sales"',
     "Best contact for partnership/QR placement conversations at Marriott Waterfront."),

    ("The Sound Hotel Seattle Belltown", "2212 2nd Ave, Seattle WA 98121",
     "Pier 66", "~0.3 mi", "3★", "thesoundhotelseattle.com",
     "Yes", "Yes — private transfer", "HIGH",
     "Director of Sales", "(Role currently open/in transition)", "", "",
     '"Sound Hotel Seattle" "General Manager" OR "Director of Sales"',
     "Tapestry Collection by Hilton. Director of Sales role was open as of early 2026. Confirm current GM via hotel directly."),

    ("Mayflower Park Hotel", "405 Olive Way, Seattle WA 98101",
     "Pier 66 & Pier 91", "~1.0 mi / ~3.2 mi", "3★", "mayflowerpark.com",
     "Yes", "Yes — both terminals", "HIGH",
     "Andrew Harris", "General Manager", "", "",
     '"Mayflower Park Hotel" "Andrew Harris" OR "General Manager"',
     "Appointed Jan 5 2026. Manages both Hotel Theodore and Mayflower. Shuttle to Pier 66 ($15/person) and Pier 91."),

    ("Mayflower Park Hotel", "405 Olive Way, Seattle WA 98101",
     "Pier 66 & Pier 91", "~1.0 mi / ~3.2 mi", "3★", "mayflowerpark.com",
     "Yes", "Yes — both terminals", "HIGH",
     "Leslie Womack", "Director of Sales", "", "",
     '"Mayflower Park Hotel" "Leslie Womack" OR "Director of Sales"',
     "20+ years hospitality. Best contact for distribution/partnership conversation at Mayflower."),

    ("Kimpton Hotel Vintage Seattle", "1100 5th Ave, Seattle WA 98101",
     "Pier 66", "~0.7 mi", "4★", "hotelvintage-seattle.com",
     "Yes", "No", "MEDIUM",
     "", "General Manager / Director of Sales", "", "",
     '"Hotel Vintage Seattle" "General Manager" OR "Director of Sales"',
     "IHG brand. Cruise proximity packages offered."),

    ("Coast Seattle Downtown Hotel by APA", "1415 5th Ave, Seattle WA 98101",
     "Pier 66", "~0.8 mi", "3★", "coasthotels.com",
     "Yes — Bon Voyage Package", "No", "MEDIUM",
     "", "General Manager / Director of Sales", "", "",
     '"Coast Seattle Downtown Hotel" "General Manager" OR "Director of Sales"',
     "$50 dining credit + early check-in cruise package."),

    # ── PIER 91 HOTELS ───────────────────────────────────────────────────
    ("Mediterranean Inn", "425 Queen Anne Ave N, Seattle WA 98109",
     "Pier 91", "~1.5 mi", "3★", "mediterranean-inn.com",
     "Yes", "Yes ~$10/person", "HIGH",
     "Sheila Ordonez", "General Manager", "", "",
     '"Mediterranean Inn Seattle" "Sheila Ordonez" OR "General Manager"',
     "Closest hotel with active cruise shuttle to Pier 91. Good QR placement candidate."),

    ("Staypineapple The Maxwell Hotel", "300 Roy St, Seattle WA 98109",
     "Pier 91", "~1.2 mi", "3★", "staypineapple.com",
     "No", "No", "MEDIUM",
     "", "General Manager / Director of Sales", "", "",
     '"Maxwell Hotel Seattle" OR "Staypineapple Seattle" "General Manager"',
     "Closest full-service hotel to Pier 91. No formal cruise program yet — opportunity."),

    ("Astra Hotel Seattle", "2000 2nd Ave, Seattle WA 98121",
     "Pier 91", "~2.5 mi", "4★", "astrahotelseattle.com",
     "Yes — Snooze & Cruise", "No", "MEDIUM",
     "", "General Manager / Director of Sales", "", "",
     '"Astra Hotel Seattle" "General Manager" OR "Director of Sales"',
     "Active 'Snooze and Cruise' package — already thinking about cruise passenger experience."),

    ("Marqueen Hotel", "600 Queen Anne Ave N, Seattle WA 98109",
     "Pier 91", "~1.5 mi", "4★", "marqueen.com",
     "No", "No", "LOW",
     "", "General Manager / Owner", "", "",
     '"Marqueen Hotel Seattle" "Manager" OR "Owner"',
     "Boutique. No formal cruise program."),

    ("1 Hotel Seattle", "1112 4th Ave, Seattle WA 98101",
     "Pier 91", "~3.5 mi", "5★", "1hotels.com",
     "No", "Yes — local shuttle", "LOW",
     "", "General Manager / Director of Sales", "", "",
     '"1 Hotel Seattle" "General Manager" OR "Director of Sales"',
     "Luxury. Complimentary local shuttle — confirm Pier 91 coverage."),
]

for i, row in enumerate(hotel_data):
    ws3.append(list(row))
    alt = i % 2 == 1
    style_row(ws3, i + 2, bg=LIGHT_GREY if alt else WHITE)

set_widths(ws3, [28, 34, 12, 16, 6, 26, 16, 18, 12, 24, 30, 30, 16, 46, 52])
freeze(ws3)


# ════════════════════════════════════════════════════════════════════════════
# SHEET 4 — HOW TO USE
# ════════════════════════════════════════════════════════════════════════════
ws4 = wb.create_sheet("How To Use")
ws4.column_dimensions["A"].width = 110

guide = [
    ("WANDER — Port of Seattle Prospect & Contact List", True, DARK_BLUE, WHITE, 14),
    ("", False, WHITE, "000000", 10),
    ("PURPOSE", True, MID_BLUE, WHITE, 11),
    ("Map the cruise, hotel, and tourism ecosystem around the Port of Seattle for QR code placement and GTM outreach.", False, LIGHT_BLUE, "000000", 10),
    ("Goal: get Wander QR codes placed at cruise terminals, hotels, and tourism offices before the 2026 season opens in mid-April.", False, LIGHT_BLUE, "000000", 10),
    ("", False, WHITE, "000000", 10),
    ("SHEETS IN THIS WORKBOOK", True, MID_BLUE, WHITE, 11),
    ("1. Priority Contacts  — Port of Seattle + Visit Seattle + State of WA Tourism. Start here. These are the highest-leverage outreach targets.", False, LIGHT_BLUE, "000000", 10),
    ("2. Cruise Lines  — 11 operators at Pier 91 and Pier 66. Named contacts where found. LinkedIn search strings for the rest.", False, LIGHT_BLUE, "000000", 10),
    ("3. Hotels  — 13 hotels near the terminals. Named contacts where found. Prioritized by proximity and cruise program activity.", False, LIGHT_BLUE, "000000", 10),
    ("", False, WHITE, "000000", 10),
    ("RECOMMENDED OUTREACH SEQUENCE", True, TEAL, WHITE, 11),
    ("Step 1 — Port of Seattle: Contact Marie Ellingson (mellingson@portseattle.org) first. She manages cruise vendor/partner relationships at both terminals.", False, LIGHT_TEAL, "000000", 10),
    ("Step 2 — Visit Seattle: Contact Marco Leal (mleal@visitseattle.org) — VP Destination Development. Most aligned role to Wander's pitch.", False, LIGHT_TEAL, "000000", 10),
    ("Step 3 — Hotels: Start with Edgewater (Ian McClendon) and Marriott Waterfront (Haley Connors). Both physically adjacent to Pier 66.", False, LIGHT_TEAL, "000000", 10),
    ("Step 4 — Cruise Lines: Virgin Voyages and MSC are NEW to Seattle in 2026 — highest receptivity. Then Holland America (Jessica Ashe).", False, LIGHT_TEAL, "000000", 10),
    ("", False, WHITE, "000000", 10),
    ("FINDING MISSING CONTACTS ON LINKEDIN", True, MID_BLUE, WHITE, 11),
    ("1. Copy the LinkedIn Search String from the row.", False, LIGHT_GREY, "000000", 10),
    ("2. Paste into LinkedIn search bar → click People filter.", False, LIGHT_GREY, "000000", 10),
    ("3. Target titles: Shore Excursions Manager, Director of Destination Experiences, Director of Sales, General Manager, VP Business Development.", False, LIGHT_GREY, "000000", 10),
    ("4. Add their Name, Title, and Profile URL to the contact columns in this file.", False, LIGHT_GREY, "000000", 10),
    ("", False, WHITE, "000000", 10),
    ("GTM PRIORITY GUIDE", True, MID_BLUE, WHITE, 11),
    ("HIGH — First wave outreach. High passenger volume, active cruise programs, or new 2026 entrants building from scratch.", False, LIGHT_GREY, "000000", 10),
    ("MEDIUM — Second wave after initial traction.", False, LIGHT_GREY, "000000", 10),
    ("LOW — Smaller volume, luxury segment, or no existing cruise program. Not the right early-stage fit.", False, LIGHT_GREY, "000000", 10),
    ("", False, WHITE, "000000", 10),
    ("SEASON CONTEXT", True, MID_BLUE, WHITE, 11),
    ("Season opens: mid-April 2026 — target distribution deals signed by April 1", False, LIGHT_BLUE, "000000", 10),
    ("Season closes: late October 2026", False, LIGHT_BLUE, "000000", 10),
    ("2025 season: ~1.9M passengers (record). 2026 expected to exceed 2M.", False, LIGHT_BLUE, "000000", 10),
    ("New 2026 entrants: Virgin Voyages (Brilliant Lady) and MSC Cruises (MSC Poesia) — both homeporting at Pier 91", False, LIGHT_BLUE, "000000", 10),
    ("", False, WHITE, "000000", 10),
    ("LAST UPDATED", True, MID_BLUE, WHITE, 11),
    ("2026-03-12 | Research by Claude (Wander project) | Sources: portseattle.org, visitseattle.org, industry.stateofwatourism.com, public press releases", False, LIGHT_GREY, "000000", 10),
]

for text, bold, bg, fg, size in guide:
    ws4.append([text])
    r = ws4.max_row
    c = ws4.cell(row=r, column=1)
    c.font      = Font(bold=bold, color=fg, name="Calibri", size=size)
    c.fill      = PatternFill("solid", fgColor=bg)
    c.alignment = Alignment(wrap_text=True, vertical="center")
    ws4.row_dimensions[r].height = 22 if bold else 18


# ── Save ─────────────────────────────────────────────────────────────────────
out = r"C:\Users\raysc\wander\research\port-of-seattle-prospects.xlsx"
wb.save(out)
print(f"Saved: {out}")
