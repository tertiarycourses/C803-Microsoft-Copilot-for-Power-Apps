#!/usr/bin/env python3
"""Generate the labs/ folder (lab-NN-*.md + README.md + tools.md) for the
NON-WSQ course DIRECTLY from the single source (course_data.py + data_domainN.py),
so the standalone lab files stay 100% aligned with the PPT, LP and LG.

The aligned parts — lab title, objective, "goal" (desc), "what you'll build",
tools, step instructions/prompts/formulas, and "Test it" — are taken verbatim
from the single source. Per-lab enrichment (approx time, prerequisites,
troubleshooting, challenge) lives in ENRICH below, keyed by global lab number.
"""
import os, sys, re, importlib, glob as _g

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import course_data as C

def _load_domains():
    acts = []
    for f in sorted(_g.glob(os.path.join(HERE, "data_domain[0-9]*.py")),
                    key=lambda q: int("".join(c for c in os.path.basename(q) if c.isdigit()) or 0)):
        n = "".join(c for c in os.path.basename(f) if c.isdigit())
        acts += getattr(importlib.import_module(os.path.basename(f)[:-3]), f"DOMAIN{n}", [])
    return acts
ACT = _load_domains()
SCENARIO = getattr(importlib.import_module("data_domain1"), "SCENARIO", "")

def _find_repo(start):
    d = start
    for _ in range(8):
        d = os.path.dirname(d)
        if os.path.isdir(os.path.join(d, "courseware")) and os.path.isdir(os.path.join(d, "labs")):
            return d
    return os.path.dirname(os.path.dirname(start))
REPO = _find_repo(HERE)
LABS = os.path.join(REPO, "labs")
TOPICS_BY_NUM = {t["num"]: t for t in C.TOPICS}

def slug(title):
    s = "".join(ch.lower() if ch.isalnum() else " " for ch in title)
    return "-".join(s.split())

def is_formula(cmd):
    toks = ("Switch(", "Filter(", "CountRows(", "ThisItem", "Color.", ".Run(", ".Value", "\" & ", "DateDiff(")
    return any(t in cmd for t in toks) or cmd.strip().startswith("=")

