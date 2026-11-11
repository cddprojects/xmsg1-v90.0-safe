"""Generates the static site in the project root.  Run:  python tools/build.py

Identity (brand, business details) lives in tools/identity.py.
Articles are in tools/articles2.py and job-type guides in tools/jobpages.py (both are
executed from this file and share its globals).
"""
import pathlib, re, shutil, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from identity import BRAND, ADDRESS, PHONE, EMAIL, REVIEWED, PRIVACY_UPDATED, PLACEHOLDERS

OUT = pathlib.Path(__file__).resolve().parent.parent
# privacy.html is the only page whose folder name differs from the file name.
FOLDERS = {"privacy.html": "privacy-policy"}
_ATTR = re.compile(r"\b(href|src)=([\'\"])([^\'\"]+)\2")
BUILT = set()

def out_path(fname):
    if fname == "index.html":
        return OUT / "index.php"
    folder = FOLDERS.get(fname)
    if folder is None:
        folder = fname[:-5] if fname.endswith(".html") else fname
    return OUT / folder / "index.html"

def _clean_link(target, prefix):
    if "#" in target:
        path, frag = target.split("#", 1)
        frag = "#" + frag
    else:
        path, frag = target, ""
    if path == "" or path.startswith(("http://", "https://", "mailto:", "tel:", "//", "data:")):
        return None
    if path in ("sgs-styles.css", "main.js") or path.startswith("images/"):
        return (prefix + path + frag) if prefix else None
    if path.endswith(".html"):
        if path == "index.html":
            return prefix + "index.php" + frag
        name = FOLDERS.get(path, path[:-5])
        return f"{prefix}{name}/{frag}"
    return None

def rewrite_links(html, fname):
    """Point the homepage at index.php and other pages at folder URLs."""
    prefix = "" if fname == "index.html" else "../"
    def repl(m):
        new = _clean_link(m.group(3), prefix)
        if new is None:
            return m.group(0)
        return f"{m.group(1)}={m.group(2)}{new}{m.group(2)}"
    return _ATTR.sub(repl, html)

NAV = [("index.html","Home"),("jobs.html","Job Types"),("knowledge-hub.html","Knowledge Hub"),("about.html","About Us")]
SUBNAV = [("services.html","All services"),("glossary.html","Glossary"),("faq.html","FAQ")]

# Photos live in /images (illustrative only; they do not show real clients or employers).
IMG_SIZE = {"hero":(1024,768)}
def img(name, alt="", cls="", lazy=True):
    w,h = IMG_SIZE.get(name,(1024,576))
    c = f' class="{cls}"' if cls else ""
    l = ' loading="lazy" decoding="async"' if lazy else ""
    return f'<img{c} src="images/{name}.jpg" alt="{alt}" width="{w}" height="{h}"{l}>'
ART_IMG = {
"article-sectors-hiring.html":"skyline","article-in-demand-roles.html":"online","article-why-second-income.html":"part-time",
"article-remote-work-trend.html":"remote","article-upskilling-2026.html":"learning","article-read-labour-data.html":"skyline",
"article-rising-costs.html":"hero","article-childcare-caregiving.html":"family","article-restart.html":"part-time",
"article-remote-cv.html":"desk","article-flexible-work-request.html":"work-from-home","article-part-time-cpf.html":"part-time",
"article-work-modes.html":"freelance","article-read-job-ad.html":"desk","article-job-scams.html":"work-from-home",
}
PAGE_IMG = {
"part-time-jobs-singapore.html":"part-time","work-from-home-jobs-singapore.html":"work-from-home","remote-jobs-singapore.html":"remote",
"online-jobs-singapore.html":"online","freelance-jobs-singapore.html":"freelance","work-from-home-routes-singapore.html":"hero",
}

# Inline SVG mark (no image file needed).
LOGO = ('<svg class="mark" viewBox="0 0 32 32" width="32" height="32" aria-hidden="true"><rect width="32" height="32" rx="8" fill="#f2b134"/>'
        '<path d="M11 23V9h11M11 16h9" fill="none" stroke="#12233f" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>')
FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%23f2b134'/%3E"
           "%3Cpath d='M11 23V9h11M11 16h9' fill='none' stroke='%2312233f' stroke-width='2.6' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E")

def icon(p):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{p}</svg>'
IC = {
 "doc":icon('<path d="M6 3h9l4 4v14H6z"/><path d="M14 3v5h5M9 13h6M9 17h6"/>'),
 "chat":icon('<path d="M4 5h16v11H9l-5 4z"/>'),
 "laptop":icon('<rect x="4" y="5" width="16" height="11" rx="2"/><path d="M2 20h20"/>'),
 "globe":icon('<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/>'),
 "wallet":icon('<rect x="3" y="6" width="18" height="14" rx="3"/><path d="M3 10h18M16 15h2"/>'),
}

