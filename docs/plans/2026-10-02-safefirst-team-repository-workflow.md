# K-SafeFirst Team Repository and Delivery Workflow

Status: Implemented locally - awaiting commit/push/PR approval
Created: 2026-10-02
Approval: User approved all plan items on 2026-10-02

## Summary

จัดตั้ง Repository ปัจจุบันให้พร้อมสำหรับทีม 3 คน โดยแปลง `proposal/Second_1PagePitch.pdf` ซึ่งเป็น Proposal ที่ผ่านเข้ารอบให้เป็น Product baseline, MVP architecture, milestones, GitHub Issues และ Pull Request workflow ที่สมาชิกและ Coding Agents ใช้ตรงกัน ผลิตภัณฑ์ใช้ชื่อ `K-SafeFirst` และ Core MVP เป็น Mobile-first Web/PWA ที่เปิดผ่านลิงก์ได้ งานนี้ครอบคลุมการประเมินความเป็นไปได้, Repository governance และแผนส่งมอบ แต่จะยังไม่เริ่มเขียน Application จนกว่าแผนได้รับอนุมัติ

## Clarifying Questions

All blocking questions are resolved:

- [x] ใช้ Repository ปัจจุบันต่อ และใช้ชื่อผลิตภัณฑ์ `K-SafeFirst`
- [x] ยกเลิกข้อจำกัดเรื่องการอ้างชื่อ KBTG/K+; ผู้ใช้จะปรับชื่อหรือข้อความดังกล่าวเองภายหลังหากต้องการ
- [x] Core MVP เป็น Mobile-first Web/PWA ที่เปิดผ่านลิงก์และใช้งานในหน้าจอมือถือได้
- [x] ทีมมี 3 คนและไม่มี Role ถาวร ใช้ Pull-based ownership: สมาชิกเลือก Issue ตามความสนใจและความพร้อม
- [x] ทุก Issue ต้องมี Owner หนึ่งคน, Acceptance Criteria และ Reviewer ที่ไม่ใช่เจ้าของงาน
- [x] ทุก PR รวมเอกสารต้องมีอย่างน้อย 1 Approval, automated checks ผ่าน, แก้ review conversations ครบ และใช้ Squash merge เข้า `main`

## Feasibility Conclusion

ทำ MVP ได้จริงภายใต้ขอบเขตต่อไปนี้:

- `Implemented`: Mobile PWA flow, เงินสำรองจำลอง, Scheduled Auto-Allocation, synthetic transaction scenarios, rule-based multi-signal risk correlation, graph-based destination-risk simulation, Low/Medium/High policy, contextual warning, server-controlled transaction hold, cancel/report flow และ audit events
- `Simulated`: บัญชีและยอดเงิน, K-ePocket-like pockets, recipient history, fraud blacklist, transaction graph, device/session signals, interest/benefit tier, K-Point/Save Point, trusted-contact notification และ transaction settlement
- `Future/Bank dependency`: ข้อมูลลูกค้าจริง, internal banking APIs, real account hold/release, official fraud lists, production graph analytics, identity verification, rewards/interest approval, regulatory controls และ incident-response integration

ห้ามเรียก Prototype ว่าเชื่อม Production แล้ว และห้ามอ้าง model accuracy, fraud reduction หรือ business impact ที่ยังไม่ได้ทดสอบ Core novelty ที่ต้องพิสูจน์คือการใช้บริบทของ Protected Reserve ร่วมกับหลายสัญญาณเพื่อเพิ่ม friction ก่อนเงินออก ไม่ใช่การสร้าง Mobile Banking App เต็มรูปแบบ

## Proposed Technical Baseline

```text
Mobile-first PWA (React + TypeScript + Vite)
                    |
              REST/JSON API
                    |
Risk API (Python + FastAPI)
  |-- Rule-based correlation and explainable reasons
  |-- Synthetic transaction graph (NetworkX)
  |-- Server-side transaction-hold state machine
  `-- Audit events without sensitive customer data
                    |
        Synthetic fixtures / local database
