# K-SafeFirst MVP Threat Model

Status: Canonical MVP security baseline

Date: 2026-10-02

Scope: Mobile-first PWA, synthetic risk API, graph fixtures, and transaction-hold simulation

## 1. Security objective

Reduce the chance that social engineering leads a user to authorize a harmful transfer from a protected reserve, while preserving legitimate access and preventing the prototype itself from misrepresenting or leaking sensitive data.

The system protects two different properties:

- **Request integrity:** the instruction, amount, recipient, and state were not altered, replayed, or duplicated.
- **Intent integrity:** available context suggests whether the authenticated user may be acting under deception or pressure.

Authentication can support request integrity, but it does not prove safe intent.

## 2. Scope and assumptions

- All persons, accounts, devices, sessions, histories, graphs, and balances are synthetic.
- The MVP does not transfer, hold, recover, or block real money.
- The browser is untrusted; the API owns risk, state, and time.
- Risk rules are deterministic and versioned. There is no trained AI/ML model in Core MVP.
- Destination risk is derived from synthetic graph fixtures, not an official list.
- Email, messages, calls, resumes, contacts, and device files are out of scope.

## 3. Assets

- integrity of the synthetic reserve and transaction state;
- correctness and explainability of risk decisions;
- inability to bypass a High-risk transaction hold from the client;
- scenario determinism and test evidence;
- privacy of test participants and repository contributors;
- integrity of audit events and policy versions;
- user trust created by accurate limitations and truth labels.

## 4. Actors

| Actor | Goal/capability |
|---|---|
| Legitimate user | Build reserve, test transfers, understand warnings, cancel or report |
| Scam operator / Fake Recruiter | Pressure the user, coach answers, split transfers, rotate recipients |
| Curious participant | Manipulate browser state, call APIs directly, replay actions |
| Malicious internet client | Abuse public endpoints, enumerate data, exhaust resources |
| Contributor error | Commit secrets, real data, unsafe claims, broken rules, or weak tests |
| Future production systems | Provide identity, account, payment, fraud, graph, reward, and incident services; unavailable to MVP |

## 5. Attack surfaces and trust boundaries

1. PWA inputs and browser storage.
2. REST API authentication/session fixture and schema parsing.
3. Risk-evaluation payload and reason-code response.
4. Synthetic graph files and scenario reset endpoints.
5. Transaction-state mutation endpoints.
6. Audit logs and CI artifacts.
7. Public deployment configuration and dependencies.

## 6. Threats and required controls

| ID | Threat | Required MVP control | Test evidence |
|---|---|---|---|
| T01 | User is coached to choose a harmless purpose | Purpose is weak/additive and cannot downgrade stronger evidence | Unit cases with identical strong signals and different purpose |
| T02 | Attacker asks for split/repeated transfers | Aggregate count and amount within a synthetic policy window | Bypass fixture produces High after aggregation |
| T03 | Attacker rotates a new recipient | New/unverified status combines with other evidence; never acts alone as proof | Medium and High boundary tests |
| T04 | Destination is connected to mule-like nodes | Graph adapter returns versioned evidence and path summary; policy uses it as one signal | Graph fixture tests and stable expected reason |
| T05 | Confirmed-risk synthetic destination | Policy rejects instruction; no release transition exists | State-machine negative tests |
| T06 | Client changes local clock to end a hold | API uses server time and returns current allowed actions | E2E/API test with manipulated client time |
| T07 | Client edits risk tier or destination flag | API derives authoritative evidence from scenario and server data | Tampered payload ignored or rejected |
| T08 | Repeated click/replay creates duplicate instruction | Idempotency key and unique command handling | Same key returns same transaction ID |
| T09 | Race between cancel and release | Atomic transition/compare-and-set semantics | Concurrency or deterministic state-transition test |
| T10 | Reserve source alone causes warning fatigue | Explicit policy invariant: reserve alone is not High | Low/Medium boundary tests |
| T11 | Legitimate emergency is trapped | Own account/verified biller neutral route remains Low; ambiguous new route is Medium unless stronger evidence exists | Emergency and false-positive scenarios |
| T12 | Savings Nudge is confused with Scam warning | Separate component, tone, actions, telemetry, and no hold | UI and E2E assertion |
| T13 | Rule details help attackers evade | Return limited observable reason codes, not weights/thresholds/full rule formula | Contract snapshot and review |
| T14 | Public API is spammed | Request limits, bounded payloads, reset throttling, timeouts | API negative tests; deployment check |
| T15 | Logs expose sensitive input | Allowlisted structured fields and synthetic IDs; no free-text message ingestion | Log-capture assertions |
| T16 | Contributor commits a secret or real data | `.gitignore`, PR checklist, secret scanning, synthetic-data review | CI and reviewer evidence |
| T17 | Dependency or build-chain compromise | Lockfiles, minimal dependencies, automated dependency review/scanning | CI evidence after scaffold |
| T18 | XSS or unsafe rendering of scenario labels | No raw HTML injection; output encoding; CSP in deployment | Frontend unit/E2E security tests |
| T19 | CSRF/CORS misuse on state-changing API | SameSite/session design, CSRF strategy if cookies are used, restricted CORS | API configuration and tests |
| T20 | Prototype is represented as production | Visible synthetic disclosure and truthful docs/UI | Content review and repository guardrail |

