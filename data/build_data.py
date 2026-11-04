#!/usr/bin/env python3
"""Build + validate data/data.json. Run: python3 data/build_data.py  (add --check to only validate)."""
import json, sys, pathlib
from urllib.parse import urlparse
D = "2026-11-04"
ALL = ["MY","SG","ID","TH","VN","PH"]
# verified=True only if the value was confirmed on the live/official page on D.
E = []
def add(name, provider, cat, value, countries, notes, apply, source, vc=False, verified=False):
    E.append(dict(name=name, provider=provider, category=cat, value=value, countries=countries,
                  eligibility=notes, needs_vc=vc, apply_url=apply, source_url=source,
                  date_checked=D, verified=verified, featured=False))
G="Global"
# ---- Cloud (verified this run) ----
add("AWS Activate Founders","Amazon Web Services","Cloud","US$1,000 credits (select startups up to US$5,000 over time)",[G],"Self-funded, new to Activate credits, working company website, founded in last 10 years.","https://aws.amazon.com/startups/credits","https://aws.amazon.com/aws-startups/learn/applying-for-aws-activate-credits-a-step-by-step-guide/",False,True)
add("AWS Activate Portfolio","Amazon Web Services","Cloud","Up to US$200,000 credits (some AWS pages still say US$100,000)",[G],"Needs an Activate Provider Organization ID (VC/accelerator), pre-Series B, founded in last 10 years.","https://aws.amazon.com/startups/credits","https://aws.amazon.com/aws-startups/learn/applying-for-aws-activate-credits-a-step-by-step-guide/",True,True)
add("Google for Startups Cloud Program (Start/Scale)","Google Cloud","Cloud","Up to US$200,000 over 2 years (Y1 100% up to US$100k, Y2 20% up to US$100k)",[G],"Pre-seed to Series A institutional/VC equity funding; angel, grant, crowdfunding don't qualify; founded within 3-5 yrs; ≤US$5k prior GCP credits.","https://startup.google.com/cloud/","https://startup.google.com/cloud/",True,True)
add("Google for Startups Cloud Program, AI tier","Google Cloud","AI","Up to US$350,000 over 2 years (Y1 100% up to US$250k)",[G],"AI-first, Gemini as core of product; Pre-Seed/Seed in last 5 yrs or Series A in last 12 months; founded in last 5 yrs. Third-party models not covered.","https://cloud.google.com/startup/ai","https://cloud.google.com/startup/ai",True,True)
add("Microsoft for Startups","Microsoft","Cloud","US$200 immediately; US$5,000 after business verification; up to US$150,000 via usage milestones",[G],"Registered legal entity for US$5k; higher tiers need 5/7/10+ Azure workloads for 60 days (US$150k also ~US$3k/month usage). No VC needed.","https://www.microsoft.com/en-us/startups","https://learn.microsoft.com/en-us/startups/microsoft-for-startups/getting-started-mfs",False,True)
add("Cloudflare for Startups (bootstrapped)","Cloudflare","Cloud","US$10,000 credits",[G],"Bootstrapped / raised under US$1M.","https://www.cloudflare.com/startups/","https://www.cloudflare.com/startups/",False,True)
add("Cloudflare for Startups (partner-backed)","Cloudflare","Cloud","US$100,000 (<US$5M raised) up to US$350,000 (US$5M+ raised)",[G],"Needs affiliation with a Cloudflare partner VC/accelerator.","https://www.cloudflare.com/startups/","https://www.cloudflare.com/startups/",True,True)
# ---- Cloud (not confirmed live) ----
add("Oracle for Startups","Oracle","Cloud","not stated (free cloud credits; amount not confirmed)",[G],"Oracle Cloud Infrastructure credits and discounts for startups; check page for current terms.","https://www.oracle.com/startup/","https://www.oracle.com/startup/")
add("DigitalOcean Hatch","DigitalOcean","Cloud","not stated (historically up to US$100,000 in credits via partners)",[G],"Program status and amount need checking; historically required partner/accelerator referral.","https://www.digitalocean.com/hatch","https://www.digitalocean.com/hatch",True)
add("Alibaba Cloud for Startups","Alibaba Cloud","Cloud","not stated",[G],"Startup credits program with strong SEA region presence (KL, Singapore, Jakarta, Manila, Bangkok).","https://www.alibabacloud.com/startup","https://www.alibabacloud.com/startup")
add("Huawei Cloud Startup Program","Huawei Cloud","Cloud","not stated",[G],"Credits and go-to-market support; active in SEA.","https://www.huaweicloud.com/intl/en-us/startup/","https://www.huaweicloud.com/intl/en-us/startup/")
add("Tencent Cloud Startup Program","Tencent Cloud","Cloud","not stated",[G],"Startup credits program; check current tiers.","https://www.tencentcloud.com/act/pro/startup","https://www.tencentcloud.com/act/pro/startup")
add("MongoDB for Startups","MongoDB","Cloud","not stated (Atlas credits)",[G],"Atlas credits plus technical advice; typically via partner.","https://www.mongodb.com/solutions/startups","https://www.mongodb.com/solutions/startups")
add("Vercel for Startups","Vercel","Cloud","not stated",[G],"Hosting credits for partner-backed startups.","https://vercel.com/startups","https://vercel.com/startups",True)
add("Supabase for Startups","Supabase","Cloud","not stated",[G],"Credits for startups via partner network; check page.","https://supabase.com/partners","https://supabase.com/partners")
add("NVIDIA Inception","NVIDIA","AI","not stated (free membership; cloud credit offers via partners)",[G],"Free program for AI startups; perks and partner cloud credits.","https://www.nvidia.com/en-us/startups/","https://www.nvidia.com/en-us/startups/")
# ---- AI APIs ----
add("ElevenLabs Startup Grants","ElevenLabs","AI","12 months free, 33M characters (valued over US$5,500 by ElevenLabs)",[G],"Business email, monetisation plan, fewer than 25 employees; agencies/consultancies excluded.","https://elevenlabs.io/startup-grants","https://elevenlabs.io/startup-grants",False,True)
add("Claude for Startups","Anthropic","AI","Up to US$100,000 Claude API credits for partner-VC-backed startups; up to US$45,000 partner offers",[G],"Reported CLOSED to new applications as of Nov 2026; partner VC backing needed for API credits.","https://claude.com/programs/startups","https://claude.com/programs/startups",True,True)
add("OpenAI for Startups","OpenAI","AI","not stated (API credits via VC partners)",[G],"Requires referral code from an eligible VC partner.","https://openai.com/business/why-openai/startups/","https://openai.com/business/why-openai/startups/",True,True)
add("Azure OpenAI via Microsoft for Startups","Microsoft","AI","Covered by Microsoft for Startups credits (see above)",[G],"Startup credits usable on Microsoft Foundry models.","https://www.microsoft.com/en-us/startups","https://learn.microsoft.com/en-us/startups/microsoft-for-startups/getting-started-mfs",False,True)
add("Amazon Bedrock via AWS Activate","Amazon Web Services","AI","Covered by AWS Activate credits",[G],"Activate credits redeemable on third-party models on Bedrock (Anthropic, Meta, Mistral etc.).","https://aws.amazon.com/startups/credits","https://aws.amazon.com/startups/",False,True)
add("Hugging Face (Enterprise/Startup offers)","Hugging Face","AI","not stated",[G],"No standing public credits program confirmed; check for current offers.","https://huggingface.co/pricing","https://huggingface.co/pricing")
add("Deepgram Startup Program","Deepgram","AI","not stated (speech API credits)",[G],"Speech-to-text credits for startups; check current amount.","https://deepgram.com/startups","https://deepgram.com/startups")
add("AssemblyAI for Startups","AssemblyAI","AI","not stated",[G],"Speech AI credits; check current terms.","https://www.assemblyai.com/startup-program","https://www.assemblyai.com/startup-program")
add("Mistral AI for Startups","Mistral AI","AI","not stated",[G],"Program status unconfirmed.","https://mistral.ai/","https://mistral.ai/")
add("Pinecone for Startups","Pinecone","AI","not stated",[G],"Vector DB credits; check page.","https://www.pinecone.io/startups/","https://www.pinecone.io/startups/")
add("Together AI Startup Accelerator","Together AI","AI","not stated",[G],"GPU/inference credits for AI startups; check page.","https://www.together.ai/startup-accelerator","https://www.together.ai/startup-accelerator")
# ---- SaaS ----
for n,p,u,note,vc in [
 ("Stripe Atlas perks","Stripe","https://stripe.com/atlas","Partner perks bundle for companies incorporated via Atlas (US Delaware entity; fee applies).",False),
 ("Notion for Startups","Notion","https://www.notion.com/startups","Plus plan credits for eligible startups; often via partner.",True),
 ("HubSpot for Startups","HubSpot","https://www.hubspot.com/startups","Discount on HubSpot software; partner affiliation usually required.",True),
 ("Intercom Early Stage","Intercom","https://www.intercom.com/early-stage","Discounted plan for early-stage startups.",False),
 ("Zendesk for Startups","Zendesk","https://www.zendesk.com/startups/","Free/discounted Zendesk for partner-backed startups.",True),
 ("Atlassian for Startups","Atlassian","https://www.atlassian.com/software/startups","Free Atlassian Cloud standard licences for eligible startups.",False),
 ("Miro for Startups","Miro","https://miro.com/startups/","Credits for Miro plans; via partner.",True),
 ("Figma for Startups","Figma","https://www.figma.com/startups/","Discount for early-stage startups.",False),
 ("Linear for Startups","Linear","https://linear.app/startups","Discount on paid plans.",True),
 ("PostHog for Startups","PostHog","https://posthog.com/startups","Product analytics credits for young startups.",False),
 ("Mixpanel for Startups","Mixpanel","https://mixpanel.com/startups","Free year of Growth plan for eligible startups.",False),
 ("Segment Startup Program","Twilio Segment","https://segment.com/industry/startups/","Free plan credits; check page.",True),
 ("Twilio Startups","Twilio","https://www.twilio.com/en-us/startups","Credits; check page.",False),
 ("GitHub for Startups","GitHub","https://github.com/enterprise/startups","Free GitHub Enterprise seats via partners.",True),
 ("JetBrains Startup Program","JetBrains","https://www.jetbrains.com/store/startups/","Discount on JetBrains tools for young companies.",False),
 ("Google Workspace via Google for Startups","Google","https://startup.google.com/cloud/","12 months Workspace Business Plus for Cloud Program members (verified).",True),
 ("Xero / local accounting perks","Xero","https://www.xero.com/my/","No startup program confirmed for MY; trial only.",False),
 ("Brex / Airwallex startup perks","Airwallex","https://www.airwallex.com/my","Airwallex operates in MY/SG; perks marketplace status unconfirmed.",False),
]:
    v = n.startswith("Google Workspace")
    add(n,p,"SaaS","not stated" if not v else "12 months Google Workspace Business Plus at no cost",[G],note,u,u,vc,v)
