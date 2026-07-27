"""
SINGLE SOURCE OF TRUTH — C803 Copilot for Power Apps (non-WSQ).

A beginner, one-day (7.5 hours), hands-on short course on building business
applications faster with Copilot, Microsoft's AI assistant inside Power Apps.
Learners enable Copilot in Power Apps Studio, prepare data in Dataverse,
generate a working canvas app from a plain-English prompt, refine screens and
Power Fx with Copilot, add an in-app Copilot chat for end users, then build a
Power Automate approval-and-notification flow, integrate it with the app, and
share and govern the result. Every artifact (PPT, LP, LG, LG.md) and every lab
is generated from this module + data_domainN.py so they stay 100% aligned.

NON-WSQ RULES — the engine enforces these, do not reintroduce them here:
  * NO assessment of any kind (no WA/SAQ, no PP, no case study, no marking).
  * NO SSG / SkillsFuture / WSQ funding or subsidy content.
  * NO TRAQOM survey, NO digital attendance, NO 75% attendance rule.
  * NO TGS course reference — this course carries the plain code C803.
"""

# ------------------------------------------------------------------ metadata
TITLE        = "Copilot for Power Apps (C803)"
SHORT_TITLE  = "Copilot for Power Apps (C803)"   # used in output filenames
COURSE_CODE  = "C803"                            # non-WSQ code — never a TGS- ref
VERSION      = "v1.0"
VERSION_DATE = "27 July 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr. Alfred Ang"
DAYS         = 1
MODE         = "Instructor-led, hands-on practical labs"

DARK_THEME = False

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Enable Copilot in Power Apps and navigate Power Apps Studio ready to build.",
    "LO2: Prepare a Dataverse table with clear names and descriptions so Copilot can build accurate apps.",
    "LO3: Write effective prompts that get Copilot to build the app you actually want.",
    "LO4: Create a working canvas app from a single plain-language prompt.",
    "LO5: Refine an app's screens, controls and layouts by describing the changes to Copilot.",
    "LO6: Generate and explain Power Fx formulas with Copilot, and verify them against your data.",
    "LO7: Add an in-app Copilot chat so end users can query the app's data in natural language.",
    "LO8: Build a Power Automate flow with Copilot and call it from a canvas app.",
    "LO9: Automate approval and notification scenarios with Copilot-built flows.",
    "LO10: Share and govern AI-assisted apps responsibly.",
]
LO_TITLES = [
    "Enable Copilot & Studio",
    "Prepare Dataverse data",
    "Prompt for apps",
    "App from a prompt",
    "Refine screens",
    "Power Fx formulas",
    "In-app Copilot chat",
    "Flows with Copilot",
    "Approvals & notifications",
    "Share & govern",
]

