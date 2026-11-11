# Long-form job type guides. Executed from build.py (shares its globals: page, out_path, BRAND, REVIEWED, ROUTES).

def _li(items): return "".join(f"<li>{i}</li>" for i in items)

def jobpage(fname,cls,eyebrow,h1,seo_title,seo_desc,intro,facts,roles,week,steps,know,questions,mistakes,faqs,related):
    facts_html="".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k,v in facts)
    roles_html="".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a,b in roles)
    week_html="".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for a,b,c in week)
    steps_html="".join(f'<li><b>{i+1}</b><h3>{t}</h3><p>{d}</p></li>' for i,(t,d) in enumerate(steps))
    know_html="".join(f'<article class="tile"><h3>{t}</h3><p>{d}</p></article>' for t,d in know)
    faq_html="".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in faqs)
    rel_html="".join(f'<a class="rel" href="{h}"><b>{t}</b><span>{d}</span></a>' for h,t,d in related)
    body=f'''
<div class="page-head jobhero {cls}"><div class="wrap">
<div class="jh-top">
<div class="jh-main"><span class="eyebrow">{eyebrow}</span><h1>{h1}</h1><p class="lede">{intro}</p>
<div class="btn-row"><a class="btn btn-primary" href="jobs.html">Compare all job types</a><a class="btn btn-ghost" href="knowledge-hub.html">Knowledge Hub</a></div></div>
<figure class="jh-img">{img(PAGE_IMG[fname],lazy=False)}</figure>
</div>
<aside class="qf" aria-label="Quick facts"><h2>Quick facts</h2><dl>{facts_html}</dl><p class="rv">Last reviewed {REVIEWED}</p></aside>
</div></div>
<div class="wrap doc">
<nav class="toc" aria-label="On this page"><ol>
<li><a href="#roles">Role overview</a></li>
<li><a href="#week">A typical week</a></li>
<li><a href="#start">Getting started</a></li>
<li><a href="#check">Before you say yes</a></li>
<li><a href="#ask">Questions to ask</a></li>
<li><a href="#faq">FAQ</a></li>
<li><a href="#related">Related reading</a></li>
</ol></nav>
<div class="doc-body">
<section id="roles"><div class="head"><span class="eyebrow">Role overview</span><h2>A look at the work itself.</h2></div>
<div class="tablewrap"><table class="cmp"><thead><tr><th>Role</th><th>What it involves</th></tr></thead><tbody>{roles_html}</tbody></table></div></section>
<section id="week"><div class="head"><span class="eyebrow">A typical week</span><h2>Fitting it around your day.</h2><p class="lede">An illustration only. Actual schedules depend on the employer.</p></div>
<div class="tablewrap"><table class="cmp"><thead><tr><th>Day</th><th>Time</th><th>Activity</th></tr></thead><tbody>{week_html}</tbody></table></div></section>
<section id="start"><div class="head"><span class="eyebrow">Getting started</span><h2>{len(steps)} steps.</h2></div><ol class="steps">{steps_html}</ol></section>
<section id="check"><div class="head"><span class="eyebrow">Before you say yes</span><h2>Points worth checking.</h2></div><div class="tiles">{know_html}</div></section>
<section id="ask"><div class="vs"><div class="vs-col good"><h2>Questions to ask</h2><ul class="qlist">{_li(questions)}</ul></div><div class="vs-col bad"><h2>Mistakes to avoid</h2><ul class="qlist bad">{_li(mistakes)}</ul></div></div></section>
<section id="faq" class="faq-sec"><div class="head"><span class="eyebrow">FAQ</span><h2>Common questions.</h2></div>{faq_html}</section>
<section id="related"><div class="head"><span class="eyebrow">Related reading</span><h2>More guides.</h2></div><div class="rels">{rel_html}</div>
<p class="notice" style="margin-top:1.5rem">General information only. Pay, hours and conditions differ by employer and are not guaranteed. Please confirm details with <a href="https://www.mom.gov.sg" rel="noopener">MOM</a>, <a href="https://www.cpf.gov.sg" rel="noopener">CPF Board</a> or <a href="https://www.iras.gov.sg" rel="noopener">IRAS</a>.</p></section>
</div></div>
<section class="cta-band"><div class="wrap" style="text-align:center;max-width:680px"><h2>Noticed something out of date?</h2><p class="lede" style="margin-inline:auto">Rules and conditions change. Let us know if anything here needs updating.</p><div class="btn-row" style="justify-content:center"><a class="btn btn-warm" href="contact.html">Contact Us</a></div></div></section>'''
    page(fname,seo_title,seo_desc,body)

