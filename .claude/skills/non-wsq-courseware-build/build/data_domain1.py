"""
Domain 1 — Get Started with Copilot in Power Apps. Labs 1-3.

THE CONNECTED PROJECT STARTS HERE, IN LAB 1.

Every lab works the SAME deliverable: a Maintenance Request solution for a
facilities-management company, "Harbourfront Facilities". In Lab 1 you enable
Copilot and get oriented in Power Apps Studio; Lab 2 prepares the Dataverse
table Copilot will build on; Lab 3 turns a good app-building prompt into a
repeatable pattern. Domain 2 then generates and refines the app, and Domain 3
automates and governs it. Wherever possible use your OWN non-confidential app
idea; the Harbourfront Facilities scenario is provided for everyone to follow.
"""

SCENARIO = (
 "Harbourfront Facilities manages several commercial buildings. Staff currently report faults — a "
 "flickering light, a blocked drain, a warm server room — by email and phone, so requests get lost and "
 "no one can see what is outstanding. Your manager wants a simple app where staff log a maintenance "
 "request, a coordinator tracks it, and high-priority requests are automatically sent for approval and "
 "the requester is notified. Across this course you use Copilot in Power Apps to build that solution end "
 "to end. Use this scenario only if you cannot use a real, non-confidential app idea of your own; your "
 "own idea is always preferred."
)

PROJECT_NOTE = (
 "BUILDING BLOCK — what you do in this lab becomes part of your Harbourfront Facilities Maintenance "
 "Request solution, the single deliverable you build, refine, automate and govern across all 10 labs."
)