# ------------------------------------------------------------------ topics
# `concepts` are plain strings ("Title — explanation.") so they render cleanly
# as both slide tiles and Learner-Guide bullets. `weighting` = share of course time.
TOPICS = [
    dict(num=1, code="01",
         title="Get Started with Copilot in Power Apps",
         subtitle="What Copilot in Power Apps and the Power Platform is · Licensing, requirements and enabling Copilot · Copilot in Power Apps Studio · Effective prompting for app building · Preparing data with Dataverse for Copilot",
         weighting="30%",
         concepts=[
            "Copilot in Power Apps — Microsoft's AI assistant built into Power Apps that turns plain-English descriptions into working app screens, tables and formulas.",
            "The Power Platform — Microsoft's low-code suite (Power Apps, Power Automate, Power BI and Copilot Studio); Copilot spans it, so an app you build can connect to flows and data.",
            "Canvas apps — the app type you build here: you describe a screen and Copilot lays out the controls, while you keep full control of the design.",
            "Licensing and requirements — Copilot features need a Power Apps environment with Copilot switched on and a Microsoft work or school account, not a personal one; some tenants also need an admin toggle.",
            "Enabling Copilot — Copilot is turned on per environment in the Power Platform admin center and in Studio's settings; the trainer confirms it is on before the labs.",
            "Power Apps Studio — the browser-based design surface where you build the app; the Copilot pane sits alongside the canvas, the tree view and the property pane.",
            "Effective prompting for apps — a good app-building prompt names the app's purpose, the data it works with, the screens you want and the audience, so Copilot builds the right thing.",
            "Dataverse — Microsoft's structured cloud database; clear table and column names with descriptions give Copilot the context it needs to build accurate apps and formulas.",
         ]),
    dict(num=2, code="02",
         title="Build Canvas Apps with Copilot",
         subtitle="Creating an app from a prompt · Refining screens, controls and layouts with Copilot · Generating and explaining Power Fx formulas with Copilot · Adding an in-app Copilot chat for users",
         weighting="45%",
         concepts=[
            "Creating an app from a prompt — describe the app you want (its purpose and its data) and Copilot generates a working, multi-screen canvas app you can run straight away.",
            "Grounding on your data — point Copilot at your Dataverse table so the generated app reads and writes your real records, not placeholder data.",
            "Refining with Copilot — keep the conversation going: ask Copilot to add a screen, change a layout, sort a gallery or restyle a control, all in plain language.",
            "Controls and layouts — galleries, forms, labels, buttons and containers are the building blocks Copilot arranges; you then fine-tune them in the property pane.",
            "Power Fx — Power Apps' Excel-like formula language; Copilot writes Power Fx for you from a description, and explains any formula step by step.",
            "Reading and trusting formulas — always read the Power Fx Copilot generates, test it against known data, and ask Copilot to explain anything unfamiliar before you rely on it.",
            "In-app Copilot chat — a Copilot control you can add to an app so your end users can ask questions of the app's data in natural language.",
            "Human in the loop — Copilot drafts screens, formulas and flows; you run them, test them and decide what to publish.",
         ]),
    dict(num=3, code="03",
         title="Automate and Extend with Copilot",
         subtitle="Building Power Automate flows with Copilot · Integrating flows with canvas apps · Approval and notification scenarios · Sharing and governing AI-assisted apps",
         weighting="25%",
         concepts=[
            "Power Automate — the Power Platform's workflow tool; Copilot builds automated flows from a plain-language description of the trigger and the actions.",
            "Building flows with Copilot — describe what should happen and when (for example 'when a high-priority request is created, email the manager for approval') and Copilot assembles the flow.",
            "Integrating flows with canvas apps — a flow can be called from a canvas app with Power Fx, so a button in your app starts the automation.",
            "Approvals — Power Automate's Approvals action sends a request to an approver, waits for their decision, and branches the flow on approve or reject.",
            "Notifications — flows can send email, Teams messages or mobile notifications to keep people informed as records change.",
            "Sharing apps — canvas apps and their flows are shared with named users or groups, as run-only users or co-owners.",
            "Governing AI-assisted apps — environments, data loss prevention (DLP) policies and connector controls keep low-code apps safe; the owner stays accountable for what the app does.",
            "Verify and document — test every Copilot-built flow end to end, and record what the app and flow do so the solution stays maintainable.",
         ]),
]

# ------------------------------------------------------------------ day themes
DAY_THEMES = {
    1: "Getting Copilot ready in Power Apps, building a canvas app with Copilot, then automating and governing it with Power Automate",
}

# ------------------------------------------------------------------ schedule
# NON-WSQ: no assessment blocks. The single training day totals 540 minutes
# (9:30-18:30) — of which 60 minutes are lunch and 30 minutes are tea breaks, so
# 450 minutes (7.5 hours) are instructional, matching the advertised duration.
def SCHEDULE(lab_titles):
    return {
     1: (DAY_THEMES[1], [
        ("9:30","9:50",20,"admin","Welcome, course introduction, ground rules, and confirming Power Apps access and that Copilot is enabled for the labs"),
        ("9:50","10:40",50,"topic","TOPIC 01 — Get Started with Copilot in Power Apps: what Copilot and the Power Platform are; licensing, requirements and enabling Copilot; a tour of Power Apps Studio; effective prompting for app building; preparing data with Dataverse (concepts + live demo)"),
        ("10:40","11:30",50,"lab","Hands-on: "+lab_titles([1,2])),
        ("11:30","11:45",15,"break","Tea break"),
        ("11:45","12:25",40,"lab","Hands-on: "+lab_titles([3])),
        ("12:25","13:00",35,"topic","TOPIC 02 — Build Canvas Apps with Copilot: creating an app from a prompt; refining screens, controls and layouts; generating and explaining Power Fx; adding an in-app Copilot chat (concepts + live demo)"),
        ("13:00","14:00",60,"lunch","Lunch break"),
        ("14:00","15:20",80,"lab","Hands-on: "+lab_titles([4,5,6])),
        ("15:20","15:45",25,"lab","Hands-on: "+lab_titles([7])),
        ("15:45","16:00",15,"break","Tea break"),
        ("16:00","16:40",40,"topic","TOPIC 03 — Automate and Extend with Copilot: building Power Automate flows with Copilot; integrating flows with canvas apps; approval and notification scenarios; sharing and governing AI-assisted apps (concepts + live demo)"),
        ("16:40","18:15",95,"lab","Hands-on: "+lab_titles([8,9,10])),
        ("18:15","18:30",15,"recap","Course wrap-up, your Copilot-for-Power-Apps workflow and next steps"),
     ]),
    }

