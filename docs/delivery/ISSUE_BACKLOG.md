# K-SafeFirst Issue-ready Backlog

Status: Ready to convert into GitHub Issues after approval to make remote changes

Date: 2026-10-02

## How to use this backlog

- IDs such as `FND-01` are planning IDs, not GitHub Issue numbers.
- Create Issues in milestone order, then replace planning IDs in dependencies with real `#numbers`.
- Each Issue should normally produce one branch and one PR.
- Do not assign fixed roles. A member claims any `Ready` Issue, subject to one substantial WIP item per person.
- `Must` items form the Core demo. `Should` improves credibility. `Stretch` cannot block Core.

## M0 — Repository Foundation

### FND-01 — Establish team repository governance

- Priority: `Must`
- Type/area: `docs`, `chore`; repository
- Dependencies: none
- Suggested branch: `chore/repository-foundation` (bootstrap exception)
- Scope: README, AGENTS, CONTRIBUTING, templates, canonical docs, roadmap, backlog, and repository guardrail.
- Acceptance Criteria:
  - source-of-truth order points to the submitted Proposal first;
  - team of three uses pull-based Issue ownership without permanent roles;
  - branch/commit/PR/review/Squash rules are consistent across files;
  - truth labels and synthetic-data boundaries are defined;
  - `python scripts/validate_repository.py` passes.

### FND-02 — Scaffold the PWA/API monorepo

- Priority: `Must`
- Type/area: `chore`; PWA/API
- Dependencies: `FND-01`
- Suggested branch: `chore/<issue-number>-application-scaffold`
- Scope: create minimal React/TypeScript/Vite PWA, FastAPI service, local commands, lockfiles, health endpoint, and starter tests.
- Acceptance Criteria:
  - clean checkout can install and start frontend/backend using documented commands;
  - mobile PWA shell and API health response render;
  - no product logic or mock production claim is added;
  - frontend/backend starter tests and builds pass;
  - README contains exact Quick Start commands.

### FND-03 — Add application CI quality gates

- Priority: `Must`
- Type/area: `ci`, `test`; CI
- Dependencies: `FND-02`
- Suggested branch: `chore/<issue-number>-application-ci`
- Scope: add lint, type-check, unit-test, build, Python test, secret, and dependency checks appropriate to the scaffold.
- Acceptance Criteria:
  - PR workflow runs reproducibly on a clean runner;
  - required checks fail on a seeded lint/test failure;
  - lockfiles are used;
  - results are named clearly for branch protection;
  - no secret or paid service is required.

## M1 — Mobile PWA Shell & Hero Journey

### PWA-01 — Build accessible mobile application shell

- Priority: `Must`
- Type/area: `feature`; PWA/UX
- Dependencies: `FND-02`
- Suggested branch: `feature/<issue-number>-mobile-shell`
- Acceptance Criteria:
  - agreed mobile viewport has readable layout and persistent navigation;
  - semantic headings, focus order, touch targets, and non-color status cues are present;
  - desktop view centers/constrains the mobile experience without breaking it;
  - component and accessibility smoke tests pass;
  - screenshots are attached to PR.

### PWA-02 — Define and load deterministic synthetic scenarios

- Priority: `Must`
- Type/area: `feature`, `test`; API/fixtures
- Dependencies: `FND-02`
- Suggested branch: `feature/<issue-number>-synthetic-scenarios`
- Acceptance Criteria:
  - scenarios include at least normal, ambiguous, Fake Recruiter, and confirmed-risk fixtures;
  - identifiers, balances, graph version, and history reset deterministically;
  - API never returns real-looking full account numbers or real personal data;
  - schema validation and reset integration tests pass;
  - UI visibly labels the demo as synthetic.

### PWA-03 — Implement transfer-review happy path

- Priority: `Must`
- Type/area: `feature`; PWA/API
- Dependencies: `PWA-01`, `PWA-02`
- Suggested branch: `feature/<issue-number>-transfer-happy-path`
- Acceptance Criteria:
  - user selects source, synthetic recipient, amount, and purpose;
  - review screen shows exactly what will be submitted;
  - normal fixture completes as `COMPLETED_SIMULATED`;
  - duplicate submission is prevented at UI and API boundary;
  - Playwright mobile happy-path test passes.

## M2 — Protected Reserve & Auto-Allocation