def page(fname, title, desc, body, extra_head=""):
    cur = ' aria-current="page"'
    nav = "".join(f'<li><a href="{h}"{cur if h==fname else ""}>{t}</a></li>' for h,t in NAV)
    subnav = "".join(f'<li><a href="{h}"{cur if h==fname else ""}>{t}</a></li>' for h,t in SUBNAV)
    res_cur = ' aria-current="true"' if fname in [h for h,_ in SUBNAV] else ""
    nav += f'<li class="has-sub"><a href="services.html" class="sub-parent"{res_cur}>Resources</a><ul class="sub">{subnav}</ul></li>'
    if PLACEHOLDERS:
        extra_head += '<meta name="robots" content="noindex,nofollow">\n'
    html = f'''<!doctype html>
<html lang="en-SG">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#12233f">
<link rel="icon" href="{FAVICON}">
<link rel="stylesheet" href="sgs-styles.css">
{extra_head}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="topbar" id="rail">
<div class="wrap bar">
<a class="brand" href="index.html">{LOGO}<span>{BRAND}</span></a>
<button class="menu-btn" aria-expanded="false" aria-controls="nav-list" aria-label="Open menu"><span class="bars" aria-hidden="true"></span></button>
<nav class="main-nav" aria-label="Main">
<ul id="nav-list">{nav}</ul>
<a class="btn btn-warm nav-cta" href="contact.html">Contact Us</a>
</nav>
</div>
</header>
<div class="stage">
<main id="main">
{body}
</main>
<footer class="site-footer"><div class="wrap">
<div class="foot-grid">
<div><a class="brand" href="index.html">{LOGO}<span>{BRAND}</span></a>
<p style="margin-top:1rem;max-width:32ch">Independent guides to careers, industries and skills in Singapore, including part-time and home-based work.</p></div>
<div><h4>Explore</h4><ul><li><a href="services.html">Services</a></li><li><a href="jobs.html">Job types</a></li><li><a href="knowledge-hub.html">Knowledge Hub</a></li><li><a href="glossary.html">Glossary</a></li><li><a href="faq.html">FAQ</a></li></ul></div>
<div><h4>Company</h4><ul><li><a href="about.html">About Us</a></li><li><a href="contact.html">Contact Us</a></li><li><a href="privacy.html">Privacy Policy</a></li><li><a href="disclaimer.html">Disclaimer</a></li></ul></div>
</div>
<div class="legal"><p>{BRAND} is an information website. We are independent and not connected with any government agency. We do not recruit, place candidates or advertise vacancies. Our guides give general information only and are not legal advice; please confirm details with MOM or CPF Board. ScamShield helpline: <strong>1799</strong>.</p>
<p>&copy; 2026 {BRAND} &middot; {ADDRESS} &middot; {PHONE} &middot; {EMAIL}</p></div>
</div></footer>
</div>
<script src="main.js"></script>
</body></html>'''
    html = rewrite_links(html, fname)
    dest = out_path(fname)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(html, encoding="utf-8")
    BUILT.add(dest)

def head(eyebrow, h1, lede=""):
    lede_html = "<p class=lede>"+lede+"</p>" if lede else ""
    return f'<div class="page-head"><div class="wrap ph-grid"><div><span class="eyebrow">{eyebrow}</span><h1>{h1}</h1></div>{lede_html}</div></div>'

def contact_form(with_topic=False):
    topic = ('<div class="field"><label for="topic">Topic</label><select id="topic"><option>A question about part-time jobs</option><option>A question about home-based or remote work</option><option>Online or freelance work</option><option>Report a problem or concern</option><option>Suggest an article</option><option>Correction or feedback</option></select></div>') if with_topic else ""
    return f'''<form id="contact-form" class="form" data-mail="{EMAIL}" novalidate>
<div class="field"><label for="name">Name</label><input id="name" required autocomplete="name"><div class="err" aria-live="polite"></div></div>
<div class="field"><label for="email">Email</label><input id="email" type="email" required autocomplete="email"><div class="err" aria-live="polite"></div></div>
{topic}<div class="field"><label for="msg">Message</label><textarea id="msg" required></textarea><div class="err" aria-live="polite"></div></div>
<button class="btn btn-primary" type="submit">Send</button>
{'<p class="notice">Sending opens your email app with your message ready. We only receive it once you press send there.</p>' if with_topic else ''}</form>'''

FORM_OK = f'''<div id="form-ok" class="ok" hidden tabindex="-1" role="status"><h3>Almost done.</h3><p>Your email app should now be open with your message ready. Please press send there to complete it. We only receive your message once you do.</p><p class="ok-sub">If nothing opened, you can write to us directly at {EMAIL}.</p></div>'''

# ---------------- shared article data
T = {  # titles, used by cards, the hub and the article pages
"article-sectors-hiring.html":"Where Singapore's Hiring Is Growing: A Sector Guide",
"article-in-demand-roles.html":"Roles in Demand in Singapore and the Skills Behind Them",
"article-why-second-income.html":"Why Side Income Is on the Rise in Singapore",
"article-remote-work-trend.html":"Flexible Work in Singapore: How Remote and Hybrid Arrangements Became Normal",
"article-upskilling-2026.html":"Upskilling in Singapore: Funding, Courses and What Changes at Work",
"article-read-labour-data.html":"How to Read Singapore's Labour Market Figures",
"article-rising-costs.html":"Household Costs and Flexible Work: Where Extra Income Can Fit",
"article-childcare-caregiving.html":"Work and Caregiving: Weighing Costs and Choices for Families",
"article-restart.html":"Going Back to Work After a Career Break",
"article-remote-cv.html":"Writing a CV for Remote and Home-Based Roles",
"article-flexible-work-request.html":"How to Ask Your Employer for Flexible Work, Step by Step",
"article-part-time-cpf.html":"Part-Time Work and CPF: What to Check on Your Payslip",
"article-work-modes.html":"Part-Time, Remote, Hybrid and Freelance: What the Terms Mean",
"article-read-job-ad.html":"How to Read a Job Ad for a Flexible Role",
"article-job-scams.html":"Seven Warning Signs of a Fake Remote Job Offer",
}
EXC = {
"article-sectors-hiring.html":"Healthcare, technology, finance and logistics are still expanding, while the roles inside them keep changing...",
"article-in-demand-roles.html":"Job titles shift, but the skills employers ask for keep falling into the same few groups...",
"article-why-second-income.html":"A growing number of people take a part-time or freelance role next to their main job...",
"article-remote-work-trend.html":"Flexible work has gone from a perk to an everyday topic between employers and staff...",
"article-upskilling-2026.html":"Training is only worth the money when it links to roles you can see advertised...",
"article-read-labour-data.html":"Unemployment, vacancies and wages each measure something different. The useful picture comes from reading them together...",
"article-rising-costs.html":"If every month seems tighter than the last, you are not imagining it...",
"article-childcare-caregiving.html":"The real question is often whether the hours work for your family, not whether you want to work...",
"article-restart.html":"Career gaps are common, and a short, calm explanation is usually enough...",
"article-remote-cv.html":"A remote employer can't watch you work, so your CV has to show that you deliver on your own...",
"article-flexible-work-request.html":"Treat your request as a proposal: describe the arrangement and show how the work will still get done...",
"article-part-time-cpf.html":"Part-time staff are still employees, and the payslip is the quickest place to check CPF...",
"article-work-modes.html":"Job ads blend three separate ideas: hours, location and legal status...",
"article-read-job-ad.html":"Two ads can look alike and still describe very different jobs. The fine print decides...",
"article-job-scams.html":"Scammers like part-time and remote roles because easy, flexible income is hard to turn down...",
}
ROUTES = "work-from-home-routes-singapore.html"

