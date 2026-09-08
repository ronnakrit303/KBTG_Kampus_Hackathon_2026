# K PLUS JobShield — V5 Synthetic Risk Policy

สถานะ: Working prototype specification — 6 กันยายน 2026

ขอบเขต: deterministic policy ด้วยข้อมูลสมมติทั้งหมด

ไม่ใช่: KBank production rule, fraud score, ML model, accuracy claim หรือผลทดสอบผู้ใช้

## Policy Goal

ใช้หลายสัญญาณร่วมกันเพื่อเลือก friction ก่อนโอน โดยรักษาหลักต่อไปนี้:

1. การใช้ `เงินสำรองตั้งหลัก` เพียงอย่างเดียวไม่ทำให้รายการเป็น Scam หรือ High Risk
2. คำตอบเรื่องวัตถุประสงค์ช่วยเพิ่มบริบท แต่ไม่มีสิทธิ์ลดระดับความเสี่ยงจากสัญญาณอื่น
3. ระบบพิจารณาการแบ่งยอดและยอดโอนสะสม ไม่ดูเฉพาะรายการล่าสุด
4. บัญชีตนเอง/verified biller ที่ไม่มี risk conflict ต้องเข้าถึงได้ตามปกติ
5. Savings Nudge เป็น self-control prompt ที่กดข้ามได้ ไม่ใช่ Fraud/Scam Intervention

## Synthetic Inputs

| Field | Values | Boundary |
|---|---|---|
| `jobshield_enabled` | on / off | user opt-in state |
| `fund_source` | บัญชีหลัก / เงินสำรองตั้งหลัก | user-designated K-ePocket context |
| `destination_class` | own / verified biller / known / new unverified | derived or simulated fixture |
| `payee_history` | first-seen / seen-before | synthetic transaction history |
| `purpose_answer` | essential / job fee / emergency / general / other / skipped | weak user-provided signal |
| `transfer_pattern` | single / repeated / split-cumulative | synthetic transaction history |
| `destination_risk` | neutral / elevated / high | simulated bank-side flag |
| `amount` | synthetic THB | not a production threshold |

ระบบไม่ใช้ career stage, อายุ, Resume, ข้อความ หรืออีเมลเป็น risk input

## Risk Actions

| Tier | Action | User authority |
|---|---|---|
| Baseline | JobShield-specific policy ไม่ทำงาน | existing bank controls remain |
| Low | normal transfer flow | normal confirmation |
| Medium | contextual warning + deliberate confirmation | pause or continue without High cooling-off |
| High | Pending Instruction before PromptPay + contextual warning + risk-based Cooling-off | cancel/report or continue only after agreed condition |
| Savings Nudge | dismissible reminder for general spending | continue immediately; no Pending Instruction |

## Deterministic Rule Precedence

ประเมินทุกกฎและใช้ผลที่เข้มที่สุด:

| Rule | Condition | Result |
|---|---|---|
| P0 | JobShield off and no simulated bank-risk outcome | Baseline |
| P1 | destination risk = high | High |
| P2 | new unverified + protected reserve + job fee/repeated/elevated destination risk | High |
| P3 | new unverified + split-cumulative + JobShield on/elevated destination risk | High |
| P4 | JobShield on + new unverified, but no High combination | Medium |
| P5 | own account/verified biller + neutral destination risk | Low |
| P6 | known payee + neutral risk + general spending from reserve | Low + Savings Nudge |
| P7 | other JobShield-on case without sufficient risk signals | Low |

ไม่มี fixed score, model weight, threshold หรือ cooling-off duration ใน Prototype

## Boundary Scenarios

| ID | Scenario | Synthetic inputs | Rule | Expected result |
|---|---|---|---|---|
| BC1-A | Fake Recruiter ขอค่าอุปกรณ์ก่อนเริ่มงาน | reserve; ฿7,900; new unverified; first-seen; job fee; elevated risk | P2 | High; Pending Instruction before PromptPay; Pause & Verify / Cancel & Report |
| BC1-B | Fake Recruiter ใช้ปลายทางที่มี high flag | reserve; ฿3,500; new unverified; purpose=other; high risk | P1 | High; purpose `other` does not downgrade |
| BC2-A | จ่ายค่าเช่าผ่าน verified biller | reserve; ฿4,500; essential; neutral risk | P5 | Low; normal flow without Scam warning |
| BC2-B | ค่าใช้จ่ายจำเป็นไปผู้รับใหม่ | reserve; ฿900; new unverified; essential; neutral risk | P4 | Medium; non-accusatory warning and deliberate confirmation |
| BC3-A | โอนไปบัญชีตนเอง | reserve; ฿6,000; own account; neutral risk | P5 | Low; no fixed delay |
| BC3-B | จ่ายค่ารักษาผ่าน verified biller | reserve; ฿4,500; emergency; neutral risk | P5 | Low; normal access |
| BC3-C | ซื้อของทั่วไปให้ผู้รับเดิม | reserve; ฿3,500; known payee; general; neutral risk | P6 | dismissible Savings Nudge; no fraud finding |
| BC4-A | Attacker coach ให้ตอบ purpose ผิด | reserve; new unverified; other; repeated; elevated risk | P2 | remains High |
| BC4-B | Attacker แบ่งยอด | reserve; 3 × ฿1,500; new unverified; split-cumulative; elevated risk | P3 | remains High after aggregation |
| BASE-1 | JobShield off | main account; new unverified; neutral risk | P0 | baseline bank controls only |

## Warning Fixtures

### Medium

- Heading: `ตรวจสอบผู้รับก่อนโอน`
- Reasons: first-seen payee / unverified payment channel
- Actions: `Pause & Verify` / `ยืนยันต่อ`
- ห้ามเรียกผู้รับว่าเป็นมิจฉาชีพเมื่อหลักฐานไม่พอ

### High

- Heading: `พักรายการนี้และตรวจสอบก่อน`
- Reasons สูงสุดสามข้อ: new payee / protected reserve / repeated transfer / destination risk / job-payment context
- Impact: แสดงยอดที่กำลังออกและยอดเงินสำรองตั้งหลักหลังทำรายการ
- Actions: `Pause & Verify` / `Cancel/Report`
- State: `ยังไม่ส่งเข้าสู่ PromptPay`

### Savings Nudge

- Heading: `ขอชวนคิดอีกครั้งก่อนใช้เงินก้อนนี้`
- Actions: `เก็บเงินไว้ก่อน` / `ยังต้องการใช้เงิน`
- ห้ามสร้าง Pending Instruction หรือใช้ข้อความ Scam

## Pass Conditions

- BC1 and BC4 remain High despite false purpose or split transfers
- BC2-A and BC3 complete without High friction
- reserve source alone never creates High
- Savings Nudge never routes to Cooling-off
- repeated taps cannot duplicate a Pending Instruction
- every completed High transfer passes the simulated condition after H06; no direct H05-to-success link
