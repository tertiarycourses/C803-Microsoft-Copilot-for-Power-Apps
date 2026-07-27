"""
Domain 3 — Automate and Extend with Copilot. Labs 8-10.

You finish the solution. Using Copilot in Power Automate, you build a flow that
sends high-priority requests for approval and notifies the requester (Lab 8) and
call that flow from your canvas app; you extend it into a full approval-and-
notification scenario that updates the record on the decision (Lab 9); and you
share the app and flow and put sensible governance around them (Lab 10). At the
end of this domain the Harbourfront Facilities solution is complete.
"""

PROJECT_NOTE = (
 "BUILDING BLOCK — what you do in this lab becomes part of your Harbourfront Facilities Maintenance "
 "Request solution, the single deliverable you build, refine, automate and govern across all 10 labs."
)

DOMAIN3 = [
 dict(
 num=8, topic=3,
 title="Build a Power Automate Flow with Copilot and Call It from the App",
 objective="Use Copilot to build an automated flow, then integrate it with the canvas app so a button starts the automation.",
 desc="Now you automate. Using Copilot in Power Automate, you describe a flow that runs when a high-priority request "
 "is created and emails the facilities manager. You test it, then wire it into your canvas app so submitting a "
 "request can trigger the automation — connecting the app you built to a real workflow. " + PROJECT_NOTE,
 build="A Copilot-built Power Automate flow that notifies the manager of high-priority requests, tested and callable from the 'Harbourfront Maintenance' app.",
 services="Power Automate, Copilot flow builder, Dataverse trigger, Office 365 Outlook, Power Fx integration",
 steps=[
 ("Go to Power Automate (from the app menu 'Flows', or make.powerautomate.com) in the same environment, and choose to create a flow with Copilot — the 'Describe it to design it' prompt box.", ""),
 ("Describe the flow you want in plain language and let Copilot assemble it.",
  "When a new row is created in my Maintenance Requests table in Dataverse and its Priority is High, send an email to the facilities manager with the request's Title, Location and Description."),
 ("Review the flow Copilot built: confirm the trigger is 'When a row is added' on Maintenance Requests, that there is a condition on Priority = High, and that the action is 'Send an email (V2)'. Add the manager's address (use your own for testing).", ""),
 ("Save the flow, name it 'Notify manager of high-priority request', and test it: create a High-priority request (in the app or the table) and confirm the email arrives.", ""),
 ("Read what Copilot built, step by step, so you understand it — ask Copilot to explain any action you are unsure of before you rely on the flow.", ""),
 ("Integrate the flow with the app: open 'Harbourfront Maintenance' in Studio, add the Power Automate flow to the app (Power Automate pane > add your flow), and select the submit button.", ""),
 ("Ask Copilot in Studio for the Power Fx to run the flow when the button is pressed, or add it yourself. Expected shape (name matches your flow):",
  "'Notifymanagerofhighpriorityrequest'.Run(TitleInput.Text, LocationInput.Text, DescriptionInput.Text)"),
 ("Run Preview, submit a High-priority request, and confirm both that the record is saved and that the flow runs and the email arrives. Save the app.", ""),
 ],
 test="The flow runs when a high-priority request is created (or the app button is pressed), the manager receives an email with the request details, and you can explain what each step of the flow does.",
 ),
 dict(
 num=9, topic=3,
 title="Automate Approval and Notification Scenarios",
 objective="Extend the flow into an approval-and-notification scenario that updates the request based on the decision.",
 desc="A notification is good; a decision is better. You extend the flow with Copilot so a high-priority request is "
 "sent to the manager for approval, and when they approve or reject, the flow updates the request's Status and "
 "notifies the requester of the outcome — a complete approval-and-notification loop. " + PROJECT_NOTE,
 build="An approval-and-notification flow: high-priority requests go to the manager for approval, the request Status is updated on the decision, and the requester is notified of the outcome.",
 services="Power Automate Approvals, conditions/branches, Dataverse update row, notifications",
 steps=[
 ("Open your 'Notify manager of high-priority request' flow and edit it. Ask Copilot to turn the notification into an approval.",
  "Instead of just emailing the manager, start an approval and wait for the manager to approve or reject this high-priority request."),
 ("Confirm Copilot added a 'Start and wait for an approval' action (Approve/Reject type) addressed to the manager, with the request's details in the approval message.", ""),
 ("Add the decision branch. Ask Copilot to handle both outcomes.",
  "After the approval, if it is approved set this request's Status to Approved; if it is rejected set the Status to Resolved with a note that it was rejected."),
 ("Confirm the flow now has a Condition on the approval outcome and an 'Update a row' action on Maintenance Requests in each branch that sets Status correctly.", ""),
 ("Add the requester notification. Ask Copilot to close the loop.",
  "After the status is updated, send an email to the person who created the request telling them whether it was approved or rejected."),
 ("Save the flow and test the approve path: create a High-priority request, open the approval (in Power Automate, Outlook or Teams), approve it, and confirm the request's Status becomes Approved and the requester is emailed.", ""),
 ("Test the reject path with a second request: reject it, and confirm the Status and the requester's email reflect the rejection.", ""),
 ("Check the app: open 'Harbourfront Maintenance' and confirm the browse gallery now shows the updated statuses from the flow — the automation and the app are working together.", ""),
 ],
 test="Approving a high-priority request sets its Status to Approved and emails the requester; rejecting one sets the Status accordingly and emails the requester; and the app's gallery reflects both outcomes.",
 ),
 dict(
 num=10, topic=3,
 title="Share and Govern Your AI-Assisted App",
 objective="Share the app and flow with the right people and apply sensible governance to your AI-assisted solution.",
 desc="An app only helps if the right people can use it — safely. You share the app with users and the flow's "
 "connections, review who can do what, and apply governance: the environment it lives in, data loss prevention "
 "awareness, and documenting what the solution does so it stays maintainable and accountable. " + PROJECT_NOTE,
 build="A shared 'Harbourfront Maintenance' app with the flow's connections in place, plus a short governance note covering sharing, environment, DLP and documentation.",
 services="App sharing, run-only vs co-owner, environments, DLP awareness, documentation",
 steps=[
 ("In the maker portal, open 'Apps', select 'Harbourfront Maintenance', and choose 'Share'.", ""),
 ("Share with a colleague or a group as run-only users (they can use the app but not edit it), and note the difference between run-only users and co-owners who can edit. Confirm the app's flow connections are included so the automation still works for shared users.", ""),
 ("Review governance — the environment: confirm which environment the app and flow live in, and understand that moving between Dev/Test/Prod environments is how organisations control release. Note your environment name.", ""),
 ("Review governance — data loss prevention (DLP): understand that admins use DLP policies to control which connectors (Dataverse, Outlook, Teams, etc.) can be combined; check your app only uses connectors your organisation allows.", ""),
 ("Ask Copilot to help you document the solution so it stays maintainable.",
  "Write a short description of this app and its flow for other makers: what it does, which Dataverse table it uses, what the approval flow does, and who it is shared with."),
 ("Save that description in the app's details (Apps > ... > Details > Description) and in your team notes, so the next person understands the solution.", ""),
 ("Confirm accountability: you — the owner — are responsible for what the app and flow do; Copilot only helped build them. Note who to contact if the flow needs changing.", ""),
 ("Final check: run the shared app once more end to end (submit a High-priority request, approve it, see the status update) to confirm the complete Harbourfront Facilities solution works.", ""),
 ],
 test="The app is shared with at least one user or group with the flow's connections included, you can state the environment and which connectors the app uses, and a plain-language description of the solution is saved with the app.",
 ),
]
