# JobShield — User Problem Evidence

สถานะ: Evidence review completed 4 กันยายน 2026  
ขอบเขต: บันทึกหลักฐานและ claim boundary สำหรับปัญหา fake-job payment scam; ไม่ใช่ข้อความ Proposal

## ข้อสรุป

มีหลักฐานทางการเพียงพอว่า “ประกาศ/ผู้รับสมัครงานปลอมที่แอบอ้างองค์กรและเรียกให้ผู้หางานโอนเงินก่อน” เป็นภัยจริงทั้งในไทยและต่างประเทศ แต่ยังไม่มีหลักฐานตรงที่ตรวจพบในการทบทวนรอบนี้ว่า First Jobbers ไทยอายุ 22–30 มีอัตราตกเป็นเหยื่อสูงกว่ากลุ่มอื่น หรือว่าผู้โจมตีรู้เสมอว่าเหยื่อเพิ่งส่ง Resume ให้บริษัทใด

ดังนั้น problem framing ที่ใช้ได้คือ `job-search transition creates a distinct exposure and decision context` ไม่ใช่ `First Jobbers are more gullible or victimized than everyone else`.

## ข้อเท็จจริงที่หลักฐานรองรับ

1. หน้า Cyber Risk ของ KBank อธิบายว่ามิจฉาชีพสร้างประกาศรับสมัครงานออนไลน์ อ้างอิงองค์กรที่มีชื่อเสียง และขอให้เหยื่อโอนเงินประกันก่อนเริ่มงาน ค่าธรรมเนียมสมัครงาน ค่าอัปเกรดงาน หรือค่าดำเนินการรับค่าจ้าง บางกรณีหลอกให้โอนซ้ำก่อนตัดการติดต่อ
2. หน้าเดียวกันแนะนำให้ตรวจบริษัทผ่านแหล่งทางการ ติดต่อบริษัทด้วยช่องทางจากเว็บไซต์จริง และไม่รีบโอน เพราะโดยปกติไม่มีค่าธรรมเนียมสมัครหรือสัมภาษณ์งาน
3. ธปท. รายงานว่าในข้อมูลการแจ้งความที่บทความนำมาวิเคราะห์สำหรับไตรมาส 4 ปี 2568 การหลอกให้โอนเงินเพื่อทำงานหารายได้พิเศษคิดเป็น 17% ของมูลค่าความเสียหายในหมวดที่แสดง หรือมากกว่า 920 ล้านบาท โดยมิจฉาชีพอาจปลอมเป็นบริษัทรับสมัครงานและเรียกค่าเริ่มงาน
4. กระทรวงแรงงานรายงานกรณีปี 2569 ที่ผู้เสียหายถูกหลอกเรื่องงานต่างประเทศ ให้โอนค่าลงทะเบียน และดำเนินการผ่านแอปธนาคารจนเกิดความเสียหาย
5. FTC ของสหรัฐฯ บันทึกรูปแบบ fake recruiter ที่ใช้ชื่อ/โลโก้บริษัทและเอกสารดูเป็นทางการ ก่อนเรียกค่าอุปกรณ์ ค่าอบรม หรือข้อมูลทางการเงิน รูปแบบนี้ใช้ยืนยัน attack pattern ได้ แต่ใช้ประมาณขนาดปัญหาในไทยไม่ได้
6. หลักฐานจาก FCA/PSR สนับสนุนหลักการว่า risk-based, transaction-specific intervention และ positive friction ใน payment journey อาจช่วยให้ผู้ใช้ทบทวนธุรกรรมได้ดีกว่า static/generic warning แต่ไม่ได้พิสูจน์ผลลัพธ์ของ JobShield ในไทย

## Claim ที่ยังเป็นสมมติฐาน

- First Jobbers มักส่ง Resume หลายแห่งและคาดหวังการติดต่อจากผู้ส่งที่ไม่คุ้นเคย
- ความต้องการได้งานทำให้ตอบสนองต่อความเร่งด่วนได้ง่ายขึ้น
- First Jobbers มี `เงินสำรองก่อนเงินเดือนแรก` จำกัดและความเสียหายก้อนเดียวอาจกระทบการเริ่มงานรุนแรง
- ผู้โจมตีรู้ชื่อบริษัทที่ผู้สมัครเพิ่งส่ง Resume ให้และ spoof บริษัทนั้นโดยตรง
- Contextual JobShield warning จะเพิ่ม Pause/Cancel โดยไม่สร้าง friction เกินยอมรับ