# ---- per-lab enrichment (NOT alignment-critical; lab-only detail) -----------
ENRICH = {
 1: dict(mins=30, prereq=["A Microsoft work or school account with access to Power Apps.",
                          "Copilot and Dataverse enabled in your environment (the trainer confirms this)."],
    trouble=["**You only have a personal Microsoft account.** Copilot for Power Apps needs a work or school account; ask the trainer for a training tenant sign-in.",
             "**No environment appears in the picker.** You may not be assigned to one yet — tell the trainer so they can add you.",
             "**The Copilot pane/icon is missing.** Copilot may be off for the environment; the trainer will enable it or share a Copilot-ready environment."],
    challenge="Open the Copilot pane in a blank app and ask it to add a screen, then undo — get a feel for how it responds before Lab 4."),
 2: dict(mins=30, prereq=["Lab 1 complete — you are signed in to the correct, Copilot-enabled environment."],
    trouble=["**'New table' is greyed out.** Dataverse may not be provisioned in your environment; tell the trainer.",
             "**A choice column won't save its options.** Add each option on its own line and save the column before adding the next.",
             "**You can't find the table later.** Check you are still in the same environment (top-right picker) — tables are per-environment."],
    challenge="Add a description to every column explaining what a facilities coordinator would put there — the richer the descriptions, the better Copilot builds in Lab 4."),
 3: dict(mins=70, prereq=["Lab 2 complete — the Maintenance Requests table exists so you can name it in a prompt."],
    trouble=["**Copilot's proposal ignores your table.** Name the exact table ('Maintenance Requests') in the prompt; Copilot grounds better when the data source is explicit.",
             "**The proposal has too many screens.** State the screens you want explicitly and say 'no other screens'.",
             "**Copilot proposes a model-driven app.** Say 'canvas app' in the prompt — this course builds canvas apps."],
    challenge="Write a second app prompt for a different idea of your own using the four-part pattern, and compare how specific you can make it."),
 4: dict(mins=45, prereq=["Lab 3 complete — you have a saved, specific app-building prompt.",
                          "The Maintenance Requests table with sample rows (Lab 2)."],
    trouble=["**The app shows no data.** Confirm you chose Dataverse and the Maintenance Requests table when Copilot asked for a data source.",
             "**A submitted request doesn't appear.** Check the form's OnSuccess refreshes the gallery; ask Copilot to 'refresh the requests gallery after a new request is submitted'.",
             "**Generation fails or times out.** Simplify the prompt to the three screens, generate, then add extras by refining in Lab 5."],
    challenge="Ask Copilot to add a search box to the browse screen that filters requests by Title, then test it."),
 5: dict(mins=45, prereq=["Lab 4 complete — the 'Harbourfront Maintenance' app runs on your data."],
    trouble=["**A refinement changed the wrong control.** Tell Copilot which screen and control you mean ('the gallery on the browse screen') and re-run.",
             "**The filter hides everything.** Check the Status choice values match ('Resolved'); ask Copilot to show the formula it used.",
             "**Layout looks cramped on tablet.** Ask Copilot to increase spacing and use a container to align the fields."],
    challenge="Ask Copilot to add a colour legend explaining what red/amber/green mean for priority."),
 6: dict(mins=75, prereq=["Lab 5 complete — a refined app with a Priority tag, a header and a detail screen."],
    trouble=["**A formula shows an error (red squiggle).** Field or choice names may differ; select the control, read the error, and ask Copilot to fix it for your exact column names.",
             "**The colour never turns red.** Confirm the Priority choice value is exactly 'High' (check the table's choice options).",
             "**The count doesn't match the gallery.** The gallery may be filtered while the count is not — align both to the same 'not Resolved' condition."],
    challenge="Ask Copilot for a formula that shows 'Overdue' when a High request has been open more than 2 days, and add it to the gallery."),
 7: dict(mins=60, prereq=["Lab 6 complete — an app with working Power Fx.",
                          "The in-app Copilot control enabled for your environment (admin setting)."],
    trouble=["**The Copilot control isn't in the Insert menu.** It is an admin-controlled preview feature; the trainer will enable it or show a shared app.",
             "**The chat answers from the web, not your data.** Set the control's data source to the Maintenance Requests table.",
             "**Answers look wrong.** Cross-check against the gallery; if the data source is right but answers drift, rephrase the question more specifically."],
    challenge="Write three example questions a facilities coordinator would ask, and confirm the in-app Copilot answers all three from your data."),
 8: dict(mins=60, prereq=["Lab 7 complete and a first version published.",
                          "Access to Power Automate in the same environment, and an Outlook mailbox for testing."],
    trouble=["**The trigger doesn't fire.** Confirm the trigger table is Maintenance Requests and that the new row's Priority is exactly 'High'.",
             "**No email arrives.** Check the Office 365 Outlook connection is signed in as you and the recipient address is valid; look at the flow run history for errors.",
             "**The app can't see the flow.** Add the flow to the app from the Power Automate pane in Studio before calling it in Power Fx."],
    challenge="Add the request's Category and a link back to the app in the notification email by refining the flow with Copilot."),
 9: dict(mins=75, prereq=["Lab 8 complete — a working flow triggered by high-priority requests, callable from the app."],
    trouble=["**The approval never arrives.** Confirm the approver address is valid and that the 'Start and wait for an approval' action is before the condition.",
             "**Status doesn't update.** Check each 'Update a row' action targets the triggering record's row ID and sets the Status choice to a valid value.",
             "**Both branches run.** Ensure the outcome is checked with a Condition (Outcome = Approve) so only one branch's actions run."],
    challenge="Add a comment box to the approval and write the manager's comment into the request's Resolution Notes on rejection."),
 10: dict(mins=60, prereq=["Lab 9 complete — the full approval-and-notification flow works end to end."],
    trouble=["**Shared users get a connection error.** Share the app's flow connections (or use a service/connection reference) so shared users can run the automation.",
             "**A colleague can edit when they shouldn't.** Re-share as a run-only user, not a co-owner.",
             "**You're unsure which connectors are allowed.** Ask your admin about the environment's DLP policy before publishing to real users."],
    challenge="Ask Copilot to write a one-paragraph 'what this app does' note suitable for a shared user's first-run screen, and add it to the home screen."),
}

