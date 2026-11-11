# All article copy. Executed from build.py (shares its globals: article, T, TAKE, EXTRA, SOURCES).
MOM="https://www.mom.gov.sg"
SRC={
"mom":("Ministry of Manpower: Labour market statistics",MOM+"/resources-and-tools/statistics"),
"momfwa":("Tripartite Guidelines on Flexible Work Arrangement Requests (TAFEP)","https://www.tafep.sg"),
"sf":("SkillsFuture Singapore","https://www.skillsfuture.gov.sg"),
"wsg":("Workforce Singapore","https://www.wsg.gov.sg"),
"mcf":("MyCareersFuture","https://www.mycareersfuture.gov.sg"),
"sd":("Singapore Department of Statistics","https://www.singstat.gov.sg"),
"cpf":("CPF Board","https://www.cpf.gov.sg"),
}
def stats(items):
    return '<div class="statrow">'+"".join(f'<div class="stat"><b>{n}</b><span>{t}</span></div>' for n,t in items)+'</div>'
for k,v in {
"article-sectors-hiring.html":["mom","wsg","sd"],
"article-in-demand-roles.html":["mom","mcf","wsg"],
"article-why-second-income.html":["mom","sd","cpf"],
"article-remote-work-trend.html":["momfwa","mom"],
"article-upskilling-2026.html":["sf","wsg"],
"article-read-labour-data.html":["mom","sd","mcf"],
}.items(): SOURCES[k]=[SRC[x] for x in v]

TAKE.update({
"article-sectors-hiring.html":["Official labour reports most often point to healthcare, technology, finance, professional services and logistics.","Growth is patchy: certain roles are hard to fill, while others draw crowds of applicants.","Before settling on a direction, read the latest quarterly MOM report.","Skills move between sectors more easily than job titles do."],
"article-in-demand-roles.html":["Demand clusters around care, data, digital work, finance and operations.","Many of these roles also exist in part-time, contract or remote form.","Salaries vary a great deal, so compare recent listings with official pay data.","A short course can open the door to a neighbouring role."],
"article-why-second-income.html":["A part-time role adds income without you giving up your main job.","Home-based and freelance work can save commuting time.","Side income works best when hours, tax and CPF are clear from day one.","Treat online earnings claims with caution, because pay follows the work done."],
"article-remote-work-trend.html":["Requests for flexible work now have a place in national guidelines.","Remote listings run from fully remote to hybrid.","Working from home is normally agreed as a set of hours and a place.","An employer may still say no, but should explain why."],
"article-upskilling-2026.html":["SkillsFuture Credit and course subsidies can bring down the cost of training.","Choose training tied to a role you can see advertised.","Short, stackable courses suit people who work part-time as well.","Make sure a course is approved before you pay for it."],
"article-read-labour-data.html":["Unemployment and vacancy figures describe different things.","Look at your own sector and role, not only the headline number.","A wage figure is a median, not a promise.","Begin with official publications and treat commentary as secondary."],
"article-rising-costs.html":["Part-time, remote and freelance work are common ways to bring in more.","Weigh take-home pay against extras such as transport and childcare.","Find out how and when you would be paid.","If money is very tight, look at government support too."],
"article-childcare-caregiving.html":["Begin with the hours you can honestly commit.","Raise flexibility before you accept a role.","Take childcare and work costs off the pay you expect.","Your decision can be revisited as life changes."],
"article-restart.html":["Gaps on a CV are common and easier to explain than most people expect.","Keep the explanation brief and truthful.","Part-time or contract work is a gentle way back in.","Update your CV, references and skills."],
"article-job-scams.html":["Real employers never ask you to pay before you start.","Be wary of unsolicited chat-app offers and pay that looks too good.","Check the company and the listing on official sources.","Don't share your Singpass, OTP or bank logins. Call 1799 if in doubt."],
"article-work-modes.html":["A job ad can describe hours, place and status, and these are three different things.","In Singapore, part-time means contracted for fewer than 35 hours a week.","Freelancers look after their own CPF and tax.","Ask about hours, how pay is worked out, CPF, contract type and notice period."],
"article-flexible-work-request.html":["Employees are able to make a formal flexible work arrangement request.","Be precise about what you want, why you want it and from when.","Suggest a trial period to make agreement easier.","Employers should answer in writing and give reasons for a refusal."],
"article-part-time-cpf.html":["CPF applies to employees who are citizens or PRs, depending on age and pay.","A payslip should list your pay and your CPF contributions.","Freelancers are not employees, so no employer CPF is paid.","Current rates are on the CPF Board website."],
"article-read-job-ad.html":["Start with the hours, how pay is calculated, the work mode and the type of employment.","A salary range, or an \"up to\" figure, is not guaranteed pay.","Check the probation and notice periods before you apply.","Verify the employer through an official source."],
"article-remote-cv.html":["Show results that you achieved by yourself.","List the remote tools you already know.","Give your time zone and availability clearly.","One or two pages is enough."],
})

