# Lab 7 — Add an In-App Copilot Chat for Users

**Topic 02:** Build Canvas Apps with Copilot  |  **Day 1**  |  **Approx. 25 min**  |  **Course:** Microsoft Copilot for Power Apps (C803)

## Scenario

Harbourfront Facilities manages several commercial buildings. Staff currently report faults — a flickering light, a blocked drain, a warm server room — by email and phone, so requests get lost and no one can see what is outstanding. Your manager wants a simple app where staff log a maintenance request, a coordinator tracks it, and high-priority requests are automatically sent for approval and the requester is notified. Across this course you use Copilot in Power Apps to build that solution end to end. Use this scenario only if you cannot use a real, non-confidential app idea of your own; your own idea is always preferred.

## Goal

Add a Copilot chat control so end users can ask questions of the app's data in natural language.

## What you'll build

An in-app Copilot chat on the 'Harbourfront Maintenance' app that answers end-user questions from the Maintenance Requests data.

**Tools and techniques:** Copilot control (Insert > Copilot), grounding on Dataverse, end-user Q&A

## Prerequisites

- Lab 6 complete — an app with working Power Fx.
- The in-app Copilot control enabled for your environment (admin setting).

## Steps

### Step 1

Confirm the Copilot control is available in your environment (an admin setting enables the in-app Copilot control). If it is off, the trainer will show a shared app with it enabled.

### Step 2

Open the app in Studio, go to the browse screen, then Insert > Input (or 'Copilot') and add the 'Copilot' control to the screen.

### Step 3

Set the control's data source to your 'Maintenance Requests' table so it answers from your app's records, not the open web.

### Step 4

Position and size the control so it sits neatly on the screen (for example a panel on the right), and give the screen room for it.

### Step 5

Run Preview and ask the in-app Copilot a question a real user would ask.

Prompt to give Copilot (type or paste into the Copilot pane):

```text
How many high-priority requests are still open, and where are they?
```

### Step 6

Ask a second, more specific question and confirm the answer matches what you can see in the gallery.

Prompt to give Copilot (type or paste into the Copilot pane):

```text
List the requests in Tower A that are not yet resolved.
```

### Step 7

Verify: cross-check one of Copilot's answers against the browse gallery or the table data — never present an answer you have not confirmed.

### Step 8

Save and publish a first version of the app (File > Save, then Publish) so it is ready to automate in Domain 3.

## Test it

The in-app Copilot control answers at least two natural-language questions from your Maintenance Requests data, and its answers match what you can verify in the app, with a first version published.

## Troubleshooting

- **The Copilot control isn't in the Insert menu.** It is an admin-controlled preview feature; the trainer will enable it or show a shared app.
- **The chat answers from the web, not your data.** Set the control's data source to the Maintenance Requests table.
- **Answers look wrong.** Cross-check against the gallery; if the data source is right but answers drift, rephrase the question more specifically.

## Challenge

Write three example questions a facilities coordinator would ask, and confirm the in-app Copilot answers all three from your data.

## Reflection

LO7 — Add an in-app Copilot chat so end users can query the app's data in natural language. In your own words, how will you use this in your own work, and how will you check Copilot got it right?

## Deliverable

Save your work — it becomes part of your **Harbourfront Facilities** Maintenance Request solution, the single deliverable you complete and govern in Lab 10.

---

*Microsoft Copilot for Power Apps (C803) · C803 · Version v1.1 · © 2026 Tertiary Infotech Academy Pte Ltd*
