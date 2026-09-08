# K PLUS JobShield — Figma Flow Specification V6

วันที่: 6 กันยายน 2026  
สถานะ: V6 SPEC READY — NOT APPLIED TO FIGMA CANVAS  
Target: https://www.figma.com/design/5uoF2s6cq2JMGRFfwmdpc2

สถานะทดสอบ: 0 pilot sessions conducted; 0 participant sessions conducted

## Scope

- ไม่มี Career Stage และไม่มี Job Search Budget
- ใช้ K-ePocket เงินสำรองตั้งหลักก้อนเดียว
- ถ้ายังไม่มีบัญชี K-ePocket ให้ hand off ไปขั้นตอนเปิดบัญชีทางการ ไม่ใช้คำว่า One-tap
- MVP Auto-Routing ใช้จำนวนคงที่และวันที่กำหนด โดยนำ Schedule Transfer มาเป็นฐาน
- เปอร์เซ็นต์ใช้คำนวณจำนวนคงที่จากรายได้ประมาณการที่ผู้ใช้กรอก ไม่ใช่ salary-event trigger
- Benefit Tier จาก qualified rounds ที่ 1/3/6 เดือน พร้อม Grace/Pause และ Checkpoint
- ทุกการนำเงินออกมี 2 user-facing routes: Mascot Savings Nudge หรือ Serious Security Warning/Cooling-off
- Core มี 3 integrations เดิม
- Prototype ใช้ deterministic policy + synthetic data ไม่มี AI/ML model

## Components

| Component | Variants |
|---|---|
| ProtectedReserveCard | empty / building / checkpoint-hold / goal-reached / after-withdrawal |
| PocketSelector | existing sub-pocket / create sub-pocket / open K-ePocket handoff |
| SavingsPlanCard | off / review / active / grace / paused / goal-reached |
| BenefitTierCard | locked / เริ่มต้น / ต่อเนื่อง / มั่นคง / progress-held |
| BenefitPreview | placeholder / business-dependent |
| QualifiedRoundRow | success / grace / failed / ineligible-withdrawn |
| WithdrawalImpact | amount / remaining balance / estimated months |
| MascotNudge | concerned / supportive-success |
| RiskReasonChip | new payee / protected reserve / repetition / destination / job payment |
| SeriousRiskBanner | contextual High Risk |
| PendingInstruction | held / verifying / eligible / cancelled |
| PrototypeTag | existing / proposed / assumption / synthetic / business-dependent |

## Global Rules

- Auto-Routing consent ไม่ถูกเลือกไว้ล่วงหน้า และปรับ/พัก/ปิดได้
- Auto-Routing สำเร็จแสดง Quiet Receipt ไม่แสดง Scam warning
- รอบพักหรือเงินไม่พอไม่เพิ่ม Progress และไม่ลด Tier
- Grace/Pause ใช้ได้ 1–2 รอบใน Prototype
- ถอนต่ำกว่า Checkpoint ไม่ลด Tier แต่พัก progress ไป Tier ถัดไป
- Mascot ใช้เฉพาะเส้นทางที่ไม่เข้า High-Risk combination
- Security Warning ใช้ข้อความจริงจัง ไม่มี Mascot
- Pause & Verify สร้าง Pending Instruction แบบ idempotent ก่อน PromptPay
- ไม่มีหน้าจอใดรับรองสิทธิ K Point/คูปอง หรืออ้าง direct profit/lending impact

## Flow S — Set Up

| ID | Screen | Interaction | Destination |
|---|---|---|---|
| S00 | JobShield introduction | เริ่มตั้งค่า | S01 |
| S01 | ตรวจบัญชี K-ePocket | มีบัญชี / ยังไม่มี | S02A/S01N |
| S01N | Official K-ePocket opening handoff | ไปเปิดบัญชี / ไว้ภายหลัง | external-return/S00 |
| S02A | เลือก Pocket เดิมหรือสร้าง Pocket ย่อยใหม่ | เลือกหรือสร้าง | S02 |
| S02 | ค่าใช้จ่ายจำเป็นต่อเดือน | กรอกจำนวน | S03 |
| S03 | เป้าหมาย 3/6 เดือน/กำหนดเอง | เลือกเป้าหมาย | S04 |
| S04 | ยอดเริ่มต้น | เติมตอนนี้/เริ่ม 0 บาท | A01 |

Copy:

- S00: สร้างเงินสำรองให้ต่อเนื่อง และเพิ่มเกราะก่อนนำออก
- Privacy: ไม่อ่านข้อความ อีเมล หรือ Resume
- S01N: เปิดบัญชี K-ePocket ตามขั้นตอนของธนาคาร แล้วกลับมาตั้งค่า JobShield
- S03 fixture: 15,000 บาท × 3 เดือน = 45,000 บาท

## Flow A — Auto-Save Plan

| ID | Screen | Interaction | Destination |
|---|---|---|---|
| A01 | เลือกจำนวนคงที่หรือคำนวณจากเปอร์เซ็นต์ | กรอกจำนวน/รายได้ประมาณการ | A02 |
| A02 | เลือกวันที่และบัญชีต้นทาง | เลือกค่า | A03 |
| A03 | Review + explicit consent | ยืนยัน/แก้ไข/ไว้ภายหลัง | A04/A01/S07 |
| A04 | Plan active | ดูแผน | S07 |
| A05 | Synthetic scheduled event | success/insufficient/paused | A06/A07 |
| A06 | Quiet Receipt | ปิด | B01 |
| A07 | Grace/Pause status | ดูผล/แก้แผน | S07/A01 |

ตัวอย่าง 10% ของรายได้ประมาณการ 25,000 บาท แปลงเป็นรายการคงที่ 2,500 บาทต่อเดือน ห้ามเขียนว่า ตรวจพบเงินเดือน หรือ หัก 10% ของเงินเข้าจริง