# ------------------------------------------------------------------ part-time
jobpage("part-time-jobs-singapore.html","jh1","Part-time jobs","Part-time jobs in Singapore: roles, hours and what to check",
f"Part-Time Jobs in Singapore: Roles, Hours, CPF and How to Start | {BRAND}",
"A practical guide to part-time jobs in Singapore: common roles, typical hours, how to start, and what to check on contracts, pay and CPF before you accept.",
"A part-time job often sits alongside study, a day job or caring duties. What matters most is practical: how shifts are scheduled, what the pay works out to after travel, and how much notice you get when plans change.",
[("Typical hours","Under 35 a week"),("Where","Usually on-site, sometimes home-based"),("Usual status","Employee"),("CPF","Generally applies to employees*"),("Good for","Students, parents, caregivers and people topping up their income")],
[("Retail and F&amp;B crew","Front-of-house work: serving customers, taking payment, restocking and closing up. Evenings and weekends are common."),("Admin assistant","Office support such as filing, data entry, diary management and fielding enquiries, mostly on weekdays."),("Tutor or centre assistant","Helping to run lessons, marking work and manning reception. Demand peaks after school and on weekends."),("Event and promotions staff","Short stints at exhibitions, roadshows and launches, hired project by project."),("Customer service associate","Answering calls, chats and emails from customers on a set shift pattern.")],
[("Monday","Free","Study or main job"),("Tuesday","6pm to 10pm","Evening shift"),("Thursday","6pm to 10pm","Evening shift"),("Saturday","10am to 6pm","Weekend shift"),("Sunday","Free","Rest and family time")],
[("Map out when you are free","Write down the days and time slots you can commit to every week, travel included. Dependability matters more than squeezing in the most hours."),("Put together a one-page CV","Highlight reliability, availability and any experience dealing with customers. One page is plenty."),("Look in the right places","Check MyCareersFuture and the careers pages of employers you recognise, and read each listing in full, hours and pay included."),("Pin down the terms","Before accepting, confirm the hours, pay rate, pay day, CPF and leave. Ask for these in writing."),("Review after a few weeks","See whether the schedule still suits you, and speak up early if it does not.")],
[("Rostering","Find out how early shifts are released and how swaps are handled. School holidays, festive periods and sales often mean extra or longer shifts."),("How you are paid","Check whether pay is hourly or monthly, when it arrives and how public holiday work is treated. Hold on to your payslips."),("CPF and leave","Ask for written confirmation that CPF is paid from month one, and how leave is calculated pro rata."),("Your main job","Look for outside-work clauses in your existing contract before committing. Work pass holders should check with MOM first.")],
["Are the weekly hours fixed, or rostered?","What is the pay rate, and which day of the month is pay day?","Is this an employment contract that includes CPF?","How much warning will I get if a shift changes?","How long is probation, and what notice applies?","Who should I speak to if my availability changes?"],
["Saying yes before you know the hours","Not checking whether pay is hourly or monthly","Taking on more than you can sustain","Overlooking restrictions in your main job's contract"],
[("What counts as part-time in Singapore?","If you are contracted for fewer than 35 hours a week, you are a part-time employee under the part-time employment rules."),("Is leave available to part-timers?","Generally yes, calculated pro rata. The MOM website sets out the current rules."),("Can I hold a part-time job as well as a full-time one?","Often you can, but check the full-time contract first because some employers require approval for outside work.")],
[("article-part-time-cpf.html","Part-Time Work and CPF","What to look for on your payslip"),("article-read-job-ad.html","Reading a job ad","Making sense of pay, hours and terms"),("work-from-home-jobs-singapore.html","Work-from-home roles","The next guide")])

