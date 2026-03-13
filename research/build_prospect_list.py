"""
Wander — Port of Seattle Prospect List Builder
Generates research/port-of-seattle-prospects.xlsx
"""

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = Workbook()

# ── Colour palette ──────────────────────────────────────────────────────────
DARK_BLUE   = "1F3864"
MID_BLUE    = "2E75B6"
LIGHT_BLUE  = "D6E4F0"
ORANGE      = "F4A300"
WHITE       = "FFFFFF"
LIGHT_GREY  = "F2F2F2"

def hdr_fill(hex_color):
    return PatternFill("solid", fgColor=hex_color)

def thin_border():
    s = Side(style="thin", color="CCCCCC")
    return Border(left=s, right=s, top=s, bottom=s)

def style_header_row(ws, row, bg, fg=WHITE, bold=True):
    for cell in ws[row]:
        cell.font      = Font(bold=bold, color=fg, name="Calibri", size=10)
        cell.fill      = hdr_fill(bg)
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border    = thin_border()

def style_data_row(ws, row_num, alternate=False):
    bg = LIGHT_GREY if alternate else WHITE
    for cell in ws[row_num]:
        cell.fill      = hdr_fill(bg)
        cell.alignment = Alignment(vertical="center", wrap_text=True)
        cell.border    = thin_border()
        cell.font      = Font(name="Calibri", size=10)

def set_col_widths(ws, widths):
    for i, w in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w

def freeze_and_filter(ws, ref="A2"):
    ws.freeze_panes = ref
    ws.auto_filter.ref = ws.dimensions


# ════════════════════════════════════════════════════════════════════════════
# SHEET 1 — CRUISE LINES
# ════════════════════════════════════════════════════════════════════════════
ws1 = wb.active
ws1.title = "Cruise Lines"
ws1.row_dimensions[1].height = 36

headers1 = [
    "Company", "Parent Company", "Website", "Terminal",
    "Cruise Type", "Market Segment", "Est. Annual Pax (Seattle)",
    "New to Seattle 2026?", "GTM Priority",
    "LinkedIn Search String", "Key Contact Name", "Key Contact Title",
    "LinkedIn URL", "Email", "Notes"
]
ws1.append(headers1)
style_header_row(ws1, 1, DARK_BLUE)

cruise_lines = [
    # Company, Parent, Website, Terminal, Type, Segment, Pax, New2026, Priority, LI Search
    ("Holland America Line", "Carnival Corporation", "hollandamerica.com",
     "Pier 91 — Smith Cove", "Alaska 7-night Inside Passage / Cruisetours",
     "Premium", "~350,000+", "No", "HIGH",
     '"Holland America Line" "Shore Excursions" OR "Partnerships" OR "Business Development" Seattle'),

    ("Princess Cruises", "Carnival Corporation", "princess.com",
     "Pier 91 — Smith Cove", "Alaska 7-night Inside Passage / Cruisetours",
     "Premium", "~300,000+", "No", "HIGH",
     '"Princess Cruises" "Shore Excursions" OR "Port Operations" OR "Partnerships" Seattle'),

    ("Norwegian Cruise Line (NCL)", "Norwegian Cruise Line Holdings", "ncl.com",
     "Pier 66 — Bell Street", "Alaska 7-night Inside Passage",
     "Contemporary", "~250,000+", "No", "HIGH",
     '"Norwegian Cruise Line" "Shore Excursions" OR "Business Development" OR "Port" Seattle'),

    ("Royal Caribbean International", "Royal Caribbean Group", "royalcaribbean.com",
     "Pier 91 — Smith Cove", "Alaska 5–13-night / Cruisetours",
     "Contemporary / Family", "~200,000+", "No", "MEDIUM",
     '"Royal Caribbean" "Shore Excursions" OR "Destination Experiences" Seattle'),

    ("Celebrity Cruises", "Royal Caribbean Group", "celebritycruises.com",
     "Pier 91 — Smith Cove", "Alaska 7-night",
     "Premium / Modern Luxury", "~150,000+", "No", "MEDIUM",
     '"Celebrity Cruises" "Shore Excursions" OR "Partnerships" Seattle'),

    ("Carnival Cruise Line", "Carnival Corporation", "carnival.com",
     "Pier 91 — Smith Cove", "Alaska 7-night",
     "Value / Family", "~150,000+", "No", "MEDIUM",
     '"Carnival Cruise Line" "Shore Excursions" OR "Destination" OR "Port" Seattle'),

    ("Cunard", "Carnival Corporation", "cunard.com",
     "Pier 91 — Smith Cove", "Alaska 7-night (luxury/classic)",
     "Luxury", "~50,000", "No", "LOW",
     '"Cunard" "Shore Excursions" OR "Partnerships" Seattle'),

    ("Virgin Voyages", "Virgin Group / Bain Capital", "virginvoyages.com",
     "Pier 91 — Smith Cove", "Alaska",
     "Premium / Millennial", "TBD", "YES — 2026", "HIGH",
     '"Virgin Voyages" "Shore Excursions" OR "Partnerships" OR "Business Development"'),

    ("MSC Cruises", "MSC Group (Private)", "msccruises.com",
     "Pier 91 — Smith Cove", "Alaska",
     "Contemporary / Family", "TBD", "YES — 2026", "HIGH",
     '"MSC Cruises" "Shore Excursions" OR "Destination" OR "Partnerships" Seattle'),

    ("Oceania Cruises", "Norwegian Cruise Line Holdings", "oceaniacruises.com",
     "Pier 66 — Bell Street", "Alaska 10-night (small ship)",
     "Premium / Upscale", "~30,000", "No", "LOW",
     '"Oceania Cruises" "Shore Excursions" OR "Destination" Seattle'),

    ("Silversea Cruises", "Royal Caribbean Group", "silversea.com",
     "Pier 66 — Bell Street", "Alaska (luxury/expedition)",
     "Ultra-Luxury", "~15,000", "No", "LOW",
     '"Silversea" "Shore Excursions" OR "Destination" OR "Expeditions"'),
]