def card(href,label,m="5 min"):
    return (f'<article class="post reveal"><a class="thumb" href="{href}" tabindex="-1" aria-hidden="true">{img(ART_IMG[href])}</a>'
            f'<div class="pbody"><div class="meta"><span class="cat">{label}</span><span>{m} read</span></div>'
            f'<h3><a href="{href}">{T[href]}</a></h3><p>{EXC[href]}</p></div></article>')
def tile_s(href,t,d,pic): return f'<a class="mini reveal" href="{href}">{img(pic)}<span class="mt"><b>{t}</b><span>{d}</span></span></a>'

# ---------------- HOME
page("index.html",f"Flexible Work Guides for Singapore: Part-Time, Home-Based and Freelance | {BRAND}",
"Plain-language guides to part-time, home-based, remote and freelance work in Singapore: typical hours, how pay and CPF work, and what to ask before you accept an offer.",f'''
<section class="hero"><div class="wrap hero-grid">
<div class="hero-copy">
<span class="eyebrow">Flexible work guides &middot; Singapore</span>
<h1>Flexible work in Singapore, <span>explained plainly.</span></h1>
<p class="lede">Straightforward guides to part-time, home-based, remote and freelance work in Singapore. Learn what the hours look like, how pay and CPF work, and which questions to ask before you say yes.</p>
<div class="btn-row"><a class="btn btn-primary" href="jobs.html">Browse job types</a><a class="btn btn-ghost" href="{ROUTES}#calc">Open the hours planner</a></div>
<p class="scope-note">Want current vacancies? <a href="jobs.html#where-to-look">Start with the official job portals</a>.</p>
</div>
<div class="hero-media">
{img("hero","A person working on a laptop at a table in a bright home",lazy=False)}
<a class="lead-card" href="article-sectors-hiring.html"><span class="cat">Featured &middot; Industry trends</span><strong>{T["article-sectors-hiring.html"]}</strong><span class="go">Read the article &rarr;</span></a>
</div>
</div></section>

<section class="clarity"><div class="wrap">
<ul class="clarity-grid">
<li class="reveal"><h3>Hours that fit your week</h3><p>Find out what a normal week looks like in part-time, home-based, remote and freelance work, and compare it with your studies, family duties or main job.</p></li>
<li class="reveal"><h3>Pay and CPF made clear</h3><p>See how pay is calculated, when CPF applies, and what to look for in a contract or payslip.</p></li>
<li class="reveal"><h3>Tell good offers from bad</h3><p>Use our question checklists and scam warning signs before you give out any personal details.</p></li>
</ul>
</div></section>

<section class="alt"><div class="wrap">
<div class="head reveal"><span class="eyebrow">The big picture</span><h2>Four changes shaping work in Singapore.</h2></div>
<ol class="shifts">
<li class="reveal"><span class="no">01</span><h3>Sectors</h3><p>Healthcare, technology, finance and logistics come up again and again in national reports.</p></li>
<li class="reveal"><span class="no">02</span><h3>Skills</h3><p>More employers describe jobs by the skills needed rather than by title alone.</p></li>
<li class="reveal"><span class="no">03</span><h3>Flexibility</h3><p>Formal guidelines have made flexible and hybrid work requests a normal conversation.</p></li>
<li class="reveal"><span class="no">04</span><h3>Side income</h3><p>Part-time, online and freelance work help many households stretch their budgets.</p></li>
</ol>
<p class="src-note">Sources: Ministry of Manpower, Workforce Singapore, SkillsFuture Singapore.</p>
</div></section>

<section><div class="wrap">
<div class="head reveal"><span class="eyebrow">Latest reads</span><h2>Careers, roles and skills.</h2></div>
<div class="posts index">
{card("article-in-demand-roles.html","In-demand roles")}
{card("article-why-second-income.html","Side income")}
{card("article-upskilling-2026.html","Education &amp; skills")}
{card("article-remote-work-trend.html","Industry trends")}
{card("article-read-labour-data.html","Career advice","4 min")}
{card("article-rising-costs.html","Life &amp; money")}
</div>
<p class="after-tiles"><a href="knowledge-hub.html">See all articles &rarr;</a></p>
</div></section>

<section class="dark" id="second-income"><div class="wrap split">
<div class="reveal feature-img">{img("family","A parent working on a laptop while a child draws at the same table")}</div>
<div class="reveal"><span class="eyebrow">Side income</span><h2>Why more people are adding part-time work to their routine.</h2>
<p class="lede">As living costs rise, many people in Singapore combine a main job with part-time, online or freelance work.</p>
<p>Flexible arrangements, such as home-based and remote roles, can cut commuting time. Pay depends on the role and the hours worked, and it is never guaranteed.</p>
<div class="btn-row"><a class="btn btn-warm" href="article-why-second-income.html">Read the article</a></div></div>
</div></section>

<section><div class="wrap">
<div class="head reveal"><span class="eyebrow">Work types</span><h2>Six common ways to work flexibly.</h2></div>
<div class="minis">
{tile_s("part-time-jobs-singapore.html","Part-time jobs","Under 35 hours a week","part-time")}
{tile_s("work-from-home-jobs-singapore.html","Work from home","Agreed hours, at home","work-from-home")}
{tile_s("remote-jobs-singapore.html","Remote roles","Location flexible","remote")}
{tile_s("online-jobs-singapore.html","Online work","Flexible sessions","online")}
{tile_s("freelance-jobs-singapore.html","Freelancing","Paid per project","freelance")}
{tile_s(ROUTES,"Home-based routes","Compared side by side","hero")}
</div></div></section>

<section class="alt"><div class="wrap">
<div class="head reveal"><span class="eyebrow">Rights &amp; money</span><h2>Practical reads.</h2></div>
<div class="posts index">
{card("article-flexible-work-request.html","Rights")}
{card("article-part-time-cpf.html","Rights","4 min")}
{card("article-remote-cv.html","Career","4 min")}
</div></div></section>

<section id="contact-us"><div class="wrap split">
<div><span class="eyebrow">Contact</span><h2>Have a question or a topic idea?</h2><p class="lede">Write to us. We read every message and use your suggestions to plan new guides.</p></div>
<div>{contact_form()}
{FORM_OK}</div>
</div></section>
''')

