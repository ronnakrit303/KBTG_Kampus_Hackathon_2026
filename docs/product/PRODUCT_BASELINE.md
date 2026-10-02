# K-SafeFirst Product Baseline

Status: Approved implementation baseline

Date: 2026-10-02

Canonical product promise: [`proposal/Second_1PagePitch.pdf`](../../proposal/Second_1PagePitch.pdf)

## 1. Purpose

This document translates the submitted one-page proposal into a scope that a three-person team can implement and test as a Mobile-first Web/PWA. It does not replace the submitted proposal. If wording conflicts, preserve the submitted product intent and open a decision Issue before changing scope.

## 2. Problem

First Jobbers may be waiting for unfamiliar employers to contact them while they have limited savings and a strong desire to secure work. A Fake Recruiter can exploit that context by requesting an application, training, equipment, or deposit payment. The user may pass normal authentication and authorize the transfer personally, so authentication alone does not prove that the intent is safe.

K-SafeFirst addresses the decision point immediately before a potentially harmful transfer while also helping the user establish a reserve that is worth protecting.

## 3. Target users

- Primary: First Jobbers aged 22–30 who are searching for work, waiting for their first salary, or beginning early employment.
- Secondary prototype audience: judges and usability-test participants evaluating whether the warning and transaction-hold flow is understandable.
- The system does not need to infer employment status or read a resume, email, message, or call.

## 4. Value proposition

> Build a protected reserve automatically, then apply explainable friction when several signals suggest that social engineering is pressuring the user to send that reserve to a risky destination.

User value:

- makes a 3–6 month reserve goal visible and easier to build;
- separates an ordinary savings reminder from a serious Scam intervention;
- explains observable reasons before money leaves;
- provides a clear path to pause, verify, cancel, or report.

Product and security value to demonstrate—not claim as measured production impact:

- combines savings context with transaction-risk context;
- creates auditable evidence for policy and incident analysis;
- can reduce avoidable dispute and investigation workload if validated in production;
- can support engagement if reserve and benefit mechanics receive business approval.

## 5. Hero Scenario

```text
First Jobber receives a Fake Recruiter request
                    |
Starts a transfer from Protected Reserve
to a new personal recipient for a job-related fee
                    |
Backend correlates reserve source, new payee,
purpose/pattern, destination graph, and session signals
                    |
High-risk suspicious case is held before settlement
                    |
User sees 2–3 reasons and chooses
Verify / Cancel / Report
```

The prototype must also show legitimate and ambiguous cases so it does not equate every reserve withdrawal or new recipient with Scam.

## 6. End-to-end MVP journey

1. User opens K-SafeFirst and selects a synthetic persona/scenario.
2. User sets monthly essential expenses and a 3-month, 6-month, or custom reserve target.
3. User chooses a starting amount, including zero.
4. User configures Scheduled Auto-Allocation by source, amount, and date. The prototype simulates success or insufficient balance.
5. Dashboard shows current reserve, target coverage, Save Point/Benefit progress, and transaction history.
6. User initiates a synthetic transfer and reviews source, recipient, amount, and purpose.
7. Backend returns an explainable `Low`, `Medium`, or `High` result.
8. The policy maps the result to normal flow, contextual warning, transaction hold, or rejection.
9. User completes a valid action: continue, verify, cancel, or report.
10. Demo reset restores deterministic fixtures for the next participant.

## 7. Risk policy

| Level | Meaning | Prototype response |
|---|---|---|
| `Low` | No meaningful Scam signal; e.g. own account or verified biller with neutral destination risk | Continue normal simulated transfer; no Scam warning |
| `Medium` | Some uncertainty; e.g. new unverified recipient without a High-risk combination | Contextual warning with reasons and deliberate confirmation; user may continue |
| `High — suspicious` | Several independent Scam signals or graph risk combine, but destination is not confirmed | Stop the instruction before simulated settlement and enter a server-controlled hold; allow verify, cancel, or report |
| `High — confirmed` | Synthetic fixture represents a confirmed Scam/Fraud-risk destination | Reject the simulated transfer under prototype policy |