```

- Frontend tests: Vitest และ Playwright สำหรับ Hero Scenario บน mobile viewport
- Backend tests: pytest สำหรับ risk rules, state transitions และ bypass cases
- API contract: OpenAPI; ใช้ stable scenario IDs แทนข้อมูลบัญชีจริง
- CI: GitHub Actions สำหรับ lint, type-check, unit tests, integration tests และ secret scan
- Deployment: วางเป็น Web service ที่แชร์ลิงก์ได้ โดยเลือกผู้ให้บริการภายหลังและไม่ผูก Architecture กับ Vendor
- Security baseline: TLS เมื่อ Deploy, no real credentials/customer data, server-authoritative timers, input validation, rate limiting, idempotency และ sanitized audit logs

## File And Code References

- `proposal/Second_1PagePitch.pdf` — Canonical submission baseline ที่กรรมการเห็น
- `docs/plans/2026-09-03-k-plus-track-3-concept-decision.md` — Decision history และ Post-submission status; ใช้เป็นข้อมูลสนับสนุนเท่านั้นเมื่อขัดกับ Proposal
- `AGENTS.md` — Instruction เดิมมุ่งรอบสมัคร ต้องปรับให้ Proposal ที่ส่งแล้วเป็น Canonical baseline และเพิ่มกติกาสำหรับ Team implementation โดยไม่ลบประวัติเดิมที่ยังมีประโยชน์
- `.gitignore` — มี baseline สำหรับ secrets, Python, Node และ editor files แล้ว
- `research/deep-technical-security-and-detection.md` — Technical security baseline สำหรับ trusted request, multi-signal risk, graph risk, policy และ incident telemetry
- `research/threat-model-v5.md` — Threat scenarios และ trust boundaries เดิม
- `research/synthetic-risk-table-v5.md` — Synthetic scenarios สำหรับ Low/Medium/High policy
- `origin/main` — Repository ปัจจุบันยังเป็นเอกสาร/งานสมัคร ไม่มี application source หรือ CI; worktree มี user-owned changes จึงยังไม่ควรสร้าง/switch branch ก่อนกำหนด boundary
- [Project 361 CONTRIBUTING example](https://github.com/zero-h0ur/CS361_G03_Cooperative-Education-Planning-Management-System-/blob/main/CONTRIBUTING.md) — ใช้รูปแบบ issue-linked branch, Conventional-style commit, PR review และ squash merge เป็นตัวอย่าง ไม่คัดลอกชื่อหรือบริบทของโครงการ

## Plan Todos

- [x] สร้าง `README.md` สำหรับ Project overview, Quick start, branch naming, issue-to-PR workflow และ Definition of Done
- [x] ปรับ `AGENTS.md` ให้ยึด `proposal/Second_1PagePitch.pdf` เป็น Canonical baseline พร้อม synthetic-data boundary, security rules, non-goals, source-of-truth order และคำสั่งตรวจสอบก่อนส่ง PR
- [x] สร้าง `CONTRIBUTING.md` โดยยึดแนวทาง Project 361: sync main → issue → branch → test → commit → push → PR → review → squash merge
- [x] สร้าง `.github/ISSUE_TEMPLATE/` และ `.github/pull_request_template.md` เพื่อบังคับ Acceptance Criteria, test evidence, security/privacy impact และ screenshot สำหรับ UI
- [x] สร้างเอกสาร Product/Technical context สำหรับมนุษย์และ AI ได้แก่ `docs/product/PRODUCT_BASELINE.md`, `docs/architecture/SYSTEM_ARCHITECTURE.md`, `docs/security/THREAT_MODEL.md`, `docs/testing/TEST_STRATEGY.md`, `docs/delivery/ROADMAP.md` และ `docs/delivery/ISSUE_BACKLOG.md`
- [x] แปลง Proposal เป็น MVP scope ที่ implement ได้จริง โดยแยก `Implemented`, `Simulated`, `Future/Bank dependency` และห้ามอ้าง Production integration
- [x] กำหนด Milestones และ Issue backlog: Foundation, Mobile UX, Reserve/Auto-Allocation, Risk Engine/Graph, Intervention/Delay, Testing/Observability และ Demo/Pitch readiness
- [x] กำหนด Branch protection ที่แนะนำ: ห้าม direct push เข้า `main`, PR ต้องผูก Issue, อย่างน้อย 1 approval, status checks ผ่าน และ squash merge
- [x] หลังอนุมัติแผน สร้าง setup branch `chore/repository-foundation` โดยไม่ Commit/Push งานผู้ใช้ที่ไม่เกี่ยวข้อง
- [x] Validate เอกสารด้วย link/path scan, YAML parse, Python compile, conflict-marker scan และตรวจว่า Issue/PR examples, Milestones และ Definition of Done สอดคล้องกัน

## Planned Milestones

1. `M0 — Repository Foundation`
   - README, AGENTS, CONTRIBUTING, templates, labels/milestone conventions และ CI skeleton
   - Exit: สมาชิกใหม่หรือ Coding Agent อ่านเอกสารแล้วสร้าง Issue → Branch → PR ได้โดยไม่ต้องเดากติกา
2. `M1 — Mobile PWA Shell & Hero Journey`
   - Mobile layout, navigation, synthetic personas/scenarios และ end-to-end clickable happy path
   - Exit: เปิดลิงก์ใน mobile viewport และเดิน Flow ตั้งแต่ Dashboard ถึง Transfer review ได้
3. `M2 — Protected Reserve & Auto-Allocation`
   - Reserve goal, scheduled allocation simulation, insufficient-balance handling, Save Point/Benefit representation
   - Exit: Scenario ออมสำเร็จ/ไม่สำเร็จ/ถอนฉุกเฉินทำงานตามกติกาและไม่มีเงินจริง
4. `M3 — Multi-signal Risk & Graph Simulation`
   - Normalized event schema, rule engine, synthetic graph, destination flags, explainable Low/Medium/High result
   - Exit: Boundary scenarios และ attacker-coached bypass ให้ผลที่ทำซ้ำได้ พร้อมเหตุผล 2–3 ข้อ
5. `M4 — Risk-based Intervention`
   - Contextual warning, deliberate confirmation, server-side hold, countdown display, verify/cancel/report transitions
   - Exit: Client ข้าม timer หรือกดย้ำไม่ได้ และ High-risk confirmed destination ถูกปฏิเสธตาม Prototype policy
6. `M5 — Security, Quality & Observability`
   - Threat tests, API validation, idempotency, rate limits, dependency/secret scan, privacy-safe audit trail, accessibility checks
   - Exit: CI ผ่านและมี evidence สำหรับ normal, false-positive, emergency และ bypass scenarios
7. `M6 — Deploy, Usability Test & Demo Readiness`
   - Deploy link, seed/reset demo, pilot 1 คนก่อน แล้วจึง formative test 5–8 คน, demo script และ limitation sheet
   - Exit: Link ใช้งานได้, test sessions รายงานตามจริงเท่านั้น และทีม Demo Hero Scenario ได้ภายในเวลาที่กำหนด

## Grill-Me Outcome

- Transcript: `tmp/grill-me/session-team-repo-2026-10-02-20261002-033543.md`
- Outcome: `tmp/grill-me/outcome-team-repo-2026-10-02-20261002-033543.md`
- Summary: ใช้ Repository ปัจจุบันและชื่อ K-SafeFirst; MVP เป็น Mobile-first Web/PWA; ทีม 3 คนไม่มี Role ถาวร ใช้ Issue ownership และ Peer-reviewed PR workflow

## Build From Plan

- Ready to build: Yes
- Selected todos: All after approval
- Execution notes: Re-read the plan and worktree before execution; preserve existing user changes; create the repository-foundation branch only after approval; do not commit, push, create remote Issues/Milestones or open PRs unless the user separately authorizes those external Git actions

## Implementation Result

- Local branch: `chore/repository-foundation`
- Repository foundation files created and canonical `AGENTS.md` updated
- GitHub Issue forms, PR template, and repository-guardrails workflow created
- Product, architecture, security, testing, roadmap, and issue backlog documents created
- Remote GitHub state unchanged: no commit, push, Issue, Milestone, branch-protection setting, or PR created
- Local validation: passed

## Validation

- Confirm all planned Markdown files render and all relative links resolve
- Run `rg` over the implementation scope for accidental real customer/account data, secrets and unsupported production claims
- Check branch names and examples follow `<type>/<issue-number>-<short-description>`
- Confirm every milestone maps to small issues with Acceptance Criteria and each issue can be delivered by one reviewable PR
- Confirm MVP claims are labelled `Implemented`, `Simulated` or `Future/Dependency`
- Confirm no secrets, real banking data, credentials or private customer information are introduced

## Risks

- Proposal scope is broader than a small team can implement at production fidelity; interest, rewards, trusted-contact notification and payment holding require explicit simulation boundaries
- Existing worktree contains unrelated user-owned modifications; careless branch creation or commit could mix them into the setup PR
- Overly large milestones or PRs would recreate the coordination problem this workflow is meant to solve
- Public repository content may expose competition strategy or names the team intends to keep private
- ไม่มี Role ถาวรช่วยให้ทีมยืดหยุ่น แต่เสี่ยงที่งานสำคัญไม่มีคนหยิบ จึงต้องใช้ Issue Owner, milestone board และ WIP limit อย่างเคร่งครัด

## Approval

- Status: Approved by user on 2026-10-02