# ------------------------------------------------------------------ deck content
COURSE_OVERVIEW = dict(
    section_title="Course Fundamentals",
    concepts_title="How Copilot Works in Power Apps",
    concepts=[
        "From dragging controls to describing outcomes — you tell Copilot the app you want and it builds the screens, the data connections and the formulas.",
        "It works on your real data — point Copilot at a Dataverse table and the app reads and writes your records, not a generic sample.",
        "Two surfaces, one assistant — Copilot builds the app in Studio, and a Copilot control lets your users query the app's data in plain language too.",
        "You stay accountable — Copilot drafts screens, Power Fx and flows; you run, test and decide what to publish.",
    ],
    framework_title="The Describe–Review–Refine Loop",
    framework=[
        ("Prepare", "Know the app's purpose, who will use it, and which Dataverse table holds its data."),
        ("Describe", "Write a clear prompt — the purpose, the data, the screens and the audience."),
        ("Generate", "Let Copilot build the app, the formula or the flow."),
        ("Review", "Run it, test it against known data, and read any Power Fx before you trust it."),
        ("Refine", "Ask Copilot to adjust, then publish and share when it is right."),
    ],
    statement=dict(
        headline="Copilot builds fastest when your prompt is specific and your data is well described.",
        body="This course is hands-on: you build one connected solution — a Maintenance Request app for a facilities team, backed by Dataverse, with Power Fx, an in-app Copilot chat and an approval-and-notification flow — describing each part to Copilot and checking its work before you publish.",
        kicker="THE WORKING RULE",
    ),
    pillars_title="What You'll Build",
    pillars=[
        ("A Copilot-ready foundation", ["Copilot enabled in Power Apps Studio", "A well-described Dataverse table", "A reusable app-prompt pattern"]),
        ("A working canvas app", ["An app generated from a prompt", "Refined screens and layouts", "Power Fx formulas you understand", "An in-app Copilot chat for users"]),
        ("Automation and governance", ["An approval-and-notification flow", "The flow called from the app", "The app shared and governed safely"]),
    ],
    arc_title="How Every Lab Works",
    arc=[
        "The trainer demonstrates the Copilot technique on the shared Harbourfront Facilities app.",
        "You do it yourself in Power Apps — on the sample scenario, or on your own non-confidential app idea.",
        "You run and verify the result against the lab's explicit 'Test it' check.",
        "You read any Power Fx or flow Copilot generated and confirm it does what you asked.",
        "You keep the working app, formula or flow — it becomes part of your Copilot-for-Power-Apps toolkit.",
    ],
)