# ------------------------------------------------------------------ work from home
jobpage("work-from-home-jobs-singapore.html","jh2","Work from home","Work-from-home roles in Singapore: what they involve and how to start",
f"Work-From-Home Roles in Singapore: Jobs, Setup and What to Ask | {BRAND}",
"A guide to working from home in Singapore: common roles, a sample week, the setup you need, and what to check on contracts and expectations.",
"Most home-based jobs in Singapore are service or admin roles with fixed hours. A good one and a poor one tend to differ in the details: who supplies equipment, how closely you are monitored and who covers which costs.",
[("Typical hours","Agreed hours, part-time or full-time"),("Where","At home"),("Usual status","Normally employee"),("CPF","Generally applies to employees*"),("Good for","Parents, caregivers and anyone who wants to cut commuting")],
[("Customer support agent","Replying to customers by chat, email or phone through the company's systems."),("Data entry and back-office admin","Keeping records up to date, processing forms and checking figures."),("Virtual assistant","Looking after calendars, inboxes and bookings for a business or a busy individual."),("Content and social media support","Writing posts, scheduling them, making simple graphics and answering community comments."),("Transcription and translation","Converting recordings to text or translating documents, often paid per task.")],
[("Monday to Friday","9am to 1pm","Support shift from home"),("Wednesday","2pm to 3pm","Video check-in with the team"),("Afternoons","Free","Errands, family or other work"),("Weekend","Off","No work")],
[("Create a workable space","You need a quiet corner, dependable internet and a laptop. Ask whether the employer supplies equipment."),("Take stock of your skills","Think about communication, accuracy and the tools you already handle, such as email, spreadsheets and chat apps."),("Search official channels","Use MyCareersFuture and the careers pages of employers you have checked. Find out whether the role is employment or freelance."),("Clarify what is expected","Ask about reply times, core hours, tools, supervision and how performance is judged."),("Get the terms in writing","Hours, pay, CPF, equipment and notice period should all be written down.")],
[("Equipment and costs","Find out who provides the laptop and software, and whether you are expected to pay for your own internet or electricity."),("Monitoring and availability","Some roles log activity or expect quick replies. Ask how performance is measured and what response times apply."),("Employee or freelance","The job title won't say. The answer decides CPF, leave and who deals with tax, so ask directly."),("Customer data","If you handle customer information, expect company rules on devices and storage, in line with the PDPA.")],
["Is this employment, or freelance work?","What are the core hours, and how is time recorded?","Who supplies the equipment and software?","How is pay worked out, and when does it arrive?","Is training paid?","Can the hours change, and with how much notice?"],
["Assuming that home-based means no set hours","Not finding out whether CPF applies","Handling company data on a shared or unsecured device","Leaving the terms unwritten"],
[("Are home-based jobs in Singapore genuine?","Yes. Many employers recruit for support, admin and content roles that can be done at home. Check the employer and the terms just as you would for any job."),("How does working from home differ from remote work?","Working from home usually means fixed hours from your own home. Remote work can mean any location, and sometimes an overseas team. Our remote jobs guide explains more."),("Will I need my own laptop?","That depends on the employer, so ask before you accept.")],
[("remote-jobs-singapore.html","Remote jobs in Singapore","The wider picture"),("article-work-modes.html","What the terms mean","Part-time, remote, hybrid and freelance"),("article-flexible-work-request.html","Asking for flexible work","If you already have a job")])

