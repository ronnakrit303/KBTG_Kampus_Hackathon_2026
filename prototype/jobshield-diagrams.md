# K PLUS JobShield — System Diagrams

อัปเดตล่าสุด: 6 กันยายน 2026
สถานะ: **V6 เป็น canonical repository diagram; Figma canvas ยังไม่ได้ Sync V6**

## Current V6

- Draw.io ที่แก้ไขได้: [jobshield-kplus-integration-benefits-v6.drawio](./jobshield-kplus-integration-benefits-v6.drawio)
- End-to-End Flow ภาษาไทย: [jobshield-flow-v6.md](./jobshield-flow-v6.md)
- Figma screen/state specification: [figma-flow-spec-v6.md](./figma-flow-spec-v6.md)
- Figma scope-sync handoff: [figma-scope-sync-v6.md](./figma-scope-sync-v6.md)

ภาพ Preview ที่ตรวจจากไฟล์ V6:

- [หน้า 1 — End-to-End Lifecycle](./jobshield-kplus-integration-benefits-v6-page-1.png)
- [หน้า 2 — Auto-Save and Benefit](./jobshield-kplus-integration-benefits-v6-page-2.png)
- [หน้า 3 — Withdraw and Protect](./jobshield-kplus-integration-benefits-v6-page-3.png)
- [หน้า 4 — Integration and Value Loop](./jobshield-kplus-integration-benefits-v6-page-4.png)

## วิธีอ่านตามกลุ่มผู้ชม

- ผู้บริหาร: อ่านหน้า 1 เพื่อเข้าใจแนวคิด แล้วไปหน้า 4 เพื่อดูความแตกต่าง ความเป็นไปได้ และคุณค่าทางธุรกิจ
- คนทั่วไปหรือผู้ใช้: อ่านหน้า 1 → หน้า 2 → หน้า 3 เพื่อเห็นตั้งแต่เริ่มออมจนถึงตอนนำเงินออก
- ทีม Product/Cyber Security: อ่านหน้า 3 และหน้า 4 เพื่อดูเงื่อนไขความเสี่ยง จุดพักคำสั่ง และ capability boundary

## โครงสร้าง 4 หน้า

1. **ภาพรวมสำหรับผู้บริหาร** — อธิบาย JobShield ในประโยคเดียว แล้วไล่จากเริ่มตั้งค่า ออมต่อเนื่อง เห็นความคืบหน้า จนถึงการปกป้องก่อนนำเงินออก
2. **การออมและสิทธิประโยชน์** — อธิบายการตั้งออมรายเดือน รอบออมสำเร็จ การผ่อนผัน ยอดอ้างอิง ระดับ 1/3/6 รอบ และสิทธิประโยชน์ที่ยังต้องผ่านการอนุมัติ
3. **การนำเงินออกและการป้องกัน** — แยกมาสคอตเตือนเรื่องการออมสำหรับรายการทั่วไป ออกจากคำเตือนจริงจังและการพักคำสั่งสำหรับรายการที่พบหลายสัญญาณเสี่ยง
4. **ระบบเดิม สิ่งที่เพิ่ม และคุณค่าธุรกิจ** — แสดง 3 ส่วนหลักของ K PLUS ที่นำมาใช้ ข้อเสนอใหม่ของ JobShield สิ่งที่ยังต้องยืนยัน และประโยชน์ที่เป็นสมมติฐาน

## คำอธิบายสัญลักษณ์

- เส้นทึบ = เส้นทางการทำงานหรือข้อมูลใน Core concept
- เส้นประ = ความสัมพันธ์เชิงสมมติฐานหรือสิ่งที่ยังต้องทดสอบ/อนุมัติ ไม่ใช่ผลลัพธ์รับรอง
- กรอบเส้นประสีแดง = internal dependency หรือ Business-dependent capability ที่ public sources ยังไม่ยืนยัน
- `Destination risk` = synthetic flag ที่ใช้จำลองสัญญาณจากระบบ Fraud Risk ฝั่งธนาคาร ทีมไม่ได้อ้างว่าเข้าถึงข้อมูลภายในจริง
- `Pending Instruction` = คำสั่งและยอดของรายการ High-Risk ที่พักไว้ก่อนส่งเข้าสู่ระบบโอน/PromptPay ไม่ได้ล็อกทั้งบัญชีหรือดึงเงินคืนหลังโอน
- `Dynamic Time Lock` = การกำหนดระยะพักตามระดับความเสี่ยงภายใน Cooling-off ไม่ใช่ฟีเจอร์แยก

## Scope Lock

- ใช้เงินก้อนเดียวชื่อ `เงินสำรองตั้งหลัก (Protected Reserve)` โดยไม่มี Stage branching
- ไม่มี Job Search Budget
- JobShield ไม่อ่านข้อความ อีเมล หรือ Resume
- Prototype ใช้ deterministic multi-signal policy และ synthetic data; ไม่มี AI/ML model จริง
- Core มี 3 Integration เท่านั้น: `K-ePocket`, `K PLUS Transaction + Bank-side Fraud Risk` และ `K PLUS Security & Fraud Response`
- K Point/คูปองเป็นเพียงตัวอย่างสิทธิประโยชน์ภายใต้เงื่อนไขธนาคาร ไม่ระบุคะแนน มูลค่า หรือรับรองสิทธิ
- เงินฝากที่เพิ่มขึ้นอาจสนับสนุนฐานเงินทุนและ Engagement แต่ไม่อ้างว่าเงินฝากทุกบาทเปลี่ยนเป็นสินเชื่อหรือกำไรโดยตรง

## Prior Snapshots

- V5: [jobshield-continuous-reserve-v5.drawio](./jobshield-continuous-reserve-v5.drawio)
- V4: [jobshield-integrated-lifecycle-v4.drawio](./jobshield-integrated-lifecycle-v4.drawio)
- V3: [jobshield-integrated-lifecycle-v3.drawio](./jobshield-integrated-lifecycle-v3.drawio)
- V2: [jobshield-integrated-lifecycle-v2.drawio](./jobshield-integrated-lifecycle-v2.drawio)
- Original: [jobshield-system-flow.drawio](./jobshield-system-flow.drawio)

ไฟล์ prior snapshots เก็บไว้เพื่อย้อนดูพัฒนาการของแนวคิดเท่านั้น ห้ามใช้เป็น source of truth สำหรับ Prototype หรือ Proposal รุ่นถัดไป

## Testing Status

- Pilot sessions conducted: `0`
- Participant sessions conducted: `0`
- Synthetic participant results: ไม่มี

ภาพ Preview และการตรวจโครงสร้างเป็น QA evidence ไม่ใช่ผลทดสอบกับผู้ใช้