สมมติฐานเหล่านี้ต้องทดสอบด้วยการสัมภาษณ์หรือ formative usability test และห้ามเขียนเป็นสถิติหรือพฤติกรรมของ First Jobbers ทุกคน

## Problem Statement Boundary สำหรับขั้นถัดไป

ข้อความเชิงแนวคิดที่ปลอดภัยต่อหลักฐาน:

> ระหว่างช่วงหางาน First Jobbers ต้องรับการติดต่อจากผู้ส่งที่ยังไม่คุ้นเคย และอาจถูกผู้รับสมัครงานปลอมกดดันให้โอนค่าธรรมเนียมหรือเงินประกันก่อนเริ่มงาน เมื่อผู้ใช้เป็นผู้ยืนยันรายการเอง มาตรการยืนยันตัวตนเพียงอย่างเดียวไม่ยืนยันว่าการตัดสินใจนั้นปราศจาก social engineering

ห้ามใช้ใน Proposal โดยยังไม่แก้:

- “First Jobbers เป็นกลุ่มที่ถูกหลอกมากที่สุด”
- “ผู้สมัครงานส่วนใหญ่ส่ง Resume จำนวนมากและรีบกดทุกลิงก์”
- “JobShield ป้องกัน recruitment scam ได้ทั้งหมด”
- นำตัวเลข 920 ล้านบาทไปเรียกว่า “ความเสียหายของ First Jobbers” หรือ “fake recruiter หลังส่ง Resume” เพราะแหล่งจริงเป็นหมวดงานหารายได้พิเศษที่กว้างกว่า

## Research Gate 1

**ผล: PASS WITH CLAIM LIMITS**

- ผ่าน: fake-job/recruitment-payment scam เป็นภัยจริงและมีแหล่งไทยทางการรองรับ
- ไม่ผ่านสำหรับ claim เฉพาะ: ยังไม่มี comparative evidence ว่าอายุ 22–30 เสี่ยงกว่ากลุ่มอื่น
- แนวทาง: ใช้ transitional-risk context และผลกระทบต่อเงินสำรองเป็น product rationale; ตัด prevalence comparison ออก

## Sources

- KBank, “หลอกรับสมัครงานออนไลน์,” เข้าถึง 4 ก.ย. 2569: https://www.kasikornbank.com/th/personal/digital-banking/kbankcyberrisk/pages/jobscam.aspx
- ธปท., “รวมพลังทุกภาคส่วนเพื่อรับมือภัยการเงินดิจิทัล,” เข้าถึง 4 ก.ย. 2569: https://www.bot.or.th/th/research-and-publications/articles-and-publications/bot-magazine-issues/phrasiam-69-1/synergy-against-fraud.html
- กระทรวงแรงงาน, “เตือนเว็บไซต์ปลอม…อ้างพาไปทำงานต่างประเทศ,” เข้าถึง 4 ก.ย. 2569: https://www.mol.go.th/news/595086
- US FTC, “Scammers impersonate well-known companies…,” เข้าถึง 4 ก.ย. 2569: https://consumer.ftc.gov/consumer-alerts/2023/08/scammers-impersonate-well-known-companies-recruit-fake-jobs-linkedin-other-job-platforms
- US FTC, “Applying for jobs? Be on the lookout for scams,” เข้าถึง 4 ก.ย. 2569: https://consumer.ftc.gov/consumer-alerts/2022/05/applying-jobs-be-lookout-scams
- FCA, “Anti-fraud controls and complaint handling in firms,” เข้าถึง 4 ก.ย. 2569: https://www.fca.org.uk/publications/multi-firm-reviews/anti-fraud-controls-complaint-handling-firms-focus-app-fraud
- PSR, “Using behavioural economics to understand and prevent APP fraud,” เข้าถึง 4 ก.ย. 2569: https://www.psr.org.uk/media/efpdiwpk/using-behavioural-economics-to-understand-and-prevent-app-fraud.pdf