# ---------------- JOBS
GUIDE={k:f'<div class="btn-row"><a class="btn btn-primary" href="{v}">Read the full guide</a></div>' for k,v in {"part-time":"part-time-jobs-singapore.html","work-from-home":"work-from-home-jobs-singapore.html","remote":"remote-jobs-singapore.html","online":"online-jobs-singapore.html","freelance":"freelance-jobs-singapore.html"}.items()}
def jobsec(id_,alt,eyebrow,h2,intro,roles,suit,check):
    rl="".join(f"<li>{r}</li>" for r in roles)
    sl="".join(f"<li>{r}</li>" for r in suit)
    cl="".join(f"<li>{r}</li>" for r in check)
    pic={"part-time":"part-time","work-from-home":"work-from-home","remote":"remote","online":"online","freelance":"freelance","contract":"desk"}[id_]
    return f'''<section id="{id_}"{' class="alt"' if alt else ''}><div class="wrap jsec">
<div class="head"><span class="eyebrow">{eyebrow}</span><h2>{h2}</h2><p class="lede">{intro}</p>{img(pic,cls="jimg")}</div>
<div class="jbody"><div class="cols3"><div><h3>Typical roles</h3><ul>{rl}</ul></div><div><h3>A good fit if</h3><ul>{sl}</ul></div><div><h3>Ask before you agree</h3><ul>{cl}</ul></div></div>
{GUIDE.get(id_,"")}</div></div></section>'''

jobs_body=head("Job types","Part-time, home-based, remote and freelance work in Singapore.","A guide to the main kinds of flexible work in Singapore: what each one involves and what to check before you agree.")
jobs_body+='''<section class="alt"><div class="wrap"><div class="head"><span class="eyebrow">At a glance</span><h2>Six kinds of work compared.</h2><p class="lede">A short summary only. Terms differ from one employer to the next, so read yours with care.</p></div>
<div class="tablewrap"><table class="cmp"><thead><tr><th>Job type</th><th>Typical hours</th><th>Where</th><th>Usual status</th><th>CPF</th></tr></thead><tbody>
<tr><td><a href="#part-time">Part-time jobs</a></td><td>Under 35 hrs a week</td><td>On-site or home</td><td>Employee</td><td>Generally applies*</td></tr>
<tr><td><a href="#work-from-home">Work from home</a></td><td>Agreed hours</td><td>Home</td><td>Usually employee</td><td>Generally applies*</td></tr>
<tr><td><a href="#remote">Remote roles</a></td><td>Full or part</td><td>Anywhere</td><td>Employee or contractor</td><td>Depends on status</td></tr>
<tr><td><a href="#online">Online work</a></td><td>Flexible slots</td><td>Online</td><td>Varies</td><td>Depends on status</td></tr>
<tr><td><a href="#freelance">Freelancing</a></td><td>You decide</td><td>Anywhere</td><td>Self-employed</td><td>You manage your own</td></tr>
<tr><td><a href="#contract">Contract and temp</a></td><td>Fixed term</td><td>Varies</td><td>Employee, often via agency</td><td>Generally applies*</td></tr>
</tbody></table></div><p class="notice">*For employees, depending on age, residency and pay. Check CPF Board for current rules. Earnings differ and are not guaranteed.</p></div></section>'''
jobs_body+=jobsec("part-time",False,"Part-time jobs","Part-time jobs in Singapore","Positions with under 35 contracted hours each week. You are usually an employee on a written contract.",
 ["Retail and F&amp;B crew","Office and admin assistants","Tutors and tuition-centre helpers","Event and promotion staff","Customer service associates"],
 ["Study or family duties limit your time","You would like some extra income","You are returning to work gradually"],
 ["How many hours, and which shifts","How and when pay is worked out","CPF and leave","The notice period"])
jobs_body+=jobsec("work-from-home",True,"Work from home","Work-from-home roles in Singapore","Jobs carried out at home within agreed hours, often in service and admin. Working from home and freelancing are not the same thing.",
 ["Chat and email customer support","Data entry and back-office admin","Virtual assistants","Content and social media support","Transcription and translation"],
 ["Family means you need to be home","You want to cut commuting time and cost","You have a quiet corner and dependable internet"],
 ["Employee contract or freelance arrangement?","Who provides the equipment?","Hours and expected reply times","How your work is assessed"])
jobs_body+=jobsec("remote",False,"Remote roles","Remote jobs in Singapore","Roles that don't tie you to one location. Some are with Singapore companies, and others are with overseas teams who want people on Singapore hours.",
 ["Digital marketing and SEO","Graphic and web design","Software development and QA","Account and project management","Recruitment coordination"],
 ["You have a specialist skill","You work well unsupervised","You write clearly and enjoy it"],
 ["Time zone and core hours","Who the employer is, and whether a Singapore entity pays you","Currency and method of payment","How tax and CPF apply"])
jobs_body+=jobsec("online",True,"Online work","Online work and working online from home","Work done wholly over the internet, from live teaching to moderation and research. Real online work is paid by a company you can check, for tasks that are clearly defined.",
 ["Online tutoring","Community and chat moderation","Online research and data labelling","E-commerce listing and order support","Virtual event support"],
 ["You like choosing your time slots","You are at ease with screen-based work","You can stick to a schedule"],
 ["Who pays you, and when","Any request for equipment or registration fees (a warning sign)","What training is given","Terms of the trial period"])