## 7. Risk-decision invariants

```text
Reserve only                                      != High
Purpose only                                      != High
New recipient only                                -> usually Medium
Confirmed synthetic Scam/Fraud destination        -> Reject
Several independent Scam signals                  -> Hold
Own account or verified biller + neutral risk      -> Low
Known recipient + ordinary reserve spending        -> Savings Nudge, no hold
```

The strongest applicable policy wins. A lower-risk user answer cannot override stronger server-side evidence.

## 8. Transaction-state authorization

Allowed high-level transitions:

- `EVALUATED -> HELD` only by backend policy.
- `HELD -> CANCELLED` by an authorized user command.
- `HELD -> REPORTED` by an authorized user command.
- `HELD -> VERIFIED` only after the prototype verification condition is recorded.
- `VERIFIED -> RELEASE_ELIGIBLE` only after backend time/policy checks.
- `RELEASE_ELIGIBLE -> COMPLETED_SIMULATED` only by backend simulation.
- any active state -> `REJECTED` when confirmed synthetic risk policy requires it.

Forbidden examples:

- client requests `HELD -> COMPLETED_SIMULATED` directly;
- changing local time releases a hold;
- reusing an idempotency key with different amount/recipient silently succeeds;
- a rejected instruction becomes releasable;
- cancelling one instruction changes another.

## 9. Privacy and data minimization

Collect/store only what the MVP needs:

- opaque synthetic persona, payee, scenario, and transaction IDs;
- normalized enums for purpose, destination class, graph risk, and session posture;
- synthetic amount and event time;
- policy version, reason codes, state transitions, and command outcome.

Do not collect/store:

- real account numbers, credentials, government identifiers, contacts, resumes;
- email/message/call contents or suspicious-link contents;
- biometric data;
- free-text participant disclosures in application logs;
- full IP or device fingerprint unless a later approved test justifies and governs it.

Usability notes must use participant codes and be stored separately from application telemetry.

## 10. Explainability and warning safety

- Show two or three reasons tied to observable facts.
- Do not accuse an unconfirmed recipient of being a criminal.
- Show the amount at risk and that the instruction has not been settled.
- Separate `Pause & Verify` from `Cancel & Report`.
- Never use a mascot in a serious Scam warning; reserve mascots/nudges for non-fraud savings reflection.
- Avoid repeated generic alerts; intervention strength follows evidence.
- Provide an accessible path that does not depend only on color, animation, or time pressure.

## 11. Incident and observability events

Minimum events:

```text
RISK_EVALUATED
WARNING_PRESENTED
DELIBERATE_CONFIRMATION_REQUESTED
TRANSACTION_HELD
VERIFICATION_SELECTED
TRANSACTION_CANCELLED
SCAM_REPORT_CREATED
TRANSACTION_REJECTED
RELEASE_ELIGIBLE
COMPLETED_SIMULATED
INVALID_TRANSITION_REJECTED
IDEMPOTENT_REPLAY_RETURNED
```

Each event records an opaque transaction ID, scenario ID, policy version, event type, server time, and minimal outcome. Do not log secrets or raw personal content.

## 12. Residual risks

- A user who continues trusting the scammer may still proceed after a hold if policy allows release.
- New mule accounts may have no useful graph history.
- Synthetic results cannot prove production precision, recall, fairness, or loss reduction.
- A public demo can be abused even without real data; rate and resource limits remain necessary.
- A policy that appears reasonable in fixtures may create warning fatigue or false positives in reality.
- Trusted-contact involvement can create privacy, coercion, accessibility, and availability problems; it remains simulated and optional until tested.

## 13. Security release gate

A milestone involving transactions cannot close unless:

- required threats have mapped tests;
- state and time are backend-authoritative;
- duplicate/replay and invalid-transition tests pass;
- logs contain synthetic minimum data;
- warning copy reflects evidence and uncertainty;
- limitations are documented;
- another team member reviews the security impact.
