# Lab 3 — Write Effective Prompts for App Building

**Topic 01:** Get Started with Copilot in Power Apps  |  **Day 1**  |  **Approx. 70 min**  |  **Course:** Microsoft Copilot for Power Apps (C803)

## Scenario

Harbourfront Facilities manages several commercial buildings. Staff currently report faults — a flickering light, a blocked drain, a warm server room — by email and phone, so requests get lost and no one can see what is outstanding. Your manager wants a simple app where staff log a maintenance request, a coordinator tracks it, and high-priority requests are automatically sent for approval and the requester is notified. Across this course you use Copilot in Power Apps to build that solution end to end. Use this scenario only if you cannot use a real, non-confidential app idea of your own; your own idea is always preferred.

## Goal

Compare a vague app prompt with a specific one and capture a reusable four-part prompt pattern for building apps.

## What you'll build

A written four-part app-prompt pattern (Purpose · Data · Screens · Audience) and one strong, tested app-building prompt saved for reuse.

**Tools and techniques:** Copilot prompt box, prompt design, Purpose/Data/Screens/Audience pattern

## Prerequisites

- Lab 2 complete — the Maintenance Requests table exists so you can name it in a prompt.

## Steps

### Step 1

From the Power Apps home page, open the 'Start with Copilot' prompt box (you will preview prompts here; you build the real app in Lab 4).

### Step 2

Type a deliberately vague prompt and read how generic Copilot's proposed app is.

Prompt to give Copilot (type or paste into the Copilot pane):

```text
Build me an app for maintenance.
```

### Step 3

Now type a specific prompt for the same intent and compare what Copilot proposes.

Prompt to give Copilot (type or paste into the Copilot pane):

```text
Build a canvas app for building staff to log maintenance requests using my Maintenance Requests table in Dataverse. It needs a screen to browse open requests, a screen to view one request in detail, and a form to submit a new request. The audience is non-technical facilities staff, so keep it simple and clearly labelled.
```

### Step 4

Write down the four parts that made the second prompt work: the Purpose (what the app is for), the Data (which table), the Screens (what pages you want) and the Audience (who uses it).

### Step 5

Capture your reusable pattern where you can find it — a notes doc, or pinned in your team's notes.

Prompt to give Copilot (type or paste into the Copilot pane):

```text
PURPOSE: what the app is for | DATA: which Dataverse table | SCREENS: the pages you want | AUDIENCE: who uses it and how simple it must be
```

### Step 6

Add the conditions that keep results trustworthy: always name the exact table, list the screens explicitly, and state the audience so Copilot pitches the design correctly.

### Step 7

Rewrite one app idea of your own using the pattern (or refine the maintenance prompt), and read Copilot's proposal — do not build it yet.

### Step 8

Save your best app-building prompt — you will reuse this pattern and this exact prompt in Lab 4 to generate the app.

## Test it

You can show two proposals for the same intent (vague vs specific), a written four-part prompt pattern, and one saved app-building prompt ready to use in Lab 4.

## Troubleshooting

- **Copilot's proposal ignores your table.** Name the exact table ('Maintenance Requests') in the prompt; Copilot grounds better when the data source is explicit.
- **The proposal has too many screens.** State the screens you want explicitly and say 'no other screens'.
- **Copilot proposes a model-driven app.** Say 'canvas app' in the prompt — this course builds canvas apps.

## Challenge

Write a second app prompt for a different idea of your own using the four-part pattern, and compare how specific you can make it.

## Reflection

LO3 — Write effective prompts that get Copilot to build the app you actually want. In your own words, how will you use this in your own work, and how will you check Copilot got it right?

## Deliverable

Save your work — it becomes part of your **Harbourfront Facilities** Maintenance Request solution, the single deliverable you complete and govern in Lab 10.

---

*Microsoft Copilot for Power Apps (C803) · C803 · Version v1.2 · © 2026 Tertiary Infotech Academy Pte Ltd*
