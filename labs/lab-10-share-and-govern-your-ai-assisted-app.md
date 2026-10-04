# Lab 10 — Share and Govern Your AI-Assisted App

**Topic 03:** Automate and Extend with Copilot  |  **Day 2**  |  **Approx. 60 min**  |  **Course:** Microsoft Copilot for Power Apps (C803)

## Scenario

Harbourfront Facilities manages several commercial buildings. Staff currently report faults — a flickering light, a blocked drain, a warm server room — by email and phone, so requests get lost and no one can see what is outstanding. Your manager wants a simple app where staff log a maintenance request, a coordinator tracks it, and high-priority requests are automatically sent for approval and the requester is notified. Across this course you use Copilot in Power Apps to build that solution end to end. Use this scenario only if you cannot use a real, non-confidential app idea of your own; your own idea is always preferred.

## Goal

Share the app and flow with the right people and apply sensible governance to your AI-assisted solution.

## What you'll build

A shared 'Harbourfront Maintenance' app with the flow's connections in place, plus a short governance note covering sharing, environment, DLP and documentation.

**Tools and techniques:** App sharing, run-only vs co-owner, environments, DLP awareness, documentation

## Prerequisites

- Lab 9 complete — the full approval-and-notification flow works end to end.

## Steps

### Step 1

In the maker portal, open 'Apps', select 'Harbourfront Maintenance', and choose 'Share'.

### Step 2

Share with a colleague or a group as run-only users (they can use the app but not edit it), and note the difference between run-only users and co-owners who can edit. Confirm the app's flow connections are included so the automation still works for shared users.

### Step 3

Review governance — the environment: confirm which environment the app and flow live in, and understand that moving between Dev/Test/Prod environments is how organisations control release. Note your environment name.

### Step 4

Review governance — data loss prevention (DLP): understand that admins use DLP policies to control which connectors (Dataverse, Outlook, Teams, etc.) can be combined; check your app only uses connectors your organisation allows.

### Step 5

Ask Copilot to help you document the solution so it stays maintainable.

Prompt to give Copilot (type or paste into the Copilot pane):

```text
Write a short description of this app and its flow for other makers: what it does, which Dataverse table it uses, what the approval flow does, and who it is shared with.
```

### Step 6

Save that description in the app's details (Apps > ... > Details > Description) and in your team notes, so the next person understands the solution.

### Step 7

Confirm accountability: you — the owner — are responsible for what the app and flow do; Copilot only helped build them. Note who to contact if the flow needs changing.

### Step 8

Final check: run the shared app once more end to end (submit a High-priority request, approve it, see the status update) to confirm the complete Harbourfront Facilities solution works.

## Test it

The app is shared with at least one user or group with the flow's connections included, you can state the environment and which connectors the app uses, and a plain-language description of the solution is saved with the app.

## Troubleshooting

- **Shared users get a connection error.** Share the app's flow connections (or use a service/connection reference) so shared users can run the automation.
- **A colleague can edit when they shouldn't.** Re-share as a run-only user, not a co-owner.
- **You're unsure which connectors are allowed.** Ask your admin about the environment's DLP policy before publishing to real users.

## Challenge

Ask Copilot to write a one-paragraph 'what this app does' note suitable for a shared user's first-run screen, and add it to the home screen.

## Reflection

LO10 — Share and govern AI-assisted apps responsibly. In your own words, how will you use this in your own work, and how will you check Copilot got it right?

## Deliverable

Save your work — it becomes part of your **Harbourfront Facilities** Maintenance Request solution, the single deliverable you complete and govern in Lab 10.

---

*Microsoft Copilot for Power Apps (C803) · C803 · Version v1.2 · © 2026 Tertiary Infotech Academy Pte Ltd*
