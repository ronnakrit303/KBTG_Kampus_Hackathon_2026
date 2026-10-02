# K-SafeFirst Delivery Roadmap

Status: Approved milestone plan

Date: 2026-10-02

Team model: three members, no permanent roles, pull-based Issue ownership

## 1. Delivery principle

Build one trustworthy end-to-end Hero Scenario before adding breadth. Each milestone must leave the repository demonstrable and reviewable. A milestone closes only when its exit criteria have evidence; completing code without tests, documentation, or UI integration does not close it.

Calendar dates are intentionally unset until the team receives the Pitching Day/hackathon schedule. Milestone dependencies and priorities remain valid without dates. Once the deadline is known, add due dates and preserve a final buffer rather than compressing M5–M6.

## 2. Dependency map

```text
M0 Repository Foundation
          |
          v
M1 Mobile PWA Shell & Hero Journey
       |                 |
       v                 v
M2 Reserve          M3 Risk & Graph
       \                 /
        \               /
         v             v
        M4 Risk-based Intervention
                    |
                    v
        M5 Security, Quality & Observability
                    |
                    v
        M6 Deploy, User Test & Demo Readiness
```

M2 and M3 can proceed in parallel after the M1 contract and shell are stable. M4 integrates them. M5 begins incrementally earlier but cannot close until M4 is complete.

## 3. Milestones

### M0 — Repository Foundation

Goal: every member and coding agent follows the same product truth, workflow, and quality rules.

Deliverables:

- README and canonical documentation map;
- AGENTS instructions;
- CONTRIBUTING workflow;
- Issue and PR templates;
- repository validation workflow;
- issue-ready roadmap/backlog.

Exit criteria:

- a new contributor can identify source of truth and create a valid Issue branch and PR;
- team rules state one Owner, one non-author approval, passing checks, resolved threads, and Squash merge;
- canonical links and repository validator pass;
- no application functionality is falsely marked Implemented.

### M1 — Mobile PWA Shell & Hero Journey

Goal: create the smallest navigable PWA skeleton and shared synthetic contract.

Deliverables:

- React/TypeScript/Vite PWA and FastAPI service skeleton;
- responsive mobile shell and accessible navigation;
- synthetic persona/scenario list and deterministic reset;
- transfer-review happy-path screens using a temporary API contract;
- base unit, API, and Playwright setup.

Exit criteria:

- one command or documented pair of commands starts the local system;
- a mobile viewport can navigate Dashboard → Transfer → Review → Result;
- scenario reset produces the same identifiers and balances;
- CI builds frontend/backend and runs starter tests.

### M2 — Protected Reserve & Auto-Allocation

Goal: demonstrate the financial-management layer without real accounts or payroll detection.

Deliverables:

- monthly-essential-expense and 3/6/custom-month target setup;
- starting amount including zero;
- Scheduled Auto-Allocation rule by source, amount, and date;
- success and insufficient-balance simulation;
- reserve coverage, Save Point, and prototype Benefit progress;
- distinct dismissible Savings Nudge.

Exit criteria:

- reserve arithmetic and boundaries have unit tests;
- insufficient balance never creates a negative synthetic balance;
- Auto-Allocation is explicitly consented, editable, pausable, and labelled simulated;
- benefits do not promise approved points, interest, or monetary value;
- Savings Nudge never enters transaction hold.

### M3 — Multi-signal Risk & Graph Simulation

Goal: produce deterministic, explainable risk evidence for normal, ambiguous, suspicious, and confirmed cases.

Deliverables:

- normalized transaction/risk schema;
- versioned rule engine and precedence;
- repeated/split-transfer aggregation;
- synthetic NetworkX graph and destination evidence;
- `Low / Medium / High` tier, action, policy version, and reason codes;
- S01–S12 fixture set where applicable.

Exit criteria:

- reserve source or purpose alone cannot produce High;
- false-purpose and split-transfer bypass fixtures remain High when stronger evidence exists;
- own-account/verified-biller neutral fixtures remain Low;
- graph results are reproducible and visibly synthetic;
- no AI/ML or production-accuracy claim appears.

