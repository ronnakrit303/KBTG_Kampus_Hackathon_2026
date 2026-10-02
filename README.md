# K-SafeFirst

K-SafeFirst is a Mobile-first Web/PWA prototype that helps First Jobbers build a protected reserve and pause before a social-engineering scam causes an authorized transfer. The project combines savings support with explainable, risk-based transaction intervention.

The team is building a hackathon prototype with synthetic data. It is not a production banking service and does not connect to real accounts, payment rails, customer records, fraud lists, rewards, or interest systems.

## Canonical product source

The proposal already submitted to judges is [Second_1PagePitch.pdf](proposal/Second_1PagePitch.pdf). Its implementable interpretation is [PRODUCT_BASELINE.md](docs/product/PRODUCT_BASELINE.md).

When documents disagree, follow the source order in [AGENTS.md](AGENTS.md).

## MVP outcome

A reviewer should be able to open one link in a mobile browser and demonstrate:

1. setting a protected reserve goal;
2. simulating scheduled Auto-Allocation;
3. initiating normal and suspicious transfers;
4. receiving explainable `Low / Medium / High` decisions;
5. seeing a suspicious instruction held before simulated settlement;
6. choosing to verify, cancel, or report; and
7. resetting the demo to a known synthetic scenario.

## Truth labels

| Label | Meaning |
|---|---|
| `Implemented` | Runs in this repository and has relevant test evidence. |
| `Simulated` | Uses deterministic synthetic fixtures to demonstrate expected behavior. |
| `Future/Bank dependency` | Requires production data, approval, infrastructure, or regulated operations. |

See [PRODUCT_BASELINE.md](docs/product/PRODUCT_BASELINE.md) before making product claims.

## Planned stack

```text
React + TypeScript + Vite PWA
            |
        REST/JSON
            |
Python + FastAPI risk service
  |-- versioned rules
  |-- synthetic NetworkX graph
  |-- transaction-hold state machine
  `-- privacy-safe audit events
```

The application scaffold will be introduced through a dedicated Issue. Repository governance is being established first.

## Repository map

```text
.
|-- AGENTS.md                  Team and coding-agent rules
|-- CONTRIBUTING.md            Issue, branch, commit, PR, and review workflow
|-- proposal/                  Submitted proposal and proposal artifacts
|-- docs/
|   |-- product/               Canonical implementable product baseline
|   |-- architecture/          System boundaries and API/state design
|   |-- security/              Threat model and security invariants
|   |-- testing/               Test strategy and quality gates
|   `-- delivery/              Roadmap and issue-ready backlog
|-- research/                  Evidence and historical analysis
|-- prototype/                 Existing visual prototypes and diagrams
`-- scripts/                   Repository validation utilities
```

## Team workflow

The team has three members and no permanent roles. Claim any unassigned Issue that matches your interest and capacity. Each Issue still needs one Owner, Acceptance Criteria, dependencies, and a Reviewer.

```text
Choose/claim Issue
       |
Create one branch
       |
Implement + test
       |
Commit + push
       |
Open linked PR
       |
1 peer approval + checks pass
       |
Squash merge + delete branch
```

No direct push to `main`. Documentation follows the same PR workflow as code.

## Branch naming

Use lowercase English and hyphens:

```text
feature/<issue-number>-<short-description>
fix/<issue-number>-<short-description>
security/<issue-number>-<short-description>
test/<issue-number>-<short-description>
docs/<issue-number>-<short-description>
refactor/<issue-number>-<short-description>
chore/<issue-number>-<short-description>
```

Examples:

```text
feature/12-reserve-goal-screen
security/24-transaction-hold-state-machine
test/31-fake-recruiter-e2e
docs/42-update-api-boundaries
```

The bootstrap branch `chore/repository-foundation` is the only exception because it predates remote Issue creation.

## Commit format

```text
<type>: <imperative summary>
```

Examples:

```text
feat: add protected reserve goal form
security: enforce server-side hold expiry
test: cover repeated transfer bypass scenario
docs: clarify simulated destination risk
```

## Before starting work

1. Read [AGENTS.md](AGENTS.md).
2. Read the selected Issue and claim it.
3. Check dependencies in [ISSUE_BACKLOG.md](docs/delivery/ISSUE_BACKLOG.md).
4. Sync `main` and create the Issue branch.
5. Keep one substantial Issue in progress per member.

Full commands, review rules, and Definition of Done are in [CONTRIBUTING.md](CONTRIBUTING.md).

## Current planning documents

- [Product baseline](docs/product/PRODUCT_BASELINE.md)
- [System architecture](docs/architecture/SYSTEM_ARCHITECTURE.md)
- [Threat model](docs/security/THREAT_MODEL.md)
- [Test strategy](docs/testing/TEST_STRATEGY.md)
- [Roadmap](docs/delivery/ROADMAP.md)
- [Issue-ready backlog](docs/delivery/ISSUE_BACKLOG.md)

## Safety and privacy

- Use synthetic data only.
- Never commit secrets or real personal, account, message, or customer information.
- Do not claim a real production integration.
- Do not call deterministic prototype rules “AI”.
- Report usability-test counts exactly as conducted; never generate participant results.