# ------------------------------------------------------------------ LG content
LG_INTRO = (
    "This Learner Guide accompanies the Copilot for Power Apps (C803) course, conducted by "
    "Tertiary Infotech Academy Pte Ltd. It carries the full detail of all 10 hands-on labs, in the "
    "order you will run them, together with the concepts each lab depends on."
)
LG_INTRO2 = (
    "The labs build one connected result. You take the role of a coordinator at a facilities-management "
    "company, 'Harbourfront Facilities', and use Copilot in Power Apps to build a Maintenance Request "
    "solution: you enable Copilot and prepare a Dataverse table, generate a canvas app from a prompt, "
    "refine its screens and Power Fx, add an in-app Copilot chat, then build an approval-and-notification "
    "flow, integrate it with the app, and share and govern it — checking Copilot's work at every step. "
    "Wherever you can, use your own non-confidential app idea so you leave with skills applied to your own "
    "work; the supplied Harbourfront Facilities scenario is provided for everyone to follow along."
)
LG_SETUP = dict(
    needs=[
        "A laptop (Windows or Mac) with a current Chrome or Edge browser.",
        "A Microsoft work or school account (not a personal Microsoft account) with access to Power Apps at make.powerapps.com — a Microsoft 365 developer or trial tenant is enough to follow every lab.",
        "A Power Apps environment with Dataverse and Copilot enabled — the trainer confirms your environment and that Copilot is switched on at the start of the day.",
        "Access to Power Automate (flow.microsoft.com or the Flows area in Power Apps) using the same account, for the automation labs.",
        "The 'Harbourfront Facilities — Maintenance' scenario notes (the column list and sample requests the trainer shares) — or your own non-confidential app idea and data.",
    ],
    verify_text="Before Lab 1, confirm you can sign in at make.powerapps.com, that you can see and select your Power Apps environment, and that the Copilot pane appears when you create or open an app. If Copilot is not visible or Dataverse is unavailable, tell the trainer.",
    verify_code="Sign in at make.powerapps.com  ·  select your environment (top-right)  ·  New > check the Copilot pane appears  ·  open Tables to confirm Dataverse is available",
    conventions=[
        "Placeholders such as <YOUR ENVIRONMENT> or <YOUR NAME> are replaced with your own values.",
        "Prompts you give Copilot are shown in a shaded box — type or paste them into the Copilot pane (in Studio) or the app-creation prompt box.",
        "App paths (for example Power Apps > Solutions, or Studio > Insert > Copilot) and menu names are written as you will use them; Copilot's own buttons and wording may change over time.",
        "Every lab ends with a 'Test it' step — run the app, formula or flow and verify the result before you move on.",
    ],
)
LAB_NOTE = (
    "Use only accounts and data you are authorised to use. Never put passwords, personal identifiers or "
    "confidential business data into a Copilot prompt or a Dataverse table used for practice — use the "
    "supplied Harbourfront Facilities sample scenario if in doubt. Power Apps, Copilot and Power Automate "
    "screens, menu names and buttons may differ slightly between tenants and change over time; the trainer "
    "will point out the current location on the day."
)
LG_WRAPUP = dict(
    title="Wrap-Up",
    intro="In one day you have taken a facilities team's everyday need — logging, approving and tracking maintenance requests — and turned it into a working, automated Power Apps solution, using Copilot at every step and checking its work before publishing.",
    sections=[
        dict(title="What you built", bullets=[
            "Copilot enabled in Power Apps Studio and a clear picture of what Copilot can and cannot do.",
            "A well-described Dataverse table that gives Copilot the context to build accurately.",
            "A reusable app-prompt pattern (purpose, data, screens, audience) you can apply to any app.",
            "A working canvas app generated from a prompt, with refined screens, controls and layouts.",
            "Power Fx formulas written and explained by Copilot — and verified by you against known data.",
            "An in-app Copilot chat that lets end users ask questions of the app's data.",
            "A Power Automate approval-and-notification flow, built with Copilot and called from the app.",
            "The app and flow shared with the right people and governed with sensible safeguards.",
        ]),
        dict(title="What to do next", bullets=[
            "Point these techniques at one real, recurring request or process in your own team and build it.",
            "Keep verifying: run every Copilot-built app and flow end to end, and read the Power Fx before you trust it.",
            "Save your best app-building prompts so you and your team can reuse them.",
            "Keep confidential data out of prompts and practice tables, and note where Copilot helped so your work stays accountable.",
        ]),
    ],
)
LG_NEXT_STEPS = [
    "First pass: complete every lab yourself, following the steps and verifying each 'Test it' check.",
    "Second pass: rebuild the Maintenance Request solution from memory, writing your own Copilot prompts.",
    "Apply the techniques to a real, non-confidential app or process from your own organisation.",
    "Review each lab's detailed steps in this guide and re-run the labs in your own Power Apps environment.",
]
LG_GLOSSARY = [
    ("Copilot", "Microsoft's AI assistant built into Power Apps; it turns plain-English descriptions into app screens, Power Fx formulas and flows, and explains what it built."),
    ("Power Apps", "Microsoft's low-code platform for building business applications; this course builds canvas apps in it."),
    ("Power Platform", "Microsoft's low-code suite — Power Apps, Power Automate, Power BI and Copilot Studio — that share data and connectors."),
    ("Canvas app", "A Power Apps app where you (and Copilot) arrange controls freely on each screen, giving full control of the layout."),
    ("Power Apps Studio", "The browser-based design surface at make.powerapps.com where you build and edit an app, with the Copilot pane alongside."),
    ("Dataverse", "Microsoft's structured cloud database of tables, columns and relationships that stores the app's data."),
    ("Table", "A Dataverse structure that holds records (rows) with defined columns — for example the Maintenance Requests table in this course."),
    ("Column", "A single field in a table (such as Priority or Status); clear names and descriptions help Copilot build accurately."),
    ("Prompt", "The plain-language instruction you give Copilot; a good app prompt states the purpose, the data, the screens and the audience."),
    ("Power Fx", "Power Apps' Excel-like formula language; Copilot can write it from a description and explain any formula step by step."),
    ("Gallery", "A control that lists many records (rows) from a table, such as the list of maintenance requests."),
    ("Form", "A control for viewing, editing or creating a single record, such as submitting a new request."),
    ("Power Automate", "The Power Platform's workflow tool; Copilot builds automated flows from a description of the trigger and actions."),
    ("Flow", "An automated workflow in Power Automate — a trigger followed by actions, such as sending an approval when a request is created."),
    ("Approval", "A Power Automate action that sends a request to an approver, waits for their decision, and branches on approve or reject."),
    ("Connector", "A pre-built link that lets an app or flow talk to a service such as Dataverse, Outlook or Teams."),
    ("Data loss prevention (DLP)", "Governance policies that control which connectors an app or flow may combine, to keep business data safe."),
    ("Publish", "Saving and releasing a version of an app so shared users run the latest version."),
    ("Human in the loop", "The practice of a person reviewing, testing and approving AI-generated screens, formulas and flows before they are relied upon."),
]

# ------------------------------------------------------------------ version history
VERSION_HISTORY = [
    ("1.0", VERSION_DATE, "Initial release — C803 Copilot for Power Apps courseware.", TRAINER),
]
