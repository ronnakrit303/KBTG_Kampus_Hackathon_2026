# Human-Centered Security for K PLUS JobShield

วันที่ทบทวนหลักฐาน: 19 กันยายน 2026  
สถานะ: Research note — ใช้กำหนดกรอบปัญหาและออกแบบ Prototype ไม่ใช่ผลทดสอบประสิทธิผลของ JobShield

## ข้อสรุปสำหรับผู้บริหาร

ประโยคว่า **“จุดอ่อนอยู่ที่ User ไม่ใช่ระบบ” ไม่แม่นยำพอและมีความเสี่ยงต่อการโทษเหยื่อ** กรอบที่เหมาะสมกว่าคือ:

> Scam เป็นความเสี่ยงแบบ Sociotechnical: ผู้โจมตีใช้บริบท ความไว้วางใจ ความเร่งด่วน และแรงกดดัน ทำให้ผู้ใช้ที่ยืนยันตัวตนถูกต้องอนุมัติธุรกรรมภายใต้ข้อมูลเท็จ ขณะที่ระบบชำระเงินอาจทำงานถูกต้องตามคำสั่งทุกขั้นตอน

ดังนั้นปัญหาไม่ใช่เพียง `Identity ถูกขโมย` แต่เป็นช่องว่างระหว่าง:

- `Authentication`: คนที่ทำรายการเป็นเจ้าของบัญชีจริงหรือไม่
- `Authorization`: เจ้าของบัญชีกดยืนยันรายการจริงหรือไม่
- `Intent Integrity`: การตัดสินใจนั้นตั้งอยู่บนข้อมูลจริง หรือเกิดจากการปลอมตัวและ Social Engineering

JobShield มุ่งปิดช่องว่างข้อที่สาม โดยช่วยให้ผู้ใช้หยุด ตรวจสอบ และยกเลิกได้ก่อนเงินออก โดยไม่แทนที่ระบบยืนยันตัวตนและ Fraud Analytics เดิมของธนาคาร

## 1. Threat Model: ระบบไม่ถูกเจาะ แต่ผู้ใช้ยังเสียเงินได้อย่างไร

```text
Fake recruiter สร้างเรื่องที่สอดคล้องกับสิ่งที่ผู้ใช้กำลังรอ
        ↓
แอบอ้างบริษัทจริง + สร้างความเร่งด่วน + ขอค่าใช้จ่ายก่อนเริ่มงาน
        ↓
ผู้ใช้เชื่อว่าปลายทางและวัตถุประสงค์ถูกต้อง
        ↓
ผู้ใช้เปิด K PLUS ด้วยอุปกรณ์และตัวตนจริง
        ↓
PIN/Biometrics ผ่าน และผู้ใช้กดยืนยันเอง
        ↓
ระบบชำระเงินดำเนินการถูกต้อง แต่ Intent ถูก Social Engineering
        ↓
เงินถูกส่งไปยังบัญชีของผู้โจมตีหรือบัญชีม้า
```

