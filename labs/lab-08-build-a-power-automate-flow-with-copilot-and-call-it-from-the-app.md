# Lab 8 — Build a Power Automate Flow with Copilot and Call It from the App

**Topic 03:** Automate and Extend with Copilot  |  **Day 1**  |  **Approx. 32 min**  |  **Course:** Microsoft Copilot for Power Apps (C803)

## Scenario

Harbourfront Facilities manages several commercial buildings. Staff currently report faults — a flickering light, a blocked drain, a warm server room — by email and phone, so requests get lost and no one can see what is outstanding. Your manager wants a simple app where staff log a maintenance request, a coordinator tracks it, and high-priority requests are automatically sent for approval and the requester is notified. Across this course you use Copilot in Power Apps to build that solution end to end. Use this scenario only if you cannot use a real, non-confidential app idea of your own; your own idea is always preferred.

## Goal

Use Copilot to build an automated flow, then integrate it with the canvas app so a button starts the automation.

## What you'll build

A Copilot-built Power Automate flow that notifies the manager of high-priority requests, tested and callable from the 'Harbourfront Maintenance' app.

**Tools and techniques:** Power Automate, Copilot flow builder, Dataverse trigger, Office 365 Outlook, Power Fx integration

## Prerequisites

- Lab 7 complete and a first version published.
- Access to Power Automate in the same environment, and an Outlook mailbox for testing.

## Steps

### Step 1

Go to Power Automate (from the app menu 'Flows', or make.powerautomate.com) in the same environment, and choose to create a flow with Copilot — the 'Describe it to design it' prompt box.

### Step 2

Describe the flow you want in plain language and let Copilot assemble it.

Prompt to give Copilot (type or paste into the Copilot pane):

```text
When a new row is created in my Maintenance Requests table in Dataverse and its Priority is High, send an email to the facilities manager with the request's Title, Location and Description.
```

### Step 3

Review the flow Copilot built: confirm the trigger is 'When a row is added' on Maintenance Requests, that there is a condition on Priority = High, and that the action is 'Send an email (V2)'. Add the manager's address (use your own for testing).

### Step 4

Save the flow, name it 'Notify manager of high-priority request', and test it: create a High-priority request (in the app or the table) and confirm the email arrives.

### Step 5

Read what Copilot built, step by step, so you understand it — ask Copilot to explain any action you are unsure of before you rely on the flow.

### Step 6

Integrate the flow with the app: open 'Harbourfront Maintenance' in Studio, add the Power Automate flow to the app (Power Automate pane > add your flow), and select the submit button.

### Step 7

Ask Copilot in Studio for the Power Fx to run the flow when the button is pressed, or add it yourself. Expected shape (name matches your flow):

Power Fx (paste onto the control's property; adjust field names to match your table):

```text
'Notifymanagerofhighpriorityrequest'.Run(TitleInput.Text, LocationInput.Text, DescriptionInput.Text)
```

### Step 8

Run Preview, submit a High-priority request, and confirm both that the record is saved and that the flow runs and the email arrives. Save the app.

## Test it

The flow runs when a high-priority request is created (or the app button is pressed), the manager receives an email with the request details, and you can explain what each step of the flow does.

## Troubleshooting

- **The trigger doesn't fire.** Confirm the trigger table is Maintenance Requests and that the new row's Priority is exactly 'High'.
- **No email arrives.** Check the Office 365 Outlook connection is signed in as you and the recipient address is valid; look at the flow run history for errors.
- **The app can't see the flow.** Add the flow to the app from the Power Automate pane in Studio before calling it in Power Fx.

## Challenge

Add the request's Category and a link back to the app in the notification email by refining the flow with Copilot.

## Reflection

LO8 — Build a Power Automate flow with Copilot and call it from a canvas app. In your own words, how will you use this in your own work, and how will you check Copilot got it right?

## Deliverable

Save your work — it becomes part of your **Harbourfront Facilities** Maintenance Request solution, the single deliverable you complete and govern in Lab 10.

---

*Microsoft Copilot for Power Apps (C803) · C803 · Version v1.1 · © 2026 Tertiary Infotech Academy Pte Ltd*
