# JobShield V6 K PLUS Integration and Savings Benefits

Status: Complete
Created: 2026-09-06
Approval: User approved all todos on 2026-09-06

## Summary

ปรับ JobShield จาก V5 ให้ใช้ความสามารถสาธารณะที่ยืนยันได้ของ K PLUS เป็นฐาน ได้แก่ K-ePocket, เป้าหมายการออม, กลไก Schedule Transfer, ธุรกรรมโอน/จ่าย, การยืนยันตัวตน, การแจ้งเตือน และช่องทางรายงานภัย แล้วเพิ่มเฉพาะ orchestration ที่เป็นข้อเสนอใหม่: `Protected Reserve + goal-aware saving plan + context-aware pre-transfer protection` พร้อม Benefit Loop ที่ส่งเสริมการออมโดยไม่อ้างว่ารางวัลหรือผลตอบแทนได้รับอนุมัติแล้ว

การสื่อสารประโยชน์ต่อธนาคารจะใช้ถ้อยคำว่า “อาจช่วยเพิ่มยอดเงินฝากและความสัมพันธ์ระยะยาวกับลูกค้า” ไม่สรุปแบบหนึ่งต่อหนึ่งว่าเงินออมเพิ่มเท่ากับปล่อยกู้หรือกำไรเพิ่มเท่านั้น เพราะผลลัพธ์จริงขึ้นกับต้นทุนเงินฝาก สภาพคล่อง เงินกองทุน ความต้องการสินเชื่อ ความเสี่ยงเครดิต และ Business Approval

## Clarifying Questions

- [x] Benefit Ladder ควรให้ตามยอดเงินคงเหลือ หรือให้ตามพฤติกรรมออมสม่ำเสมอ/การถึงเป้าหมาย -> ผูกกับระยะเวลาที่ Auto-Routing สำเร็จต่อเนื่อง ไม่ผูกกับยอดเงินดิบหรือ manual saving
- [x] เดือนที่เงินไม่พอหรือผู้ใช้พัก Auto-Routing จะรีเซ็ต Benefit หรือใช้ grace/pause โดยไม่เพิ่มรอบ -> รักษาระดับเดิม ให้ Grace/Pause 1–2 รอบ และรอบที่ข้ามไม่นับเพิ่ม
- [x] Benefit ที่แสดงใน Core Prototype จะเป็นรูปแบบใด โดยต้องไม่สื่อว่า K Point/ดอกเบี้ยหรือสิทธิได้รับอนุมัติแล้ว -> ใช้ Tier เริ่มต้น/ต่อเนื่อง/มั่นคง พร้อม Progress; K Point/คูปองเป็นตัวอย่างภายใต้เงื่อนไขธนาคาร ไม่ระบุคะแนนหรือมูลค่า และไม่ใช้ดอกเบี้ยขั้นบันไดใน MVP
- [x] การถอนเงินสำรองที่จำเป็นและถูกต้องควรมีผลต่อ Benefit Tier หรือไม่ -> ไม่ลด Tier เดิม แต่พักการเลื่อน Tier จนยอดกลับถึง Checkpoint; รอบใหม่ต้อง Auto-Routing สำเร็จและมียอดสุทธิคงอยู่ถึงวันสรุปรอบ
- [x] Mascot Pop-up ควรปรากฏกับการนำเงินออกประเภทใด -> เงินสำรองมีไว้สำหรับเหตุฉุกเฉินและไม่ใช่กระเป๋าใช้จ่าย ทุกการนำออกจึงอยู่ใน 2 เส้นทาง: ไม่มี Fraud signal ใช้ Mascot Savings Nudge ที่ข้ามได้; มีหลาย Scam/Fraud signals ใช้คำเตือนจริงจัง ไม่มี Mascot และเข้าสู่ Cooling-off
- [x] ในเส้นทางไม่มี Fraud signal กรณีผู้ใช้ระบุว่าเป็นเหตุฉุกเฉินจริงควรใช้ถ้อยคำยืนยันแบบใด -> Mascot เตือนด้วยความเป็นห่วงว่าเป็นเงินฉุกเฉิน พร้อมปุ่ม `ใช้เงินสำรอง` และ `เก็บไว้ก่อน`; เมื่อยืนยันใช้ให้ส่งกำลังใจสั้น ๆ โดย copy เป็น Draft ที่เกลาภายหลังและไม่ถามซ้ำ
- [x] Benefit Tier เริ่มต้น/ต่อเนื่อง/มั่นคงควรเลื่อนเมื่อครบกี่รอบ Auto-Routing ที่เข้าเกณฑ์ -> 1 รอบ = เริ่มต้น, 3 รอบ/เดือน = ต่อเนื่อง, 6 รอบ/เดือน = มั่นคง; เป็น Prototype Rule ที่ต้องทดสอบและผ่าน Business Approval
- [x] ยอมรับการลด Business Claim จากเหตุ–ผลแบบรับรองว่าเงินออมเพิ่มทำให้ปล่อยกู้/กำไร/Benefit เพิ่ม เป็นวงจรคุณค่าที่ระบุว่าเป็นสมมติฐานและมีเงื่อนไขหรือไม่ -> ใช้ข้อความว่าอาจเพิ่มยอดเงินฝากที่มีเสถียรภาพและ Engagement ซึ่งสนับสนุนฐานเงินทุน/โอกาสสร้างคุณค่า; Benefit ขึ้นกับต้นทุน ความเสี่ยง กฎเกณฑ์ และ Business Approval