Rules:

- reserve source alone cannot create `High`;
- the purpose answer may add context but cannot lower risk created by stronger signals;
- repeated and split transfers are aggregated;
- explanations show at most three observable reasons and never reveal the complete rule formula;
- a Savings Nudge for non-essential spending is separate, dismissible, and never creates a hold.

## 8. Savings and benefit mechanics

The submitted concept contains reserve-building and engagement ideas. The MVP demonstrates them without claiming approved banking-product terms.

| Capability | MVP treatment | Truth level |
|---|---|---|
| Reserve goal and monthly coverage | Executable UI and synthetic state after M2 | Planned `Implemented` |
| Scheduled Auto-Allocation | Deterministic date/amount/source simulation; no payroll detection | Planned `Simulated` |
| Insufficient balance | Skip allocation, never go negative, show a neutral result | Planned `Implemented` against synthetic balance |
| Save Point / Minimum Retained Balance | Prototype rule and progress visualization | Planned `Simulated` |
| Benefit Tier | Prototype progress labels; no guaranteed monetary value | Planned `Simulated` |
| Interest tiers and K-Point examples | UI copy only when clearly marked subject to approval | `Future/Bank dependency` |

The MVP must not suggest that points or interest have been approved or that user deposits automatically create a measured profit for a bank.

## 9. Capability boundaries

### Planned to run in the repository

- Mobile PWA user journey and responsive screens.
- Deterministic synthetic scenarios and reset.
- Versioned rule evaluation and reason codes.
- Synthetic transaction graph and destination-risk flag.
- Backend transaction-hold state machine and idempotent commands.
- Audit-event timeline without sensitive data.
- Automated tests for normal, suspicious, confirmed, false-positive, emergency, and bypass scenarios.

### Simulated integrations

- balances, accounts, pockets, recipients, verified billers, transaction history;
- device/session posture and fraud-risk flags;
- transaction settlement and reporting;
- trusted-contact request/response if included after Core flow;
- benefit, Save Point, point, and interest displays.

### Future/Bank dependencies

- real account and payment integration;
- official Scam/Fraud lists and production graph analytics;
- identity verification, device attestation, and regulated authorization;
- holding, rejecting, releasing, or recovering real money;
- fraud operations, SIEM, case management, and customer support;
- rewards, points, interest, partner benefits, compliance, legal, and product approval.

## 10. Explicit non-goals

- building a full mobile-banking clone;
- reading email, messages, resumes, calls, contacts, or device files;
- detecting every Scam type;
- training an ML model without defensible labels and evaluation;
- claiming production precision, recall, cost saving, revenue, adoption, or fraud-loss reduction;
- using real customer or banking data;
- replacing identity verification, fraud operations, or payment infrastructure.

## 11. Success criteria

Product/UX:

- a participant can explain why a warning appeared;
- the Fake Recruiter scenario leads to pause/cancel behavior more often than a generic warning in a later real test;
- legitimate own-account and verified-biller scenarios complete without High-risk friction;
- mobile tasks are readable and operable at the target viewport.

Security/engineering:

- risk decisions are reproducible from versioned fixtures;
- all required boundary and bypass scenarios have automated oracles;
- the client cannot release a held transaction by changing its local clock or state;
- duplicate actions do not create duplicate transaction instructions;
- logs contain no real or unnecessary sensitive data.

Evidence:

- pilot occurs before formative sessions;
- session counts and observations are reported exactly as conducted;
- metrics are labelled prototype results and never generalized to production without evidence.

## 12. Failure conditions

The current concept must be reconsidered if:

- users cannot distinguish a savings reminder from a serious Scam warning;
- legitimate emergency access is routinely treated as High risk;
- the Hero Scenario depends on unavailable data that cannot be represented honestly;
- the browser controls the transaction hold or can bypass backend state;
- the prototype requires real banking data to demonstrate its core value;
- scope prevents the team from delivering one reliable end-to-end flow.
