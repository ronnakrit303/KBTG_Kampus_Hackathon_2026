# K-SafeFirst System Architecture

Status: Proposed MVP architecture

Date: 2026-10-02

Product source: [`PRODUCT_BASELINE.md`](../product/PRODUCT_BASELINE.md)

## 1. Architecture goal

Deliver a link-accessible Mobile-first PWA that demonstrates the product and security decisions with deterministic synthetic data. The architecture must preserve an important production principle: the untrusted client presents information and user choices, while the backend owns risk decisions, transaction state, idempotency, and release timing.

## 2. System context

```text
Participant / Judge
        |
        | mobile browser
        v
K-SafeFirst PWA
        |
        | HTTPS REST/JSON
        v
K-SafeFirst API
  |-- Reserve service
  |-- Scenario service
  |-- Risk orchestrator
  |-- Policy engine
  |-- Transaction state machine
  |-- Audit-event service
  |
  +--> Synthetic graph adapter
  +--> Synthetic fixture store

Future production boundaries, not connected:
bank account/pocket service, payment hub, official fraud analytics,
identity/device trust, rewards, fraud operations, SIEM, notifications
```

## 3. Planned repository structure

```text
apps/
`-- web/                         React + TypeScript + Vite/PWA
services/
`-- risk-api/                    FastAPI application
    |-- app/api/                 HTTP endpoints and schemas
    |-- app/domain/              Reserve, risk, policy, transaction state
    |-- app/adapters/            Synthetic graph and fixture adapters
    `-- tests/                   Unit and integration tests
packages/
`-- contracts/                   Generated or shared API types if justified
tests/
`-- e2e/                         Playwright mobile journeys
fixtures/
`-- synthetic/                   Versioned personas, recipients, graphs, cases
docs/                            Canonical product/technical documentation
```

Do not create this whole tree in one setup PR. Introduce each part through the milestone Issue that owns it.

## 4. Components and responsibilities

| Component | Responsibility | Must not do |
|---|---|---|
| PWA | Mobile UI, accessibility, local presentation state, API calls, reason display | Calculate authoritative risk, release held transactions, trust local clock |
| Scenario service | Load/reset deterministic synthetic personas and histories | Store real customer information |
| Reserve service | Synthetic target, balance, allocation plan, Save Point and benefit progress | Move real funds or detect salary deposits |
| Risk orchestrator | Normalize transaction, payee, pattern, graph, and session signals | Treat one weak signal as proof of Scam |
| Policy engine | Map evidence to action using versioned deterministic rules | Hide rule version or mutate history silently |
| Graph adapter | Derive synthetic destination-risk evidence from graph fixtures | Claim access to an official bank transaction graph |
| Transaction state machine | Enforce allowed transitions, hold expiry, rejection, idempotency | Trust a client-supplied final state or countdown |
| Audit-event service | Record minimum synthetic evidence and transitions | Log secrets, full personal text, or unnecessary identifiers |

## 5. Core request flows

### 5.1 Reserve setup and Auto-Allocation

```text
PWA -> API: create/update reserve goal
API -> Reserve service: validate monthly expense and target period
Reserve service -> Fixture store: persist synthetic goal
API -> PWA: balance, target, coverage, next allocation

PWA -> API: create allocation rule(source, amount, date, consent)
API -> Reserve service: validate positive amount and source
Reserve service -> Audit: ALLOCATION_RULE_CREATED

Scheduler/simulation -> Reserve service: run due allocation
Reserve service -> balance check
  enough    -> update synthetic balances + ALLOCATION_SUCCEEDED
  not enough -> no debit, no negative balance + ALLOCATION_SKIPPED
```

This is scheduled internal allocation simulation. It does not detect payroll or execute real transfers.

### 5.2 Risk evaluation

```text
PWA -> API: submit transfer intent + idempotency key
API: authenticate synthetic session and validate schema
API -> Risk orchestrator:
  reserve context
  recipient class/history
  amount and cumulative velocity
  purpose as weak context
  graph destination flag
  device/session fixture
Risk orchestrator -> Policy engine: normalized evidence
Policy engine -> API: tier + action + reason codes + policy version
API -> Transaction state machine: create authoritative instruction
API -> PWA: instruction ID, state, tier, reasons, allowed actions
```

### 5.3 High-risk intervention

```text
Suspicious High
  -> HELD before simulated settlement
  -> backend issues holdUntil using server time
  -> PWA displays countdown and reasons
  -> user may VERIFY, CANCEL, or REPORT
  -> release is allowed only after policy conditions pass

Confirmed High
  -> REJECTED
  -> no release action
  -> user may REPORT or return
```

Repeated commands with the same idempotency key must return the original instruction rather than creating another one.