### RES-01 — Implement reserve-goal setup

- Priority: `Must`
- Type/area: `feature`; reserve/PWA/API
- Dependencies: `PWA-01`, `PWA-02`
- Suggested branch: `feature/<issue-number>-reserve-goal`
- Acceptance Criteria:
  - monthly essential expense accepts valid positive synthetic values;
  - user selects 3 months, 6 months, or a bounded custom target;
  - target calculation and starting amount including zero are correct;
  - invalid/overflowing values return accessible errors;
  - unit/API/UI tests cover boundaries.

### RES-02 — Simulate Scheduled Auto-Allocation

- Priority: `Must`
- Type/area: `feature`; reserve/API
- Dependencies: `RES-01`
- Suggested branch: `feature/<issue-number>-scheduled-allocation`
- Acceptance Criteria:
  - user explicitly chooses source, positive amount, and monthly date;
  - due simulation moves synthetic balance only when sufficient;
  - insufficient balance skips without negative balance or repeated hidden retry;
  - rule can be edited, paused, and disabled;
  - UI and audit events label behavior as simulation, not payroll detection.

### RES-03 — Show reserve dashboard, Save Point, and benefit progress

- Priority: `Should`
- Type/area: `feature`; reserve/UX
- Dependencies: `RES-01`, `RES-02`
- Suggested branch: `feature/<issue-number>-reserve-dashboard`
- Acceptance Criteria:
  - dashboard shows balance, target, coverage months, next allocation, and history;
  - prototype Save Point and Benefit Tier are explained without guaranteed points/interest;
  - withdrawal below a Save Point shows impact before confirmation;
  - logic has deterministic tests;
  - copy distinguishes prototype rule from approved product term.

### RES-04 — Implement dismissible Savings Nudge

- Priority: `Should`
- Type/area: `feature`; reserve/UX
- Dependencies: `PWA-03`, `RES-01`
- Suggested branch: `feature/<issue-number>-savings-nudge`
- Acceptance Criteria:
  - appears only for configured ordinary reserve spending fixture;
  - uses supportive language and offers `ใช้เงินสำรอง` / `เก็บไว้ก่อน` or approved equivalents;
  - can be skipped immediately;
  - creates no Scam event and no transaction hold;
  - visual, semantic, and telemetry tests distinguish it from Scam warnings.

## M3 — Multi-signal Risk & Graph Simulation

### RSK-01 — Define normalized risk-event contract

- Priority: `Must`
- Type/area: `feature`, `docs`; risk/API
- Dependencies: `PWA-02`, `PWA-03`
- Suggested branch: `feature/<issue-number>-risk-contract`
- Acceptance Criteria:
  - contract covers reserve context, recipient/history, amount/velocity, purpose, graph flag, and session posture;
  - values are bounded enums/numbers without arbitrary message contents;
  - OpenAPI examples use synthetic data;
  - client cannot submit an authoritative tier or state;
  - contract tests and architecture docs agree.

### RSK-02 — Implement versioned multi-signal policy

- Priority: `Must`
- Type/area: `security`, `feature`; risk/API
- Dependencies: `RSK-01`
- Suggested branch: `security/<issue-number>-risk-policy`
- Acceptance Criteria:
  - result includes tier, action, policy version, and limited reason codes;
  - reserve or purpose alone cannot produce High;
  - user purpose cannot downgrade stronger evidence;
  - S01–S10 policy oracles pass where graph output can be stubbed;
  - no numeric production score, AI, precision, or recall claim is introduced.

### RSK-03 — Implement synthetic graph destination risk

- Priority: `Must`
- Type/area: `security`, `feature`; graph/risk
- Dependencies: `RSK-01`
- Suggested branch: `security/<issue-number>-synthetic-graph-risk`
- Acceptance Criteria:
  - versioned graph fixtures represent neutral, elevated, mule-like, and confirmed-risk destinations;
  - extraction uses bounded traversal and deterministic features;
  - API returns evidence category/path summary without exposing full detection formula;
  - graph tests cover isolated/new nodes and suspicious connectivity;
  - UI/docs state clearly that data is simulated.

### RSK-04 — Aggregate repeated and split transfers

