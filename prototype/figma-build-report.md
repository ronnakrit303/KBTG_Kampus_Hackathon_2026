# K PLUS JobShield — Figma Build Report

วันที่: 4 กันยายน 2026; scope status updated 6 กันยายน 2026

สถานะ: Existing 31-screen clickable prototype is a prior snapshot; V6 `Protected Reserve + Auto-Save + Benefit + Risk-based Protection` ถูกระบุใน repository แล้วแต่ **not applied to canvas**; `0 pilot sessions conducted`; `0 participant sessions conducted`

## Target

- File: [K PLUS JobShield — Clickable Prototype](https://www.figma.com/design/5uoF2s6cq2JMGRFfwmdpc2)
- Workspace: Drafts ใน `Re: Verse's team`
- File key: `5uoF2s6cq2JMGRFfwmdpc2`
- Visual boundary: concept prototype ไม่ใช่ official K PLUS UI หรือ design system

## Build Inventory

- 3 pages: cover/instructions, foundations, clickable prototype
- 31 mobile screens ขนาด 390 × 844
- 44 prototype reactions เชื่อมสำเร็จ
- Missing destinations: 0
- 10 flow starting points:
  - `START-SETUP`
  - `START-SCENARIOS`
  - `START-HIGH-FULL`
  - `START-S1-CONTEXTUAL`
  - `START-S1-GENERIC`
  - `START-S2-CONTEXTUAL`
  - `START-S2-GENERIC`
  - `START-LEGIT-LOW`
  - `START-LEGIT-MEDIUM`
  - `START-EMERGENCY`

V6 planned but not yet built on the canvas:

- setup, schedule-based auto-save, Benefit Tier และ two-route withdrawal screens ตาม `prototype/figma-flow-spec-v6.md`
- ไม่มี career-stage selection, reserve-name transition หรือ Job Search Budget
- planned start points ระบุครบใน `prototype/figma-flow-spec-v6.md`
- High-risk reserve withdrawal ใช้ระบบคำเตือนเดิม `H05 → H06` แทนการสร้าง fraud-warning system ซ้ำ

## Validation Performed

- Structural audit: 31 named screens present
- Reaction audit: 44/44 links resolved; no missing destination
- Policy-path audit from link graph:
  - `H05 → H06/H09` occurs before any simulated transfer success
  - legitimate path `L01 → L02 → L03` has no High-Risk warning
  - emergency path `E01 → E02 → E03` has no High-Risk warning
- Visual spot-check completed for `A04` and `E02`; Thai rendering, hierarchy, borders and buttons were visible

## Remaining Visual QA

Figma Starter plan reached the MCP tool-call limit while requesting additional screenshots. Before pilot, the visual owner must open the file and inspect at minimum:

1. `H05` contextual High-Risk warning
2. `H06` paused/not-sent state
3. `G05-E`, `C05-T`, `G05-T` matched test variants
4. `L02` verified payment-channel wording
5. contrast, Thai text scaling, clipping and keyboard/focus order where Figma supports it

Latest V6 scope copy that still must be applied and verified on the canvas:

- use `เงินสำรองตั้งหลัก` as the only current reserve name
- show Dynamic Time Lock only as part of risk-based Cooling-off
- limit Core to 3 integrations: K-ePocket, K PLUS Transaction + Bank-side Fraud Risk and K PLUS Security & Fraud Response
- keep Email/Link scanning and Fraud Specialist outside Core as Optional/Future
- state that H06 is a Pending Instruction before the payment system/PromptPay
- do not claim a model that has not been built; the Prototype uses deterministic rules/policy and synthetic data
- หากยังไม่มีบัญชี K-ePocket ให้ส่งผู้ใช้ไปยัง official account-opening flow แล้วกลับมาสร้าง/เลือก Pocket ย่อย; ไม่อ้างว่าเปิดบัญชีแบบ one-tap
- show that Pause holds only the instruction and exact amount, not the whole account/pocket, and repeated taps do not bypass it
- add starting amount, fixed-amount monthly Schedule, target/cap, Qualified Round, Grace/Checkpoint, Tier progress และ risk-based withdrawal flow ตาม `prototype/figma-flow-spec-v6.md`
- separate friendly self-control nudges from serious High-Risk Scam warnings
- แสดง K Point/partner coupon ได้เฉพาะ Benefit Preview ภายใต้เงื่อนไขธนาคาร; ไม่ระบุคะแนน/มูลค่า และไม่มี step-up interest ใน MVP

Do not describe this remaining review as completed until it is actually performed.

Human sign-off checklist: `prototype/visual-owner-review.md`
Current pending V6 patch: `prototype/figma-scope-sync-v6.md`

ล่าสุดเมื่อ 5 กันยายน 2026: Figma Starter MCP call limit ยัง active และการตรวจผ่าน Figma MCP คืนข้อความ rate-limit อีกครั้ง จึงยังไม่สามารถเขียน latest scope copy/extension ลง canvas, ดึงภาพเพิ่ม หรือเซ็นแทน human visual owner ได้ ไม่มีการ retry ซ้ำหลัง error

## Research Accounting

- Pilot participants: 0
- Pilot sessions conducted: 0
- Study participants recruited: 0
- Participant sessions conducted: `0 sessions conducted`
- Synthetic participant results: none created

Automated link audits, screenshots and the builder's walkthrough are QA evidence, not participant evidence.