# ------------------------------------------------------------------ remote
jobpage("remote-jobs-singapore.html","jh3","Remote roles","Remote jobs in Singapore: skills, employers and what to clarify",
f"Remote Jobs in Singapore: Roles, Skills, Time Zones and Tax | {BRAND}",
"A guide to remote jobs for people in Singapore: common roles, skills employers look for, time zone and employing-entity questions, and how tax and CPF can differ.",
"Remote roles usually reward specialist skills, and plenty are with overseas teams. If you live in Singapore, the questions that matter are practical ones: who your employer is, how your hours overlap with theirs, and how tax and CPF will work.",
[("Typical hours","Part-time or full-time"),("Where","Anywhere, with agreed overlap hours"),("Usual status","Employee or contractor"),("CPF","Depends on employer and status*"),("Good for","Self-directed people with specialist skills")],
[("Digital marketing and SEO","Planning campaigns and content, tracking results and improving search visibility."),("Graphic and web design","Creating visuals, page layouts and websites for brands."),("Software and QA","Writing or testing code as part of a distributed team."),("Account or project management","Keeping clients, timelines and deliverables on track online."),("Customer success","Helping new customers get started with, and get value from, software or online services.")],
[("Monday to Thursday","9am to 5pm","Core hours and a short daily stand-up"),("Friday","9am to 1pm","Half day for planning and reporting"),("Weekend","Off","No work")],
[("Let your work speak","Assemble a small portfolio or a few work samples. Remote employers cannot watch you work, so evidence of results counts."),("Aim at suitable roles","Search by skill, and look for listings that are open to people based in Singapore."),("Find out who the employer is","Confirm the legal employer, its location and the way you will be paid."),("Get ready for video interviews","Test your camera, microphone and connection, and have examples of independent work to hand."),("Ask about tax and CPF","Find out how employment, tax and CPF will be handled for your circumstances.")],
[("Employing entity","CPF is linked to employment by a Singapore employer. If your employer is overseas, or you work as a contractor, the position can be different. Check with CPF Board and IRAS."),("Time zone","Find out which hours you must be online and how much room there is to adjust them."),("Pay","Confirm the currency, how you will be paid and when, plus any conversion or bank charges."),("Tax","Money from an overseas employer is still income. Ask IRAS how it applies to you.")],
["Who is my legal employer, and where are they based?","Which time zone and core hours apply?","Am I an employee or a contractor?","Which currency and payment method will be used?","What equipment and tools will I be given?","How will tax and CPF be dealt with?"],
["Overlooking how far the time zones overlap","Assuming CPF comes with an overseas contractor role","Failing to keep income records for tax","Leaving the terms unwritten"],
[("Is remote work only for people in tech?","No. Marketing, design, support, project management and content roles are often remote too."),("Must I be in Singapore to be hired?","Some employers require it for tax or legal reasons and others don't. Raise it early."),("Is income from an overseas employer taxable?","How it is treated depends on your situation. Ask IRAS or a tax professional.")],
[("freelance-jobs-singapore.html","Freelance work in Singapore","If you would rather be self-employed"),("article-remote-cv.html","A CV for remote roles","Showing you can work independently"),("online-jobs-singapore.html","Online work","Work delivered entirely online")])

# ------------------------------------------------------------------ online
jobpage("online-jobs-singapore.html","jh4","Online work","Online work in Singapore: roles, pay terms and what to check",
f"Online Work in Singapore: Roles, Pay Terms and What to Check | {BRAND}",
"A guide to online work from home in Singapore: common roles, a sample week, how to start, and questions to ask about pay and terms.",
"Online work covers everything from tutoring and moderation to research and shop support. With so much variety, the key points to nail down are who is paying you and on what terms.",
[("Typical hours","Flexible slots or fixed sessions"),("Where","Online"),("Usual status","Varies: employee or freelance"),("CPF","Depends on status*"),("Good for","People who like flexible slots and screen-based work")],
[("Online tutor","Giving lessons to students on video, one to one or in small groups."),("Community and chat moderator","Making sure online spaces stay safe and relevant."),("Online researcher or data labeller","Looking up, verifying or tagging information for projects."),("E-commerce support","Adding product listings, processing orders and replying to shop enquiries."),("Virtual event support","Running chat, sign-ups and the technical side of online events.")],
[("Tuesday","7pm to 9pm","Tutoring sessions online"),("Thursday","7pm to 9pm","Tutoring sessions online"),("Sunday","2pm to 5pm","Order and listing support"),("Other days","Free","Main job, study or rest")],
[("Choose what you can offer","Teaching, writing, research, admin and customer support are all sought after online."),("Get your tools ready","You will need dependable internet, a quiet place and whatever software the role uses."),("Look for a business you can identify","You should be able to find out who is paying you, and how."),("Agree the terms in writing","Make sure the rate, hours, payment date and your status as employee or freelancer are on paper."),("Begin modestly","Ask for a trial period or a small first batch of work before you commit further.")],
[("Who pays you","Before you start, you should know the business name and how payment will reach you."),("Costs of starting","Nobody should charge you to begin work. If a fee comes up, stop and check the business."),("Your status","Online roles may be employment or freelance, and that changes CPF, leave and tax."),("Trial work","Find out whether the first tasks are paid, and on what terms.")],
["Who is the business, and how can I check it?","Is pay by the hour, by the task or by the month?","When, and how, will I be paid?","Will I be charged anything to start? (You should not be.)","Is this employment or freelance work?","What happens when a session is cancelled?"],
["Paying a fee to start work","Working without knowing who is paying you","Forgetting about tax on freelance income","Relying on chat messages in place of written terms"],
[("Is online work legitimate?","A lot of it is. Online tutoring, moderation and support are established roles. Check the employer and the terms."),("What does online work from home mean?","It is work you do from home over the internet, such as tutoring, support or admin, for an agreed rate."),("Is CPF paid on online work?","Only if you are an employee under a contract of service. Freelancers handle their own contributions.")],
[("work-from-home-jobs-singapore.html","Work-from-home roles","Fixed-hours roles done at home"),("freelance-jobs-singapore.html","Freelance work","Self-employed online work"),("article-read-job-ad.html","Reading a job ad","Making sense of pay and terms")])