for i, row in enumerate(cruise_lines):
    ws1.append(list(row) + ["", "", "", "", ""])
    style_data_row(ws1, i + 2, alternate=(i % 2 == 1))

set_col_widths(ws1, [28, 26, 28, 24, 36, 22, 24, 16, 12, 52, 24, 28, 36, 28, 36])
freeze_and_filter(ws1)
ws1.row_dimensions[1].height = 40


# ════════════════════════════════════════════════════════════════════════════
# SHEET 2 — HOTELS
# ════════════════════════════════════════════════════════════════════════════
ws2 = wb.create_sheet("Hotels")
ws2.row_dimensions[1].height = 36

headers2 = [
    "Hotel Name", "Address", "Terminal Proximity", "Distance to Terminal",
    "Star Rating", "Website", "Cruise Package?", "Shuttle Program?",
    "Shuttle Details", "GTM Priority",
    "LinkedIn Search String", "Key Contact Name", "Key Contact Title",
    "LinkedIn URL", "Email", "Notes"
]
ws2.append(headers2)
style_header_row(ws2, 1, MID_BLUE)

hotels = [
    # Near Pier 66
    ("The Edgewater Hotel", "2411 Alaskan Way (Pier 67), Seattle WA 98121",
     "Pier 66 — Bell Street", "~0.14 mi / 2-min walk", "4-star", "edgewaterhotel.com",
     "Yes", "No (walk-in)", "Directly adjacent to terminal", "HIGH",
     '"Edgewater Hotel Seattle" "General Manager" OR "Director of Sales" OR "Partnerships"'),

    ("Seattle Marriott Waterfront", "2100 Alaskan Way, Seattle WA 98121",
     "Pier 66 — Bell Street", "~0.1 mi", "4-star", "marriott.com",
     "Yes — Park & Cruise", "Yes", "On-site parking + cruise package", "HIGH",
     '"Seattle Marriott Waterfront" "General Manager" OR "Director of Sales" OR "Concierge"'),

    ("The Sound Hotel Seattle Belltown", "2212 2nd Ave, Seattle WA 98121",
     "Pier 66 — Bell Street", "~0.3 mi", "3-star", "thesoundhotel.com",
     "Yes", "Yes — private transfer", "All Black Limo partnership ~$75/vehicle", "HIGH",
     '"Sound Hotel Seattle" "General Manager" OR "Director of Sales" OR "Partnerships"'),

    ("The Belltown Inn", "2301 3rd Ave, Seattle WA 98121",
     "Pier 66 — Bell Street", "~0.5 mi walk", "3-star", "belltowninn.com",
     "No", "No", "Walkable, no formal program", "MEDIUM",
     '"Belltown Inn Seattle" "Manager" OR "Front Desk Manager" OR "Operations"'),

    ("Kimpton Hotel Vintage Seattle", "1100 5th Ave, Seattle WA 98101",
     "Pier 66 — Bell Street", "~0.7 mi", "4-star", "hotelvintage-seattle.com",
     "Yes", "No", "Cruise proximity packages via IHG", "MEDIUM",
     '"Hotel Vintage Seattle" "General Manager" OR "Director of Sales" OR "Concierge"'),

    ("Mayflower Park Hotel", "405 Olive Way, Seattle WA 98101",
     "Pier 66 & Pier 91", "~1.0 mi / ~3.2 mi", "3-star", "mayflowerpark.com",
     "Yes", "Yes — both terminals", "Scheduled shuttle $15/person + $25 F&B credit", "HIGH",
     '"Mayflower Park Hotel Seattle" "General Manager" OR "Director of Sales" OR "Concierge"'),

    ("Coast Seattle Downtown Hotel by APA", "1415 5th Ave, Seattle WA 98101",
     "Pier 66 — Bell Street", "~0.8 mi", "3-star", "coasthotels.com",
     "Yes — Bon Voyage Package", "No", "$50 dining credit + early check-in", "MEDIUM",
     '"Coast Seattle Downtown Hotel" "General Manager" OR "Director of Sales"'),

    # Near Pier 91
    ("Mediterranean Inn", "425 Queen Anne Ave N, Seattle WA 98109",
     "Pier 91 — Smith Cove", "~1.5 mi", "3-star", "mediterraneanninn.com",
     "Yes", "Yes", "Scheduled cruise shuttle ~$10/person", "HIGH",
     '"Mediterranean Inn Seattle" "Manager" OR "Owner" OR "Operations"'),

    ("Staypineapple The Maxwell Hotel", "300 Roy St, Seattle WA 98109",
     "Pier 91 — Smith Cove", "~1.2 mi", "3-star", "staypineapple.com",
     "No", "No", "Closest full-service hotel to Pier 91", "MEDIUM",
     '"Maxwell Hotel Seattle" OR "Staypineapple Seattle" "General Manager" OR "Director of Sales"'),

    ("Astra Hotel Seattle", "2000 2nd Ave, Seattle WA 98121",
     "Pier 91 — Smith Cove", "~2.5 mi", "4-star", "astrahotelseattle.com",
     "Yes — Snooze and Cruise", "No", "Dedicated cruise package", "MEDIUM",
     '"Astra Hotel Seattle" "General Manager" OR "Director of Sales" OR "Partnerships"'),

    ("Marqueen Hotel", "600 Queen Anne Ave N, Seattle WA 98109",
     "Pier 91 — Smith Cove", "~1.5 mi", "4-star", "marqueen.com",
     "No", "No", "Boutique; no formal program", "LOW",
     '"Marqueen Hotel Seattle" "Manager" OR "Owner"'),

    ("Hyatt Place Seattle/Downtown", "110 6th Ave N, Seattle WA 98109",
     "Pier 91 — Smith Cove", "~1.8 mi", "3-star", "hyatt.com",
     "No", "No", "Near Seattle Center", "LOW",
     '"Hyatt Place Seattle Downtown" "General Manager" OR "Director of Sales"'),

    ("1 Hotel Seattle", "1112 4th Ave, Seattle WA 98101",
     "Pier 91 — Smith Cove", "~3.5 mi", "5-star", "1hotels.com",
     "No", "Yes — local shuttle", "Complimentary local shuttle; confirm Pier 91 coverage", "LOW",
     '"1 Hotel Seattle" "General Manager" OR "Director of Sales" OR "Concierge"'),
]