EXTRA.update({
"article-sectors-hiring.html":([("Where are the newest sector figures published?","The Ministry of Manpower releases labour market reports each quarter, and Workforce Singapore posts updates on industry transformation."),("If a sector is growing, is it easy to get hired?","Not always. How competitive it is depends on the role and on the skills and experience asked for.")],[("article-in-demand-roles.html","Roles in demand"),("article-read-labour-data.html","Reading labour market figures"),("article-upskilling-2026.html","Upskilling in Singapore")]),
"article-in-demand-roles.html":([("Can sought-after roles be done part-time or remotely?","Some can, especially analysis, content, support and project work. The employer is the best person to ask."),("Is a degree always needed?","Not always. Many employers now name skills and certifications next to a degree, or in place of one.")],[("article-sectors-hiring.html","Sectors to watch"),("article-upskilling-2026.html","Upskilling in Singapore"),("remote-jobs-singapore.html","Remote jobs guide")]),
"article-why-second-income.html":([("How much time does a side income take?","That depends on your goal and your hourly rate. Our <a href='work-from-home-routes-singapore.html#calc'>hours planner</a> gives a rough idea."),("Should I tell my main employer?","Look at your employment contract, since some require approval for work outside the job.")],[("part-time-jobs-singapore.html","Part-time jobs guide"),("work-from-home-jobs-singapore.html","Work-from-home guide"),("freelance-jobs-singapore.html","Freelance guide")]),
"article-remote-work-trend.html":([("May I ask to work from home?","Yes, by submitting a formal flexible work arrangement request. Our step-by-step guide shows how."),("Can Singapore residents take remote roles?","Many can. Check which time zone, employing entity and payroll apply.")],[("article-flexible-work-request.html","Asking for flexible work"),("remote-jobs-singapore.html","Remote jobs guide"),("article-remote-cv.html","A CV for remote roles")]),
"article-upskilling-2026.html":([("Who is eligible for SkillsFuture Credit?","Eligible Singapore citizens can use it, and mid-career workers get extra support. Amounts and eligibility change, so the SkillsFuture website has the latest details."),("Is it possible to study and work part-time?","Yes. Plenty of courses are modular and part-time, built for working adults.")],[("article-in-demand-roles.html","Roles in demand"),("article-restart.html","Starting again after a break"),("article-remote-cv.html","A CV for remote roles")]),
"article-read-labour-data.html":([("Why do official vacancies differ from what I see online?","Official figures count the vacancies employers report, while online listings may be duplicated or already filled."),("Where can I find the official tables?","The MOM Manpower Research and Statistics pages and SingStat publish them.")],[("article-sectors-hiring.html","Sectors to watch"),("article-in-demand-roles.html","Roles in demand"),("glossary.html","Glossary")]),
"article-job-scams.html":([("What if I have already replied?","Stop replying, send no money, save screenshots and talk to your bank. You can call the ScamShield helpline on 1799 for advice."),("How do I confirm a job exists?","Find the role on the company's own website or on MyCareersFuture, then contact the company using details you found yourself.")],[("part-time-jobs-singapore.html","Part-time jobs guide"),("online-jobs-singapore.html","Online work guide")]),
"article-work-modes.html":([("Does part-time mean the same as freelance?","No. Part-time staff are employees on a contract of service, whereas freelancers are self-employed."),("Is a remote part-time job possible?","Yes. Hours and location are independent of each other, so a role can be part-time and remote, or full-time and on-site.")],[("part-time-jobs-singapore.html","Part-time jobs guide"),("remote-jobs-singapore.html","Remote jobs guide"),("freelance-jobs-singapore.html","Freelance guide")]),
"article-rising-costs.html":([("How many hours would a worthwhile side income need?","It depends on the hourly rate and your goal. Try our <a href='work-from-home-routes-singapore.html#calc'>hours planner</a>."),("Do I pay tax on a side income?","Earnings from employment and freelance work are generally taxable and need to be declared. Check with IRAS.")],[("work-from-home-routes-singapore.html","Working from home: routes compared"),("part-time-jobs-singapore.html","Part-time jobs guide"),("article-part-time-cpf.html","Part-time work and CPF")]),
"article-childcare-caregiving.html":([("Do any jobs fit around school hours?","Some part-time and home-based roles have hours that work around school. Ask about flexibility early on."),("Could my current employer change my hours?","You can submit a formal flexible work request. Our guide explains the process.")],[("article-flexible-work-request.html","Asking for flexible work"),("work-from-home-jobs-singapore.html","Work-from-home guide"),("part-time-jobs-singapore.html","Part-time jobs guide")]),
"article-restart.html":([("How long is too long for a gap?","There is no set limit. Employers usually care more about what you can do today and how you account for the gap."),("Is part-time work a good first step?","It can be. Part-time or contract work helps rebuild confidence and recent experience, and many people begin that way.")],[("part-time-jobs-singapore.html","Part-time jobs guide"),("article-remote-cv.html","A CV for remote roles"),("article-read-job-ad.html","Reading a job ad")]),
"article-flexible-work-request.html":([("Is a refusal possible?","Yes. An employer may decline, though it is expected to give its reasons in writing. The MOM guidelines have the detail."),("Is it worth proposing a trial?","Yes. A trial with a review date can make it easier for an employer to agree.")],[("article-work-modes.html","What the terms mean"),("work-from-home-jobs-singapore.html","Work-from-home guide"),("remote-jobs-singapore.html","Remote jobs guide")]),
"article-part-time-cpf.html":([("Will part-timers receive an itemised payslip?","Employees should get one. MOM lists the current requirements."),("Do freelancers receive CPF from their clients?","No, because freelancers are self-employed. CPF Board explains the MediSave obligations.")],[("part-time-jobs-singapore.html","Part-time jobs guide"),("freelance-jobs-singapore.html","Freelance guide"),("glossary.html","Glossary")]),
"article-read-job-ad.html":([("How should I read an \"up to\" salary?","As the ceiling of a range, not an amount you can count on. Ask what people in the role usually earn."),("What does probation mean?","A trial period at the start of a job, when the notice period may differ. Your contract will say.")],[("glossary.html","Glossary"),("part-time-jobs-singapore.html","Part-time jobs guide"),("article-part-time-cpf.html","Part-time work and CPF")]),
"article-remote-cv.html":([("Is it worth stating my time zone?","Yes. Say where you are, the hours you work and how much overlap you can offer."),("Is a portfolio necessary?","It helps for creative, technical and content roles, but not for every job.")],[("remote-jobs-singapore.html","Remote jobs guide"),("work-from-home-jobs-singapore.html","Work-from-home guide"),("online-jobs-singapore.html","Online work guide")]),
})

