# Lab 9 — Automate Approval and Notification Scenarios

**Topic 03:** Automate and Extend with Copilot  |  **Day 2**  |  **Approx. 75 min**  |  **Course:** Microsoft Copilot for Power Apps (C803)

## Scenario

Harbourfront Facilities manages several commercial buildings. Staff currently report faults — a flickering light, a blocked drain, a warm server room — by email and phone, so requests get lost and no one can see what is outstanding. Your manager wants a simple app where staff log a maintenance request, a coordinator tracks it, and high-priority requests are automatically sent for approval and the requester is notified. Across this course you use Copilot in Power Apps to build that solution end to end. Use this scenario only if you cannot use a real, non-confidential app idea of your own; your own idea is always preferred.

## Goal

Extend the flow into an approval-and-notification scenario that updates the request based on the decision.

## What you'll build

An approval-and-notification flow: high-priority requests go to the manager for approval, the request Status is updated on the decision, and the requester is notified of the outcome.

**Tools and techniques:** Power Automate Approvals, conditions/branches, Dataverse update row, notifications

## Prerequisites

- Lab 8 complete — a working flow triggered by high-priority requests, callable from the app.

## Steps

### Step 1

Open your 'Notify manager of high-priority request' flow and edit it. Ask Copilot to turn the notification into an approval.

Prompt to give Copilot (type or paste into the Copilot pane):

```text
Instead of just emailing the manager, start an approval and wait for the manager to approve or reject this high-priority request.
```

### Step 2

Confirm Copilot added a 'Start and wait for an approval' action (Approve/Reject type) addressed to the manager, with the request's details in the approval message.

### Step 3

Add the decision branch. Ask Copilot to handle both outcomes.

Prompt to give Copilot (type or paste into the Copilot pane):

```text
After the approval, if it is approved set this request's Status to Approved; if it is rejected set the Status to Resolved with a note that it was rejected.
```

### Step 4

Confirm the flow now has a Condition on the approval outcome and an 'Update a row' action on Maintenance Requests in each branch that sets Status correctly.

### Step 5

Add the requester notification. Ask Copilot to close the loop.

Prompt to give Copilot (type or paste into the Copilot pane):

```text
After the status is updated, send an email to the person who created the request telling them whether it was approved or rejected.
```

### Step 6

Save the flow and test the approve path: create a High-priority request, open the approval (in Power Automate, Outlook or Teams), approve it, and confirm the request's Status becomes Approved and the requester is emailed.

### Step 7

Test the reject path with a second request: reject it, and confirm the Status and the requester's email reflect the rejection.

### Step 8

Check the app: open 'Harbourfront Maintenance' and confirm the browse gallery now shows the updated statuses from the flow — the automation and the app are working together.

## Test it

Approving a high-priority request sets its Status to Approved and emails the requester; rejecting one sets the Status accordingly and emails the requester; and the app's gallery reflects both outcomes.

## Troubleshooting

- **The approval never arrives.** Confirm the approver address is valid and that the 'Start and wait for an approval' action is before the condition.
- **Status doesn't update.** Check each 'Update a row' action targets the triggering record's row ID and sets the Status choice to a valid value.
- **Both branches run.** Ensure the outcome is checked with a Condition (Outcome = Approve) so only one branch's actions run.

## Challenge

Add a comment box to the approval and write the manager's comment into the request's Resolution Notes on rejection.

## Reflection

LO9 — Automate approval and notification scenarios with Copilot-built flows. In your own words, how will you use this in your own work, and how will you check Copilot got it right?

## Deliverable

Save your work — it becomes part of your **Harbourfront Facilities** Maintenance Request solution, the single deliverable you complete and govern in Lab 10.

---

*Microsoft Copilot for Power Apps (C803) · C803 · Version v1.2 · © 2026 Tertiary Infotech Academy Pte Ltd*
