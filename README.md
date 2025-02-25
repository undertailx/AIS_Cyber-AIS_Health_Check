# Project

โปรเจคนี้เป็นสคริปต์สำหรับการทำงานอัตโนมัติด้วย Selenium:

- **main.py**: สคริปต์สำหรับล็อกอินและนำทางไปยังคอร์สต่าง ๆ บนแพลตฟอร์มการเรียนรู้ และตอบคำถามโดยอัตโนมัติจากการแมปคำตอบที่กำหนดไว้

  - : https://learndiaunjaicyber.ais.co.th/ สื่อการเรียนรู้นักเรียน อุ่นใจปลอดภัยไซเบอร์ ระดับ Fundamental Level

- **main2.py**: สคริปต์สำหรับตรวจสุขภาพดิจิทัลโดยการตั้งค่า cookie สำหรับล็อกอิน และนำทางผ่านหลายหน้าเพื่อให้ตอบคำถามอัตโนมัติ
  - : https://digitalhealthcheck.ais.th/th/home Ais Health Check Auto Stars all stages

# Setup

1. ติดตั้ง dependencies:
   pip install -r requirements.txt
2. ตรวจสอบว่าได้ติดตั้ง ChromeDriver และเพิ่มลงใน PATH ของระบบแล้ว

3. main.py (Auto Login setting account in code)
   main2.py (ต้องเอา Cookies มาใส่เอง)

# Usage

- สำหรับ Aiscyber Fundamental Level:
  python main.py
- สำหรับ Ais Health Check:
  python main2.py
