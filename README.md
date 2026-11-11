# FlexiBrowse (layout v2)

Independent information website (PHP homepage, HTML, CSS, JS) with guides on part-time, home-based, remote, online and freelance work in Singapore. It does not list vacancies or place candidates.

The text is freshly written (same facts, new wording) and the layout is new: left navigation rail on desktop, list layouts, a contents rail on job guides, a takeaways panel on articles, system fonts only (no third-party font requests) and no image files.

## Run locally

```
python tools/build.py                     # regenerates every page (Python 3.11+)
php -S 127.0.0.1:8000                     # then open http://127.0.0.1:8000/
```

The landing page is `index.php`. Serve the site with a PHP-enabled web server. Other pages use folder-based `index.html` files.

## Images

Photos are in `images/` (10 JPEGs, about 200 to 360 KB each). They are AI-generated illustrations of typical work settings, not real clients, employers or testimonials, and they carry no text or logos. They are mapped to pages in `tools/build.py` (`ART_IMG`, `PAGE_IMG`). To swap one, replace the file in `images/` with another 16:9 JPEG of the same name (`hero.jpg` is 4:3). Replace them with your own photography or licensed stock before launch if you prefer.

## Files

- `tools/identity.py`: brand name and contact details (address, phone, email). Currently **temporary dummy values**. **Edit this first.**
- `tools/build.py`, `tools/articles2.py`, `tools/jobpages.py`: page copy and templates.
- `sgs-styles.css`: all layout and visual design.
- `main.js`: menu, Knowledge Hub filters, glossary search, hours planner, mailto contact form.
- `tools/verify.py`: checks internal links, leftover old branding, placeholders and risky phrases, and measures text overlap with another site:
  `python tools/verify.py "<path to other site folder>"`

## Before going live

1. Open `tools/identity.py`, replace `ADDRESS`, `PHONE` and `EMAIL` with real, working details, and set `DUMMY_DETAILS = False`.
2. Run `python tools/build.py`.
3. While `DUMMY_DETAILS` is `True`, every page carries `noindex,nofollow` and `robots.txt` blocks crawlers. Setting it to `False` removes both on the next build.
4. Check that the brand name is free to use (IPOS trademark search, ACRA name search, domain availability).
5. Confirm the time-sensitive facts against the official sources (CPF rules, the 35-hour part-time definition, flexible work guidelines, 1799 ScamShield helpline).
6. If you add analytics or ad tags, update the Privacy Policy to describe cookies and advertising data use.
7. The contact form opens the visitor's email app (`mailto:`). It sends nothing until they press send. Use a real form service if you want in-page submissions, and update the thank-you page and privacy policy to match.