# ------------------------------------------------------------------ freelance
jobpage("freelance-jobs-singapore.html","jh5","Freelancing","Freelance work in Singapore: how to start and what to know",
f"Freelance Work in Singapore: How to Start, Contracts, Tax and MediSave | {BRAND}",
"A guide to freelancing in Singapore: common freelance roles, how to find clients, contracts, invoicing, tax and MediSave basics.",
"Freelancing swaps a regular payslip for control over your time and your clients. In return, contracts, invoices and tax all land on your desk.",
[("Typical hours","Set by you"),("Where","Anywhere"),("Usual status","Self-employed"),("CPF","You handle your own contributions*"),("Good for","People with a portfolio or a specialist skill")],
[("Design and branding","Producing logos, social media graphics, layouts and illustrations."),("Writing and translation","Drafting articles and copy, editing text and translating between languages."),("Video and photo editing","Cutting footage, retouching photos and producing short clips."),("Bookkeeping and admin","Logging transactions and tidying up records for small businesses."),("Web and app development","Creating and maintaining websites and small applications.")],
[("Monday","9am to 12pm","Work for client A"),("Tuesday and Wednesday","10am to 3pm","Work for client B, plus admin"),("Thursday","Afternoon","Sending invoices and seeking new clients"),("Friday","Free","A day off, or your main job")],
[("Pick a niche","Concentrate on one or two services that you do well and can describe in a single sentence."),("Assemble a portfolio","Two or three strong examples are enough to begin with."),("Set your pricing","Charge by the hour or by the project, and allow for revisions, admin and tax."),("Look for clients","Try referrals, your own network, online platforms and professional profiles."),("Write everything down","A written agreement should cover the scope, deadlines, revisions and payment terms."),("Keep a record of income","Log every payment, because freelance income has to be declared.")],
[("Contract for services","Set out the scope, deadline, revisions and payment terms on paper. For bigger projects, think about asking for a deposit."),("Tax","Freelance earnings are taxable and must be declared to IRAS. Keep records of what comes in and goes out."),("MediSave","Depending on income, self-employed people may have to contribute to MediSave. CPF Board has the details."),("Business registration","Depending on how you trade, you might need to register a business with ACRA. ACRA and IRAS can advise.")],
["What does the project cover, exactly?","How many rounds of revisions are included?","What is the payment schedule, and when is each payment due?","Who owns the finished work?","Is a deposit needed?","How are changes to the scope handled?"],
["Starting without a written agreement","Pricing too low and forgetting admin time","Neglecting to record income for tax","Juggling more clients than you can handle"],
[("Is employer CPF paid to freelancers?","No. Freelancers get no employer CPF contribution, though self-employed people may need to pay into MediSave, depending on income. CPF Board has current information."),("Must I register a business before freelancing?","That depends on how you work. ACRA and IRAS can tell you what applies to your case."),("Where do freelancers in Singapore find clients?","Typical sources are referrals, professional networks and online platforms.")],
[("remote-jobs-singapore.html","Remote jobs","If you would rather be employed"),("article-work-modes.html","What the terms mean","Freelancer or employee"),(ROUTES,"Working from home: routes compared","Weigh up the options")])