# ---- Industry and skills
article("article-sectors-hiring.html","A plain-language look at the industries that official labour reports keep highlighting, and what they could mean for your next career move.","Industry trends",f'''
<p class="lede">The job market in Singapore doesn't head in a single direction. A few sectors keep expanding, others are being reshaped, and the work inside each is shifting fast. This is the overall picture.</p>
{stats([("5","sectors named most often: healthcare, technology, finance, professional services and logistics"),("Quarterly","how often MOM releases labour market reports"),("35 hrs","the dividing line between part-time and full-time")])}
<h2>Healthcare and care services</h2><p>Because the population is ageing, there is steady demand for nurses, allied health professionals, and eldercare and community care staff. Many of these jobs offer part-time or shift-based hours.</p>
<h2>Technology and digital</h2><p>Data, cybersecurity, cloud and AI-related skills feature repeatedly in national skills reports. Contract and remote working are common in this area.</p>
<h2>Finance and professional services</h2><p>Employers still need people in compliance, risk, analytics and advisory work, and more of them now offer hybrid schedules.</p>
<h2>Logistics, engineering and the green economy</h2><p>Supply chain, advanced manufacturing and sustainability jobs are part of Singapore's industry transformation plans.</p>
<h2>Where that leaves you</h2><p>If you are planning a full career change, or a part-time job to sit alongside your current one, focus on the skills behind a sector instead of the title on the door. Those skills travel further than most people assume.</p>
<div class="callout"><p>These figures are updated every quarter, so check the latest MOM and Workforce Singapore publications listed below.</p></div>''')

