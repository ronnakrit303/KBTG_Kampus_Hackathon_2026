# K PLUS SafeStart — Pitch Proposal V.2

**สถานะ:** ร่าง Proposal สำหรับใช้ประกวด Track 3 (Cyber Security & Digital Trust)
**อัปเดตล่าสุด:** ผสานข้อมูล Research ด้านวินัยการออม (Wealth Gap), PDPA, Security Techniques, และ Cost Saving

---

## 1. Title & Value Proposition

**ชื่อโปรเจกต์:** K PLUS SafeStart (จัดเงินเป็น ปลอดภัยก่อนโอน)
**Value Proposition:** 
โซลูชัน 2-in-1 ที่ช่วยสะกิด (Nudge) ดึงเงินออมอัตโนมัติเพื่อสร้างเกราะทางการเงิน (Emergency Fund) และปกป้องเงินก้อนนั้นด้วยสถาปัตยกรรมความปลอดภัยระดับฮาร์ดแวร์ก่อนถูกหลอกโอน

---

## 2. Problem Statement (ปัญหาที่ต้องการแก้ไข)

First Jobber กำลังเผชิญความเปราะบางแบบซ้อนทับ (Double Vulnerability) ที่ทำให้ความเชื่อมั่นทางการเงินสั่นคลอน:
1. **Wealth Gap & ขาดวินัยการออม:** ข้อมูล ธปท. (ปี 2567) ระบุว่า 77.3% ของคนไทยมีเงินสำรองฉุกเฉินไม่ถึง 6 เดือน และ First Jobber กว่า 50% เริ่มเป็นหนี้ ทำให้ไม่มีเบาะรองรับเมื่อตกงานหรือเกิดเหตุไม่คาดฝัน
2. **Scam Target:** เมื่อมีความเปราะบางทางการเงิน คนกลุ่มนี้มักตกเป็นเหยื่อ Social Engineering ง่ายขึ้น (เช่น หลอกเป็น Recruiter เก็บค่าเข้าทำงาน/สัมมนา) และหากเผลอกดลิงก์อันตราย มัลแวร์ดูดเงิน (Remote Access Trojan) จะลอบทำงาน ซึ่งรหัส PIN 6 หลักเพียงอย่างเดียวไม่สามารถปกป้องเงินก้อนสุดท้ายนี้ได้

---

## 3. Target Users (กลุ่มเป้าหมาย)

- **First Jobbers อายุ 22–30 ปี:** ผู้ที่เพิ่งเริ่มทำงาน รับเงินเดือนก้อนแรก หรือกำลังหางาน ซึ่งต้องการทั้งตัวช่วยสร้างวินัยการออมและเกราะป้องกันกลโกงทางไซเบอร์

---

## 4. Proposed Solution (สิ่งที่นำเสนอ)

ระบบทำงานผ่าน 3 ขั้นตอน (Core Features สำหรับ Phase 1):

*   **Step 1: Auto-Vault (สร้างเงินออมฉุกเฉินอัตโนมัติ)**
    *   ใช้ทฤษฎี Behavioral Economics (Save More Tomorrow) ฟีเจอร์ **"Nudge & Sweep"** จะวิเคราะห์ฐานเงินเดือนเพื่อแนะนำสัดส่วนออม (เช่น 10%) และตั้งเป้า 3-6 เดือนของรายจ่าย
    *   ระบบตัดเงินอัตโนมัติเข้ากระเป๋า "Protected Savings" โดยมี Reward เป็นดอกเบี้ยพิเศษแบบจำกัดเพดาน (เช่น 1.5% สูงสุด 50,000 บาท) เพื่อจูงใจ
*   **Step 2: Biometric & Device Binding Shield (ปกป้องขั้นสุด)**
    *   การโอนเงินออกจาก Protected Savings ไม่สามารถใช้ PIN ปกติได้ แต่ถูกยกระดับความปลอดภัยด้วยการผูกเครื่อง **(Hardware-Backed Device Binding)** และบังคับสแกนใบหน้า **(FIDO2 Biometrics)** ป้องกันมัลแวร์รีโมทมากดโอน
*   **Step 3: AI Contextual Intervention & Graph Network (ตัดวงจรโอนออก)**
    *   หากผู้ใช้พยายามโอนเงินฉุกเฉินไปยังบัญชีต้องสงสัย ระบบจะตรวจจับด้วย **Graph Analysis** (หาเครือข่ายบัญชีม้า) 
    *   หากเสี่ยงสูง ระบบจะบังคับ **Cooling-off Period** (หน่วงเวลา) แสดงหน้าต่างเตือนแบบอธิบายเหตุผล (Explainable Warning) พร้อมปุ่ม 1-Click Panic Button ระงับบัญชีทันที

*(หมายเหตุ: ระบบ Reward แบบ K Point หรือ Gamification แจก Badge เก็บไว้พัฒนาต่อใน Phase 2 เพื่อโฟกัสโซลูชันหลักให้แข็งแกร่ง)*

---

## 5. Value Proposition (คุณค่าที่ส่งมอบ)

**สำหรับ First Jobbers (User):**
- เปลี่ยนความตั้งใจออมให้สำเร็จจริงโดยอัตโนมัติ และมั่นใจได้ 100% ว่าเงินฉุกเฉินก้อนสำคัญจะปลอดภัยจากมัลแวร์ดูดเงินและมิจฉาชีพ

**สำหรับ K PLUS (Business/Bank Value):**
- **CASA Growth:** ธนาคารได้ฐานเงินฝากออมทรัพย์ต้นทุนต่ำ (Sticky Deposits) ที่เติบโตอย่างมั่นคง ช่วยรักษา Net Interest Margin (NIM)
- **Massive Cost Saving:** งานวิจัยอุตสาหกรรม (LexisNexis) ชี้ว่าทุก $1 ของ Fraud ธนาคารแบกต้นทุนแฝงถึง $4.36 และต้นทุน Call Center ในการจัดการข้อพิพาทสูงถึง 1,200-1,700 บาท/สาย การใช้ SafeStart บล็อคความเสี่ยงตั้งแต่ต้นทาง จะลดภาระ Operation ของธนาคารได้มหาศาล

---

## 6. Track Perspective: Cyber Security & Digital Trust (Track 3)

K PLUS SafeStart นำเสนอการแก้ปัญหาผ่านเลนส์วิศวกรรมความปลอดภัยเชิงลึก:
- **Defense in Depth:** สร้างเลเยอร์ป้องกันซ้อนทับ ตั้งแต่อุปกรณ์ (TEE) -> สถาปัตยกรรมยืนยันตัวตน (FIDO2) -> และ AI ตรวจจับบัญชีม้า (Graph Network)
- **Privacy by Design (PDPA Compliance):** ระบบประเมินความเสี่ยงใช้เพียง Transaction Metadata และยึดหลัก Data Minimization ห้ามดักอ่าน SMS/Chat ของผู้ใช้โดยเด็ดขาด ธุรกรรมทั้งหมดอยู่ภายใต้ Explicit Consent ตามพ.ร.บ. คุ้มครองข้อมูลส่วนบุคคล
- **Resilience vs. Friction:** วางสมดุลไม่ให้ระบบจับผิด (False Positive) จนผู้ใช้เดือดร้อน โดยอนุญาตทางผ่าน (Break-glass) สำหรับบิลประจำที่ verified แล้ว 

---
*ข้อมูลสนับสนุนทั้งหมดอ้างอิงจาก Research สถิติของ ธปท. ปี 2567, LexisNexis Risk Solutions, และทฤษฎี Nudge Theory*