### M4 — Risk-based Intervention

Goal: enforce the decision before simulated settlement and communicate it clearly.

Deliverables:

- backend-authoritative transaction state machine;
- Medium contextual warning and deliberate confirmation;
- High suspicious transaction hold with server time;
- High confirmed rejection;
- verify, cancel, and report commands;
- refresh/reopen state recovery;
- optional trusted-contact mock only after Core states pass.

Exit criteria:

- client cannot release a held or rejected instruction directly;
- local-clock changes do not end a hold;
- repeated clicks/requests are idempotent;
- serious Scam warning shows amount and 2–3 reasons and is distinct from Savings Nudge;
- invalid transitions are rejected and audited.

### M5 — Security, Quality & Observability

Goal: turn the demo into a defensible cybersecurity prototype rather than a scripted UI.

Deliverables:

- schema limits, safe errors, rate limits, CORS/CSRF decision, dependency controls;
- structured privacy-safe audit events;
- full rule/state/API tests;
- Playwright mobile Hero Scenario and bypass tests;
- accessibility and performance checks;
- CI quality gates and limitation documentation.

Exit criteria:

- S01–S12 have executable evidence at the appropriate layer;
- secrets/dependency checks and application tests pass;
- logs contain only allowlisted synthetic data;
- warning and controls meet agreed accessibility checks;
- performance results state environment and actual measurements;
- residual risks and Future/Bank dependencies are visible.

### M6 — Deploy, Usability Test & Demo Readiness

Goal: produce a stable link and evidence-backed demo/pitch handoff.

Deliverables:

- HTTPS deployment and health/smoke check;
- per-session or protected demo reset;
- physical-mobile verification and QR/link handoff;
- one real pilot, corrections, then 5–8 real formative sessions;
- demo script, backup recording/screenshots, architecture summary, and limitation sheet.

Exit criteria:

- public link completes the Hero Scenario on the agreed physical device/browser;
- pilot happened before formative sessions;
- participant count and findings are real and traceable to notes;
- the team can reset and demonstrate Low, Medium, High suspicious, and High confirmed flows;
- a fallback demo exists for network failure;
- judges can distinguish Implemented, Simulated, and Future/Bank dependency.

## 4. Issue board policy

Recommended statuses:

```text
Backlog -> Ready -> In progress -> In review -> Done
                         |
                         `-> Blocked
```

Rules:

- an Issue moves to `Ready` only when Acceptance Criteria and dependencies are clear;
- each member has at most one substantial `In progress` Issue;
- an Issue in `Blocked` names the blocking Issue or decision;
- no one starts a later-milestone dependency simply to avoid finishing review/test work;
- review is team work, not idle time for the author to start unlimited new tasks.

## 5. Recommended labels

Type:

- `type:feature`, `type:bug`, `type:security`, `type:test`, `type:docs`, `type:research`, `type:chore`

Area:

- `area:pwa`, `area:api`, `area:risk`, `area:graph`, `area:reserve`, `area:ux`, `area:ci`, `area:docs`

Priority:

- `priority:must`, `priority:should`, `priority:stretch`

State/special:

- `blocked`, `needs-decision`, `privacy-impact`, `security-impact`, `good-first-issue`

## 6. Milestone creation order on GitHub

Create GitHub Milestones in order `M0` through `M6`. Add the Issues from [`ISSUE_BACKLOG.md`](ISSUE_BACKLOG.md), preserving the dependency field. Do not assign every Issue immediately; members claim work as capacity becomes available.

Before starting a milestone:

1. confirm the previous milestone exit criteria;
2. move only dependency-free Issues to `Ready`;
3. nominate one integration Issue if multiple parallel slices must meet;
4. verify the demo remains runnable;
5. keep Stretch work outside the Critical Path.

## 7. Release and change control

- Tag a stable demo only after M5 gates and deployed smoke tests pass.
- Product-scope changes require an Issue labelled `needs-decision` and updates to `PRODUCT_BASELINE.md`.
- Architecture/security invariant changes require another member's explicit review.
- A deadline does not justify fabricated evidence, real data, direct `main` pushes, or bypassing test/review gates.