jobs_body+=jobsec("freelance",False,"Freelancing","Freelance work in Singapore","Project work where you are self-employed. You choose your clients, and you also deal with your own CPF, tax and admin.",
 ["Design, illustration and branding","Copywriting and translation","Video and photo editing","Bookkeeping and admin support","Web and app development"],
 ["You want to control your own timetable","You have a portfolio or a niche skill","Uneven income doesn't worry you"],
 ["Scope, deadlines and revisions","Payment terms and any deposit","A written contract for services","Your tax responsibilities"])
jobs_body+=jobsec("contract",True,"Contract and temp","Contract and temporary jobs","Fixed-term roles that cover a project, a busy season or maternity leave. A practical way to gain recent experience.",
 ["Admin and operations cover","Seasonal retail and logistics","Project coordinators","Customer service surge teams"],
 ["You like knowing when it ends","You are coming back after a break","You want to try a firm or industry first"],
 ["Length and renewal of the contract","Whether an agency employs you","Leave and CPF","Whether it could become permanent"])
jobs_body+=f'''<section id="work-from-home-routes"><div class="wrap center"><div class="head"><span class="eyebrow">Working from home</span><h2>Working from home: the main routes.</h2><p class="lede">People looking for income from home usually choose part-time work, freelance projects or contract work. Each is described above. Earnings differ by role, skills and hours and are never guaranteed.</p></div>
<div class="btn-row"><a class="btn btn-primary" href="{ROUTES}">Compare the routes</a><a class="btn btn-ghost" href="#part-time">Part-time jobs</a><a class="btn btn-ghost" href="article-work-modes.html">Read: what the terms mean</a></div></div></section>
<section class="alt" id="where-to-look"><div class="wrap"><div class="head"><span class="eyebrow">Where to look</span><h2>Find genuine openings through official channels.</h2><p class="lede">Current vacancies are posted on these trusted sources.</p></div>
<div class="types">
<div class="type"><span class="n">01</span><h3><a href="https://www.mycareersfuture.gov.sg" rel="noopener">MyCareersFuture</a></h3><p>The government job portal, with search filters and salary information.</p></div>
<div class="type"><span class="n">02</span><h3>Employer careers pages</h3><p>Apply on the official website of a company you have checked.</p></div>
<div class="type"><span class="n">03</span><h3><a href="https://www.mom.gov.sg" rel="noopener">MOM Employment Agency directory</a></h3><p>Check that a recruiter or agency has a valid licence before you share your details.</p></div>
</div></div></section>'''
page("jobs.html",f"Job Types in Singapore: Part-Time, Home-Based, Remote and Freelance | {BRAND}",
"Compare part-time, home-based, remote, online, freelance and contract work in Singapore: typical hours, status, CPF and what to ask before you agree.",jobs_body)

# ---------------- SERVICES
page("services.html",f"Services: Guides and Tools for Flexible Work | {BRAND}","Guides and tools for people exploring flexible work in Singapore, including job type guides, a weekly hours planner and a glossary.",
head("Services","What you will find here.","Free articles, guides and tools about careers and flexible work in Singapore. You don't need to sign up.")+f'''
<section><div class="wrap">
<div class="tiles">
<article class="tile reveal"><div class="ic">{IC["laptop"]}</div><h3>Job type guides</h3><p>For six kinds of flexible work: example roles, a week in the job, first steps, and what to check in contracts, pay and CPF.</p><a class="more" href="jobs.html">Browse job types &rarr;</a></article>
<article class="tile reveal"><div class="ic">{IC["wallet"]}</div><h3>Hours planner</h3><p>Put in a monthly amount and an hourly rate, and see roughly how many hours a week that means.</p><a class="more" href="{ROUTES}#calc">Try the planner &rarr;</a></article>
<article class="tile reveal"><div class="ic">{IC["doc"]}</div><h3>Knowledge Hub</h3><p>Reading on your rights, CPF, job ads, CVs and the cost of living.</p><a class="more" href="knowledge-hub.html">Read articles &rarr;</a></article>
<article class="tile reveal"><div class="ic">{IC["chat"]}</div><h3>Glossary</h3><p>Job-ad jargon such as PMET, CPF and FWA, put plainly.</p><a class="more" href="glossary.html">Look up a term &rarr;</a></article>
<article class="tile reveal"><div class="ic">{IC["globe"]}</div><h3>Official sources</h3><p>Links to where current vacancies and information about your rights are published.</p><a class="more" href="jobs.html#where-to-look">See the sources &rarr;</a></article>
</div></div></section>
<section class="alt"><div class="wrap split">
<div><span class="eyebrow">Get in touch</span><h2>Questions or ideas?</h2><p>Tell us what you would like covered, or point out anything we should correct.</p>
<div class="btn-row"><a class="btn btn-primary" href="contact.html">Contact Us</a></div></div>
</div></section>''')

# ---------------- KNOWLEDGE HUB
posts=[
("trends","Industry trends","article-sectors-hiring.html","5 min",True),
("roles","In-demand roles","article-in-demand-roles.html","5 min",False),
("second","Side income","article-why-second-income.html","5 min",False),
("trends","Industry trends","article-remote-work-trend.html","4 min",False),
("edu","Education & skills","article-upskilling-2026.html","5 min",False),
("career","Career advice","article-read-labour-data.html","4 min",False),
("second","Side income","article-rising-costs.html","5 min",False),
("second","Side income","article-childcare-caregiving.html","5 min",False),
("career","Career advice","article-restart.html","5 min",False),
("career","Career advice","article-remote-cv.html","4 min",False),
("rights","Rights & money","article-flexible-work-request.html","5 min",False),
("rights","Rights & money","article-part-time-cpf.html","4 min",False),
("career","Career advice","article-work-modes.html","5 min",False),
("career","Career advice","article-read-job-ad.html","4 min",False),
("scam","Scams","article-job-scams.html","6 min",False),
]
cards=""
for cat,label,href,m,feat in posts:
    btn_=('<a class="btn btn-warm" href="'+href+'">Read now</a>') if feat else ""
    body_=(f'<a class="thumb" href="{href}" tabindex="-1" aria-hidden="true">{img(ART_IMG[href],lazy=not feat)}</a>'
           f'<div class="pbody"><div class="meta"><span class="cat">{label}</span><span>{m} read</span></div>'
           f'<h3><a href="{href}">{T[href]}</a></h3><p>{EXC[href]}</p>{btn_}</div>')
    feat_=" feature" if feat else ""
    cards+=f'<article class="post{feat_}" data-cat="{cat}">{body_}</article>'