# ---- SEA government & programs ----
add("Cradle CIP Spark","Cradle Fund (MOF)","Grant","Up to RM150,000 conditional grant, max 18 months",["MY"],"2+ individuals (1 Malaysian, 1 resident) or company <5 yrs, revenue <RM3M, owns IP. No paid-up capital needed.","https://www.cradle.com.my/cip-spark/","https://www.cradle.com.my/cip-spark/",False,True)
add("Cradle CIP Sprint","Cradle Fund (MOF)","Grant","Up to RM600,000 conditional convertible grant, max 18 months",["MY"],"Sdn Bhd <7 yrs, revenue <RM5M, RM10k paid-up, 2+ directors (1 Malaysian), owns IP.","https://www.cradle.com.my/cip-sprint/","https://www.cradle.com.my/cip-sprint/",False,True)
add("MDEC Digital Content Grant 2026 (Marketing & Commercialisation)","MDEC","Grant","Up to RM300,000, up to 100% of eligible cost",["MY"],"Malaysian animation/games companies, operating 1+ yr, MD or MSC status.","http://www.mdec.my/grants/dcg","http://www.mdec.my/grants/dcg",False,True)
add("MDEC Digital Content Grant 2026 (Mega)","MDEC","Grant","Up to RM2 million, up to 50% of project cost",["MY"],"Malaysian animation/games companies; capital/ownership criteria apply.","http://www.mdec.my/grants/dcg","https://www.businesstoday.com.my/2026/07/15/content-creators-may-start-applying-for-grants-up-to-rm2-million-from-mdec/",False,True)
add("Malaysia Digital (MD) status","MDEC","Program","Tax incentives (not cash); amount not stated",["MY"],"Malaysian-incorporated tech companies; application via MDEC.","https://mdec.my/malaysiadigital","https://mdec.my/malaysiadigital")
add("MRANTI programmes (ex-MaGIC)","MRANTI","Accelerator","not stated",["MY"],"Malaysian Research Accelerator for Technology & Innovation; runs accelerators and commercialisation support.","https://mranti.my/","https://mranti.my/")
add("Malaysia Debt Ventures / MYStartup","MOSTI / Cradle","Program","not stated",["MY"],"MYStartup single window lists national startup support; check current calls.","https://mystartup.gov.my/","https://mystartup.gov.my/")
add("Startup SG Founder","Enterprise Singapore","Grant","S$20,000 to S$50,000 at 1:1 co-matching",["SG"],"First applicant a first-time founder; Pte Ltd <6 months old; 51% SG citizen/PR owned; via Accredited Mentor Partner.","https://www.startupsg.gov.sg/programmes/4894/startup-sg-founder","https://iie.smu.edu.sg/startup-sg-founder-grant",False,True)
add("Startup SG Tech","Enterprise Singapore","Grant","not stated (proof-of-concept/value grants)",["SG"],"Singapore-registered tech startups; check current quantum.","https://www.startupsg.gov.sg/programmes/4897/startup-sg-tech","https://www.startupsg.gov.sg/programmes/4897/startup-sg-tech")
add("Startup SG Equity","Enterprise Singapore / SEEDS Capital","Program","not stated (co-investment)",["SG"],"Government co-investment alongside qualifying third-party investors.","https://www.startupsg.gov.sg/programmes/4895/startup-sg-equity","https://www.startupsg.gov.sg/programmes/4895/startup-sg-equity",True)
add("Productivity Solutions Grant (PSG)","Enterprise Singapore","Grant","not stated (% support on pre-approved solutions)",["SG"],"SG-registered, 30%+ local shareholding; pre-approved IT solutions.","https://www.gobusiness.gov.sg/productivity-solutions-grant/","https://www.gobusiness.gov.sg/productivity-solutions-grant/")
add("Thailand NIA innovation grants","National Innovation Agency (NIA)","Grant","Up to THB 5 million, typically up to 75% of project cost",["TH"],"Thai-registered entity, 51%+ Thai owned.","https://www.nia.or.th/QAGrant","https://www.nia.or.th/QAGrant",False,True)
add("DOST-PCIEERD Startup Grant Fund","DOST-PCIEERD","Grant","Up to PHP 5 million over 18 months",["PH"],"Philippine tech startups; 2026 call ran 3-31 July 2026 (check next call).","https://pcieerd.dost.gov.ph/work-with-us/2026-call-for-proposal-for-the-pcieerd-startup-grant-fund-program/","https://pcieerd.dost.gov.ph/work-with-us/2026-call-for-proposal-for-the-pcieerd-startup-grant-fund-program/",False,True)
add("L-CAMP Vietnam (Lotte Ventures)","Lotte Ventures Vietnam","Accelerator","Proof-of-concept grants totalling up to US$80,000",["VN"],"2026 applications closed 19 June 2026; watch for next cohort.","https://technode.global/2026/06/01/lotte-ventures-vietnam-launches-80000-open-innovation-program-to-connect-startups-with-corporate-ecosystem/","https://technode.global/2026/06/01/lotte-ventures-vietnam-launches-80000-open-innovation-program-to-connect-startups-with-corporate-ecosystem/",False,True)
add("UGM Startup Grant","Universitas Gadjah Mada","Grant","Up to IDR 12 million",["ID"],"UGM students/alumni; 2026 registration closed 27 March 2026.","https://ditpui.ugm.ac.id/info-hibah/hibah-prime-step/start-up-grant/","https://ditpui.ugm.ac.id/info-hibah/hibah-prime-step/start-up-grant/",False,True)
add("Google for Startups Accelerator: Southeast Asia","Google","Accelerator","Equity-free; amount not stated",["MY","SG","ID","TH","VN","PH"],"Seed to Series A tech startups in SEA; cohort-based.","https://startup.google.com/programs/accelerator/southeast-asia/","https://startup.google.com/programs/accelerator/southeast-asia/")
add("AWS Generative AI Accelerator","Amazon Web Services","Accelerator","not stated (credits; previous cohorts up to US$1M)",[G],"Cohort-based; check current cohort.","https://aws.amazon.com/startups/accelerators","https://aws.amazon.com/startups/accelerators")
add("Antler Southeast Asia","Antler","Accelerator","not stated (pre-seed investment for equity)",["MY","SG","ID","VN","PH","TH"],"Residency programme; investment for equity (not free money).","https://www.antler.co/location/southeast-asia","https://www.antler.co/location/southeast-asia",True)
add("Iterative","Iterative","Accelerator","not stated (investment for equity)",["MY","SG","ID","TH","VN","PH"],"SEA-focused YC-style accelerator; equity investment.","https://www.iterative.vc/","https://www.iterative.vc/",True)
add("500 Global Southeast Asia","500 Global","Accelerator","not stated",["MY","SG","ID","TH","VN","PH"],"Accelerator/flagship programmes; check open calls.","https://500.co/","https://500.co/",True)
add("Y Combinator","Y Combinator","Accelerator","US$500,000 standard deal (not re-checked this run)",[G],"Open to SEA founders; equity + SAFE.","https://www.ycombinator.com/apply","https://www.ycombinator.com/deal",True)