## Flow B — Benefit Progress

| ID | Screen | Interaction | Destination |
|---|---|---|---|
| B01 | Checkpoint check | synthetic eligible/ineligible | B02/B04 |
| B02 | Qualified round counted | ดู Tier | B03 |
| B03 | Tier progress | กลับ Dashboard | S07 |
| B04 | Progress held | เติมกลับ/ดูเหตุผล | S07 |

Prototype rules:

- รอบเข้าเกณฑ์เมื่อ scheduled transfer สำเร็จและยอดสุทธิคงอยู่ถึงวันสรุปรอบ
- 1 รอบ = เริ่มต้น, 3 รอบ = ต่อเนื่อง, 6 รอบ = มั่นคง
- Tier เดิมไม่ลดจาก withdrawal หรือ grace
- Progress ไป Tier ถัดไปพักจนกลับถึง Checkpoint
- BenefitPreview ใช้ข้อความ ตัวอย่างสิทธิประโยชน์ภายใต้เงื่อนไขธนาคาร เท่านั้น

## Screen S07 — Reserve Dashboard

แสดงยอด/เป้าหมาย, Estimated months covered, Auto-Routing state/รอบถัดไป, Benefit Tier/progress, Grace คงเหลือ, Checkpoint hold และปุ่มเติมเงิน/แก้แผน/พักแผน/นำเงินออก

## Flow W — Withdraw And Protect

| ID | Screen | Interaction | Destination |
|---|---|---|---|
| W01 | จำนวนเงิน ปลายทาง วัตถุประสงค์กว้าง ๆ | ตรวจสอบ | W02 |
| W02 | Multi-signal policy | not High / High | W03/H05 |
| W03 | Mascot Savings Nudge | ใช้เงินสำรอง/เก็บไว้ก่อน | W04/S07 |
| W04 | Normal transfer confirmation | ยืนยัน | W05 |
| W05 | Transfer success + supportive Mascot | เสร็จสิ้น | T00 |

W03 Draft copy:

ขอชวนคิดอีกครั้งนะ เงินก้อนนี้คือเงินสำรองสำหรับเหตุฉุกเฉิน คุณยังต้องการใช้เงินก้อนนี้ใช่ไหม?

แสดงยอดที่จะใช้ ยอดหลังรายการ และจำนวนเดือนที่เหลือโดยประมาณ

W05 Draft copy:

รับทราบ ขอให้ทุกอย่างผ่านไปได้ด้วยดีนะ

Savings Nudge กดข้ามได้ครั้งเดียว ไม่ถามซ้ำ ไม่สร้าง Pending Instruction และไม่ใช้คำว่า Scam

## Flow H — High-Risk Fake Recruiter

Synthetic fixture: 7,900 บาทจากเงินสำรองตั้งหลัก ไปบัญชีบุคคลใหม่ สำหรับค่าอุปกรณ์ก่อนเริ่มงาน พร้อม repetition หรือ simulated destination risk

| ID | Screen | Interaction | Destination |
|---|---|---|---|
| H01 | New-payee transfer | ถัดไป | H02 |
| H02 | เลือกเงินสำรองตั้งหลัก | เลือก | H03 |
| H03 | Review | ตรวจสอบก่อนโอน | H04 |
| H04 | Broad context question | ตอบหรือข้าม | H05 |
| H05 | Serious contextual warning; no Mascot | Pause & Verify / Cancel & Report | H06/H09 |
| H06 | Pending Instruction ก่อน PromptPay | ตรวจสอบ | H07 |
| H07 | Independent verification guidance | จำลองผล | H08 |
| H08 | Reassessment | verified/unclear | H10/H09 |
| H09 | Cancel & Report | ยืนยัน consent | H11 |
| H10 | Final deliberate confirmation | ทำต่อ/ยกเลิก | H12/H11 |
| H11 | Cancelled; money not sent | กลับ Dashboard | S07 |
| H12 | Transfer complete — simulation | จบ | T00 |

H05 แสดงเหตุผลไม่เกิน 3 ข้อ: ผู้รับใหม่, ใช้เงินสำรองตั้งหลัก, และเกี่ยวข้องกับค่าใช้จ่ายก่อนเริ่มงาน

## Link Map

S00 → S01 → S02A → S02 → S03 → S04 → A01 → A02 → A03 → A04 → S07

S01 → S01N → official opening → S02A

A05 success → A06 → B01 → B02/B04 → B03/S07

S07 → W01 → W02 → W03/H05

W03 → W04/S07 → W05

H05 → H06/H09 → H07 → H08 → H10/H09 → H12/H11

## Test Start Points

- START-SETUP → S00
- START-AUTO-SAVE → A01
- START-AUTO-SUCCESS → A05 success
- START-GRACE → A05 insufficient
- START-BENEFIT-1/3/6 → B03 แต่ละ Tier
- START-CHECKPOINT-HOLD → B04
- START-WITHDRAW-NUDGE → W01 not High
- START-HIGH-CONTEXTUAL → H01
- START-HIGH-GENERIC → generic-warning matched fixture

## Build And Pilot Gate

- Apply V6 screens/copy to Figma canvas
- Verify links and start points in Present mode
- ตรวจ Thai overflow, contrast, focus order, text scaling และ touch targets
- Visual owner sign-off เป็น READY FOR PILOT
- Pilot จริง 1 คนก่อน participant sessions 5–8 คน

ห้ามเปลี่ยนสถานะเป็น tested จนกว่าจะเกิด session จริง ปัจจุบันยังเป็น 0 pilot sessions conducted และ 0 participant sessions conducted