page("knowledge-hub.html",f"Knowledge Hub: Careers, Industries and Skills in Singapore | {BRAND}","Articles on Singapore career paths, industry trends, in-demand roles, training, workers' rights and flexible work.",
head("Knowledge Hub","Articles on careers, industries and skills in Singapore.","Industry trends, in-demand roles, training and the growth of side income, with sources.")+f'''
<section><div class="wrap">
<div class="filters" role="group" aria-label="Filter articles">
<button class="chip" data-filter="all" aria-pressed="true">All</button>
<button class="chip" data-filter="trends" aria-pressed="false">Industry trends</button>
<button class="chip" data-filter="roles" aria-pressed="false">In-demand roles</button>
<button class="chip" data-filter="edu" aria-pressed="false">Education &amp; skills</button>
<button class="chip" data-filter="second" aria-pressed="false">Side income</button>
<button class="chip" data-filter="career" aria-pressed="false">Career advice</button>
<button class="chip" data-filter="rights" aria-pressed="false">Rights &amp; money</button>
<button class="chip" data-filter="scam" aria-pressed="false">Scams</button></div>
<div class="posts index">{cards}</div></div></section>''')

# ---------------- ARTICLES (template)
TAKE={}
EXTRA={}
SOURCES={}
def article(fname,desc,cat,body):
    title=T[fname]
    tk=TAKE.get(fname)
    box=('<aside class="takeaways" aria-label="Key takeaways"><h2>Key takeaways</h2><ol>'+"".join(f"<li>{t}</li>" for t in tk)+"</ol></aside>") if tk else ""
    ex=EXTRA.get(fname)
    if ex:
        body+="<h2>Common questions</h2>"+"".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in ex[0])
        body+='<h2>Keep reading</h2><ul>'+"".join(f'<li><a href="{h}">{t}</a></li>' for h,t in ex[1])+'</ul>'
    src=SOURCES.get(fname)
    if src:
        body+='<h2>Sources</h2><ul class="sources">'+"".join(f'<li><a href="{u}" rel="noopener">{t}</a></li>' for t,u in src)+'</ul>'
    grid_cls="art-grid" if box else "art-grid solo"
    page(fname,title+f" | {BRAND}",desc,f'''<div class="art-head"><div class="wrap"><span class="eyebrow">{cat}</span><h1>{title}</h1><p class="byline">Last reviewed {REVIEWED}</p></div></div>
<div class="wrap art-cover">{img(ART_IMG[fname],lazy=False)}</div>
<section class="art-sec"><div class="wrap {grid_cls}">
<div class="article">{body}
<p style="margin-top:2.5rem"><a href="knowledge-hub.html">&larr; Back to Knowledge Hub</a></p></div>
{box}</div></section>''')

exec(open(pathlib.Path(__file__).with_name("articles2.py"),encoding="utf-8").read())

# ---------------- GLOSSARY
terms=[("Base pay","The fixed portion of your earnings, before commission, bonuses or allowances."),
("Commission-only","Your earnings rest wholly on sales or results, with no fixed amount underneath."),
("Ad hoc","Occasional or one-off work, with no ongoing obligation for either side."),
("Retainer","A recurring fee paid to a freelancer so they stay available for an agreed amount of work."),
("Flexi-hours","Start and finish times that can move, usually around a set block of core hours."),
("FWA","Flexible work arrangement. It covers flexi-time, flexi-place and flexi-load."),
("Core hours","The stretch of the day when colleagues expect you to be reachable, even in flexible or remote roles."),
("Hybrid","A pattern that divides the week between the office and another place, often home."),
("Freelancer","Someone who is self-employed and paid per project or task, and who manages their own tax and contributions."),
("Platform worker","A person who gets work through an app or website, as with ride-hailing and delivery."),
("Gig","A short job built around one task."),
("Contract / temp","Employment for a fixed period, sometimes arranged through an agency."),
("Probation","A trial period at the start of a job, when each side sees if it works."),
("Notice period","How much warning you or the employer must give before the job ends."),
("Training bond","An agreement to stay for a set time after training, or to repay its cost if you leave."),
("PMET","Professionals, Managers, Executives and Technicians."),
("Money mule","Someone whose bank account is used to pass on scam proceeds, often without knowing it. Doing so is a criminal offence.")]
tl="".join(f'<div class="term"><dt>{a}</dt><dd>{b}</dd></div>' for a,b in terms)
page("glossary.html",f"Singapore Recruitment Glossary | {BRAND}","Plain-English definitions of recruitment, part-time, remote and hybrid work terms used in Singapore.",
head("Glossary","Job-ad terms, explained.")+f'''
<section><div class="wrap" style="max-width:860px">
<label for="glossary-search" class="eyebrow">Search the glossary</label>
<input id="glossary-search" class="search" type="search" placeholder="Try &quot;CPF&quot; or &quot;hybrid&quot;" autocomplete="off">
<dl class="glossary">{tl}</dl><p id="glossary-empty" hidden>Nothing found. <a href="contact.html">Ask us to add it.</a></p></div></section>''')