# ---- 2026-11-04 verification pass: overrides (value, eligibility, urls, status, verified) ----
REMOVED = {"Figma for Startups","Mistral AI for Startups","Segment Startup Program","Twilio Startups",
           "Hugging Face (Enterprise/Startup offers)","Supabase for Startups","Xero / local accounting perks","Brex / Airwallex startup perks"}
U = {
 "Oracle for Startups": dict(name="Oracle Startup Growth Engine", value="US$5,000 to US$60,000 OCI Universal Credits (12 months)", eligibility="Legally registered tech company with a validated product and a workload for OCI; Oracle selects at its discretion, credits not guaranteed. Launched Oct 2026, replaces Oracle for Startups.", apply_url="https://www.oracle.com/se/artificial-intelligence/startup-growth-engine/", source_url="https://www.oracle.com/europe/artificial-intelligence/startup-growth-engine/terms/", verified=True),
 "DigitalOcean Hatch": dict(name="DigitalOcean Startups (ex-Hatch)", value="Credits, amount varies (not stated); selected startups invited to GPU credit packages", eligibility="AI-native startups prioritised; raised US$10M or less; company website + company email; service businesses/agencies not eligible.", apply_url="https://www.digitalocean.com/startups", source_url="https://www.digitalocean.com/startups", needs_vc=False, verified=True),
 "Alibaba Cloud for Startups": dict(name="Alibaba Cloud AI Catalyst Program", value="Up to US$120k AI credits + up to 2B free Model Studio tokens", eligibility="not stated on page (selection-based).", apply_url="https://www.alibabacloud.com/en/startup/ai", source_url="https://www.alibabacloud.com/en/startup/ai", verified=True),
 "Huawei Cloud Startup Program": dict(value="Up to USD150,000 Huawei Cloud cash credits voucher", verified=True),
 "Tencent Cloud Startup Program": dict(value="not stated (credits/discounts assigned after review)", eligibility="VC-backed startups; verified Tencent Cloud account; reviewed within ~2 weeks.", apply_url="https://www.tencentcloud.com/campaign/startupprogram", source_url="https://www.tencentcloud.com/campaign/startupprogram", needs_vc=True, verified=False),
 "MongoDB for Startups": dict(value="Atlas credits + Voyage AI tokens (amount not stated; Inspire tier for bootstrapped, Grow for funded)", eligibility="<7 years old, Series A or earlier, single software product (agencies excluded), new to program, active website + LinkedIn.", needs_vc=False, verified=True),
 "Vercel for Startups": dict(value="Up to US$30,000 in Flexible Commitment Amount + Enterprise-tier access", eligibility="'Eligible teams' (criteria not stated on page).", verified=True),
 "NVIDIA Inception": dict(value="Free membership; partner cloud credits and preferred hardware/software pricing (amount not stated)", verified=True),
 "Deepgram Startup Program": dict(value="US$1,000 starter credits for direct applicants; tiers up to US$100,000 over 12 months", eligibility="AI builder or early-stage startup, in production or launching within 6 months; >US$10M raised reviewed case by case; needs Deepgram console account.", apply_url="https://deepgram.com/startup-program", source_url="https://deepgram.com/startup-program", verified=True),
 "AssemblyAI for Startups": dict(value="Fixed credit amount (not stated), 12 months recurring free credits, then startup discounts", eligibility="Bootstrapped through Series A, building with voice/audio, launching within 6 months.", apply_url="https://www.assemblyai.com/contact/startup-program", source_url="https://www.assemblyai.com/contact/startup-program", verified=True),
 "Pinecone for Startups": dict(value="Usage credits and discounts (amount not stated)", eligibility="Fewer than 100 employees; Series A or earlier.", apply_url="https://www.pinecone.io/startup-program/", source_url="https://www.pinecone.io/startup-program/", verified=True),
 "Together AI Startup Accelerator": dict(value="Up to US$15K (≤US$5M raised), US$30K (US$5M-10M), US$50K (>US$10M) platform credits", eligibility="Selection-based; tier set by amount raised.", verified=True),
 "Stripe Atlas perks": dict(value="US$500 on incorporation + Treasury account; US$2.5K Stripe credits; US$200K+ partner offers", eligibility="Incorporate a US company via Stripe Atlas (fee applies); US$500 needs Stripe Treasury account within 7 days.", apply_url="https://stripe.com/atlas", source_url="https://stripe.com/en-my/atlas", verified=True),
 "Notion for Startups": dict(value="Up to 6 months free Business plan with Notion AI (up to US$12,000 value)", eligibility="Non-paying Notion customers with under 100 employees.", needs_vc=False, verified=True),
 "HubSpot for Startups": dict(value="90% off Year 1 (Seed and Series A)", eligibility="Seed (under US$2M raised) and Series A founders.", verified=True),
 "Intercom Early Stage": dict(value="93% off Intercom + 1 year of Fin free", eligibility="Up to US$10M funding, fewer than 15 employees, not a current Intercom customer.", verified=True),
 "Zendesk for Startups": dict(value="Up to 2 years of Zendesk free", eligibility="'Qualified startups' (criteria not stated on page).", verified=True),
 "Atlassian for Startups": dict(value="Premium edition $0 for 12 months, up to 50 users", eligibility="Partner accelerator/incubator affiliation; raised no more than US$10M.", needs_vc=True, verified=True),
 "Miro for Startups": dict(value="Free Miro credits (early startups); up to 25% discount (scale-ups)", eligibility="not stated", verified=True),
 "Linear for Startups": dict(value="not stated (offers via partner VCs/accelerators/communities)", eligibility="Via a Linear startup partner.", verified=True),
 "PostHog for Startups": dict(value="US$50,000 PostHog credits for 12 months + US$12,000 partner benefits", eligibility="Early-stage teams (see page for criteria).", verified=True),
 "Mixpanel for Startups": dict(value="First year free (described as worth US$145,000): full suite, 1B events, 1M Session Replays", eligibility="Startups (criteria on page).", verified=True),
 "GitHub for Startups": dict(value="US$10,000 flexible platform credits", eligibility="Partner-affiliated startups.", verified=True),
 "JetBrains Startup Program": dict(value="50% off up to 10 IDE subscriptions (all products pack), for up to 5 years", eligibility="Privately owned; established within last 5 years; website/online presence; commercial licences only.", apply_url="https://www.jetbrains.com/startups/", source_url="https://www.jetbrains.com/startups/", verified=True),
 "Malaysia Digital (MD) status": dict(value="Tax incentives (not cash); separate MD Tax Incentive application", eligibility="Malaysian-incorporated, resident; MD activity; paid-up capital ≥RM1,000 (RM50,000 for tax incentive). MD tax incentive applications open until 31 Dec 2027.", apply_url="https://www.mdec.my/malaysiadigital", source_url="https://www.mdec.my/static/pdf/malaysiadigital/Malaysia-Digital-MD-Status-Guidelines_Effective-28-August-2025.pdf", verified=True),
 "MRANTI programmes (ex-MaGIC)": dict(value="not stated (programmes: Global Accelerator Programme, Global Market Fit, VentureX, etc.)", verified=True),
 "Malaysia Debt Ventures / MYStartup": dict(name="MYStartup (national startup directory)", value="not stated (directory of government/private funding)", eligibility="Directory/single window; individual schemes have own criteria.", apply_url="https://www.mystartup.gov.my/", source_url="https://www.mystartup.gov.my/", verified=True),
 "Startup SG Tech": dict(value="not stated on page (POC/POV grant, milestone-based; EnterpriseSG holds share-subscription right)", eligibility="Startups with proprietary technology and scalable model.", verified=True),
 "Startup SG Equity": dict(value="Co-investment up to S$12 million (2:1 up to S$1M in first institutional round, then tapering)", eligibility="Singapore-based deep-tech startups with proprietary IP, alongside qualifying investors.", source_url="https://www.seedscapital.sg/about-us/our-co-investment-model/", verified=True),
 "Productivity Solutions Grant (PSG)": dict(value="not stated on page (support % for pre-approved solutions)", eligibility="Registered and operating in Singapore; solution used in Singapore; 30% local shareholding for selected solutions; 3 local employees for consultancy.", apply_url="https://grants.gobusiness.gov.sg/support/productivity-solutions-grant", source_url="https://grants.gobusiness.gov.sg/support/productivity-solutions-grant", verified=True),
 "Google for Startups Accelerator: Southeast Asia": dict(value="Equity-free; Google product credits (amount not stated)", eligibility="SEA-based tech startups, ideally Seed to Series B, deeply technical (AI/ML). Applications currently closed.", status="closed", verified=True),
 "AWS Generative AI Accelerator": dict(value="Up to US$1,000,000 AWS credits (2025 cohort)", eligibility="Early-stage generative AI startups; 8-week program. 2026 window (10 Jun–10 Jul) reported closed; official page not loaded.", source_url="https://press.aboutamazon.com/aws/2025/10/aws-selects-40-promising-ai-startups-from-around-the-world-for-the-2025-generative-ai-accelerator", status="closed", verified=False),
 "Antler Southeast Asia": dict(name="Antler Singapore (SEA)", value="US$150,000 for ~10% (US$100k SAFE + US$50k uncapped MFN SAFE), up to US$400,000 incl. matching", eligibility="6-week in-person residency in Singapore (next 5 Oct 2026); Malaysia also has a Direct Investment Track for teams with MVP and traction.", apply_url="https://www.antler.co/location/singapore", source_url="https://www.antler.co/location/singapore", verified=True),
 "Iterative": dict(value="US$150K to US$500K investment (equity)", eligibility="SEA-focused batch, twice a year; Winter 2027 applications open.", verified=True),
 "500 Global Southeast Asia": dict(value="not stated", eligibility="500.co lists Southeast Asia programmes; no SEA terms found on homepage.", verified=False),
 "Claude for Startups": dict(status="closed"),
 "Y Combinator": dict(value="US$500,000 standard deal (US$125K for 7% + US$375K uncapped MFN SAFE)", verified=True),
}
E = [e for e in E if e["name"] not in REMOVED]
for e in E:
    e.setdefault("status","open")
    if e["name"] in U: e.update(U[e["name"]]); e["date_checked"]=D