article("article-in-demand-roles.html","Which kinds of roles employers are recruiting for across care, data, digital, finance and operations, and how to interpret the trend.","In-demand roles",f'''
<p class="lede">Titles change from year to year, yet the skills employers want fall into a handful of familiar groups.</p>
{stats([("Care","nursing, allied health, eldercare"),("Data","analysts, engineers, AI support"),("Digital","product, marketing, cybersecurity"),("Ops","logistics, projects, compliance")])}
<h2>Care and health</h2><p>Manpower plans keep returning to nurses, therapists, care associates and community support workers.</p>
<h2>Data and technology</h2><p>There is a need for data analysts, software engineers and cloud and security specialists, and a good share of this work can be done remotely or on contract.</p>
<h2>Digital marketing and content</h2><p>Performance marketing, SEO, content creation and design are the main skills. Freelance and project work are popular ways to get started.</p>
<h2>Finance, compliance and operations</h2><p>Jobs in risk, audit, project coordination and supply chain stay steady across many industries.</p>
<h2>Making use of this list</h2><ul><li>See what recent MyCareersFuture listings actually pay.</li><li>Pay attention to the skills required, not just the job title.</li><li>Find out if part-time, hybrid or contract versions are offered.</li></ul>
<p>Want to know what this kind of work looks like day to day? Our <a href="jobs.html">job types</a> overview explains.</p>''')

article("article-why-second-income.html","Why part-time, home-based and freelance work are becoming a common way to add income in Singapore.","Side income",f'''
<p class="lede">Growing numbers of people are taking a part-time role next to their main job, or picking up freelance projects at weekends. The reasons are down to earth.</p>
{stats([("<35 hrs","contracted hours a week for part-time work"),("3","usual routes: part-time, freelance, online"),("1","income that seldom covers every cost")])}
<h2>Costs drive the trend</h2><p>Rent, childcare, healthcare and daily spending all put pressure on households. Extra income gives some breathing space and leaves your main career untouched.</p>
<h2>More flexible options exist now</h2><p>Part-time listings, home-based roles, online work and freelance projects make it simpler to slot extra work into your week. Most of it is ordinary paid work done at home or online, with pay that follows the role and the hours.</p>
<h2>A side role can be a low-risk experiment</h2><p>It is also a cheap way to try a new field, build up a portfolio or ease back in after a break.</p>
<h2>Sort these out before you start</h2><ul><li>How many hours you can really give each week.</li><li>How tax and CPF apply, depending on whether you are employed or self-employed.</li><li>Whether your main contract permits other work.</li></ul>
<p>Our <a href="work-from-home-routes-singapore.html">guide to working from home</a> compares the options.</p>''')

article("article-remote-work-trend.html","How flexible work requests, remote roles and hybrid schedules have become part of ordinary conversations between staff and employers.","Industry trends",f'''
<p class="lede">What used to be a perk is now a routine topic between employers and staff.</p>
{stats([("2024","when the national flexible work guidelines took effect"),("2 months","how long an employer has to reply to a formal request"),("3","forms: flexi-place, flexi-time, flexi-load")])}
<h2>The shift</h2><p>Employers are now expected to have a process for weighing flexible work requests. Approval isn't guaranteed, but you now have a clear route for asking.</p>
<h2>How remote and hybrid look in practice</h2><p>Some remote roles are fully remote, while others require a fixed number of days in the office. Working from home in Singapore normally means agreed hours with a local employer.</p>
<h2>What employers want to see</h2><p>They look for clear communication, dependable results and a suitable place to work. Proposing a short trial with a review date often helps.</p>
<p>Thinking of asking? Read <a href="article-flexible-work-request.html">how to submit a flexible work request</a>.</p>''')