for i, row in enumerate(hotels):
    ws2.append(list(row) + ["", "", "", "", ""])
    style_data_row(ws2, i + 2, alternate=(i % 2 == 1))

set_col_widths(ws2, [28, 36, 22, 18, 12, 26, 20, 16, 36, 12, 52, 24, 28, 36, 28, 36])
freeze_and_filter(ws2)


# ════════════════════════════════════════════════════════════════════════════
# SHEET 3 — INSTRUCTIONS
# ════════════════════════════════════════════════════════════════════════════
ws3 = wb.create_sheet("How To Use")
ws3.column_dimensions["A"].width = 100

instructions = [
    ("WANDER — Port of Seattle Prospect List", True, DARK_BLUE, WHITE, 14),
    ("", False, WHITE, "000000", 10),
    ("PURPOSE", True, MID_BLUE, WHITE, 11),
    ("This workbook maps the cruise line and hotel ecosystem at the Port of Seattle for GTM outreach.", False, LIGHT_BLUE, "000000", 10),
    ("Use this list to identify and contact decision-makers who can unlock cruise passenger distribution for Wander.", False, LIGHT_BLUE, "000000", 10),
    ("", False, WHITE, "000000", 10),
    ("SHEETS", True, MID_BLUE, WHITE, 11),
    ("Cruise Lines — 11 operators that dock at Pier 91 or Pier 66. Sorted by GTM Priority.", False, LIGHT_BLUE, "000000", 10),
    ("Hotels — 13 hotels near the cruise terminals. Sorted by terminal proximity and priority.", False, LIGHT_BLUE, "000000", 10),
    ("", False, WHITE, "000000", 10),
    ("HOW TO FIND LINKEDIN CONTACTS", True, MID_BLUE, WHITE, 11),
    ("1. Copy the 'LinkedIn Search String' for a target company.", False, LIGHT_GREY, "000000", 10),
    ('2. Paste it into LinkedIn search (use People filter).', False, LIGHT_GREY, "000000", 10),
    ("3. Find the best match: Shore Excursions Manager, Director of Sales, Business Development, GM.", False, LIGHT_GREY, "000000", 10),
    ("4. Paste their name, title, and profile URL into the contact columns.", False, LIGHT_GREY, "000000", 10),
    ("", False, WHITE, "000000", 10),
    ("GTM PRIORITY GUIDE", True, MID_BLUE, WHITE, 11),
    ("HIGH — Target first. Either high passenger volume, active cruise packages, or new 2026 entrants (Virgin, MSC).", False, LIGHT_GREY, "000000", 10),
    ("MEDIUM — Target in wave 2 after initial outreach converts.", False, LIGHT_GREY, "000000", 10),
    ("LOW — Smaller volume or luxury segment; not the right profile for early-stage distribution.", False, LIGHT_GREY, "000000", 10),
    ("", False, WHITE, "000000", 10),
    ("SEASON CONTEXT", True, MID_BLUE, WHITE, 11),
    ("Season opens: mid-April 2026 (target: have distribution deal in place by April 1)", False, LIGHT_GREY, "000000", 10),
    ("Season closes: late October 2026", False, LIGHT_GREY, "000000", 10),
    ("2025 season passengers: ~1.9M (record). 2026 expected to exceed.", False, LIGHT_GREY, "000000", 10),
    ("Primary itinerary: Alaska Inside Passage, 7-night roundtrip from Seattle", False, LIGHT_GREY, "000000", 10),
    ("", False, WHITE, "000000", 10),
    ("LAST UPDATED", True, MID_BLUE, WHITE, 11),
    ("2026-03-12 | Research by Claude (Wander project)", False, LIGHT_GREY, "000000", 10),
]

for text, is_header, bg, fg, size in instructions:
    ws3.append([text])
    row_num = ws3.max_row
    cell = ws3.cell(row=row_num, column=1)
    cell.font = Font(bold=is_header, color=fg, name="Calibri", size=size)
    cell.fill = PatternFill("solid", fgColor=bg)
    cell.alignment = Alignment(wrap_text=True, vertical="center")
    if is_header:
        ws3.row_dimensions[row_num].height = 24
    else:
        ws3.row_dimensions[row_num].height = 18

# Save
out_path = r"C:\Users\raysc\wander\research\port-of-seattle-prospects.xlsx"
wb.save(out_path)
print(f"Saved: {out_path}")
