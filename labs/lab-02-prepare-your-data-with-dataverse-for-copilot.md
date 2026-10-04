# Lab 2 — Prepare Your Data with Dataverse for Copilot

**Topic 01:** Get Started with Copilot in Power Apps  |  **Day 1**  |  **Approx. 25 min**  |  **Course:** Microsoft Copilot for Power Apps (C803)

## Scenario

Harbourfront Facilities manages several commercial buildings. Staff currently report faults — a flickering light, a blocked drain, a warm server room — by email and phone, so requests get lost and no one can see what is outstanding. Your manager wants a simple app where staff log a maintenance request, a coordinator tracks it, and high-priority requests are automatically sent for approval and the requester is notified. Across this course you use Copilot in Power Apps to build that solution end to end. Use this scenario only if you cannot use a real, non-confidential app idea of your own; your own idea is always preferred.

## Goal

Create a well-described Dataverse table so Copilot has the context it needs to build an accurate app.

## What you'll build

A Dataverse table named 'Maintenance Requests' with clearly named, described columns, choice options for Category, Priority and Status, and two sample records.

**Tools and techniques:** Dataverse, Tables, columns, choice columns

## Prerequisites

- Lab 1 complete — you are signed in to the correct, Copilot-enabled environment.

## Steps

### Step 1

In the maker portal left menu, open 'Tables' (under Dataverse), then choose '+ New table' > 'New table'. Name it 'Maintenance Request' (Power Apps sets the plural 'Maintenance Requests' automatically).

### Step 2

Keep the default primary column but rename its display name to 'Title' with the description 'Short summary of the fault' — clear names and descriptions are exactly what Copilot reads to understand your data.

### Step 3

Add a single-line text column 'Location' (description: 'Building, floor and room, e.g. Tower A, L3, Server Room').

### Step 4

Add a Choice column 'Category' with the choices: Electrical, Plumbing, HVAC, General (description: 'Type of maintenance issue').

### Step 5

Add a Choice column 'Priority' with the choices: Low, Medium, High (description: 'How urgent the request is').

### Step 6

Add a multiline text column 'Description' (description: 'What is wrong, in the requester's own words').

### Step 7

Add a Choice column 'Status' with the choices: New, Approved, In Progress, Resolved (description: 'Where the request is in its lifecycle'), and set its default to New.

### Step 8

Add a single-line text column 'Assigned To' (description: 'Technician handling the request') and a multiline text column 'Resolution Notes' (description: 'What was done to fix it'). Save the table.

### Step 9

Add two sample rows via 'Edit' (data): e.g. Title 'Flickering light in Tower A lobby', Location 'Tower A, L1, Lobby', Category Electrical, Priority Medium, Status New; and Title 'Server room too warm', Location 'Tower B, L4, Server Room', Category HVAC, Priority High, Status New.

## Test it

The 'Maintenance Requests' table exists in Dataverse with named, described columns, Category/Priority/Status have the right choices, and two sample requests are saved.

## Troubleshooting

- **'New table' is greyed out.** Dataverse may not be provisioned in your environment; tell the trainer.
- **A choice column won't save its options.** Add each option on its own line and save the column before adding the next.
- **You can't find the table later.** Check you are still in the same environment (top-right picker) — tables are per-environment.

## Challenge

Add a description to every column explaining what a facilities coordinator would put there — the richer the descriptions, the better Copilot builds in Lab 4.

## Reflection

LO2 — Prepare a Dataverse table with clear names and descriptions so Copilot can build accurate apps. In your own words, how will you use this in your own work, and how will you check Copilot got it right?

## Deliverable

Save your work — it becomes part of your **Harbourfront Facilities** Maintenance Request solution, the single deliverable you complete and govern in Lab 10.

---

*Microsoft Copilot for Power Apps (C803) · C803 · Version v1.1 · © 2026 Tertiary Infotech Academy Pte Ltd*