article("article-upskilling-2026.html","SkillsFuture support, subsidies and short courses, and how to pick training that links to roles employers actually advertise.","Education & skills",f'''
<p class="lede">Training can lead somewhere new, provided it connects to jobs you can actually see advertised.</p>
{stats([("Credit","SkillsFuture Credit for eligible citizens"),("Mid-career","extra support; check SkillsFuture for current amounts"),("Modular","courses built for working adults")])}
<h2>Work backwards from the job</h2><p>Choose two or three ads for roles you would like, note the skills they list, then look for courses that close the gaps.</p>
<h2>Funding worth checking</h2><p>SkillsFuture Credit, mid-career support and course subsidies can all cut costs. Because amounts and eligibility are revised from time to time, check SkillsFuture before paying.</p>
<h2>Short courses and part-time study</h2><p>Plenty of programmes are modular and run in the evenings or online, which works well if you already have a part-time job.</p>
<h2>Steer clear of</h2><ul><li>Courses that are not approved.</li><li>Any programme that promises you a job or an income.</li></ul>
<p>Thinking about returning to work? See <a href="article-restart.html">going back to work after a break</a>.</p>''')

article("article-read-labour-data.html","A short guide to unemployment, job vacancy and wage figures, so you can read official labour reports with confidence.","Career advice",f'''
<p class="lede">A headline squeezes a lot into a few words. This is what the main labour numbers really measure.</p>
{stats([("Unemployment","share of the labour force looking for work"),("Vacancies","openings reported by employers"),("Median wage","the middle value, not the average")])}
<h2>The unemployment rate</h2><p>It tells you how many people are looking for work. In Singapore it is low, but it says nothing about underemployment or skills mismatches.</p>
<h2>Job vacancies</h2><p>This figure counts the openings that employers report, which is not the same as the number of ads you see online.</p>
<h2>Wages</h2><p>A median shows the middle of the range. What any one person earns depends on their experience and employer.</p>
<h2>A quick routine</h2><ul><li>Skim the summary of the latest MOM report.</li><li>Look up the sector table for your field.</li><li>Set it against recent listings.</li></ul>
<p>You might also like <a href="article-sectors-hiring.html">which sectors are hiring</a>.</p>''')

# ---- Life and money
article("article-rising-costs.html","Where flexible work can help with household costs in Singapore, and what to weigh up first.","Life & Money",'''
<p class="lede">When each month feels tighter than the one before, it isn't in your head, and you're in good company. Housing, groceries, transport and family expenses press on many households here.</p>
<h2>How extra income can help</h2><p>Your rent may be fixed, but your earnings may not be. Part-time, remote or contract work can add to your income without tying you to a full-time timetable.</p>
<h2>Match the arrangement to your budget</h2><ul><li><strong>Part-time:</strong> regular hours, normally as an employee on a contract.</li><li><strong>Remote or hybrid:</strong> fewer hours and less money spent on commuting.</li><li><strong>Freelance or contract:</strong> may pay more per hour, but less predictably, and CPF and tax are yours to manage.</li></ul>
<h2>Weigh everything up</h2><p>Set take-home pay against the added costs of transport, meals out and childcare. Find out how pay is worked out and how often it is paid.</p>
<div class="callout"><p>If money is very tight, look at government help as well. SupportGoWhere (supportgowhere.gov.sg) lists schemes you might qualify for. Treat anyone who promises quick money for an upfront fee with suspicion.</p></div>
<p>Browse flexible options in our <a href="jobs.html">job types guide</a>.</p>''')

article("article-childcare-caregiving.html","Weighing work against childcare and caregiving in Singapore.","Life & Money",'''
<p class="lede">Many parents and caregivers aren't asking whether to work. They are asking whether the pay and the hours genuinely add up.</p>
<h2>Begin with the hours you really have</h2><p>Note down what you can truly give each week, allowing for the school run, meals and appointments. A role that fits those hours beats a better rate that doesn't.</p>
<h2>Bring up flexibility early</h2><ul><li>Are the hours fixed, or can you pick your slots?</li><li>Can part of the work happen at home?</li><li>What is the plan if a child or parent is unwell?</li></ul>
<h2>Work out the real numbers</h2><p>Take childcare, transport and other work-related costs away from the pay you expect. A few hours in a good fit can be worth more than many hours in a stressful job.</p>
<h2>Go easy on yourself</h2><p>Working part-time, or pausing work, is not a failure. You can change your mind as your family's needs change.</p>
<p>Our <a href="jobs.html">job types guide</a> covers roles with flexible hours.</p>''')

