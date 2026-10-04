# Lab 6 — Generate and Explain Power Fx Formulas with Copilot

**Topic 02:** Build Canvas Apps with Copilot  |  **Day 1**  |  **Approx. 75 min**  |  **Course:** Microsoft Copilot for Power Apps (C803)

## Scenario

Harbourfront Facilities manages several commercial buildings. Staff currently report faults — a flickering light, a blocked drain, a warm server room — by email and phone, so requests get lost and no one can see what is outstanding. Your manager wants a simple app where staff log a maintenance request, a coordinator tracks it, and high-priority requests are automatically sent for approval and the requester is notified. Across this course you use Copilot in Power Apps to build that solution end to end. Use this scenario only if you cannot use a real, non-confidential app idea of your own; your own idea is always preferred.

## Goal

Use Copilot to write Power Fx formulas from a description, explain existing formulas, and verify them against your data.

## What you'll build

Several verified Power Fx formulas on your app (a priority colour, an open-requests count, and a days-open value), plus a plain-English explanation of one formula.

**Tools and techniques:** Power Fx, Copilot formula generation and explanation, verification

## Prerequisites

- Lab 5 complete — a refined app with a Priority tag, a header and a detail screen.

## Steps

### Step 1

With the app open, select the Priority tag/label in the gallery. Ask Copilot for a formula that colours it by priority.

Prompt to give Copilot (type or paste into the Copilot pane):

```text
Write a Power Fx formula for the Fill (or Color) of this label that shows red when Priority is High, amber when Medium, and green when Low.
```

### Step 2

Paste Copilot's formula onto the control's Color/Fill property. Below is the shape to expect — adjust the field and choice names to match your table.

Power Fx (paste onto the control's property; adjust field names to match your table):

```text
Switch(ThisItem.Priority.Value, "High", Color.Red, "Medium", Color.Orange, "Low", Color.Green, Color.Gray)
```

### Step 3

Verify: run Preview and confirm a High request shows red, a Medium amber, a Low green. If a colour is wrong, tell Copilot which value is off and re-run.

### Step 4

Add a header count of open requests. Select the browse screen header, add a label, and ask Copilot for the formula.

Prompt to give Copilot (type or paste into the Copilot pane):

```text
Write a Power Fx formula for a label's Text that counts how many requests in the Maintenance Requests table have a Status that is not Resolved, shown as 'Open requests: N'.
```

### Step 5

Paste the formula and check the number matches what you can count in the gallery. Expected shape:

Power Fx (paste onto the control's property; adjust field names to match your table):

```text
"Open requests: " & CountRows(Filter('Maintenance Requests', Status.Value <> "Resolved"))
```

### Step 6

On the detail screen, add a 'Days open' label and ask Copilot for a formula using the created date.

Prompt to give Copilot (type or paste into the Copilot pane):

```text
Write a Power Fx formula for a label's Text that shows how many whole days it has been since this request was created, using its Created On date.
```

### Step 7

Ask Copilot to explain one of its formulas so you understand it before you rely on it.

Power Fx (paste onto the control's property; adjust field names to match your table):

```text
Explain, step by step, what this formula does: Switch(ThisItem.Priority.Value, "High", Color.Red, "Medium", Color.Orange, "Low", Color.Green, Color.Gray)
```

### Step 8

Read the explanation and write one sentence in your notes on what Switch does and why you would trust this formula. Save the app.

## Test it

The priority tag is colour-coded correctly, the header shows a correct count of open requests, the detail screen shows a sensible days-open value, and you can explain in one sentence what one of the formulas does.

## Troubleshooting

- **A formula shows an error (red squiggle).** Field or choice names may differ; select the control, read the error, and ask Copilot to fix it for your exact column names.
- **The colour never turns red.** Confirm the Priority choice value is exactly 'High' (check the table's choice options).
- **The count doesn't match the gallery.** The gallery may be filtered while the count is not — align both to the same 'not Resolved' condition.

## Challenge

Ask Copilot for a formula that shows 'Overdue' when a High request has been open more than 2 days, and add it to the gallery.

## Reflection

LO6 — Generate and explain Power Fx formulas with Copilot, and verify them against your data. In your own words, how will you use this in your own work, and how will you check Copilot got it right?

## Deliverable

Save your work — it becomes part of your **Harbourfront Facilities** Maintenance Request solution, the single deliverable you complete and govern in Lab 10.

---

*Microsoft Copilot for Power Apps (C803) · C803 · Version v1.2 · © 2026 Tertiary Infotech Academy Pte Ltd*