DOMAIN1 = [
 dict(
 num=1, topic=1,
 title="Enable Copilot and Get Oriented in Power Apps Studio",
 objective="Sign in to Power Apps, confirm Copilot is enabled, and find your way around Power Apps Studio and the Copilot pane.",
 desc="This lab gets Copilot working for you. You sign in at make.powerapps.com, check you are in the right "
 "environment, confirm Copilot is switched on, and create a throwaway app so you can see the Copilot pane, "
 "the canvas, the tree view and the property pane — the surfaces you use all day. " + PROJECT_NOTE,
 build="A confirmed, Copilot-enabled Power Apps environment and a short tour note of where the Copilot pane, tree view, canvas and property pane are.",
 services="make.powerapps.com, Power Apps Studio, Copilot pane, a Microsoft work or school account",
 steps=[
 ("Open a browser and sign in at make.powerapps.com with your Microsoft work or school account (not a personal Microsoft account). This is the Power Apps maker portal where you build all day.", ""),
 ("Check your environment: at the top-right, open the environment picker and select the environment your trainer names. Copilot and Dataverse must be enabled there — if the picker is empty or Copilot is missing, tell the trainer.", ""),
 ("Confirm Copilot is available: from the home page choose 'Start with Copilot' (or '+ Create' > 'Start with a page design'). If a prompt box invites you to 'Describe the app you'd like to build', Copilot is enabled.", ""),
 ("Create a throwaway canvas app to explore Studio: choose '+ Create' > 'Blank app' > 'Blank canvas app', name it 'Studio Tour', pick Tablet format, and click Create. This opens Power Apps Studio.", ""),
 ("Find the four surfaces you will use all day, and note where each is: the Tree view (left) listing screens and controls; the Canvas (centre) where the app is designed; the Property pane (right) for the selected control; and the Copilot pane (open it from the Copilot icon on the top toolbar).", ""),
 ("Ask Copilot what it can do, so you see the pane respond, then read its answer.",
  "What can you help me build and change in this Power Apps canvas app?"),
 ("Confirm the ground rule: Copilot drafts screens, formulas and flows inside Studio, but nothing is shared or published until you choose to. Close the 'Studio Tour' app without saving — it was only for the tour.", ""),
 ],
 test="You are signed in to make.powerapps.com in the correct environment, the Copilot pane opens and responds to a question, and you can point to the tree view, canvas, property pane and Copilot pane in Studio.",
 ),
 dict(
 num=2, topic=1,
 title="Prepare Your Data with Dataverse for Copilot",
 objective="Create a well-described Dataverse table so Copilot has the context it needs to build an accurate app.",
 desc="Copilot builds better apps on well-described data. You create the Maintenance Requests table in Dataverse, "
 "add clearly named columns with descriptions and choice options, and add a couple of sample rows — so that when "
 "Copilot builds the app in Domain 2 it understands each field. " + PROJECT_NOTE,
 build="A Dataverse table named 'Maintenance Requests' with clearly named, described columns, choice options for Category, Priority and Status, and two sample records.",
 services="Dataverse, Tables, columns, choice columns",
 steps=[
 ("In the maker portal left menu, open 'Tables' (under Dataverse), then choose '+ New table' > 'New table'. Name it 'Maintenance Request' (Power Apps sets the plural 'Maintenance Requests' automatically).", ""),
 ("Keep the default primary column but rename its display name to 'Title' with the description 'Short summary of the fault' — clear names and descriptions are exactly what Copilot reads to understand your data.", ""),
 ("Add a single-line text column 'Location' (description: 'Building, floor and room, e.g. Tower A, L3, Server Room').", ""),
 ("Add a Choice column 'Category' with the choices: Electrical, Plumbing, HVAC, General (description: 'Type of maintenance issue').", ""),
 ("Add a Choice column 'Priority' with the choices: Low, Medium, High (description: 'How urgent the request is').", ""),
 ("Add a multiline text column 'Description' (description: 'What is wrong, in the requester's own words').", ""),
 ("Add a Choice column 'Status' with the choices: New, Approved, In Progress, Resolved (description: 'Where the request is in its lifecycle'), and set its default to New.", ""),
 ("Add a single-line text column 'Assigned To' (description: 'Technician handling the request') and a multiline text column 'Resolution Notes' (description: 'What was done to fix it'). Save the table.", ""),
 ("Add two sample rows via 'Edit' (data): e.g. Title 'Flickering light in Tower A lobby', Location 'Tower A, L1, Lobby', Category Electrical, Priority Medium, Status New; and Title 'Server room too warm', Location 'Tower B, L4, Server Room', Category HVAC, Priority High, Status New.", ""),
 ],
 test="The 'Maintenance Requests' table exists in Dataverse with named, described columns, Category/Priority/Status have the right choices, and two sample requests are saved.",
 ),
 dict(
 num=3, topic=1,
 title="Write Effective Prompts for App Building",
 objective="Compare a vague app prompt with a specific one and capture a reusable four-part prompt pattern for building apps.",
 desc="A generated app is only as good as the prompt behind it. You draft a vague prompt, then a specific one that "
 "names the app's purpose, the data, the screens and the audience, and distil what worked into a reusable pattern "
 "you will use for the rest of the course. You do this in the Copilot prompt box without building the full app yet. " + PROJECT_NOTE,
 build="A written four-part app-prompt pattern (Purpose · Data · Screens · Audience) and one strong, tested app-building prompt saved for reuse.",
 services="Copilot prompt box, prompt design, Purpose/Data/Screens/Audience pattern",
 steps=[
 ("From the Power Apps home page, open the 'Start with Copilot' prompt box (you will preview prompts here; you build the real app in Lab 4).", ""),
 ("Type a deliberately vague prompt and read how generic Copilot's proposed app is.",
  "Build me an app for maintenance."),
 ("Now type a specific prompt for the same intent and compare what Copilot proposes.",
  "Build a canvas app for building staff to log maintenance requests using my Maintenance Requests table in Dataverse. It needs a screen to browse open requests, a screen to view one request in detail, and a form to submit a new request. The audience is non-technical facilities staff, so keep it simple and clearly labelled."),
 ("Write down the four parts that made the second prompt work: the Purpose (what the app is for), the Data (which table), the Screens (what pages you want) and the Audience (who uses it).", ""),
 ("Capture your reusable pattern where you can find it — a notes doc, or pinned in your team's notes.",
  "PURPOSE: what the app is for | DATA: which Dataverse table | SCREENS: the pages you want | AUDIENCE: who uses it and how simple it must be"),
 ("Add the conditions that keep results trustworthy: always name the exact table, list the screens explicitly, and state the audience so Copilot pitches the design correctly.", ""),
 ("Rewrite one app idea of your own using the pattern (or refine the maintenance prompt), and read Copilot's proposal — do not build it yet.", ""),
 ("Save your best app-building prompt — you will reuse this pattern and this exact prompt in Lab 4 to generate the app.", ""),
 ],
 test="You can show two proposals for the same intent (vague vs specific), a written four-part prompt pattern, and one saved app-building prompt ready to use in Lab 4.",
 ),
]
