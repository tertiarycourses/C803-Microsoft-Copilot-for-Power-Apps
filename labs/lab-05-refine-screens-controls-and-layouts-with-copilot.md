# Lab 5 — Refine Screens, Controls and Layouts with Copilot

**Topic 02:** Build Canvas Apps with Copilot  |  **Day 1**  |  **Approx. 27 min**  |  **Course:** Copilot for Power Apps (C803)

## Scenario

Harbourfront Facilities manages several commercial buildings. Staff currently report faults — a flickering light, a blocked drain, a warm server room — by email and phone, so requests get lost and no one can see what is outstanding. Your manager wants a simple app where staff log a maintenance request, a coordinator tracks it, and high-priority requests are automatically sent for approval and the requester is notified. Across this course you use Copilot in Power Apps to build that solution end to end. Use this scenario only if you cannot use a real, non-confidential app idea of your own; your own idea is always preferred.

## Goal

Improve the generated app's screens, controls and layout by describing the changes to Copilot in plain language.

## What you'll build

A refined 'Harbourfront Maintenance' app: the browse gallery sorted and filtered sensibly, clearer labels, and a tidier layout produced by describing changes to Copilot.

**Tools and techniques:** Copilot pane in Studio, galleries, forms, labels, layout and styling

## Prerequisites

- Lab 4 complete — the 'Harbourfront Maintenance' app runs on your data.

## Steps

### Step 1

Open the 'Harbourfront Maintenance' app in Studio and open the Copilot pane.

### Step 2

Ask Copilot to sort the browse gallery so the newest requests are first.

Prompt to give Copilot (type or paste into the Copilot pane):

```text
Sort the requests gallery on the browse screen so the most recently created requests appear at the top.
```

### Step 3

Ask Copilot to show only open work by filtering out resolved requests.

Prompt to give Copilot (type or paste into the Copilot pane):

```text
On the browse screen, show only requests whose Status is not Resolved.
```

### Step 4

Ask Copilot to make each gallery item clearer by showing the key fields.

Prompt to give Copilot (type or paste into the Copilot pane):

```text
In each item of the requests gallery, show the Title in bold, then Location and Category on one line, and show the Priority as a coloured tag.
```

### Step 5

Ask Copilot to improve a label and the screen title for a non-technical audience.

Prompt to give Copilot (type or paste into the Copilot pane):

```text
Rename the browse screen's title to 'Open Maintenance Requests' and change the new-request button label to '+ New Request'.
```

### Step 6

Ask Copilot to tidy the detail screen's layout.

Prompt to give Copilot (type or paste into the Copilot pane):

```text
On the detail screen, group the request fields into a single readable card with clear field labels and consistent spacing.
```

### Step 7

After each change, run Preview (F5) and confirm the app still works and looks clearer; if a change is not what you meant, tell Copilot what to adjust and re-run.

### Step 8

Save the app. Keep note of one change Copilot made that you would otherwise have done by hand — that is the time it saves you.

## Test it

The browse gallery is sorted newest-first and hides resolved requests, gallery items and the detail screen are clearer, and the app still runs correctly in Preview after the refinements.

## Troubleshooting

- **A refinement changed the wrong control.** Tell Copilot which screen and control you mean ('the gallery on the browse screen') and re-run.
- **The filter hides everything.** Check the Status choice values match ('Resolved'); ask Copilot to show the formula it used.
- **Layout looks cramped on tablet.** Ask Copilot to increase spacing and use a container to align the fields.

## Challenge

Ask Copilot to add a colour legend explaining what red/amber/green mean for priority.

## Reflection

LO5 — Refine an app's screens, controls and layouts by describing the changes to Copilot. In your own words, how will you use this in your own work, and how will you check Copilot got it right?

## Deliverable

Save your work — it becomes part of your **Harbourfront Facilities** Maintenance Request solution, the single deliverable you complete and govern in Lab 10.

---

*Copilot for Power Apps (C803) · C803 · Version v1.0 · © 2026 Tertiary Infotech Academy Pte Ltd*
