"""Site identity. Edit the values below, then run:  python tools/build.py

DUMMY_DETAILS = True means the contact details below are temporary demo values. While it is
True, the build marks every page `noindex` and writes a robots.txt that blocks crawlers, so a
copy with fake contact details can't be indexed or used for ads by accident.

Before going live: put in real, working details, set DUMMY_DETAILS = False, then rebuild.
(Google expects genuine, reachable contact details on a business website.)
"""

BRAND = "Talent Lore"

# Contact details shown across the site.
# Keep DUMMY_DETAILS = True while any of these are still temporary. Set it to False once all
# three are real, working details you control (this also removes noindex and the robots.txt block).
ADDRESS = "137 Telok Ayer Street, Singapore 068602"
PHONE = "+65 9876 5432"
EMAIL = "hello@talentlore.com"
DUMMY_DETAILS = True

# Shown on guides as "Last reviewed ...". Only change this after you have actually re-checked the pages.
REVIEWED = "November 2026"
PRIVACY_UPDATED = "10 November 2026"

# Anything listed here keeps the whole site noindex / robots-blocked.
PLACEHOLDERS = {k: v for k, v in {"ADDRESS": ADDRESS, "PHONE": PHONE, "EMAIL": EMAIL}.items()
                if DUMMY_DETAILS or v.startswith("[")}