article("article-restart.html","Going back to work after a career gap in Singapore.","Life & Money",'''
<p class="lede">CV gaps are common, whether from caring for family, retrenchment, illness, study or simply a need to rest. Employers meet them more often than you might think.</p>
<h2>Keep the explanation short and true</h2><p>Two calm sentences will do: what happened, what you did or learned meanwhile, and what you want to do next.</p>
<h2>Ease back in</h2><p>Part-time or contract work helps you rebuild confidence, references and recent experience, without the pressure of going straight back to full-time.</p>
<h2>Bring your profile up to date</h2><ul><li>Put recent skills, courses or volunteering on your CV.</li><li>Ask a past colleague for a short reference.</li><li>Browse SkillsFuture options for relevant skills.</li></ul>
<div class="callout"><p>Start at a pace that feels right for you. Nobody sets a deadline for beginning again.</p></div>
<p>Our <a href="jobs.html">job types guide</a> suggests places to begin.</p>''')

# ---- Rights, basics and scams
article("article-flexible-work-request.html","A step-by-step guide to making a flexible work arrangement request in Singapore.","Rights",'''
<p class="lede">If you are already employed and would like fewer hours, some days at home or different timings, you can put in a formal request. Good preparation improves your odds.</p>
<h2>Be clear about the type of request</h2><ul><li><strong>Flexi-place:</strong> working from home or elsewhere for part or all of the time.</li><li><strong>Flexi-time:</strong> starting and finishing at different times.</li><li><strong>Flexi-load:</strong> working fewer hours, as in part-time work or job-sharing.</li></ul>
<h2>The steps</h2><ol><li>Read your contract and any company policy.</li><li>Decide what you want, for how long, and from what date.</li><li>Explain how the work will still be done, including any handover.</li><li>Propose a trial period with a review date.</li><li>Put the request in writing.</li><li>Follow up politely if you hear nothing.</li></ol>
<h2>What to expect in return</h2><p>National guidelines say employers should look at requests fairly, reply in writing within a set time and give reasons for any refusal. The MOM website has the current details.</p>
<div class="callout"><p>A request doesn't guarantee a yes. A clear, practical proposal with a trial period gives you the best chance.</p></div>''')

article("article-part-time-cpf.html","How CPF applies to part-time work in Singapore.","Rights",'''
<p class="lede">You already know CPF exists. For a part-time role, the real question is whether it is being paid, and paid correctly.</p>
<h2>Who receives CPF contributions</h2><p>CPF applies to employees who are Singapore Citizens or Permanent Residents, depending on age and monthly wages. Foreigners on work passes are generally not covered. Rates change, so check the CPF Board website.</p>
<h2>What to look for on a payslip</h2><ul><li>Gross pay and the pay period.</li><li>Deductions, including your own CPF contribution where it applies.</li><li>The employer's CPF contribution, shown on its own line.</li><li>Net pay.</li></ul>
<h2>And for freelancers?</h2><p>A freelancer is self-employed, so no employer pays CPF for them. Depending on income, self-employed people may have to contribute to MediSave.</p>
<h2>Worth asking</h2><ul><li>Am I an employee under a contract of service?</li><li>Will CPF be paid every month?</li><li>Will I get an itemised payslip?</li></ul>
<p>Our <a href="part-time-jobs-singapore.html">part-time jobs guide</a> has more.</p>''')

article("article-read-job-ad.html","What to look for in ads for part-time, home-based and remote jobs in Singapore.","Basics",'''
<p class="lede">You've read plenty of job ads. Ads for flexible roles follow their own patterns, and a few details matter more than the rest.</p>
<h2>The details that tell you if it fits</h2><ul><li><strong>Hours:</strong> fixed shifts, a roster, or a vague "flexible" with no figures.</li><li><strong>Work mode:</strong> "WFH" might mean always at home or one day a week. Ask which.</li><li><strong>Type of employment:</strong> employee, contract or freelance. This changes CPF, leave and tax.</li><li><strong>How pay works:</strong> hourly, monthly, per task or by commission.</li></ul>
<h2>Read the pay wording carefully</h2><p>"Up to" describes a ceiling, not a promise. Commission-only pay rests entirely on results. A range shown on MyCareersFuture hints at what the employer plans to pay. Ask what people in the role normally earn.</p>
<h2>Fine print to double-check</h2><ul><li>Training bonds or clawback clauses.</li><li>How long probation lasts and what notice applies during it.</li><li>Exclusivity, or limits on other work if you have another job.</li><li>Who provides equipment and who pays for internet or travel.</li></ul>
<h2>Check who is hiring</h2><p>Make sure the company is real and is the one recruiting. Prefer official channels such as MyCareersFuture or the company's careers page. Our <a href="glossary.html">glossary</a> explains unfamiliar terms.</p>''')