def lab_md(a):
    e = ENRICH.get(a["num"], dict(mins=25, prereq=[], trouble=[], challenge=""))
    t = TOPICS_BY_NUM[a["topic"]]
    lo = C.LEARNING_OUTCOMES[a["num"]-1] if a["num"]-1 < len(C.LEARNING_OUTCOMES) else ""
    lo_text = re.sub(r'^LO\d+:\s*', '', lo).strip().rstrip('.')
    lo_label = lo.split(':', 1)[0] if ':' in lo else f"LO{a['num']}"
    out = []
    out.append(f"# Lab {a['num']} — {a['title']}")
    out.append("")
    out.append(f"**Topic {t['code']}:** {t['title']}  |  **Day {C.LAB_DAY.get(a['num'], 1)}**  |  **Approx. {e['mins']} min**  |  **Course:** {C.TITLE}")
    out.append("")
    out.append("## Scenario"); out.append("")
    out.append(SCENARIO); out.append("")
    out.append("## Goal"); out.append("")
    out.append(a["objective"]); out.append("")
    out.append("## What you'll build"); out.append("")
    out.append(a["build"]); out.append("")
    out.append(f"**Tools and techniques:** {a['services']}"); out.append("")
    if e["prereq"]:
        out.append("## Prerequisites"); out.append("")
        for p in e["prereq"]:
            out.append(f"- {p}")
        out.append("")
    out.append("## Steps"); out.append("")
    for i, (instr, cmd) in enumerate(a["steps"], 1):
        out.append(f"### Step {i}"); out.append("")
        out.append(instr); out.append("")
        if cmd:
            if is_formula(cmd):
                out.append("Power Fx (paste onto the control's property; adjust field names to match your table):")
            else:
                out.append("Prompt to give Copilot (type or paste into the Copilot pane):")
            out.append("")
            out.append("```text")
            out.append(cmd)
            out.append("```")
            out.append("")
    out.append("## Test it"); out.append("")
    out.append(a["test"]); out.append("")
    if e["trouble"]:
        out.append("## Troubleshooting"); out.append("")
        for tb in e["trouble"]:
            out.append(f"- {tb}")
        out.append("")
    if e["challenge"]:
        out.append("## Challenge"); out.append("")
        out.append(e["challenge"]); out.append("")
    out.append("## Reflection"); out.append("")
    out.append(f"{lo_label} — {lo_text}. In your own words, how will you use this in your own work, and how will you check Copilot got it right?")
    out.append("")
    out.append("## Deliverable"); out.append("")
    out.append("Save your work — it becomes part of your **Harbourfront Facilities** Maintenance Request solution, the single deliverable you complete and govern in Lab 10.")
    out.append("")
    out.append("---"); out.append("")
    out.append(f"*{C.TITLE} · {C.COURSE_CODE} · Version {C.VERSION} · © 2026 {C.ORG}*")
    out.append("")
    return "\n".join(out)

# ---- write lab files --------------------------------------------------------
os.makedirs(LABS, exist_ok=True)
written = []
for a in ACT:
    fn = f"lab-{a['num']:02d}-{slug(a['title'])}.md"
    with open(os.path.join(LABS, fn), "w", encoding="utf-8") as f:
        f.write(lab_md(a))
    written.append((a, fn))
    print("Saved", fn)