# ---------------- FAQ
faqs=[(f"Is {BRAND} a job board?","No. We write about kinds of work and how they operate in Singapore. To see live vacancies, go to MyCareersFuture or an employer's own careers page."),
(f"Is there a charge for {BRAND}?","No. Everything here is free and needs no account. Be wary of anyone who asks you to pay before you can start a job."),
("Where should I look for part-time work in Singapore?","Start with MyCareersFuture and the careers pages of employers you have checked. Our part-time guide lists questions to ask before you say yes."),
("Do real work-from-home jobs exist in Singapore?","They do. Support, admin, content and many specialist roles are done from home. A genuine employer pays for defined work and does not charge you to begin."),
("How do people bring in income from home?","Mostly through ordinary jobs done at home: part-time employment, freelance projects or contract roles. What you earn depends on the role, your skills and your hours, and it is never certain."),
("Is remote work the same as working from home?","Not quite. Working from home means doing agreed hours at your own place. A remote role lets you work from anywhere and may involve an overseas team, so ask which one is on offer."),
("How can I tell if an online job is genuine?","Find out who pays you, get the terms in writing and walk away from any fee to get started. Legitimate examples include tutoring, moderation and customer support."),
("Do freelancers get CPF?","Not from clients. A freelancer is self-employed and looks after their own contributions, tax and admin. CPF Board and IRAS publish the current rules."),
("May I ask my employer for remote or hybrid hours?","Yes. Employees can put in a formal flexible work arrangement request, and employers are expected to consider it fairly under national guidelines. A yes is not assured."),
("How can I check a recruitment agency?","Look it up in the Employment Agency directory on the MOM website before handing over personal details.")]
fl="".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in faqs)
page("faq.html",f"FAQ: Flexible Work in Singapore | {BRAND}","Answers to common questions about part-time, home-based, remote, online and freelance work in Singapore.",
head("FAQ","Quick answers.")+f'<section><div class="wrap" style="max-width:820px">{fl}<p style="margin-top:2rem">Still have a question? <a href="contact.html">Contact us</a>.</p></div></section>')

# ---------------- ABOUT
page("about.html",f"About Us | {BRAND}",f"{BRAND} is an independent publisher of sourced, practical information on part-time, home-based, remote, online and freelance work in Singapore.",
head("About Us","Information on flexible work in Singapore.")+f'''
<section><div class="wrap split">
<div class="reveal">{img("learning","Adults learning together in a training room",cls="rounded")}<h2 style="margin-top:1.75rem">Who this is for</h2><p>{BRAND} is an independent publication about careers, industry trends and skills in Singapore. It is written for anyone planning a next move, or weighing up part-time, home-based, online or freelance work as a source of extra income. We are not connected with any government agency.</p>
<p>You have limited time, real bills and little patience for jargon. So each guide explains what the work involves, what a typical week looks like, and what to check before you agree to anything.</p></div>
<div class="reveal"><h2>How we write our guides</h2><div class="types">
<div class="type" style="grid-template-columns:1fr"><div><h3>Written for job seekers</h3><p>Every guide answers the questions people actually ask: hours, how pay is worked out, CPF, contracts and how to begin.</p></div></div>
<div class="type" style="grid-template-columns:1fr"><div><h3>Based on official sources</h3><p>We link to MOM, CPF Board, IRAS and MyCareersFuture so you can confirm the details yourself.</p></div></div>
<div class="type" style="grid-template-columns:1fr"><div><h3>Reviewed and dated</h3><p>Each guide shows when it was last reviewed, so you can judge how current it is.</p></div></div></div></div>
</div></section>
<section class="alt"><div class="wrap split">
<div class="reveal"><span class="eyebrow">Who we are</span><h2>The business behind this site.</h2>
<ul class="contact-list">
<li><b>Address</b>{ADDRESS}</li>
<li><b>Email</b>{EMAIL}</li>
<li><b>Phone</b>{PHONE}</li>
</ul></div>
<div class="reveal">{img("skyline","The Singapore skyline at sunset",cls="rounded")}</div>
</div></section>
<section><div class="wrap center"><div class="head"><span class="eyebrow">What you will find</span><h2>Articles, job type guides and tools.</h2></div>
<div class="btn-row"><a class="btn btn-primary" href="jobs.html">Browse job types</a><a class="btn btn-ghost" href="knowledge-hub.html">Knowledge Hub</a></div>
<p class="notice" style="max-width:70ch;margin:2rem auto 0">{BRAND} shares general information about work in Singapore. It is not legal, financial or employment advice.</p></div></section>''')

# ---------------- CONTACT
page("contact.html",f"Contact Us | {BRAND}",f"Contact {BRAND} with a question, a correction or a topic suggestion about flexible work in Singapore.",
head("Contact Us","Get in touch.","Ask a question, report a mistake or suggest a topic. Please leave out your NRIC, bank or Singpass details.")+f'''
<section><div class="wrap split">
<div>
{contact_form(with_topic=True)}
{FORM_OK}
</div>
<div><h2>Contact details</h2><ul class="contact-list">
<li><b>Email</b>{EMAIL}</li>
<li><b>Phone</b>{PHONE}</li>
<li><b>Address</b>{ADDRESS}</li>
</ul></div>
</div></section>''')

# ---------------- DISCLAIMER
page("disclaimer.html",f"Disclaimer | {BRAND}",f"Disclaimer for {BRAND}, an information website about part-time, home-based, remote and freelance work in Singapore.",
head("Disclaimer","Disclaimer")+f'''
<section><div class="wrap article">
<h2>General information only</h2><p>{BRAND} offers general information on part-time, home-based, remote, online, freelance and contract work in Singapore. It is not an employment agency. It does not list vacancies, and it does not recruit, screen, place or introduce anyone.</p>
<h2>No assurance about work or pay</h2><p>Nothing here is an offer of work or a statement of what you will earn. Pay, hours and terms vary by employer and role, and they change over time.</p>
<h2>Not advice</h2><p>The content is not legal, financial, tax or employment advice. Rules on CPF, contracts and flexible work are revised from time to time, so please confirm them with the Ministry of Manpower, CPF Board, IRAS or a qualified adviser.</p>
<h2>Other websites</h2><p>Some pages link to official or third-party sites for reference. We don't run them and can't answer for what they say.</p>
<h2>Keeping it correct</h2><p>We aim to keep the information accurate and up to date, but can't promise that nothing has changed since it was last reviewed. If you spot an error, <a href="contact.html">let us know</a>.</p>
</div></section>''')