# ---- 2026-11-04 status pass: dated rounds checked against official pages ----
TBA="closed (next round TBA)"
S = {
 "DOST-PCIEERD Startup Grant Fund": (TBA, "Philippine tech startups; 2026 call ran 3-31 July 2026, next call TBA."),
 "L-CAMP Vietnam (Lotte Ventures)": (TBA, None),
 "UGM Startup Grant": (TBA, None),
 "Google for Startups Accelerator: Southeast Asia": (TBA, "SEA-based tech startups, Seed to Series B, deeply technical (AI/ML). 2026 applications ran 25 May-20 Jun 2026; register interest for the next cohort."),
 "Claude for Startups": (TBA, None),
 "AWS Generative AI Accelerator": (TBA, None),
 "MDEC Digital Content Grant 2026 (Marketing & Commercialisation)": (TBA, "Malaysian animation/games companies, operating 1+ yr, MD or MSC status. DCG 2026 applications closed 30 Sep 2026; MDEC will announce a reopening."),
 "MDEC Digital Content Grant 2026 (Mega)": (TBA, "Malaysian animation/games companies; capital/ownership criteria apply. DCG 2026 applications closed 30 Sep 2026."),
 "Cradle CIP Spark": ("rolling", None),
 "Cradle CIP Sprint": ("rolling", None),
 "Startup SG Founder": ("rolling", None),
 "Startup SG Tech": ("rolling", None),
 "Productivity Solutions Grant (PSG)": ("rolling", None),
 "Thailand NIA innovation grants": ("rolling", None),
 "Antler Singapore (SEA)": ("rolling", "6-week in-person residency in Singapore (latest started 5 Oct 2026; applications taken continuously for the next one); Malaysia also has a Direct Investment Track for teams with MVP and traction."),
 "Iterative": ("open", None),
 "Y Combinator": ("open", None),
}
for e in E:
    if e["name"] in S:
        st, el = S[e["name"]]; e["status"]=st; e["date_checked"]=D
        if el: e["eligibility"]=el