## File And Code References

- `docs/plans/2026-09-03-k-plus-track-3-concept-decision.md` - source of truth ของ V5 และขอบเขต Core Integration 3 ส่วน
- `proposal/content-skeleton.md` - non-final proposal content ที่ต้องปรับ benefit/value claims โดยไม่แตะ Final PDF เดิม
- `research/competitor-gap.md` - capability/novelty boundary เทียบของเดิมใน K PLUS
- `research/sources.md` - แหล่งทางการและ access date
- `prototype/figma-flow-spec-v5.md` - current screen/state contract; เก็บเป็น snapshot และสร้าง V6 แยก
- `prototype/figma-scope-sync-v5.md` - current Figma patch; canvas ยังไม่ถือว่าอัปเดตเป็น V6
- `prototype/protected-reserve-v5-spec.md` - current reserve, Auto-Routing และ withdrawal behavior
- `prototype/jobshield-continuous-reserve-v5.drawio` - current 3-page Draw.io; เก็บ V5 และสร้าง V6 แยก
- `prototype/jobshield-diagrams.md` - diagram index ที่ต้องชี้ V6 เป็น current หลังสร้างและตรวจแล้ว
- Official K PLUS/K-ePocket: https://www.kasikornbank.com/th/kplus/
- Official Schedule Transfer: https://www.kasikornbank.com/th/kplus/instruction/forward-transfers
- Official K Point: https://www.kasikornbank.com/th/personal/digital-banking/kplus-kpoint
- Official fraud-reporting hub: https://www.kasikornbank.com/th/personal/digital-banking/kbankcyberrisk/pages/index.aspx

## Plan Todos

- [x] ล็อก Benefit Ladder ให้ชัดว่าอะไรอยู่ใน Core Prototype และอะไรเป็น Future/Business-dependent concept
- [x] อัปเดต source-of-truth plan และ non-final content skeleton ให้ใช้ capability mapping ใหม่ โดยคง Core Integration เพียง 3 ส่วนเดิม
- [x] อัปเดต competitor/source notes: K-ePocket/goal/Schedule Transfer/K Point เป็น existing capability; direct sub-pocket routing, salary-event trigger, stop-at-cap และ reward entitlement เป็น internal/unconfirmed dependency
- [x] สร้าง `prototype/jobshield-flow-v6.md` อธิบาย End-to-End Flow ตั้งแต่ onboarding, Build & Benefit, Protect, Continue ด้วยภาษาไทยที่อ่านง่าย
- [x] สร้าง `prototype/figma-flow-spec-v6.md` และ V6 scope-sync patch โดยไม่แก้หรืออ้างว่า Figma canvas ถูกอัปเดตแล้ว
- [x] สร้าง Draw.io V6 แยกจาก V5 พร้อมหน้า Benefit Loop และความสัมพันธ์ต่อผู้ใช้/KBank โดยไม่ทำให้ Business claim ดูเป็นข้อเท็จจริงที่รับรองแล้ว
- [x] Render preview และตรวจ XML, broken connectors, overlapping lines/boxes, Thai glyphs และความสอดคล้องของคำ
- [x] ตรวจทุก artifact ว่าไม่มี Stage branching, Job Search Budget, AI/ML claim, guaranteed K Point/ดอกเบี้ย หรือ one-tap K-ePocket account-opening claim
- [x] คงสถานะการทดสอบจริงเป็น `0 pilot sessions conducted` และ `0 participant sessions conducted`; ไม่สร้างผลทดสอบสมมติ

