# K PLUS JobShield — Figma Build Report

วันที่: 4 กันยายน 2026; scope status updated 5 กันยายน 2026  
สถานะ: Clickable prototype built; latest canvas copy sync pending; pilot not started; final Proposal not started

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

Latest scope copy that still must be applied and verified on the canvas:

- use `เงินสำรองก่อนเงินเดือนแรก`
- show Dynamic Time Lock only as part of risk-based Cooling-off
- limit Core to 3 integrations: K-ePocket, K PLUS Transaction + Bank-side Fraud Risk and K PLUS Security & Fraud Response
- keep Email/Link scanning and Fraud Specialist outside Core as Optional/Future
- state that H06 is a Pending Instruction before the payment system/PromptPay
- do not claim a model that has not been built; the Prototype uses deterministic rules/policy and synthetic data

Do not describe this remaining review as completed until it is actually performed.

Human sign-off checklist: `prototype/visual-owner-review.md`
Exact pending copy patch: `prototype/figma-scope-sync-patch.md`

ล่าสุดเมื่อ 5 กันยายน 2026: Figma Starter MCP call limit ยัง active จึงยังไม่สามารถเขียน latest scope copy ลง canvas, ดึงภาพเพิ่ม หรือเซ็นแทน human visual owner ได้

## Research Accounting

- Pilot participants: 0
- Pilot sessions conducted: 0
- Study participants recruited: 0
- Participant sessions conducted: `0 sessions conducted`
- Synthetic participant results: none created

Automated link audits, screenshots and the builder's walkthrough are QA evidence, not participant evidence.
