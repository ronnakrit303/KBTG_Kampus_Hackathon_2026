# K-SafeFirst Test Strategy

Status: Canonical quality strategy

Date: 2026-10-02

## 1. Objective

Provide credible evidence that the Mobile-first PWA demonstrates its claims reliably, distinguishes legitimate from risky flows, resists obvious client-side bypasses, and reports user-research results honestly.

The MVP can validate deterministic behavior and usability hypotheses. It cannot establish production fraud-detection accuracy without representative labelled data.

## 2. Quality dimensions

| Dimension | Main question |
|---|---|
| Product correctness | Does each scenario follow the approved flow and wording? |
| Security correctness | Can the client bypass risk/state/time or duplicate a command? |
| Risk-policy correctness | Do rules satisfy invariants and boundary cases? |
| Reliability | Are reset and repeat runs deterministic? |
| Mobile UX | Can a participant complete tasks in a mobile viewport? |
| Accessibility | Are content, focus, labels, contrast, and non-color cues usable? |
| Performance | Is interaction fast enough for a live demo under synthetic load? |
| Evidence integrity | Are results, sessions, and limitations reported without invention? |

## 3. Test layers

### 3.1 Static and repository checks

- required canonical files exist;
- no merge-conflict markers;
- local Markdown links resolve for canonical documents;
- no committed `.env`, private key, or obvious credential fixture;
- TypeScript type-check and lint after frontend scaffold;
- Python format/lint/type checks after backend scaffold;
- dependency and secret scanning in CI.

### 3.2 Unit tests

Frontend:

- reason-code to Thai copy mapping;
- formatting of amount, coverage, countdown, and state;
- warning component behavior and accessible labels;
- Savings Nudge never uses Scam-warning action/state.

Backend:

- each risk rule and precedence;
- purpose cannot downgrade stronger signals;
- split/repeated aggregation;
- graph feature extraction;
- reserve allocation success/skip rules;
- every allowed and forbidden state transition;
- idempotency behavior and key/payload mismatch;
- allowlisted audit-event fields.

### 3.3 API integration tests

- OpenAPI request/response validation;
- scenario reset restores known state;
- create transaction returns expected tier/action/reasons;
- held state survives refresh and reports server time;
- invalid enum, amount, size, transition, or missing key is rejected;
- synthetic confirmed destination cannot be released;
- concurrent/repeated commands resolve to one authoritative outcome.

### 3.4 End-to-end tests

Use Playwright mobile viewport for:

1. reserve goal and starting amount;
2. Auto-Allocation success;
3. Auto-Allocation skipped for insufficient balance;
4. Low-risk own-account or verified-biller transfer;
5. Medium-risk new recipient with deliberate confirmation;
6. High-risk Fake Recruiter hold and `Pause & Verify`;
7. High-risk cancellation and reporting;
8. confirmed-risk rejection;
9. Savings Nudge that can be skipped without a hold;
10. refresh/reopen during a hold;
11. repeated tap does not create another instruction;
12. demo reset returns to fixture baseline.

### 3.5 Security tests

- edit local countdown/clock and attempt early release;
- send a client-selected Low tier for a High fixture;
- tamper amount/recipient after evaluation;
- reuse idempotency key with same and changed payload;
- attempt direct forbidden state transitions;
- inject markup/script into allowed text fields;
- exceed request limits and payload bounds;
- inspect logs for prohibited raw or real data;
- verify error messages do not expose rule thresholds or stack traces.

### 3.6 Usability and formative evaluation

Required sequence:

1. Complete clickable flow.
2. Conduct one real pilot participant.
3. Correct runbook, wording, and blocking defects.
4. Conduct 5–8 real formative sessions.

Until sessions occur, state exactly: `0 sessions conducted`.

Use synthetic Scam and legitimate scenarios. Compare contextual warning with a generic warning when the test design supports it. Record:

- comprehension of warning reasons;
- choice to pause/cancel/continue;
- legitimate-task completion;
- time on task;
- confusion and warning-dismissal behavior;
- qualitative trust and perceived control.

Do not invent participant quotes, rates, or outcomes. Store participant codes separately from any contact details.

## 4. Canonical scenario matrix

| ID | Scenario | Expected policy/action |
|---|---|---|
| S01 | Own account, neutral destination | Low; normal simulated completion |
| S02 | Verified biller for essential expense | Low; no Scam warning |
| S03 | New unverified recipient, neutral evidence | Medium; reasons + deliberate confirmation |
| S04 | Fake Recruiter, reserve, new personal recipient, job fee, elevated graph risk | High suspicious; held before settlement |
| S05 | Same as S04 but purpose changed to `other` | Remains High |
| S06 | Split repeated payments to risky new recipient | High after aggregation |
| S07 | Confirmed synthetic Scam/Fraud-risk destination | Rejected; no release |
| S08 | Known recipient, general spending from reserve | Savings Nudge; no hold |
| S09 | Emergency payment to verified biller | Low; normal access |
| S10 | Emergency payment to new unverified recipient without stronger evidence | Medium, not automatically High |
| S11 | Duplicate click/request | One transaction ID; idempotent response |
| S12 | Client clock advanced during hold | Still held according to server time |

## 5. Test oracle principles

- Assert tier, action, state, allowed actions, policy version, and reason codes.
- Avoid asserting an implementation-specific numeric score unless a reviewed decision introduces one.
- Freeze fixture and server time where deterministic behavior is required.
- Keep policy oracles independent from the production rule implementation where practical.
- A test must fail if reserve source alone causes High.
- A test must fail if a lower-risk purpose changes stronger evidence to Low/Medium.

## 6. Coverage expectations

Coverage percentage is a diagnostic, not the goal. Required behavior matters more.

- Risk rules and state machine: every branch and forbidden transition covered.
- API: success, validation failure, conflict, idempotent replay, and internal failure behavior.
- PWA Hero Scenario: full E2E coverage on at least one supported mobile viewport.
- UI components: critical warnings, actions, and accessibility states covered.

Do not claim detection `precision` or `recall` from hand-authored fixtures. On synthetic fixtures, report scenario pass rate or policy-test coverage. Production precision/recall requires representative labelled outcomes and governance.

## 7. Performance targets for MVP

These are engineering budgets to test, not measured claims until results exist:

- local/small deployed risk evaluation: target p95 under 500 ms;
- normal mobile interaction response: target under 1 second excluding network outage;
- initial usable mobile screen: target under 3 seconds on the agreed demo network/device;
- scenario reset: target under 2 seconds;
- no unbounded graph traversal or payload processing.

Record environment, data size, method, and actual result before quoting performance.

## 8. CI gates by phase

M0:

- repository validator.

M1–M2:

- frontend install, lint, type-check, unit tests, build;
- backend import/compile, lint, unit tests;
- canonical fixture validation.

M3–M5:

- API integration, graph/rule/state tests;
- Playwright Hero Scenario;
- dependency and secret scan;
- build artifact and accessibility smoke checks.

M6:

- deployed smoke test;
- demo reset verification;
- link/QR check on physical mobile device;
- pilot/test records checked for truthful counts.

## 9. PR test evidence

Every PR records:

- exact commands run;
- pass/fail result;
- test environment when relevant;
- screenshots/recording for UI;
- skipped checks and why;
- new or changed test cases;
- residual risk and follow-up Issue.

“Should pass” is not test evidence.

## 10. Release gate

The MVP is demo-ready only when:

- S01–S12 have executable evidence appropriate to their layer;
- the deployed link works on a physical mobile browser;
- held/rejected flows cannot be bypassed through the client;
- reset is deterministic;
- no real data or secret is present;
- serious Scam warning and ordinary Savings Nudge are visually and semantically distinct;
- one real pilot has occurred before 5–8 formative sessions;
- known limitations and simulated integrations are visible to the team and judges.