args = sys.argv[1:]
p = pathlib.Path(__file__).parent/"data.json"
if "--check" in args:
    E = json.loads(p.read_text())["entries"]
req = ["name","provider","category","value","countries","eligibility","needs_vc","apply_url","source_url","date_checked","verified"]
CATS = {"Cloud","AI","SaaS","Grant","Accelerator","Program"}
errs=[]; seen=set()
for i,e in enumerate(E):
    for k in req:
        if k not in e or e[k] in ("",None,[]): errs.append(f"#{i} {e.get('name')}: missing {k}")
    if e.get("category") not in CATS: errs.append(f"#{i}: bad category {e.get('category')}")
    for k in ("apply_url","source_url"):
        if urlparse(e.get(k,"")).scheme not in ("http","https"): errs.append(f"#{i}: bad {k}")
    for c in e.get("countries",[]):
        if c not in ALL+[G]: errs.append(f"#{i}: bad country {c}")
    if e["name"] in seen: errs.append(f"duplicate {e['name']}")
    if e.get("status") not in ("open","rolling","closed (next round TBA)"): errs.append(f"#{i} {e['name']}: bad status {e.get('status')}")
    seen.add(e["name"])
if errs: print("\n".join(errs)); sys.exit(1)
if "--check" not in args:
    p.write_text(json.dumps({"updated":D,"countries":ALL,"entries":E},indent=1,ensure_ascii=False))
from collections import Counter
print(f"OK {len(E)} entries, verified {sum(e['verified'] for e in E)}")
print("by category", dict(Counter(e['category'] for e in E)))
print("by country", dict(Counter(c for e in E for c in e['countries'])))