# ------------------------------------------------------------------ routes compared
jobpage(ROUTES,"jh6","Working from home","Working from home in Singapore: the main routes compared",
f"Working From Home in Singapore: Part-Time, Freelance and Online Routes Compared | {BRAND}",
"Compare the main ways of earning from home in Singapore: part-time jobs, work-from-home roles, online work and freelancing, with a simple hours planner.",
"Most people who want to earn from home in Singapore pick one of four routes: a part-time job, a home-based role, online work or freelancing. Each one suits a different mix of hours, skills and need for stability.",
[("Routes","Part-time, work from home, online, freelance"),("Time needed","From a few hours a week"),("Best start","Choose the route that matches your hours"),("Earnings","Differ by role and skills, never guaranteed")],
[("Part-time employment","Regular hours under a contract, either at a workplace or at home. <a href='part-time-jobs-singapore.html'>Read the guide</a>."),("Work-from-home role","A defined position with set hours, done from home. <a href='work-from-home-jobs-singapore.html'>Read the guide</a>."),("Online work","Tutoring, moderation, research and support delivered over the internet. <a href='online-jobs-singapore.html'>Read the guide</a>."),("Freelance projects","Work paid per project, with you in charge of the schedule. <a href='freelance-jobs-singapore.html'>Read the guide</a>.")],
[("Step 1","Set a monthly target","Decide how much extra you would like to bring in each month."),("Step 2","Estimate an hourly rate","Take a rate from a real listing or from your own quote."),("Step 3","Work out the weekly hours","Use the planner on this page.")],
[("Set your target","Note down the extra monthly amount you need, alongside your fixed costs."),("Count your spare hours","Be honest about how many hours you can give each week."),("Choose a route","Steady hours point to part-time work, while skills and independence point to freelancing."),("Search official sources","MyCareersFuture and employers' own pages are good places to start."),("Check back after a month","See whether the hours, the pay and your energy levels are still working.")],
[("Realistic expectations","Earnings depend on the role, your skills and your hours. Treat any offer of high pay for little effort with suspicion."),("Costs","Allow for transport, equipment, internet and any tax on what you earn."),("Your rights","Employees have contracts, CPF and leave, while freelancers look after their own tax and contributions."),("Balance","Extra income shouldn't leave you exhausted, so build in time to rest.")],
["How many hours can I give each week?","Do I need a steady income, or flexibility?","Is this employment or self-employment?","What costs will I have?","How will I keep track of income for tax?","Does my main job allow outside work?"],
["Chasing offers that promise easy money","Overlooking costs and tax","Committing to more hours than you can keep up","Leaving the terms unwritten"],
[("Is there a single best way to earn from home in Singapore?","No, it depends on your skills and available hours. Part-time and home-based roles give steady hours, while freelancing gives you more control."),("Can I begin without experience?","Some entry-level roles, such as support or admin, don't ask for much experience, though employers differ."),("Do I have to declare money earned at home?","Yes. Income from employment and freelance work is taxable. Check with IRAS.")],
[("part-time-jobs-singapore.html","Part-time jobs","Steady hours"),("freelance-jobs-singapore.html","Freelance work","Control over your schedule"),("article-rising-costs.html","Household costs and flexible work","Where extra income can fit")])

# Hours planner on the routes page (inserted before the FAQ), plus wording specific to this page.
_p=out_path(ROUTES)
_h=_p.read_text(encoding="utf-8")
_calc='''<section id="calc-sec" class="calc-sec"><div class="split"><div><span class="eyebrow">Hours planner</span><h2>How many hours a week might a target need?</h2><p class="lede">Enter your own figures. Nothing is saved or sent, and this is a planning aid, not a promise of income.</p></div>
<form class="fit" id="calc" onsubmit="return false"><div class="field"><label for="c-target">Extra monthly amount you are aiming for ($)</label><input id="c-target" type="number" min="0" inputmode="decimal"></div>
<div class="field"><label for="c-rate">Hourly rate you expect ($)</label><input id="c-rate" type="number" min="0" inputmode="decimal"></div>
<div id="c-out" class="fit-out" role="status" aria-live="polite" hidden></div></form></div></section>'''
_h=_h.replace('<section id="faq" class="faq-sec">',_calc+'<section id="faq" class="faq-sec">',1)
assert 'id="calc"' in _h, "hours planner was not inserted"
for a,b in [("Role overview","The routes"),("A look at the work itself.","The four routes at a glance."),("A typical week","Work it out"),("Fitting it around your day.","Three steps to a realistic plan."),
            ("An illustration only. Actual schedules depend on the employer.","Use the planner further down for step 3."),("<th>Day</th><th>Time</th><th>Activity</th>","<th>Step</th><th>Action</th><th>Detail</th>")]:
    assert a in _h, "missing: "+a
    _h=_h.replace(a,b)
_p.write_text(_h,encoding="utf-8")
