# K PLUS JobShield — Pitch Proposal V.4

**สถานะ:** ร่าง Proposal สำหรับ Track 3 (Cyber Security & Digital Trust)
**อัปเดตล่าสุด:** คืนน้ำหนักให้แกนหลักของ Cyber Security (จาก V.1) โดยนำเรื่องการออมและ PDPA/Cost Saving มาเสริมเป็นฐานที่ทำให้ระบบสมบูรณ์ขึ้น

---

## 1. Title & Value Proposition

**ชื่อโปรเจกต์:** K PLUS JobShield 
**Value Proposition:** 
ปกป้อง “เงินสำรองก่อนเงินเดือนแรก” จากมิจฉาชีพหางาน ด้วย Career Mode ที่เชื่อมบริบทการออม (Fund Source) สัญญาณธุรกรรม และระบบแทรกแซงความเสี่ยงระดับฮาร์ดแวร์ก่อนที่เงินจะถูกโอนออกไป

---

## 2. Problem Statement (ปัญหาที่ต้องแก้)

มิจฉาชีพมักอาศัยความเปราะบางของกลุ่มเริ่มทำงาน ปลอมเป็นบริษัท (Fake Recruiter) เพื่อหลอกเก็บค่าสมัครหรือค่าอุปกรณ์ก่อนเริ่มงาน 
ปัญหาหลักทางไซเบอร์คือ ธุรกรรมเหล่านี้เป็น **Authorized Push Payment (APP)** ที่ผู้ใช้ตกอยู่ใต้ Social Engineering และเป็นผู้กดยืนยันการโอนเอง ทำให้รหัส PIN และระบบยืนยันตัวตนปกติไม่สามารถป้องกันได้ ในขณะที่คำเตือนทั่วไปของธนาคารก็ไม่มีบริบทเพียงพอที่จะรู้ว่า "เงินก้อนนี้คือเงินสำรองก้อนสุดท้ายในชีวิต" (สถิติ ธปท. ชี้ว่า 77.3% ของคนไทยขาดเงินสำรองฉุกเฉิน)

---

## 3. Target Users (กลุ่มเป้าหมาย)

- **First Jobbers อายุ 22–30 ปี:** ผู้ที่กำลังสมัครงาน รอเริ่มงาน หรือรอเงินเดือนแรก ที่เลือกเปิด *Career Mode* ด้วยตนเอง (Opt-in) โดยปัญหาคือบริบทของการเริ่มงาน (Transitional Context) ไม่ใช่การเหมารวมว่ากลุ่มนี้มีความรู้ต่ำ

---

## 4. Proposed Solution (3 ขั้นตอนก่อนเงินออก)

บูรณาการ K-ePocket และ Fraud Controls เพื่อปกป้องเงินสำรอง:

*   **Step 1: Prepare (จัดเตรียม & ออม)**
    *   ผู้ใช้เปิด Career Mode ระบบใช้ *Nudge Theory* ดึงเงินแบ่งเข้ากระเป๋า **"เงินสำรองก่อนเงินเดือนแรก"** อัตโนมัติ (แยกออกจาก Job Search Budget ทั่วไป) พร้อมให้ดอกเบี้ยจำกัดเพดานเป็น Reward เพื่อจูงใจให้ล็อคเงิน
*   **Step 2: Detect (ตรวจจับด้วย Multi-Signal)**
    *   ก่อนโอน ระบบจะประเมิน **Multi-signal Policy**: [1. แหล่งเงินคือกระเป๋าสำรอง] + [2. ผู้รับใหม่] + [3. ยอดโอนสะสม] + [4. Destination Risk จาก **Graph Analysis** ตรวจหาเครือข่ายบัญชีม้า]
    *   ทำงานภายใต้ **Privacy by Design (PDPA)** ไม่อ่านข้อความส่วนตัว แต่อาศัย Transaction Metadata 
*   **Step 3: Intervene (แทรกแซงตามความเสี่ยง)**
    *   ปรับ Friction ตามความเสี่ยง (Risk-based Control):
        - *Low Risk:* ธุรกรรมปกติ
        - *Medium Risk:* เตือนแบบระบุเหตุผล (Explainable Warning)
        - *High Risk:* บังคับเข้า **Cooling-off Period** (พักคำสั่งก่อนส่งเข้า PromptPay) ล็อคการปลดด้วย **FIDO2 Biometrics & Hardware-Backed Device Binding** ป้องกันมัลแวร์รีโมท พร้อมแสดงปุ่ม Pause & Verify / Cancel

---

## 5. Value Proposition (คุณค่าที่ส่งมอบ)

**สำหรับ First Jobbers:**
- ปกป้องเงินก้อนสำคัญ ณ จุดตัดสินใจก่อนโอน อธิบายได้ว่าเตือนเพราะอะไร (เช่น "ผู้รับใหม่ + ดึงเงินสำรองมาจ่าย") และยังมีทางผ่านสำหรับบิลฉุกเฉินที่ปลอดภัย

**สำหรับ K PLUS (Business Value):**
- **Massive Cost Saving:** งานวิจัยอุตสาหกรรม (LexisNexis) ชี้ว่า 1 ดอลลาร์ของ Fraud ธนาคารแบกต้นทุนแฝงการจัดการถึง $4.36 และต้นทุน Call Center เฉลี่ย 1,200-1,700 บาท/สาย JobShield เปลี่ยนการแก้ปัญหาจากปลายทางมาเป็น Pre-loss Intervention ลดเคส Dispute ได้มหาศาล พร้อมเพิ่มฐานเงินฝากออมทรัพย์ (CASA)

---

## 6. Track Perspective: Cyber Security & Digital Trust (Track 3)

รับมือ Authorized Push Payment (APP) ด้วย **Defense in Depth** ก่อนเงินออก:
- **Explainable Policy & Privacy:** กฎประเมินความเสี่ยงที่ผู้ใช้เข้าใจได้ ทำงานบน Data Minimization ตามกฎหมาย โดยไม่ต้องอ่านข้อมูลส่วนตัวเป็นค่าเริ่มต้น
- **Evasion-aware:** ประเมินยอดโอนสะสม (Cumulative) เพื่อรับมือกรณีมิจฉาชีพหลอกให้แบ่งโอนยอดเล็ก (Split amounts)
- **Hardware-Level Defense:** ยกระดับการอนุมัติเงินจากกระเป๋าสำรอง ด้วยชิปความปลอดภัยในเครื่องและชีวมิติ ป้องกันการควบคุมระยะไกล (RAT)
- *(Prototype Boundary: ใช้ Synthetic Data และ Deterministic Rules ในการจำลองสัญญาณ Destination Risk ระยะ Cooling-off จริงต้องผ่าน Policy Validation ของธนาคาร)*

