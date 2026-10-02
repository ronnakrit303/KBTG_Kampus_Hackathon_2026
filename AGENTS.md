# AGENTS.md — K-SafeFirst Team Development

## 1. Mission

This repository is the shared workspace for developing **K-SafeFirst**, a post-selection hackathon prototype for First Jobbers aged 22–30. The team has passed the first-round proposal screening. The active goal is now to build and validate a credible Mobile-first Web/PWA demonstration—not to rewrite the submitted proposal.

All human contributors and coding agents must optimize for a small, demonstrable, security-focused MVP. Never imply that this repository is a production banking system or that it connects to real customer, account, fraud, or payment infrastructure.

Communicate with the user primarily in Thai. Keep standard technical terms in English when they improve precision.

## 2. Canonical source order

When files disagree, use this order:

1. `proposal/Second_1PagePitch.pdf` — the product promise already submitted to judges.
2. `docs/product/PRODUCT_BASELINE.md` — the approved, implementable interpretation of that proposal.
3. `docs/architecture/SYSTEM_ARCHITECTURE.md`, `docs/security/THREAT_MODEL.md`, and `docs/testing/TEST_STRATEGY.md` — technical constraints.
4. The active GitHub Issue and its Acceptance Criteria.
5. Tests and code.
6. Older files under `research/`, `prototype/`, or `docs/plans/` — supporting history only.

Do not silently change a higher-priority source. If implementation evidence shows that the baseline must change, open a decision Issue and update the affected documents in the same or a preceding PR.

## 3. Product baseline

The differentiating hypothesis is:

> Protect a user-designated reserve at the moment social engineering is pressuring the user to authorize a risky transfer, while helping the user build that reserve over time.

The Hero Scenario is a Fake Recruiter asking a First Jobber to pay an application, training, equipment, or deposit fee to a new personal account.

Core MVP capabilities:

1. Protected Reserve and a savings goal.
2. Scheduled Auto-Allocation simulation.
3. Multi-signal transaction-risk correlation.
4. Synthetic graph-based destination risk.
5. Explainable `Low / Medium / High` policy decisions.
6. Contextual warning and deliberate confirmation.
7. Server-controlled transaction hold for suspicious High-risk cases.
8. Cancel, report, verify, and auditable state transitions.

The product is Scam-first. Fraud detection, graph analysis, device/session posture, and policy enforcement are defensive mechanisms supporting Scam prevention; they are not separate products.

## 4. Truth labels

Every feature or claim must be labelled accurately:

- `Implemented` — executable in this repository and covered by relevant tests.
- `Simulated` — deterministic synthetic behavior used to demonstrate an integration or scenario.
- `Future/Bank dependency` — requires production data, approval, infrastructure, or regulated operations unavailable to this team.

The MVP uses synthetic data only. Never use real names, account numbers, credentials, private messages, customer records, internal bank data, or production endpoints.

Do not claim:

- real AI/ML unless a trained, evaluated model actually exists;
- production fraud accuracy, precision, recall, loss reduction, adoption, or cost saving;
- access to official blacklists, transaction graphs, identity systems, payment rails, rewards, or interest configuration;
- that a transaction hold moves or freezes real money;
- that the system prevents every Scam or Fraud case.

## 5. Technical baseline

Target delivery: Mobile-first Web/PWA opened through a link.

- Frontend: React + TypeScript + Vite/PWA.
- Backend: Python + FastAPI.
- API: REST/JSON with OpenAPI.
- Risk policy: deterministic, versioned rules.
- Destination risk: NetworkX with synthetic graph fixtures.
- State: local development database or deterministic in-memory fixtures until persistence is justified.
- Tests: Vitest, Playwright, and pytest.
- CI: GitHub Actions.

The browser is not a trusted enforcement point. Risk decisions, transaction-hold state, release time, idempotency, and final transition authorization must be controlled by the backend.

## 6. Security invariants

These rules are non-negotiable unless a reviewed decision explicitly replaces them:

- Protected Reserve alone never makes a transaction High risk.
- User-provided purpose is a weak signal and cannot downgrade stronger evidence.
- Split and repeated transfers are evaluated cumulatively in a policy window.
- Own-account and verified-biller fixtures with neutral destination risk remain usable without a fixed delay.
- A Savings Nudge is dismissible and never creates a transaction hold.
- Suspicious High-risk transactions are held before simulated settlement.
- Confirmed Scam/Fraud-risk destinations are rejected by policy.
- Repeated clicks cannot create duplicate instructions; mutation requests use idempotency.
- The countdown shown in the client is informational; the backend owns the authoritative time and state.
- Warnings expose two or three understandable reasons, not thresholds or the complete detection formula.
- The prototype does not read email, messages, resumes, calls, contacts, or device files.
- Audit events contain synthetic identifiers and the minimum data necessary to explain state changes.

See `docs/security/THREAT_MODEL.md` for threats, controls, and residual risks.

## 7. Team model

The team has three members and no permanent roles. Use pull-based ownership:

- A member claims an unassigned Issue before starting.
- Every Issue has one Owner, explicit Acceptance Criteria, dependencies, and test evidence requirements.
- Keep at most one substantial Issue `in progress` per member.
- Anyone may work on frontend, backend, security, tests, research, or documentation.
- Cross-review is required so knowledge does not stay with one person.

Do not assign fixed team roles unless the user later requests them.

## 8. Required Git workflow

Follow `CONTRIBUTING.md`.

1. Start from an approved Issue.
2. Sync local `main`.
3. Create one branch for one Issue using `<type>/<issue-number>-<short-description>`.
4. Make only scoped changes.
5. Run the checks required by the Issue and this file.
6. Commit using `<type>: <imperative summary>`.
7. Push the branch and open a PR linked with `Closes #<issue-number>`.
8. The author must not approve their own PR.
9. At least one other member must approve; automated checks must pass and review conversations must be resolved.
10. Squash merge into `main`, then delete the branch.

Never push directly to `main`. Never bundle unrelated cleanup into a feature PR. Documentation changes also require an Issue and PR.

## 9. Branch, commit, and PR conventions

Allowed branch types:

- `feature/<issue-number>-<description>`
- `fix/<issue-number>-<description>`
- `security/<issue-number>-<description>`
- `test/<issue-number>-<description>`
- `docs/<issue-number>-<description>`
- `refactor/<issue-number>-<description>`
- `chore/<issue-number>-<description>`

Use lowercase English and hyphens. The current bootstrap branch `chore/repository-foundation` is the only exception because templates are being created before remote Issues exist.

Allowed commit types: `feat`, `fix`, `security`, `test`, `docs`, `refactor`, `chore`, `ci`.

Every PR must include:

- problem and scoped solution;
- linked Issue;
- user-visible and technical changes;
- security/privacy impact;
- tests run and their actual results;
- screenshots or a short recording for UI changes;
- truth label changes (`Implemented`, `Simulated`, `Future/Bank dependency`);
- limitations and follow-up work.

## 10. Definition of Done

An Issue is done only when:

- all Acceptance Criteria are demonstrably satisfied;
- code, UI copy, documentation, fixtures, and API contract agree;
- relevant unit, integration, E2E, security, and accessibility checks pass;
- no secret, real customer data, or unsupported production claim is introduced;
- failure, false-positive, emergency, and repeated-click paths are considered where relevant;
- the PR is small enough to review, linked to the Issue, approved by another member, and ready to squash;
- follow-up work is recorded instead of hidden in comments or assumptions.

Do not fabricate usability sessions. The required order is clickable flow → one real pilot → corrections → 5–8 real formative sessions. Record `0 sessions conducted` until a session actually occurs.

## 11. Working with existing files

- Preserve user changes and unrelated worktree modifications.
- Use `rg` or `rg --files` for discovery.
- Use `apply_patch` for text edits.
- Do not overwrite `proposal/Second_1PagePitch.pdf`.
- Older JobShield diagrams and research may use outdated names or flows. Treat them as references, not requirements.
- If a task touches architecture, security policy, API behavior, or test oracles, update the relevant canonical document in the same PR.
- Do not commit generated dependencies, secrets, local environments, test reports, or temporary files.

## 12. First actions in every coding-agent session

1. Read this file completely.
2. Read the active Issue and its Acceptance Criteria.
3. Read only the canonical product, architecture, security, and test documents relevant to that Issue.
4. Inspect current branch and worktree; do not absorb unrelated changes.
5. State the intended change and verification briefly before editing.
6. Implement the smallest complete slice.
7. Run proportionate checks and report actual results, limitations, and changed files.

If no Issue exists or scope is ambiguous, stop and ask for one material decision. Do not invent a new feature merely because it appears in an older research file.