# ---------------- PRIVACY
page("privacy.html",f"Privacy Policy | {BRAND}",f"How {BRAND} collects, uses, discloses and protects personal data under Singapore's Personal Data Protection Act 2012 (PDPA).",
head("Privacy Policy","Privacy Policy",f"Last updated: {PRIVACY_UPDATED}")+f'''
<section><div class="wrap article">
<p>This website is published as {BRAND}. This policy describes what personal data we handle when you visit or write to us, and why, in line with Singapore's Personal Data Protection Act 2012 (the "PDPA").</p>
<p>Using the site or sending us your details means you accept the practices set out below.</p>

<h2>1. About this website</h2>
<p>{BRAND} is an independent site with articles and tools on careers, industries and skills in Singapore. It is not an employment agency. It does not list vacancies and does not recruit, screen or place candidates.</p>

<h2>2. What we collect</h2>
<p>We hold personal data only if you send it to us yourself, through the contact form or by email. That can include:</p>
<ul><li>your name;</li><li>your email address;</li><li>whatever you write in your message.</li></ul>
<p>Please do not include your NRIC number, Singpass details, OTPs, bank details or passwords. We will never ask for any of them.</p>
<p>The hours planner works inside your browser. Whatever you type there stays on your device and is never sent to us.</p>

<h2>3. Server and technical records</h2>
<p>Our hosting service may log routine technical details such as your IP address, browser type and the pages you open. These records help keep the site secure and running.</p>

<h2>4. Why we use your data</h2>
<p>Your personal data is used only to:</p>
<ul><li>answer your question, comment or correction;</li><li>weigh up a topic you propose;</li><li>keep the site safe and working;</li><li>comply with the law.</li></ul>
<p>We will not send you marketing without your consent, and we do not sell personal data.</p>

<h2>5. Who may receive it</h2>
<p>We pass personal data on only in these cases:</p>
<ul><li>to providers that host the site or handle our email, and who are bound to look after it;</li><li>when the law requires or permits it, such as a court order or a request from a regulator or the authorities;</li><li>when you have agreed.</li></ul>

<h2>6. Data held overseas</h2>
<p>A provider may store or process data outside Singapore. If so, we take reasonable steps to make sure it is protected to a standard comparable to the PDPA.</p>

<h2>7. Security and how long we keep data</h2>
<p>We take reasonable precautions against unauthorised access, collection, use, disclosure, copying, changes or disposal of the data we hold. Because nothing sent over the internet is entirely safe, we can't promise complete security.</p>
<p>Data is kept only while it is needed for the purposes in section 4, or where the law says we must keep it. After that we delete it or make it anonymous.</p>

<h2>8. Your choices and rights</h2>
<p>Under the PDPA, you can:</p>
<ul><li>request a copy of the personal data we hold about you, and be told how it has been used or disclosed over the past year;</li><li>ask for mistakes or gaps in it to be corrected;</li><li>withdraw consent to how we collect, use or disclose it.</li></ul>
<p>Send any request to our Data Protection Officer using the details below. We may ask you to prove who you are and will answer within a reasonable time. If you withdraw consent, we will tell you what that means, and we might not be able to carry on with your enquiry.</p>

<h2>9. Links to other sites</h2>
<p>Pages here point to websites run by other organisations, including government agencies. Their privacy practices are their own, so read their policies before you share your data with them.</p>

<h2>10. Younger visitors</h2>
<p>The site is meant for a general adult audience, not for children. If you think a child has sent us personal data, contact us and we will remove it.</p>

<h2>11. Updates</h2>
<p>This policy may be revised from time to time. The current version, with its date, is always on this page.</p>

<h2>12. Data Protection Officer</h2>
<p>For questions, requests or complaints about personal data, contact:</p>
<ul><li><strong>Data Protection Officer, {BRAND}</strong></li><li>Email: {EMAIL}</li><li>Phone: {PHONE}</li><li>Address: {ADDRESS}</li></ul>
<p>If our reply does not satisfy you, you may approach the Personal Data Protection Commission at <a href="https://www.pdpc.gov.sg" rel="noopener">www.pdpc.gov.sg</a>.</p>
</div></section>''')

# ---------------- THANK YOU
page("thank-you.html",f"Thank You | {BRAND}",f"A note for visitors who have just written to {BRAND}.",
head("Thank you","Thanks for getting in touch.","If your email app opened with your message, please press send there to complete it. We only receive a message once you send it.")+f'''
<section><div class="wrap">
<p style="max-width:62ch">While you are here, you are welcome to read more of our articles on careers, industries and skills in Singapore.</p>
<div class="btn-row"><a class="btn btn-primary" href="knowledge-hub.html">Read more articles</a><a class="btn btn-ghost" href="index.html">Back to home</a></div>
<p class="notice" style="margin-top:2rem">Prefer to write directly? Email {EMAIL} or call {PHONE}.</p>
</div></section>''',extra_head='<meta name="robots" content="noindex">\n')

exec(open(pathlib.Path(__file__).with_name("jobpages.py"),encoding="utf-8").read())

# ---------------- housekeeping
# Remove stale pages from earlier builds (e.g. a renamed page) and old root-level html files.
for old in OUT.glob("*.html"):
    old.unlink()
for d in OUT.iterdir():
    idx = d / "index.html"
    if d.is_dir() and d.name not in ("tools", ".cursor") and idx.exists() and idx not in BUILT:
        idx.unlink()
        if not any(d.iterdir()):
            d.rmdir()
        print("removed stale page:", d.name)

(OUT / "robots.txt").write_text(
    "User-agent: *\nDisallow: /\n" if PLACEHOLDERS else "User-agent: *\nAllow: /\n", encoding="utf-8")
if PLACEHOLDERS:
    print("NOTE: placeholders remain in tools/identity.py (" + ", ".join(PLACEHOLDERS) + ").")
    print("      Pages are marked noindex and robots.txt blocks crawlers until you fill them in.")
print("built", len(BUILT), "pages")