Basel Committee อธิบาย digital fraud กลุ่มหนึ่งว่าเป็นกรณีที่ผู้จ่ายถูกหลอกให้ส่งคำสั่งชำระเงินโดยสุจริตไปยังบัญชีที่ตนเชื่อว่าเป็นผู้รับที่ถูกต้อง นี่คือเหตุผลที่การยืนยันตัวตนเพียงอย่างเดียวไม่สามารถแก้ Scam ประเภทนี้ได้ทั้งหมด [BIS/BCBS, 2023](https://www.bis.org/publications/202311-consultation-digital-fraud-and-banking-supervisory-and-financial-stability-implications.pdf)

## 2. เหตุใดผู้ใช้จึงทำตาม ทั้งที่ไม่ได้ขาดความรู้หรือความฉลาด

### 2.1 Premise Alignment — เรื่องหลอกตรงกับสิ่งที่ผู้ใช้กำลังรอ

NIST Phish Scale พบว่า เมื่อเนื้อเรื่องของข้อความสอดคล้องกับบริบทงานหรือสถานการณ์ของผู้รับ การตรวจจับ Phishing จะยากขึ้น แม้ข้อความเดียวกันอาจดูน่าสงสัยสำหรับผู้ที่ไม่มีบริบทนั้น [Steves, Greene & Theofanos, 2020](https://csrc.nist.gov/pubs/journal/2020/09/categorizing-human-phishing-detection-difficulty-a/final)

ผลต่อ First Jobbers: ผู้ที่เพิ่งส่ง Resume หลายแห่งย่อมคาดหวังการติดต่อจากบุคคลที่ยังไม่รู้จัก ข้อความ “ผ่านรอบแรก กรุณาชำระค่าอุปกรณ์/อบรมเพื่อยืนยันสิทธิ์” จึงสอดคล้องกับเป้าหมายปัจจุบันมากกว่าข้อความหลอกแบบทั่วไป

ข้อจำกัด: งาน NIST ศึกษา Phishing และการฝึกในองค์กร ไม่ได้พิสูจน์ว่า First Jobbers ไทยมีอัตราตกเป็นเหยื่อสูงกว่ากลุ่มอื่น

### 2.2 Scarcity และ Need State — ความต้องการทำให้ข้อเสนอดูน่าสนใจขึ้น

รายงานที่ Payment Systems Regulator (PSR) มอบหมายให้นักวิจัยอิสระจัดทำ ระบุความเปราะบางสำคัญของ APP Fraud ได้แก่ scarcity, willingness to trust, representativeness heuristic และการถูกเร่งให้ตัดสินใจด้วย System 1 [PSR/Axiom Economics, 2025](https://www.psr.org.uk/media/efpdiwpk/using-behavioural-economics-to-understand-and-prevent-app-fraud.pdf)

ผลต่อ First Jobbers: ความต้องการงาน รายได้ และความมั่นคงไม่ได้ทำให้ผู้ใช้ “ไม่ฉลาด” แต่ทำให้ข้อเสนอที่ดูเป็นโอกาสหายากมีน้ำหนักทางอารมณ์สูงขึ้น

### 2.3 Authority และ Trust — ผู้โจมตีขอยืมความน่าเชื่อถือจากบริษัทจริง

งานทดลอง/แบบสอบถามของ Fischer, Lea และ Evans พบความสัมพันธ์ระหว่าง Scam compliance กับการตอบสนองต่อสิ่งจูงใจมูลค่าสูง อารมณ์เชิงบวก เครื่องหมายของผู้มีอำนาจ และความมั่นใจของผู้ตอบ [Fischer, Lea & Evans, 2013](https://doi.org/10.1111/jasp.12158)

หน้าเตือนภัยของ KBank ระบุรูปแบบที่ผู้โจมตีอ้างองค์กรที่มีชื่อเสียง แล้วขอเงินประกัน ค่าสมัคร ค่าอัปเกรดงาน หรือค่าดำเนินการเบิกจ่าย และอาจหลอกให้โอนซ้ำ [KBank Job Scam](https://www.kasikornbank.com/th/personal/digital-banking/kbankcyberrisk/pages/jobscam.aspx)

### 2.4 Representativeness — รายละเอียดที่ดูมืออาชีพถูกตีความว่าเป็นของจริง

โลโก้ ชื่อตำแหน่ง เอกสาร Offer ตารางอบรม หรือโปรไฟล์ที่ดูสมจริงอาจทำให้สิ่งหลอก “มีหน้าตาเหมือน” กระบวนการรับสมัครจริง รายงาน PSR เตือนว่ามนุษย์อาจตีความรายละเอียดและ Social Proof ว่าเป็นหลักฐานความแท้ ทั้งที่รายละเอียดเหล่านั้นสามารถสร้างขึ้นได้

### 2.5 Urgency และ Hot State — เวลาน้อยลดโอกาสตรวจสอบ

PSR อธิบายว่าแรงกดดันให้รีบเลือกกระตุ้นการคิดแบบรวดเร็วหรือ System 1 การชะลอการตัดสินใจหรือเพิ่มเวลาสำหรับ Reflection/Verification อาจช่วยพาผู้ใช้กลับสู่สภาวะไตร่ตรองมากขึ้น

### 2.6 Commitment — เมื่อเริ่มทำตามแล้ว การหยุดยากขึ้น

การวิเคราะห์บทสนทนาระหว่างผู้หลอกและเหยื่อพบกระบวนการสร้างความสัมพันธ์ วางความคาดหวัง และรักษา Compliance ต่อเนื่อง ไม่ใช่คำสั่งหลอกเพียงครั้งเดียว [Carter, 2023](https://doi.org/10.1093/bjc/azac098)

ผลต่อ JobShield: ต้องตรวจการโอนซ้ำ การแบ่งยอด และยอดสะสม ไม่ประเมินแต่ละรายการโดยแยกจากประวัติระยะสั้น

### 2.7 Warning Habituation — คำเตือนที่มากเกินไปทำให้คำเตือนสำคัญอ่อนแรง

งาน SOUPS พบว่าความเคยชินต่อ Notification ที่ไม่เกี่ยวกับ Security สามารถถ่ายโอนไปยัง Security Warning ที่มีหน้าตาคล้ายกัน ทำให้ความสนใจและการทำตามคำเตือนลดลง [Vance et al., 2019](https://www.usenix.org/conference/soups2019/presentation/vance)

ผลต่อ JobShield: ห้ามแสดงคำเตือน Scam ทุกครั้งที่ถอนเงินสำรอง และต้องแยก Savings Nudge ออกจาก High-risk Security Warning ทั้งด้านโทน ภาษา สี และการกระทำ

## 3. เหตุใดจึงไม่ควรเรียกผู้ใช้ว่า “Weakest Link”

NIST ระบุว่าผู้ใช้มักไม่ได้โง่หรือจงใจละเลย แต่ถูกข้อมูลที่ไม่ครบ ความซับซ้อน ความเหนื่อยล้าจากมาตรการ Security และข้อจำกัดของบริบทกดดัน การกล่าวโทษผู้ใช้อาจสร้างความสัมพันธ์แบบ “เรากับเขา” และลดความเต็มใจที่จะขอความช่วยเหลือหรือรายงานเหตุ [Haney, 2023](https://www.nist.gov/publications/users-are-not-stupid-six-cyber-security-pitfalls-overturned)

กรอบสำหรับ Proposal/Pitch ที่แนะนำ:

> ผู้ใช้คือเป้าหมายของ Social Engineering ไม่ใช่ต้นเหตุของปัญหา JobShield จึงออกแบบ Security ให้ทำงานร่วมกับข้อจำกัดของมนุษย์ โดยเพิ่มข้อมูลที่จำเป็น ทางเลือกที่ชัดเจน และเวลาในการตรวจสอบ ณ จุดก่อนเงินออก

## 4. งานวิจัยสนับสนุนกลไกของ JobShield

| กลไก | เหตุผลเชิง Human Security | หลักฐานที่เกี่ยวข้อง | ข้อจำกัด |
|---|---|---|---|
| Multi-signal Risk Correlation | ระบบต้องช่วยระบุความเสี่ยง ไม่โยนภาระให้ผู้ใช้ตัดสินจากข้อความเพียงลำพัง | ธปท. ระบุการใช้ข้อมูลบัญชีม้าและข้อมูลโอนแบบ Real-time เพื่อเตือนก่อนธุรกรรมสำเร็จ [ธปท.](https://www.bot.or.th/th/finsafeguard/finsafeguard-measure.html) | ความสามารถจริงและ Internal API ของ KBank ต้องยืนยัน |
| Contextual Warning | อธิบายสิ่งที่ระบบสังเกตได้เพื่อลดความคลุมเครือและกระตุ้น Re-evaluation | PSR แนะนำ Risk-based และ Just-in-time intervention | ยังต้องทดสอบถ้อยคำกับ First Jobbers ไทย |
| Pause/Cancel CTA | เปลี่ยนโครงสร้างการกระทำ ไม่เพียงเพิ่มข้อมูล | การทดลองจำลอง Payment Journey กับตัวอย่างผู้ใหญ่สหราชอาณาจักรราว 10,000 คน รายงานว่า Risk-based + CTA ลดโอกาสทำรายการหลอกเมื่อเทียบ Control 81% ในการทดลอง ขณะที่ Warning เชิงพฤติกรรมอย่างเดียวลด 18% [Akesson, Gathergood & Quispe-Torreblanca, 2023](https://www.nottingham.ac.uk/cedex/documents/papers/cedex-discussion-paper-2023-08.pdf) | เป็น Online Experiment ไม่ใช่ Production K PLUS และไม่ควรใช้เป็นค่าคาดการณ์ผลในไทย |
| Risk-based Cooling-off | ลดแรงกดดันของ Hot State และเพิ่มเวลาให้ไตร่ตรอง | PSR เชื่อม Deliberation/Delay กับการแก้ System 1 thinking | ระยะเวลาที่เหมาะสมและผลต่อธุรกรรมจริงยังต้องทดสอบ |
| Independent Verification | ตัดผู้ใช้ออกจากช่องทางที่ผู้โจมตีควบคุม และตรวจ Authority จากแหล่งอื่น | KBank แนะนำให้ติดต่อบริษัทผ่านช่องทางทางการที่หาแยกเอง | Registry/Employer integration เป็น Proposed/Future Integration |
| Less-is-more Warning | ลด Alert Fatigue และ Muscle Memory | PSR และ Vance et al. สนับสนุนการจำกัด Warning ให้ตรงความเสี่ยง | ต้องวัด False Positive และ Warning-dismissal จริง |
| Server-side Decision | ป้องกันแอปที่ถูกดัดแปลง การปลอม Countdown และการกดซ้ำ | หลัก Secure Architecture; สอดคล้องกับ Mobile เป็น Display/Decision UI | ต้องยืนยัน Integration กับ Payment Hub และ Pending State |

## 5. Human-Centered Security Policy ที่เสนอ

### Low Risk

- บัญชีตนเองหรือ Verified Biller
- ไม่มี Destination Risk และไม่มีพฤติกรรมผิดปกติร่วมกัน
- ทำรายการตามปกติ หรือใช้ Savings Nudge ที่กดข้ามได้หากเป็นการถอนเงินสำรองทั่วไป

### Medium Risk

- มีสัญญาณบางส่วน แต่ยังไม่พอระบุความเสี่ยงสูง
- แสดงเหตุผลที่สังเกตได้ 2–3 ข้อ
- ให้ผู้ใช้ยืนยันอย่างตั้งใจ โดยไม่ใช้ข้อความกว้างว่า “รายการนี้อาจเสี่ยง”
- ไม่ Cooling-off อัตโนมัติทุกกรณี

### High Risk

- หลายสัญญาณเกิดพร้อมกัน เช่น Protected Reserve + ผู้รับบุคคลใหม่ + จ่ายเพื่อสมัคร/เริ่มงาน + โอนซ้ำ/แบ่งยอด + Destination Risk
- พัก `คำสั่งโอน` ที่ฝั่ง Server ก่อนส่งเข้าสู่ Payment Hub
- แสดงจำนวนเงินที่เสี่ยงและเหตุผลสั้น ๆ
- ให้ CTA หลักเป็น `หยุดไว้และตรวจสอบ` และ `ยกเลิกและรายงาน`
- ใช้ Independent Verification และ Cooling-off ตาม Policy

## 6. ตัวอย่าง Warning ที่สอดคล้องกับงานวิจัย

ไม่แนะนำ:

> รายการนี้อาจมีความเสี่ยง ต้องการดำเนินการต่อหรือไม่?

แนะนำให้ทดสอบ:

> **หยุดตรวจสอบก่อนโอน 8,000 บาท**  
> คุณกำลังนำเงินออกจาก “เงินสำรองตั้งหลัก” ไปยังบัญชีบุคคลที่ยังไม่เคยโอนให้ และระบุว่าเป็นค่าใช้จ่ายเพื่อเริ่มงาน บริษัทที่น่าเชื่อถือโดยทั่วไปไม่ควรเร่งให้ผู้สมัครโอนเงินผ่านบัญชีบุคคล

ปุ่มหลัก:

- `หยุดไว้และตรวจสอบบริษัท`
- `ยกเลิกและรายงาน`

ทางเลือกรองที่ไม่เด่นกว่า CTA ป้องกัน:

- `ดูรายละเอียดและขั้นตอนถัดไป`

หลักการออกแบบ:

- ไม่ตำหนิ ไม่ใช้คำว่า “คุณกำลังถูกหลอก” หากระบบยังไม่แน่ใจ
- ไม่เปิดสูตร Risk Score ทั้งหมดให้ผู้โจมตีสอนวิธีหลบ
- แสดง Observable Reasons ไม่เกิน 2–3 ข้อ
- แยกภาพลักษณ์ High-risk Warning ออกจาก Notification และมาสคอตทั่วไป
- รองรับ Screen Reader, ขนาดตัวอักษร, Contrast และไม่พึ่งสีเพียงอย่างเดียว

## 7. การรับมือกรณีผู้โจมตีสอนให้กดผ่านทุกขั้นตอน

คำเตือนอย่างเดียวหยุดผู้โจมตีที่กำลัง Coach เหยื่อไม่ได้เสมอ จึงต้องใช้ Defense in Depth:

1. Purpose ที่ผู้ใช้ตอบว่า “ไม่เกี่ยวกับงาน” ไม่สามารถลด Risk จากสัญญาณอื่นให้เป็นศูนย์
2. รวมยอดโอนซ้ำและการแบ่งยอดภายใน Time Window
3. ใช้ Destination/Graph Risk จากระบบธนาคารเป็นสัญญาณอิสระ
4. High Risk เปลี่ยนสถานะเป็น `PENDING_COOLING_OFF` ที่ Server ไม่ใช่ Countdown บนโทรศัพท์อย่างเดียว
5. Verification ต้องออกจากช่องทางที่ผู้โจมตีให้มา เช่น ติดต่อบริษัทจากเว็บไซต์/ทะเบียนที่ระบบค้นหาแยก
6. เก็บ Audit Trail ที่จำเป็นสำหรับ Cancel/Report และ Incident Response

ระบบยังไม่สามารถรับประกันว่าจะหยุด Scam ได้ทุกกรณี หากพ้น Cooling-off แล้วผู้ใช้ยังยืนยันตามเงื่อนไข Policy รายการอาจดำเนินต่อได้ ต้องสื่อสารข้อจำกัดนี้ตรงไปตรงมา

## 8. Privacy และ User Autonomy

- ไม่อ่านข้อความ อีเมล Resume หรือเสียงสนทนาโดยอัตโนมัติ
- ใช้ Transaction Context ที่จำเป็น เช่น แหล่งเงิน ผู้รับ ยอด เวลา ความถี่ และ Risk Flag
- หากให้ผู้ใช้ส่งข้อความ/ภาพเพื่อตรวจ ต้องขอ Consent รายครั้งและใช้เฉพาะข้อมูลที่ส่ง
- ไม่ใช้ข้อมูลที่ส่งเพื่อตรวจไปฝึกโมเดลอัตโนมัติโดยไม่มีฐานกฎหมาย/ความยินยอมที่เหมาะสม
- แจ้ง Retention ของ Indicators และ Audit Data
- ให้ผู้ใช้ยกเลิก รายงาน ออกจาก Flow และเข้าถึงเงินฉุกเฉินที่ถูกต้องตาม Policy ได้

## 9. สิ่งที่ต้องวัด ไม่ใช่สิ่งที่ควรอ้างล่วงหน้า

### Security Outcomes

- อัตรา Pause/Cancel ใน Synthetic Scam Scenario
- Attacker-coached bypass rate
- False-positive rate และ False-negative indicators
- เวลาจาก Warning ถึง Cancel/Report

### Human Factors / UX

- ผู้ใช้เข้าใจเหตุผลเตือนหรือไม่
- ผู้ใช้แยก Savings Nudge กับ Scam Warning ได้หรือไม่
- Warning-dismissal rate และ Alert Fatigue
- เวลาที่เพิ่มใน Legitimate Transfer
- ความรู้สึกถูกตำหนิ ความไว้วางใจ และความสามารถในการควบคุมเงินของตนเอง

### Validation Boundary

- Pilot จริง 1 คนก่อน
- จากนั้น Formative Test 5–8 คน
- ปัจจุบัน `0 sessions conducted`
- ห้ามอ้าง Loss Reduction, Model Accuracy หรือ Adoption ก่อนมีผลทดสอบและข้อมูลจริง

## 10. Claim ที่ใช้ได้และ Claim ที่ควรหลีกเลี่ยง

### ใช้ได้

> Fake-job payment scams ใช้การปลอมตัว ความน่าเชื่อถือ และแรงกดดันให้ผู้สมัครโอนเงินก่อนเริ่มงาน

> JobShield เสนอชั้นป้องกัน Human-Centered Security ที่เชื่อมบริบทเงินสำรอง ผู้รับ ธุรกรรม และ Destination Risk เพื่อเลือก Warning, Verification หรือ Cooling-off ก่อนเงินออก

> งานทดลองต่างประเทศสนับสนุนให้ทดสอบ Risk-based CTA และการชะลอการตัดสินใจ แต่ยังไม่ยืนยันผลลัพธ์ใน First Jobbers ไทยหรือ K PLUS Production

### หลีกเลี่ยง

- “User คือจุดอ่อนที่สุดของระบบ”
- “First Jobbers ถูกหลอกมากกว่าทุกกลุ่ม”
- “Cooling-off ป้องกัน Scam ได้แน่นอน”
- “AI รู้ว่าผู้ใช้กำลังถูกหลอก”
- “JobShield จะลดความเสียหายได้ 81%” — ตัวเลข 81% เป็นผลใน Experimental Treatment ของงานหนึ่ง ไม่ใช่ผลของ JobShield

## แหล่งหลัก

1. [NIST — Users Are Not Stupid: Six Cyber Security Pitfalls Overturned](https://www.nist.gov/publications/users-are-not-stupid-six-cyber-security-pitfalls-overturned)
2. [NIST — Categorizing Human Phishing Detection Difficulty: A Phish Scale](https://csrc.nist.gov/pubs/journal/2020/09/categorizing-human-phishing-detection-difficulty-a/final)
3. [BIS/BCBS — Digital fraud and banking](https://www.bis.org/publications/202311-consultation-digital-fraud-and-banking-supervisory-and-financial-stability-implications.pdf)
4. [PSR/Axiom Economics — Using Behavioural Economics to Understand and Prevent APP Fraud](https://www.psr.org.uk/media/efpdiwpk/using-behavioural-economics-to-understand-and-prevent-app-fraud.pdf)
5. [Akesson, Gathergood & Quispe-Torreblanca — Preventing Payments Fraud in the FinTech Era](https://www.nottingham.ac.uk/cedex/documents/papers/cedex-discussion-paper-2023-08.pdf)
6. [Fischer, Lea & Evans — Psychological determinants of scam compliance](https://doi.org/10.1111/jasp.12158)
7. [Carter — Confirm Not Command](https://doi.org/10.1093/bjc/azac098)
8. [Vance et al. — The Fog of Warnings](https://www.usenix.org/conference/soups2019/presentation/vance)
9. [Bank of Thailand — มาตรการป้องกันการใช้ระบบการเงินไทยในทางที่ผิด](https://www.bot.or.th/th/finsafeguard/finsafeguard-measure.html)
10. [KBank — หลอกรับสมัครงานออนไลน์](https://www.kasikornbank.com/th/personal/digital-banking/kbankcyberrisk/pages/jobscam.aspx)