# ---- README.md (index) ------------------------------------------------------
r = []
r.append(f"# Labs — {C.TITLE}"); r.append("")
r.append(f"**Course Code:** {C.COURSE_CODE}  |  **Version {C.VERSION} · {C.VERSION_DATE}**"); r.append("")
r.append("All 10 labs build a **single connected solution** — a **Maintenance Request** app for the fictional "
         "**Harbourfront Facilities** — which you build, refine, automate and govern with Copilot in Power Apps "
         "across the two days, starting in Lab 1 and completing in Lab 10. Wherever possible, use your own "
         "non-confidential app idea; the Harbourfront Facilities scenario is provided for everyone to follow "
         "along. There is **no assessment** — each lab verifies itself with a 'Test it' step."); r.append("")
r.append("| Topic | Lab | Title |")
r.append("|---|---:|---|")
for a, fn in written:
    r.append(f"| {TOPICS_BY_NUM[a['topic']]['code']} | {a['num']:02d} | [{a['title']}]({fn}) |")
r.append("")
r.append("## Tools"); r.append("")
r.append("See [tools.md](tools.md) for the accounts and apps used across the labs."); r.append("")
r.append("---"); r.append("")
r.append(f"*{C.TITLE} · {C.COURSE_CODE} · Version {C.VERSION} · © 2026 {C.ORG}*"); r.append("")
with open(os.path.join(LABS, "README.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(r))
print("Saved README.md")

# ---- tools.md ---------------------------------------------------------------
tools = f"""# Tools & Accounts — {C.TITLE}

**Course Code:** {C.COURSE_CODE}  |  **Version {C.VERSION} · {C.VERSION_DATE}**

Everything in this course runs in the browser. You need no installs beyond a modern browser.

## Accounts

- **A Microsoft work or school account** (not a personal Microsoft account) with access to **Power Apps** at make.powerapps.com.
- **Copilot enabled** in your Power Apps environment (the trainer confirms access at the start of Day 1).
- **Access to Power Automate** (flow.microsoft.com or the Flows area in Power Apps) using the same account, for the automation labs.
- **An Outlook mailbox** (Office 365) for testing notification and approval emails.

## Apps and services used

- **Power Apps Studio** (make.powerapps.com) — where you build and refine the canvas app, with the Copilot pane alongside.
- **Copilot in Power Apps** — the AI assistant that generates screens, Power Fx and explanations from plain-language prompts.
- **Dataverse** — the structured cloud database holding the Maintenance Requests table.
- **In-app Copilot control** — the Copilot chat you add so end users can query the app's data (admin-enabled).
- **Power Automate** — where Copilot builds the approval-and-notification flow.
- **Office 365 Outlook / Approvals** — used by the flow to email and to request approvals.

## Sample scenario

- **'Harbourfront Facilities — Maintenance'** — a facilities-management company whose staff log building faults. You build a **Maintenance Requests** Dataverse table (columns: Title, Location, Category, Priority, Description, Status, Assigned To, Resolution Notes) and an app on top of it. The trainer shares the column list and a couple of sample requests; or use your own non-confidential app idea.

## Safe use

- Use only accounts and data you are authorised to use. Never put passwords, personal identifiers or confidential business data into a Copilot prompt or a practice Dataverse table — use the sample scenario if in doubt.
- Read every Power Fx formula and test every flow end to end before you rely on it; you — the owner — stay accountable for what the app and flow do.

---

*{C.TITLE} · {C.COURSE_CODE} · Version {C.VERSION} · © 2026 {C.ORG}*
"""
with open(os.path.join(LABS, "tools.md"), "w", encoding="utf-8") as f:
    f.write(tools)
print("Saved tools.md")
print(f"\nDone — {len(written)} labs + README + tools in {LABS}")