## 6. Transaction state machine

```text
DRAFT
  |
  v
EVALUATED
  |-- Low --------------------------> COMPLETED_SIMULATED
  |-- Medium -> CONFIRMATION_REQUIRED -> COMPLETED_SIMULATED / CANCELLED
  |-- High suspicious -------------> HELD
  |                                    |-- CANCELLED
  |                                    |-- REPORTED
  |                                    `-- VERIFIED -> RELEASE_ELIGIBLE
  |                                                     `-> COMPLETED_SIMULATED
  `-- High confirmed --------------> REJECTED -> REPORTED(optional)
```

Invalid transitions return a conflict error and create a security audit event. The client never sends `COMPLETED_SIMULATED` as an accepted desired state.

## 7. Initial API contract

Suggested endpoints for later Issues:

| Method and path | Purpose |
|---|---|
| `GET /api/v1/scenarios` | List safe synthetic demo scenarios |
| `POST /api/v1/scenarios/{id}/reset` | Restore a deterministic state |
| `GET /api/v1/reserve` | Read reserve goal, balance, coverage, and progress |
| `PUT /api/v1/reserve` | Set monthly expense, target period, and starting amount |
| `PUT /api/v1/allocations/schedule` | Create or change synthetic allocation rule |
| `POST /api/v1/allocations/run` | Run a controlled due-allocation simulation |
| `POST /api/v1/risk/evaluate` | Preview tier/reasons without settlement |
| `POST /api/v1/transactions` | Create one authoritative transaction instruction |
| `GET /api/v1/transactions/{id}` | Refresh state and server time |
| `POST /api/v1/transactions/{id}/confirm` | Deliberately confirm a Medium-risk case |
| `POST /api/v1/transactions/{id}/verify` | Record the selected independent verification path |
| `POST /api/v1/transactions/{id}/cancel` | Cancel an allowed pending instruction |
| `POST /api/v1/transactions/{id}/report` | Record a synthetic report event |

Mutation endpoints require an idempotency key. Error responses use stable codes and do not expose rule thresholds.

## 8. Core data contracts

### Risk input

```json
{
  "scenarioId": "fake-recruiter-01",
  "sourceType": "PROTECTED_RESERVE",
  "recipientId": "synthetic-payee-new-01",
  "recipientClass": "NEW_UNVERIFIED_PERSONAL",
  "amount": 7900,
  "currency": "THB",
  "purposeCode": "JOB_ONBOARDING_FEE",
  "pattern": {
    "countInWindow": 1,
    "cumulativeAmount": 7900
  },
  "destinationRisk": "ELEVATED",
  "sessionPosture": "NORMAL"
}
```

### Explainable result

```json
{
  "tier": "HIGH",
  "action": "HOLD",
  "policyVersion": "prototype-v1",
  "reasonCodes": [
    "NEW_PERSONAL_RECIPIENT",
    "PROTECTED_RESERVE_SOURCE",
    "JOB_RELATED_PAYMENT"
  ],
  "disclosure": "SYNTHETIC_PROTOTYPE_RESULT"
}
```

Reason codes are mapped to Thai UI copy in the frontend but their selection is backend-authoritative.

## 9. Trust boundaries

1. **Browser boundary:** user-controlled device, local clock, browser storage, and JavaScript may be modified.
2. **API boundary:** validate authentication fixture, schema, allowed values, request size, rate, and idempotency.
3. **Risk boundary:** do not accept client-computed tier, destination flag, reason list, or state.
4. **Graph boundary:** fixtures are untrusted input until schema validation; graph output is evidence, not automatic guilt except explicit confirmed fixtures.
5. **Settlement boundary:** the MVP has no real settlement. `COMPLETED_SIMULATED` must remain visibly synthetic.
6. **Audit boundary:** only minimum synthetic identifiers and state changes enter logs.

## 10. Deployment model

Preferred MVP deployment:

- one public HTTPS URL;
- static PWA and API deployed together or behind one origin when practical;
- environment-specific configuration provided by deployment settings, not committed secrets;
- CORS restricted to the deployed frontend if origins are separated;
- health endpoint that reveals no secrets;
- fixture reset protected from abuse or scoped to per-session demo state;
- no analytics SDK until consent, retention, and data needs are documented.

The provider is intentionally undecided. Provider choice must not alter domain rules or test oracles.

## 11. Architecture decisions still requiring Issues

- persistence: in-memory per session versus SQLite;
- authentication: anonymous signed demo session versus fixed persona token;
- one-service deployment versus separate frontend/backend services;
- hold duration appropriate for a demo without misrepresenting production policy;
- whether trusted-contact simulation is Core or Stretch after the verify flow works;
- how benefit progress is displayed without implying approved monetary value.