- Priority: `Must`
- Type/area: `security`; risk/API
- Dependencies: `RSK-02`
- Suggested branch: `security/<issue-number>-transfer-aggregation`
- Acceptance Criteria:
  - aggregation window and fixture clock are versioned;
  - repeated/split synthetic transfers produce cumulative count/amount evidence;
  - changed purpose does not erase history;
  - S05/S06 bypass tests pass;
  - aggregation remains scoped per synthetic persona/destination as designed.

### RSK-05 — Map reason codes to explainable Thai copy

- Priority: `Must`
- Type/area: `feature`, `docs`; PWA/UX
- Dependencies: `RSK-02`, `RSK-03`
- Suggested branch: `feature/<issue-number>-risk-explanations`
- Acceptance Criteria:
  - warnings show at most three observable reasons and the amount at risk;
  - unconfirmed recipient is not called a criminal/scammer as a fact;
  - thresholds and full rule formula are not exposed;
  - copy covers Low/Medium/High suspicious/High confirmed;
  - snapshots/component tests and UX review pass.

## M4 — Risk-based Intervention

### INT-01 — Implement authoritative transaction state machine

- Priority: `Must`
- Type/area: `security`, `feature`; API
- Dependencies: `RSK-02`, `RSK-03`
- Suggested branch: `security/<issue-number>-transaction-state-machine`
- Acceptance Criteria:
  - allowed states/transitions match architecture and threat model;
  - suspicious High enters `HELD` before simulated completion;
  - confirmed High enters `REJECTED` with no release path;
  - invalid transitions return stable conflict errors and audit events;
  - exhaustive transition tests pass.

### INT-02 — Enforce idempotency and server-controlled hold time

- Priority: `Must`
- Type/area: `security`; API
- Dependencies: `INT-01`
- Suggested branch: `security/<issue-number>-hold-and-idempotency`
- Acceptance Criteria:
  - same key/same payload returns the same instruction;
  - same key/different payload is rejected;
  - client clock/state cannot end a hold;
  - refresh returns server time, state, and allowed actions;
  - S11/S12 and race/negative tests pass.

### INT-03 — Build contextual warning and hold screens

- Priority: `Must`
- Type/area: `feature`; PWA/UX
- Dependencies: `RSK-05`, `INT-01`
- Suggested branch: `feature/<issue-number>-intervention-screens`
- Acceptance Criteria:
  - Medium allows deliberate confirmation without High hold;
  - High suspicious shows held-before-settlement status, server countdown, amount, and reasons;
  - High confirmed shows rejection without a misleading continue action;
  - actions use clear Thai and do not rely on color alone;
  - mobile screenshots, accessibility checks, and E2E tests pass.

### INT-04 — Implement verify, cancel, and report commands

- Priority: `Must`
- Type/area: `feature`, `security`; PWA/API
- Dependencies: `INT-01`, `INT-02`, `INT-03`
- Suggested branch: `feature/<issue-number>-verify-cancel-report`
- Acceptance Criteria:
  - only state-allowed commands are shown and accepted;
  - cancel/report cannot affect another instruction;
  - verification records the selected independent path without pretending to contact a real employer;
  - audit timeline is updated with minimum synthetic data;
  - E2E covers cancel, report, refresh, and eligible simulated continuation.

### INT-05 — Add trusted-contact interaction mock

- Priority: `Stretch`
- Type/area: `feature`, `research`; UX/API
- Dependencies: `INT-04`, Core demo stable
- Suggested branch: `feature/<issue-number>-trusted-contact-mock`
- Acceptance Criteria:
  - feature is optional and visibly simulated;
  - consent, timeout, unavailable contact, coercion, and privacy limitations are documented;
  - contact cannot see unnecessary transaction details;
  - absence/rejection does not trap legitimate emergency access;
  - Core demo does not depend on this Issue.

## M5 — Security, Quality & Observability

### SEC-01 — Harden public API boundaries

- Priority: `Must`
- Type/area: `security`; API
- Dependencies: `INT-02`
- Suggested branch: `security/<issue-number>-api-hardening`
- Acceptance Criteria:
  - request size/value limits and safe error handling exist;
  - CORS and cookie/CSRF approach are documented and tested for chosen deployment;
  - reset and mutation endpoints have abuse controls appropriate to demo;
  - no stack trace, secret, or rule threshold is returned;
  - negative/security tests pass.

### OBS-01 — Implement privacy-safe audit events

