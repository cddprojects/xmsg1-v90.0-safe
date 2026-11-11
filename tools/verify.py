"""Quality checks for the built site.

Usage:
  python tools/verify.py                      # links, placeholders, risky phrasing
  python tools/verify.py "<original folder>"  # also measures text overlap with the original site
"""
import pathlib, re, sys
from html.parser import HTMLParser
from identity import DUMMY_DETAILS

NEW = pathlib.Path(__file__).resolve().parent.parent
OLD = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else None

class Text(HTMLParser):
    # Navigation and footer boilerplate is excluded so the overlap figure reflects page copy.
    SKIP = {"script", "style", "head", "title", "svg", "header", "nav", "footer"}
    def __init__(self):
        super().__init__(); self.depth = 0; self.out = []
    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP: self.depth += 1
    def handle_endtag(self, tag):
        if tag in self.SKIP and self.depth: self.depth -= 1
    def handle_data(self, data):
        t = " ".join(data.split())
        if t and not self.depth: self.out.append(t)

def text(path):
    p = Text(); p.feed(path.read_text(encoding="utf-8")); return " ".join(p.out)
def words(s): return re.findall(r"[a-z0-9']+", s.lower())
def shingles(ws, n=7): return {" ".join(ws[i:i+n]) for i in range(max(0, len(ws)-n+1))}

pages = sorted(p.relative_to(NEW) for p in NEW.rglob("index.*") if p.suffix in (".html", ".php"))
print(f"{len(pages)} pages built\n")

# 1. internal links and anchors
bad = 0
for rel in pages:
    src = (NEW / rel).read_text(encoding="utf-8")
    for url in re.findall(r'(?:href|src)="([^"]+)"', src):
        if url.startswith(("http", "mailto:", "tel:", "data:", "//")): continue
        path, _, frag = url.partition("#")
        target = (NEW / rel).parent / path if path else NEW / rel
        if path and target.is_dir():
            target = target / ("index.php" if (target / "index.php").exists() else "index.html")
        if not target.exists():
            print("BROKEN LINK  ", rel, "->", url); bad += 1
        elif frag and target.suffix in (".html", ".php"):
            ids = set(re.findall(r'\bid="([^"]+)"', target.read_text(encoding="utf-8")))
            if frag not in ids: print("BROKEN ANCHOR", rel, "->", url); bad += 1
print("links:", "OK" if not bad else f"{bad} problem(s)")

# 2. leftovers from the original site's identity
legacy = ["discovergle", "burlington", "bencoolen", "8396 3756", "support@"]
leftovers = [(rel, w) for rel in pages for w in legacy if w in (NEW / rel).read_text(encoding="utf-8").lower()]
print("original identity left behind:", "none" if not leftovers else leftovers)

# 3. placeholders (site is held back from search engines while any remain)
ph = sorted({m for rel in pages for m in re.findall(r"\[[A-Za-z][^\]<]{2,40}\]", text(NEW / rel))})
noindex = all('name="robots" content="noindex' in (NEW / rel).read_text(encoding="utf-8") for rel in pages)
print("placeholders still in pages:", ph if ph else "none")
print("all pages noindex:", noindex, "| robots.txt:", (NEW / "robots.txt").read_text().replace("\n", " "))
print("dummy contact details in use:", DUMMY_DETAILS)

# 4. risky phrasing (counts across the whole site)
whole = " ".join(text(NEW / rel).lower() for rel in pages)
print("\nphrase counts across the site:")
for ph_ in ["work from home jobs singapore", "part time job singapore", "remote job singapore", "make money at home",
            "easy money", "fast money", "guarantee", "official partner", "verified"]:
    print(f"  {ph_!r:36} {whole.count(ph_)}")
print("  (\"guarantee\"/\"easy money\"/\"fast money\" should only appear in warnings such as 'never guaranteed')")

# 5. overlap with the original site (7-word phrases)
if OLD:
    old = set()
    for p in OLD.rglob("index.html"): old |= shingles(words(text(p)))
    tot = shared = 0
    rows = []
    for rel in pages:
        s = shingles(words(text(NEW / rel)))
        sh = len(s & old); tot += len(s); shared += sh
        rows.append((sh / max(1, len(s)), str(rel), sh, len(s)))
    print("\ntext overlap with the original (share of 7-word phrases found there):")
    for pct, rel, sh, n in sorted(rows, reverse=True)[:40]:
        print(f"  {pct:5.0%}  {rel}  ({sh}/{n})")
    print(f"  overall: {shared/max(1,tot):.0%}")
    if len(sys.argv) > 2:  # python tools/verify.py <old> <page-folder>  -> list the sentences still shared
        page_ = NEW / sys.argv[2] / "index.html"
        for sent in re.split(r"(?<=[.!?])\s+", text(page_)):
            ws = words(sent); sh = shingles(ws, 5)
            old5 = old5 if "old5" in globals() else set().union(*[shingles(words(text(p)), 5) for p in OLD.rglob("index.html")])
            if sh and len(sh & old5) / len(sh) > .5: print("  SHARED:", sent[:140])
