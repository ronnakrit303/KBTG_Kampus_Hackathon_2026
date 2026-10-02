# Contributing to K-SafeFirst

This document defines how the three-person team turns work into reviewable GitHub Issues and Pull Requests. No one has a permanent role; ownership is attached to an Issue, not a person.

## Core rules

1. No direct push to `main`.
2. One Issue maps to one branch and normally one PR.
3. Claim the Issue before editing to avoid duplicate work.
4. Keep one substantial Issue in progress per member.
5. The PR author cannot approve their own PR.
6. Every PR—including documentation—needs at least one approval from another member.
7. Required checks must pass and review conversations must be resolved.
8. Use Squash merge, then delete the branch.
9. Never mix unrelated cleanup with the Issue scope.
10. Never commit real customer data, credentials, private banking data, or unsupported production claims.

## 1. Select and claim an Issue

Choose an Issue from the current milestone. Before starting:

- confirm it is unassigned;
- assign yourself as Owner;
- check dependencies and blocked work;
- confirm the Acceptance Criteria are testable;
- identify the expected reviewer when coordination is needed; and
- move it to `In progress`.

If the Issue is too large for one understandable PR, split it before coding. Do not use the PR itself to discover what the task means.

## 2. Sync `main`

```bash
git switch main
git pull --ff-only origin main
```

Do not use destructive reset commands to solve a dirty worktree. Commit, stash with a clear message, or ask the owner of the changes first.

## 3. Create a branch

Format:

```text
<type>/<issue-number>-<short-description>
```

Allowed types:

| Type | Use |
|---|---|
| `feature` | New user-visible capability |
| `fix` | Defect correction |
| `security` | Security control, threat mitigation, or hardening |
| `test` | Test-only work |
| `docs` | Documentation-only work |
| `refactor` | Internal change without intended behavior change |
| `chore` | Tooling, configuration, or maintenance |

Examples:

```bash
git switch -c feature/12-reserve-goal-screen
git switch -c security/24-hold-state-machine
git switch -c docs/42-api-boundaries
```

Use lowercase English, hyphens, and a short description. The bootstrap branch `chore/repository-foundation` is the only no-Issue exception.

## 4. Implement one complete slice

- Follow `AGENTS.md` and the canonical documents linked by the Issue.
- Prefer a vertical slice that can be demonstrated over disconnected UI or backend fragments.
- Keep API contracts, fixtures, UI copy, architecture, and tests consistent.
- Label capabilities as `Implemented`, `Simulated`, or `Future/Bank dependency`.
- Add or update tests in the same PR.
- Record a follow-up Issue for intentionally deferred work.

## 5. Validate locally

Run all checks relevant to the changed area. During the repository-foundation phase:

```bash
python scripts/validate_repository.py
```

After the application scaffold exists, the PR must also run the commands documented for frontend and backend in the root README and `docs/testing/TEST_STRATEGY.md`.

Never report a check as passed unless it was executed. If a check cannot run, explain why and describe the residual risk in the PR.

## 6. Commit

Format:

```text
<type>: <imperative summary>
```

Allowed commit types: `feat`, `fix`, `security`, `test`, `docs`, `refactor`, `chore`, `ci`.

Good examples:

```text
feat: add scheduled allocation simulator
security: reject duplicate transaction instruction
test: cover split-transfer bypass scenario
docs: classify trusted contact as simulated
```

Avoid vague messages such as `update`, `fix stuff`, or `final`.

## 7. Push and open a PR

```bash
git push -u origin <branch-name>
```

Complete the PR template and link the Issue using:

```text
Closes #<issue-number>
```

A PR must state:

- why the change is needed;
- what is in and out of scope;
- user-visible and technical changes;
- security and privacy impact;
- tests actually run and their results;
- screenshots or recording for UI changes;
- truth-label changes;
- limitations and follow-ups.

Prefer PRs that a reviewer can understand in roughly 15–30 minutes. Split a PR that spans multiple milestones or unrelated concerns.

## 8. Review

The reviewer checks:

- Acceptance Criteria and Issue scope;
- product and architecture consistency;
- unsafe assumptions or unsupported claims;
- security invariants and failure paths;
- test quality, not only test existence;
- mobile readability and accessibility for UI changes;
- synthetic-data and privacy boundaries;
- documentation and API contract changes.

Use clear review outcomes:

- `Approve` — ready after checks pass;
- `Comment` — non-blocking feedback;
- `Request changes` — a correctness, scope, security, privacy, or test issue blocks merge.

The author responds to every blocking thread. The reviewer—not the author—confirms that the concern is resolved.

## 9. Merge

Merge only when:

- the linked Issue and Acceptance Criteria are complete;
- at least one non-author approval exists;
- required checks pass;
- all review conversations are resolved;
- UI evidence is attached when applicable;
- no unrelated files are included.

Use **Squash and merge**. The squash message should match the change, for example:

```text
feat: add protected reserve goal flow (#12)
```

Delete the remote branch and move the Issue to `Done`.

## Branch protection recommendation

Configure `main` with:

- require a pull request before merging;
- require at least 1 approval;
- dismiss stale approvals when new commits are pushed;
- require conversation resolution;
- require repository validation and later application test checks;
- block force pushes and deletion;
- allow Squash merge as the default merge method.

These settings are GitHub configuration and are not applied automatically by this document.

## Definition of Done

Work is done only when:

- Acceptance Criteria pass;
- tests and checks are recorded honestly;
- relevant docs and contracts are current;
- security, privacy, false-positive, emergency, and repeated-action paths are addressed where applicable;
- no real data, secret, or production claim is present;
- the PR is approved, checks pass, and it is ready to squash.