article("article-remote-cv.html","How to tailor your CV for remote and home-based jobs in Singapore.","Career",'''
<p class="lede">An employer hiring remotely can't see you at work, so it looks for proof that you can deliver without supervision.</p>
<h2>Put results first</h2><p>Use short bullet points showing what you achieved on your own, such as tickets resolved, campaigns delivered or projects completed on schedule.</p>
<h2>Highlight remote-friendly skills</h2><ul><li>Tools you already use: email, chat apps, spreadsheets, video calls and project boards.</li><li>Clear, concise and courteous writing.</li><li>Managing your own time and being reliable.</li></ul>
<h2>Spell out your availability</h2><p>Give your working hours, your time zone and any core hours you can commit to. It matters for part-time and home-based applications alike.</p>
<h2>Keep the layout simple</h2><p>Stick to one or two pages with plain formatting and a brief summary at the top. Link to a portfolio if you have one.</p>
<p>Our <a href="work-from-home-jobs-singapore.html">work-from-home guide</a> suggests roles to aim for.</p>''')

article("article-work-modes.html","Definitions of common flexible work terms in Singapore.","Basics",'''
<p class="lede">A job ad can blur three separate things: the number of hours, the place of work and your legal status. Pulling them apart is the first step.</p>
<h2>Hours: part-time or full-time</h2><p>The Part-Time Employment Regulations define a part-time employee as someone contracted for fewer than 35 hours a week. Part-timers remain employees with a contract, and many protections apply pro rata. See MOM for the current rules.</p>
<h2>Place: remote, hybrid or on-site</h2><ul><li><strong>Remote / WFH:</strong> you work away from the employer's premises, often at home.</li><li><strong>Hybrid:</strong> a blend of both. Ask how many office days are required, and whether they are fixed.</li><li><strong>On-site:</strong> you work at the employer's premises or a client's.</li></ul>
<h2>Status: employee, contractor or platform worker</h2><p>An employee works under a contract of service. A freelancer or contractor works under a contract for services and arranges their own CPF and tax. Platform workers, such as ride-hail and delivery workers, fall under a separate framework in the Platform Workers Act.</p>
<div class="callout"><p>Put these to any employer: Is this an employment contract? How many hours a week? How is pay worked out? Is CPF payable? What is the notice period?</p></div>
<p>Come across a term you don't know? Try our <a href="glossary.html">glossary</a>.</p>''')

article("article-job-scams.html","How to recognise fake remote and part-time job offers in Singapore.","Scams",'''
<p class="lede">Scammers favour part-time and remote work because the offer of easy, flexible income is so tempting. These are the signs to look for.</p>
<h2>1. You didn't apply</h2><p>A job offer that arrives unprompted on WhatsApp, Telegram or SMS is a serious red flag. Genuine employers seldom message strangers cold with pay figures.</p>
<h2>2. Pay that doesn't fit the work</h2><p>Earning hundreds of dollars a day to "like" videos, boost ratings or finish simple tasks is not how real businesses pay.</p>
<h2>3. Money has to go in first</h2><p>Deposits, "training fees", equipment charges and top-ups to "unlock" tasks are exactly how scammers take your money.</p>
<h2>4. The interview is chat-only</h2><p>There is no company email, no video call, no named hiring manager, and no verifiable business in ACRA records.</p>
<h2>5. Pressure and secrecy</h2><p>Lines like "reply within the hour", "tell no one" and "only a few slots left" are meant to stop you checking.</p>
<h2>6. Requests for sensitive details</h2><p>Don't hand over your Singpass, OTPs, banking logins or a full photo of your NRIC before you hold a verified offer. Your bank account could end up being used for money mule activity.</p>
<h2>7. It isn't on official channels</h2><p>See whether the employer and the role show up on MyCareersFuture or on the company's official website.</p>
<div class="callout"><p><strong>If you have already engaged with them:</strong> stop all payments, save screenshots, call your bank and contact the Police. For advice, you can call the ScamShield helpline on 1799.</p></div>''')