## Grill-Me Outcome

- Transcript: [session-jobshield-v6-benefits-2026-09-06-20260906-165735.md](../../tmp/grill-me/session-jobshield-v6-benefits-2026-09-06-20260906-165735.md)
- Outcome: [outcome-jobshield-v6-benefits-2026-09-06-20260906-165735.md](../../tmp/grill-me/outcome-jobshield-v6-benefits-2026-09-06-20260906-165735.md)
- Summary: ล็อก Benefit จาก Auto-Routing ต่อเนื่อง, Grace/Pause, anti-reward-farming, Tier 1/3/6 เดือน, Mascot/Security separation และ Business Claim แบบมีเงื่อนไขแล้ว

## Build From Plan

- Ready to build: Yes — approved
- Selected todos: All after approval
- Execution notes: เก็บ V5 และ Final Proposal เดิมเป็น snapshot; V6 ใช้ deterministic rules/synthetic data และระบุ internal/business dependencies ทุกจุด

## Validation

- `python -X utf8 C:\Users\ASUS\.codex\skills\plan-mode\scripts\plan_artifact.py check docs\plans\2026-09-06-jobshield-v6-integration-benefits.md`
- `git diff --check`
- XML parse + unique node IDs + edge reference checks สำหรับ Draw.io V6
- Render Draw.io ทุกหน้าเป็น PNG และตรวจด้วยภาพจริง
- `rg` ตรวจคำต้องห้าม/คำเก่าและสถานะ testing 0/0

ผลการตรวจเมื่อ 6 กันยายน 2026:

- Draw.io V6 parse สำเร็จ 4 หน้า, duplicate node IDs ต่อหน้า = 0 และ broken source/target references = 0
- Render และตรวจภาพจริงครบ 4 หน้า; Thai glyphs อ่านได้และ connector routing ไม่ลากทับกล่องเนื้อหา
- `git diff --check` ผ่านหลังแก้ trailing whitespace
- คำเก่าหรือ capability ที่ห้าม claim ปรากฏเฉพาะข้อความปฏิเสธ/ขอบเขต ไม่ถูกใช้เป็น current behavior
- Figma canvas ยังไม่ถูก Sync V6 และสถานะทดสอบยังเป็น 0/0 ตามข้อเท็จจริง

## Risks

- Reward ตามยอดเงินอาจเอื้อผู้มีรายได้สูงและกดดันให้ First Jobbers กันเงินเกินความจำเป็น
- K Point, ดอกเบี้ยพิเศษ และสิทธิประโยชน์มีต้นทุน/ข้อกำกับและต้องผ่าน Product, Finance, Legal/Compliance approval
- Schedule Transfer สาธารณะยืนยันการตั้งรายการล่วงหน้า แต่ไม่ได้ยืนยัน event-triggered salary percentage, direct sub-pocket target หรือ stop-at-cap API
- การสื่อว่าเงินฝากเพิ่มทำให้กำไรเพิ่มโดยตรงเป็น claim ที่กว้างเกินหลักฐานและอาจถูกกรรมการทัก
- Benefit อาจทำให้แกน Track 3 อ่อนลง จึงต้องเป็น Supporting Loop ขณะที่ Risk-based Protection ยังเป็น Hero Flow
- การใช้ streak แบบรีเซ็ตทั้งหมดอาจลงโทษผู้มีรายได้ไม่สม่ำเสมอและผลักให้ผู้ใช้ฝืนออมจนเงินใช้ไม่พอ
- หาก Mascot ปรากฏทุกครั้ง รวมถึงบัญชีตนเองหรือบิลจำเป็น ผู้ใช้อาจเกิด Alert Fatigue และกดข้ามโดยไม่อ่าน
- หากใช้ Mascot แบบน่ารักใน High-Risk Scam flow อาจลดความจริงจังของคำเตือนภัยและทำให้ Savings Nudge ปะปนกับ Security Intervention
- การใช้ Mascot ตำหนิหรือชะลอเหตุฉุกเฉินจริงอาจสร้างความเครียดและ financial harm; copy ต้องเป็นกลางและข้ามได้ทันทีเมื่อไม่มี Fraud signal

## Approval

- Status: Approved all todos on 2026-09-06