- Priority: `Must`
- Type/area: `security`, `feature`; observability
- Dependencies: `INT-04`
- Suggested branch: `security/<issue-number>-audit-events`
- Acceptance Criteria:
  - canonical security events are emitted for risk/warning/hold/cancel/report/reject/release/invalid transition;
  - only allowlisted synthetic fields are recorded;
  - transaction timeline is queryable for demo explanation;
  - log tests reject prohibited/raw fields;
  - retention/production limitations are documented.

### TST-01 — Automate canonical scenario matrix

- Priority: `Must`
- Type/area: `test`; full stack
- Dependencies: `INT-04`, `OBS-01`
- Suggested branch: `test/<issue-number>-canonical-scenarios`
- Acceptance Criteria:
  - S01–S12 have executable tests at the correct layer;
  - Fake Recruiter, false purpose, split transfer, emergency, duplicate, and local-clock cases pass;
  - Playwright covers full Hero Scenario in mobile viewport;
  - failures identify scenario and expected oracle;
  - tests run in CI without real services/data.

### QLT-01 — Add accessibility and performance gates

- Priority: `Should`
- Type/area: `test`; PWA/performance
- Dependencies: `INT-03`, `TST-01`
- Suggested branch: `test/<issue-number>-accessibility-performance`
- Acceptance Criteria:
  - automated accessibility smoke checks and manual keyboard/screen-reader checklist exist;
  - warning focus and action order are verified;
  - agreed performance budgets are measured with environment documented;
  - graph/risk inputs are bounded against accidental unbounded work;
  - results are reported as measured prototype evidence, not production claims.

## M6 — Deploy, Usability Test & Demo Readiness

### DEP-01 — Deploy one-link HTTPS demo

- Priority: `Must`
- Type/area: `chore`, `security`; deployment
- Dependencies: `TST-01`, `SEC-01`
- Suggested branch: `chore/<issue-number>-deploy-demo`
- Acceptance Criteria:
  - one HTTPS link loads on an agreed physical mobile device;
  - frontend/API configuration contains no committed secret;
  - health and deployed smoke tests pass;
  - demo reset cannot corrupt other active sessions under the chosen model;
  - provider, limitations, and recovery steps are documented.

### UXR-01 — Conduct one real pilot

- Priority: `Must`
- Type/area: `research`; UX
- Dependencies: `DEP-01`
- Suggested branch: `docs/<issue-number>-pilot-results`
- Acceptance Criteria:
  - one real participant completes the approved runbook;
  - consent/privacy handling and participant code are recorded;
  - observations are factual and distinguish facilitator interpretation;
  - blocking defects and wording changes become Issues;
  - no fabricated rate, quote, or additional session is reported.

### UXR-02 — Conduct 5–8 formative sessions

- Priority: `Must`
- Type/area: `research`; UX
- Dependencies: `UXR-01` corrections complete
- Suggested branch: `docs/<issue-number>-formative-results`
- Acceptance Criteria:
  - 5–8 real sessions use the approved synthetic Scam and legitimate tasks;
  - comprehension, action choice, legitimate success, time, and confusion are recorded;
  - denominator and missing data are explicit;
  - findings do not claim population-level effectiveness;
  - prioritized changes and limitations are documented.

### DEMO-01 — Prepare resilient demo and technical handoff

- Priority: `Must`
- Type/area: `docs`, `chore`; demo
- Dependencies: `DEP-01`, `UXR-01`; `UXR-02` if schedule permits
- Suggested branch: `docs/<issue-number>-demo-readiness`
- Acceptance Criteria:
  - live script covers reserve, Low/Medium/High, hold, verify/cancel/report, and graph explanation within the allotted time;
  - backup recording/screenshots and reset instructions exist;
  - Architecture, Threat Model, tests, and limitations are answerable from canonical docs;
  - Implemented/Simulated/Future boundaries are visible;
  - all three members can run the demo without fixed-role dependency.

## Suggested Critical Path

```text
FND-01 -> FND-02 -> PWA-02 -> PWA-03
                     |          |
                     |          +-> RES-01 -> RES-02
                     `-> RSK-01 -> RSK-02 -> RSK-03/RSK-04
                                      |
                                      v
                            INT-01 -> INT-02 -> INT-04
                                      |          |
                                  INT-03          v
                                             TST-01 -> DEP-01 -> UXR-01 -> DEMO-01
```

Stretch items such as `INT-05` must never delay this path.
