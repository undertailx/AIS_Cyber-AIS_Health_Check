# WORKING 97.88%
# https://learndiaunjaicyber.ais.co.th/ # Not 100% sometimes misses. Please check stages again after running one complete round
# สื่อการเรียนรู้นักเรียน อุ่นใจปลอดภัยไซเบอร์ ระดับ Fundamental Level

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login_and_navigate(driver, username, password):
    # Login
    driver.get("https://learndiaunjaicyber.ais.co.th/account/login/")
    
    # Wait until the login fields are present (optional improvement)
    wait = WebDriverWait(driver, 10)
    
    # Updated username selector
    username_field = wait.until(EC.presence_of_element_located((By.NAME, "username_or_email")))
    password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    
    username_field.send_keys(username)
    password_field.send_keys(password)
    
    # Updated login button selector using id "btn-login"
    login_button = driver.find_element(By.ID, "btn-login")
    # Use JavaScript to avoid click interception:
    driver.execute_script("arguments[0].click();", login_button)
    
    # Wait for login to complete (e.g., URL change) before navigating further
    wait.until(lambda d: d.current_url != "https://learndiaunjaicyber.ais.co.th/account/login/")
    
    # Navigate to course page
    driver.get("https://learndiaunjaicyber.ais.co.th/course/5/playlist/9?learningpath_id=145&learningpath_sectionid=178")

def answer_questions(driver):
    # Wait for and click progress button
    progress_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa='btn-progress']"))
    )
    progress_button.click()
    
    # Wait for question containers to load
    question_containers = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.test-question.question"))
    )
    
    # Define a dictionary mapping unique parts of the question text to the expected letter
    answer_dict = {
        "ไม่ใช่กิจกรรมการใช้เวลาหน้าจอแบบมีการโต้ตอบ": "การใช้อุปกรณ์ออนไลน์สร้างคอมพิวเตอร์กราฟิก",
        "เป็นพฤติกรรมการจัดสรรเวลาการใช้หน้าจอของเด็ก": "ถูกทุกข้อ",
        "เด็กอายุน้อยกว่า": "1 ชั่วโมงต่อวัน",
        "เป็นผลเสียของการใช้เวลากับหน้าจอมากจนเกินไป": "ถูกทุกข้อ",
        "เป็นแนวทางการจัดสรรเวลาในการใช้เวลาหน้าจอ": "ถูกทุกข้อ",
        "เป็นผลกระทบของผู้ใหญ่จากการจัดสรรเวลาหน้าจอที่ไม่เหมาะสม": "ถูกทุกข้อ",
        "ไม่ใช่เป็นผลกระทบของเด็กจากการจัดสรรเวลาหน้าจอ": "มีความตื่นตัว และตัดสินใจในเรื่องต่างๆ ได้อย่างรวดเร็ว",
        "ไม่ใช่เป็นอุปสรรคในการเปลี่ยนพฤติกรรมการใช้เวลาหน้าจอ": "ถูกทุกข้อ",
        "กิจกรรมการใช้เวลาหน้าจอ แบ่งเป็น": "4 ประเภท",
        "คือความหมายของทักษะการจัดสรรเวลาหน้าจอ": "ถูกทุกข้อ"
    }
    
    for i, container in enumerate(question_containers):
        if i == 0:
            time.sleep(2)  # delay added for question 1
        question_text = container.find_element(By.CSS_SELECTOR, "div[data-qa='question-desc']").text
        print(f"Processing question: {question_text}")
        
        expected_answer = None
        for key, letter in answer_dict.items():
            if key in question_text:
                expected_answer = letter
                break
        if not expected_answer:
            print("No matching key found in question text. Skipping.")
            continue
        
        # Find choices relative to the question container
        choices = container.find_elements(By.CSS_SELECTOR, "label[role='radio']")
        selected = False
        for choice in choices:
            full_choice = choice.text.strip()
            if len(full_choice) > 2 and full_choice[1] == '.':
                full_choice = full_choice[2:].strip()  # Remove prefix; fixed .trip() to .strip()
            if full_choice.lower() == expected_answer.lower():
                print(f"Selecting choice for expected letter {expected_answer}: {full_choice}")
                driver.execute_script("arguments[0].scrollIntoView(true);", choice)
                for _ in range(2):  # force click twice
                    driver.execute_script("arguments[0].click();", choice)
                    time.sleep(0.1)
                selected = True
                break
        if not selected:
            print(f"No valid choice found for question matching {expected_answer}")
    
    # Click first submit button
    submit_button1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//button[@data-qa='btn-submit'])[1]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button1)
    submit_button1.click()
    time.sleep(1)  # small pause before waiting for the second popup
    
    # Wait for the second submit button popup to appear and click it
    submit_button2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//button[@data-qa='btn-submit'])[1]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button2)
    submit_button2.click()

def answer_questions_second(driver):
    # Navigate to second course page
    driver.get("https://learndiaunjaicyber.ais.co.th/course/6/playlist/15?learningpath_id=145&learningpath_sectionid=178")
    
    # Wait for and click the progress button for the second course
    progress_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa='btn-progress']"))
    )
    progress_button.click()
    
    # Wait for question containers to load
    question_containers = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.test-question.question"))
    )
    
    # Define answer mapping dictionary for course 2
    answer_dict2 = {
        "ส่งผลต่อการรู้เท่าทันสื่อ": "ถูกทุกข้อ",
        "ความหมายของการรู้เท่าทันสื่อ": "ถูกทุกข้อ",
        "ทักษะการรู้เท่าทันสื่อ": "ทักษะการมีส่วนร่วม (Participate Skill)",
        "รู้เท่าทันสื่อในยุค": "5 มิติ",
        "ผลกระทบของเด็ก": "มีความตื่นตัว และตัดสินใจในเรื่องต่างๆ ได้อย่างรวดเร็ว",
        "ปัจจัยของสื่อที่มีผล": "ถูกทุกข้อ",
        "ทักษะที่ช่วยให้บุคคลสามารถเชื่อมโยง": "การประเมิน (Evaluate Skill)",
        "ลักษณะของความรู้สึกต่อตนเอง": "ถูกทุกข้อ",
        "องค์ประกอบของการรู้เท่าทันสื่อ": "4 ด้าน",
        "สร้างค่านิยมและอุดมคติ": "สื่อหนังสือพิมพ์อยู่รอดได้จากรายได้ของโฆษณา"
    }
    
    for i, container in enumerate(question_containers):
        if i == 0:
            time.sleep(2)  # delay added for question 1 in course 2
        question_text = container.find_element(By.CSS_SELECTOR, "div[data-qa='question-desc']").text
        print(f"Course 2 - Processing question: {question_text}")
        
        expected_letter = None
        for key, letter in answer_dict2.items():
            if key in question_text:
                expected_letter = letter
                break
        if not expected_letter:
            print("No matching key found in question text. Skipping.")
            continue
        
        # Process answer choices
        choices = container.find_elements(By.CSS_SELECTOR, "label[role='radio']")
        selected = False
        for choice in choices:
            full_choice = choice.text.strip()
            if len(full_choice) > 2 and full_choice[1] == '.':
                full_choice = full_choice[2:].strip()
            if full_choice.lower() == expected_letter.lower():
                print(f"Course 2 - Selecting answer for expected letter {expected_letter}: {full_choice}")
                driver.execute_script("arguments[0].scrollIntoView(true);", choice)
                for _ in range(2):  # force click twice
                    driver.execute_script("arguments[0].click();", choice)
                    time.sleep(0.1)
                selected = True
                break
        if not selected:
            print(f"Course 2 - No valid choice found for question matching {expected_letter}")
    
    # Click submit buttons for course 2 (similar to first course)
    submit_button1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//button[@data-qa='btn-submit'])[1]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button1)
    submit_button1.click()
    time.sleep(1)
    
    submit_button2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//button[@data-qa='btn-submit'])[1]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button2)
    submit_button2.click()

def answer_questions_third(driver):
    # Navigate to third course page
    driver.get("https://learndiaunjaicyber.ais.co.th/course/8/playlist/23?learningpath_id=145&learningpath_sectionid=178")
    
    # Wait for and click progress button
    progress_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa='btn-progress']"))
    )
    progress_button.click()
    
    # Wait for question containers to load
    question_containers = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.test-question.question"))
    )
    
    # Define a dictionary mapping unique parts of the question text to the expected letter
    # Expected answers (using ก:0, ข:1, ค:2, ง:3): 
    # [Q1: ง, Q2: ค, Q3: ก, Q4: ง, Q5: ข, Q6: ค, Q7: ง, Q8: ง, Q9: ก, Q10: ข]
    answer_dict3 = {
        "ป้องกันการโจรกรรมอัตลักษณ์ตัวตนบนโลกไซเบอร์": "ถูกทุกข้อ",
        "หลักการตั้งรหัสผ่านที่เหมาะสมที่สุด": "นายแสนตีตั้งรหัสผ่านที่มีตัวอักษร ตัวเล็กตัวใหญ่ สัญลักษณ์ และตัวเลข เช่น @Aom99",
        "การไม่พิสูจน์ตัวตนบนโลกไซเบอร์": "ข้อมูลเหล่านั้นเป็นข้อมูลสาธารณะ ที่อนุญาตให้ทุกคนเข้าใช้บริการและเปลี่ยนแปลงได้",
        "หน้าที่ของภาครัฐในการป้องกันการโจรกรรม": "ถูกทุกข้อ",
        "ไม่ใช่ ลักษณะเฉพาะทางชีวภาพ": "ลายเซ็น",
        "ไม่ได้ ใช้อัตลักษณ์ตัวตนบนโลกไซเบอร์": "นายซี เปิดวิทยุฟังบนรถยนต์ โดยไม่เชื่อมต่ออินเทอร์เน็ต",
        "ไม่ใช่ การพิสูจน์อัตลักษณ์ตัวตน": "การพิสูจน์โดยใช้ลายเซ็นที่เซ็นบนกระดาษ",
        "วิธีการป้องกันตนเองจากอาชญากร": "ถูกทุกข้อ",
        "ไม่ใช่ สิ่งที่ควรปฏิบัติในการใช้การยืนยันตัวตน": "ตั้งรหัสการเข้าให้ง่าย เพื่อสะดวกในการจดจำ",
        "กิจกรรมด้านใดต่อไปนี้ ไม่ได้ใช้อัตลักษณ์ตัวตนบนโลกไซเบอร์?": "นายซี เปิดวิทยุฟังบนรถยนต์ โดยไม่เชื่อมต่ออินเตอร์เน็ต",
        "อัตลักษณ์ตัวตนบนโลกไซเบอร์ มีความหมาย": "การระบุสิ่งที่แสดงคุณลักษณะเฉพาะตัวบุคคลเพื่อยืนยันและพิสูจน์ตัวบุคคลได้บนโลกออนไลน์"
    }
    
    for i, container in enumerate(question_containers):
        if i == 0:
            time.sleep(2)  # delay added for question 1 in course 3
        question_text = container.find_element(By.CSS_SELECTOR, "div[data-qa='question-desc']").text
        print(f"Course 3 - Processing question: {question_text}")
        
        expected_letter = None
        for key, letter in answer_dict3.items():
            if key in question_text:
                expected_letter = letter
                break
        if not expected_letter:
            print("Course 3 - No matching key found in question text. Skipping.")
            continue
        
        choices = container.find_elements(By.CSS_SELECTOR, "label[role='radio']")
        selected = False
        for choice in choices:
            full_choice = choice.text.strip()
            if len(full_choice) > 2 and full_choice[1] == '.':
                full_choice = full_choice[2:].strip()  # Changed from .trip() to .strip()
            if full_choice.lower() == expected_letter.lower():
                print(f"Course 3 - Selecting choice for expected letter {expected_letter}: {full_choice}")
                driver.execute_script("arguments[0].scrollIntoView(true);", choice)
                for _ in range(2):  # force click twice
                    driver.execute_script("arguments[0].click();", choice)
                    time.sleep(0.1)
                selected = True
                break
        if not selected:
            print(f"Course 3 - No valid choice found for question matching {expected_letter}")
    
    # Submit answers for course 3 similar to previous courses
    submit_button1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//button[@data-qa='btn-submit'])[1]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button1)
    submit_button1.click()
    time.sleep(1)
    
    submit_button2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//button[@data-qa='btn-submit'])[1]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button2)
    submit_button2.click()

def answer_questions_four(driver):
    # Navigate to fourth course page
    driver.get("https://learndiaunjaicyber.ais.co.th/course/9/playlist/26?learningpath_id=145&learningpath_sectionid=178")
    
    # Wait for and click progress button
    progress_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa='btn-progress']"))
    )
    progress_button.click()
    
    # Wait for question containers to load
    question_containers = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.test-question.question"))
    )
    
    # Define dictionary mapping unique question text snippets to the expected answer letter
    # Using ก:0, ข:1, ค:2, ง:3
    answer_dict4 = {
        "ไม่ใช่ พฤติกรรมการละเมิดสิทธิ": "พัฒนานวัตกรรมหรือเทคโนโลยีใหม่จากสิ่งที่มีอยู่เดิม",
        "ตัวเราถูกละเมิดสิทธิ": "แจ้งความและดำเนินคดีตามกฎหมาย",
        "ความสำคัญของการรักษาความปลอดภัย": "ถูกทุกข้อ",
        "การแอบบันทึกภาพ/เสียงจากภาพยนตร์": "ละเมิดพระราชบัญญัติ เรื่องพระราชบัญญัติลิขสิทธิ์ พ.ศ. 2537 และ พระราชบัญญัติลิขสิทธิ์ (ฉบับที่ 2) พ.ศ. 2558",
        "ส่งเสริมวัฒนธรรมสิทธิทางไซเบอร์": "ถูกทุกข้อ",
        "ไม่ใช่ ลักษณะของสิทธิทางไซเบอร์": "สิทธิในการรับรู้ข้อมูลส่วนตัวของบุคคลอื่น",
        "ละเมิดข้อมูลส่วนบุคคล": "ถูกทุกข้อ",
        "ความหมายของสิทธิทางไซเบอร์": "ถูกทุกข้อ",
        "หลักการตั้งรหัสผ่าน": "ถูกทุกข้อ",
        "การกระทำที่ละเมิดสิทธิทางไซเบอร์": "ถูกทุกข้อ"
    }
    
    for i, container in enumerate(question_containers):
        if i == 0:
            time.sleep(2)  # add delay for the first question if needed
        question_text = container.find_element(By.CSS_SELECTOR, "div[data-qa='question-desc']").text
        print(f"Course 4 - Processing question: {question_text}")
        
        expected_letter = None
        for key, letter in answer_dict4.items():
            if key in question_text:
                expected_letter = letter
                break
        if not expected_letter:
            print("Course 4 - No matching key found. Skipping.")
            continue
        
        choices = container.find_elements(By.CSS_SELECTOR, "label[role='radio']")
        selected = False
        for choice in choices:
            full_choice = choice.text.strip()
            if len(full_choice) > 2 and full_choice[1] == '.':
                full_choice = full_choice[2:].strip()
            if full_choice.lower() == expected_letter.lower():
                print(f"Course 4 - Selecting answer for expected letter {expected_letter}: {full_choice}")
                driver.execute_script("arguments[0].scrollIntoView(true);", choice)
                for _ in range(2):  # force click twice
                    driver.execute_script("arguments[0].click();", choice)
                    time.sleep(0.1)
                selected = True
                break
        if not selected:
            print(f"Course 4 - No valid choice found for question matching {expected_letter}")
    
    # Click submit buttons for course 4
    submit_button1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//button[@data-qa='btn-submit'])[1]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button1)
    submit_button1.click()
    time.sleep(1)
    
    submit_button2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//button[@data-qa='btn-submit'])[1]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button2)
    submit_button2.click()

def answer_questions_five(driver):
    # Navigate to course 5 page
    driver.get("https://learndiaunjaicyber.ais.co.th/course/11/playlist/32?learningpath_id=145&learningpath_sectionid=178")
    
    # Click progress button
    progress_button = WebDriverWait(driver, 10).until(
       EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa='btn-progress']"))
    )
    progress_button.click()
    
    # Wait for questions to load
    question_containers = WebDriverWait(driver, 10).until(
       EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.test-question.question"))
    )
    
    # Dictionary for course 5 answers using ก:0, ข:1, ค:2, ง:3
    answer_dict5 = {
        "ความหมายของการรักษาความปลอดภัยด้านไซเบอร์": "ถูกทุกข้อ",
        "เอกสารข้อมูลส่วนตัว": "ถูกทุกข้อ",
        "ไม่ถูกต้องเกี่ยวกับการรักษาความปลอดภัย": "นายสมเกียรติ ตั้งรหัสผ่านเหมือนกันทุกระบบ เพราะป้องกันการลืม",
        "ไม่ใช่วิธีการในการขโมยข้อมูล": "การไม่เปิดเผยข้อมูลส่วนตัวลงบนระบบไซเบอร์",
        "ป้องกันความเป็นส่วนตัวของบุคคล": "นายจินดา เก็บข้อมูลบัตรประชาชนไว้อย่างเป็นความลับ และแสดงบัตรเมื่อมีความจำเป็นเท่านั้น",
        "ไม่เป็นปัจจัยที่มีอิทธิพล": "ถูกทุกข้อ",
        "ข้อมูลส่วนตัวในการร้องขอ": "ถูกทุกข้อ",
        "ไม่ใช่วิธีการในการรักษาความปลอดภัย": "การใช้ซอฟต์แวร์ดักจับข้อมูลเพื่อล้วงความลับของผู้อื่น",
        "ไม่ใช่ ประเด็นปัญหา": "การแสดงตัวตน",
        "ข้อใด ไม่ใช่ เป็นปัจจัยที่มีอิทธิพลต่อการเกิดอาชญากรรมบนสื่อสังคมออนไลน์": "ถูกทุกข้อ",
        "ข้อใดไม่ใช่ลักษณะของสิทธิทางไซเบอร์": "สิทธิในการรับรู้ข้อมูลส่วนตัวของบุคคลอื่น",
        "เสี่ยงต่อการถูกโจมตี": "ถูกทุกข้อ"
    }
    
    for i, container in enumerate(question_containers):
        if i == 0:
            time.sleep(2)
        question_text = container.find_element(By.CSS_SELECTOR, "div[data-qa='question-desc']").text
        print(f"Course 5 - Processing question: {question_text}")
        
        expected_letter = None
        for key, letter in answer_dict5.items():
            if key in question_text:
                expected_letter = letter
                break
        if not expected_letter:
            print("Course 5 - No matching key found. Skipping.")
            continue
        
        choices = container.find_elements(By.CSS_SELECTOR, "label[role='radio']")
        selected = False
        for choice in choices:
            full_choice = choice.text.strip()
            if len(full_choice) > 2 and full_choice[1] == '.':
                full_choice = full_choice[2:].strip()  # fixed .trip() to .strip()
            if full_choice.lower() == expected_letter.lower():
                print(f"Course 5 - Selecting choice for expected letter {expected_letter}: {full_choice}")
                driver.execute_script("arguments[0].scrollIntoView(true);", choice)
                for _ in range(2):  # force click twice
                    driver.execute_script("arguments[0].click();", choice)
                    time.sleep(0.1)
                selected = True
                break
        if not selected:
            print(f"Course 5 - No valid choice found for question matching {expected_letter}")
    
    # Submit answers for course 5
    submit_button1 = WebDriverWait(driver, 10).until(
         EC.element_to_be_clickable((By.XPATH, "(//button[@data-qa='btn-submit'])[1]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button1)
    submit_button1.click()
    time.sleep(1)
    submit_button2 = WebDriverWait(driver, 10).until(
         EC.element_to_be_clickable((By.XPATH, "(//button[@data-qa='btn-submit'])[1]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button2)
    submit_button2.click()

def answer_questions_six(driver):
    # Navigate to course 6 page
    driver.get("https://learndiaunjaicyber.ais.co.th/course/13/playlist/47?learningpath_id=145&learningpath_sectionid=178")
    
    # Click progress button
    progress_button = WebDriverWait(driver, 10).until(
         EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa='btn-progress']"))
    )
    progress_button.click()
    
    # Wait for questions to load
    question_containers = WebDriverWait(driver, 10).until(
         EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.test-question.question"))
    )
    
    # Dictionary for course 6 answers
    answer_dict6 = {
        "ไม่เป็นความผิดตามพระราชบัญญัติว่าด้วยการกระทำความผิดเกี่ยวกับคอมพิวเตอร์": "การกดไลก์ (Like)",
        "ไม่ใช่ ประเภทของพฤติกรรมการรังแกกัน": "การโดนทำร้าย ลวนลาม (Molestation)",
        "กลั่นแกล้งทางสังคม": "ถูกทุกข้อ",
        "หน้าที่ของผู้ให้บริการ": "ถูกทุกข้อ",
        "รับมือจากการกลั่นแกล้ง": "BATTER นัดเจอผู้ที่ระราน เพื่อเคลียร์ปัญหาข้องใจ",
        "ไม่ใช่วิธีการในการจัดการปัญหา": "หากมีปัญหากับใครให้นัดเคลียร์ตัวต่อตัว",
        "สัญญาณเตือน": "แสดงอารมณ์โกรธ หรือมีอาการเศร้า เสียใจหลังจากใช้อินเทอร์เน็ตหรือโทรศัพท์",
        "สาเหตุที่ทำให้เกิดพฤติกรรม": "ถูกทุกข้อ",
        "ไม่ใช่ ความหมายของการกลั่นแกล้ง": "การด่าทอ พูดจาส่อเสียดกันในพื้นที่สาธารณะ",
        "แนวทางการช่วยเหลือ": "ถูกทุกข้อ"
    }
    
    for i, container in enumerate(question_containers):
        if i == 0:
            time.sleep(2)
        question_text = container.find_element(By.CSS_SELECTOR, "div[data-qa='question-desc']").text
        print(f"Course 6 - Processing question: {question_text}")
        
        expected_letter = None
        for key, letter in answer_dict6.items():
            if key in question_text:
                expected_letter = letter
                break
        if not expected_letter:
            print("Course 6 - No matching key found. Skipping.")
            continue
        
        choices = container.find_elements(By.CSS_SELECTOR, "label[role='radio']")
        selected = False
        for choice in choices:
            full_choice = choice.text.strip()
            if len(full_choice) > 2 and full_choice[1] == '.':
                full_choice = full_choice[2:].strip()
            if full_choice.lower() == expected_letter.lower():
                print(f"Course 6 - Selecting choice for expected letter {expected_letter}: {full_choice}")
                driver.execute_script("arguments[0].scrollIntoView(true);", choice)
                for _ in range(2):  # force click twice
                    driver.execute_script("arguments[0].click();", choice)
                    time.sleep(0.1)
                selected = True
                break
        if not selected:
            print(f"Course 6 - No valid choice found for question matching {expected_letter}")
    
    # Submit answers for course 6
    submit_button1 = WebDriverWait(driver, 10).until(
         EC.element_to_be_clickable((By.XPATH, "(//button[@data-qa='btn-submit'])[1]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button1)
    submit_button1.click()
    time.sleep(1)
    submit_button2 = WebDriverWait(driver, 10).until(
         EC.element_to_be_clickable((By.XPATH, "(//button[@data-qa='btn-submit'])[1]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button2)
    submit_button2.click()

def answer_questions_seven(driver):
    # Navigate to course 7 page
    driver.get("https://learndiaunjaicyber.ais.co.th/course/14/playlist/39?learningpath_id=145&learningpath_sectionid=178")
    progress_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa='btn-progress']"))
    )
    progress_button.click()
    question_containers = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.test-question.question"))
    )
    answer_dict7 = {
        "แสดงมารยาททางไซเบอร์ที่ดีบนโลกออนไลน์": "นางแอล หาข้อมูลจากแหล่งข่าวหลายที่ ก่อนแสดงความคิดเห็น",
        "พฤติกรรมของการมีมารยาททางไซเบอร์ที่ดี": "นายอาร์ม คิด วิเคราะห์ แยกแยะ ข่าวสารทุกครั้ง ก่อนแสดงความคิดเห็นอย่างให้เกียรติกัน",
        "ไม่ได้ เป็นผลกระทบจากการขาดทักษะการใช้เทคโนโลยีอย่างมีจริยธรรม": "ปัญหาการบริหารจัดการเวลาให้มีประสิทธิภาพ",
        "ความหมายของมารยาททางไซเบอร์ที่ถูกต้องที่สุด": "พฤติกรรมอันพึงประสงค์ของการปฏิสัมพันธ์บนโลกออนไลน์ซึ่งเน้นความมีกาลเทศะ และมีความประพฤติดี",
        "หลักการสำคัญของการมีมารยาททางไซเบอร์ที่ดี": "คำนึงถึงหลักการเอาใจเขามาใส่ใจเรา",
        "ไม่ใช่หลักการที่เป็นจริยธรรม": "ความประหยัด",
        "ไม่ใช่ข้อกำหนดจรรยาบรรณ": "การบริหารจัดการเวลาค่าใช้จ่ายให้คุ้มค่ากับสิ่งที่ได้ลงมือกระทำ",
        "กลวิธีการจัดการเมื่อเกิดปัญหาการถูกละเมิดมารยาท": "ถูกทุกข้อ",
        "ไม่ได้ เป็นการจัดการเมื่อเกิดปัญหาการถูกละเมิดมารยาท": "นายบี จ้างแฮกเกอร์เพื่อล้วงข้อมูลของผู้ที่แกล้งนายบี",
        "การแสดงมารยาททางไซเบอร์ที่ดี": "การซื้อหรือใช้โปรแกรมที่ถูกลิขสิทธิ์"
    }
    for i, container in enumerate(question_containers):
        if i == 0:
            time.sleep(2)
        question_text = container.find_element(By.CSS_SELECTOR, "div[data-qa='question-desc']").text
        print(f"Course 7 - Processing question: {question_text}")
        expected_letter = None
        for key, letter in answer_dict7.items():
            if key in question_text:
                expected_letter = letter
                break
        if not expected_letter:
            print("Course 7 - No matching key found. Skipping.")
            continue
        choices = container.find_elements(By.CSS_SELECTOR, "label[role='radio']")
        selected = False
        for choice in choices:
            full_choice = choice.text.strip()
            if len(full_choice) > 2 and full_choice[1] == '.':
                full_choice = full_choice[2:].strip()
            if full_choice.lower() == expected_letter.lower():
                driver.execute_script("arguments[0].scrollIntoView(true);", choice)
                for _ in range(2):  # force click twice
                    driver.execute_script("arguments[0].click();", choice)
                    time.sleep(0.1)
                selected = True
                break
        if not selected:
            print(f"Course 7 - No valid choice found for question matching {expected_letter}")
    submit_button1 = WebDriverWait(driver, 10).until(
         EC.element_to_be_clickable((By.XPATH, "(//button[@data-qa='btn-submit'])[1]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button1)
    submit_button1.click()
    time.sleep(1)
    submit_button2 = WebDriverWait(driver, 10).until(
         EC.element_to_be_clickable((By.XPATH, "(//button[@data-qa='btn-submit'])[1]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button2)
    submit_button2.click()

def answer_questions_eight(driver):
    # Navigate to course 8 page
    driver.get("https://learndiaunjaicyber.ais.co.th/course/15/playlist/42?learningpath_id=145&learningpath_sectionid=178")
    progress_button = WebDriverWait(driver, 10).until(
         EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa='btn-progress']"))
    )
    progress_button.click()
    question_containers = WebDriverWait(driver, 10).until(
         EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.test-question.question"))
    )
    answer_dict8 = {
        "ประเภทของร่องรอยทางไซเบอร์": "ถูกทั้งข้อ ก. และข้อ ข.",
        "พฤติกรรมการป้องกันตัวเองบนโลกออนไลน์ที่ผิดวิธี": "นายศักรินทร์ ตั้งรหัสผ่านตามเบอร์โทรศัพท์เพื่อให้ง่ายต่อการจดจำ",
        "ร่องรอยทางไซเบอร์ แบ่งออกเป็น": "3 ประเภท",
        "การป้องกันร่องรอยทางไซเบอร์ที่ถูกต้อง": "นางวิภาวี คำนึงอยู่เสมอว่าโลกออนไลน์เป็นพื้นที่สาธารณะ มากกว่าเป็นพื้นที่ส่วนตัว เลยต้องคิดอย่างมีวิจารณญาณทุกครั้งที่เข้าใช้งาน",
        "ไม่ใช่ แนวทางการป้องกันและลดร่องรอย": "ปิดเครื่องคอมพิวเตอร์ทุกครั้งหลังจากใช้งานเสร็จ",
        "ประโยชน์ของร่องรอยทางไซเบอร์": "ถูกทุกข้อ",
        "การป้องกันตัวเองบนโลกออนไลน์อย่างถูกวิธี": "ถูกทุกข้อ",
        "ข้อมูลอะไร ที่ถูกบันทึก": "ถูกทุกต้อง",
        "หลักฐานการกระทำ": "ร่องรอยทางไซเบอร์",
        "ร่องรอยทางไซเบอร์ที่ผู้ใช้ไม่มีเจตนา": "IP Address"
    }
    for i, container in enumerate(question_containers):
        if i == 0:
            time.sleep(2)
        question_text = container.find_element(By.CSS_SELECTOR, "div[data-qa='question-desc']").text
        print(f"Course 8 - Processing question: {question_text}")
        expected_letter = None
        for key, letter in answer_dict8.items():
            if key in question_text:
                expected_letter = letter
                break
        if not expected_letter:
            print("Course 8 - No matching key found. Skipping.")
            continue
        choices = container.find_elements(By.CSS_SELECTOR, "label[role='radio']")
        selected = False
        for choice in choices:
            full_choice = choice.text.strip()
            if len(full_choice) > 2 and full_choice[1] == '.':
                full_choice = full_choice[2:].strip()
            if full_choice.lower() == expected_letter.lower():
                driver.execute_script("arguments[0].scrollIntoView(true);", choice)
                for _ in range(2):  # force click twice
                    driver.execute_script("arguments[0].click();", choice)
                    time.sleep(0.1)
                selected = True
                break
        if not selected:
            print(f"Course 8 - No valid choice for letter {expected_letter}")
    submit_button1 = WebDriverWait(driver, 10).until(
         EC.element_to_be_clickable((By.XPATH, "(//button[@data-qa='btn-submit'])[1]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button1)
    submit_button1.click()
    time.sleep(1)
    submit_button2 = WebDriverWait(driver, 10).until(
         EC.element_to_be_clickable((By.XPATH, "(//button[@data-qa='btn-submit'])[1]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button2)
    submit_button2.click()

def answer_questions_nine(driver):
    # Navigate to course 9 page
    driver.get("https://learndiaunjaicyber.ais.co.th/course/87/playlist/2114?learningpath_id=145&learningpath_sectionid=180")
    progress_button = WebDriverWait(driver, 10).until(
         EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa='btn-progress']"))
    )
    progress_button.click()
    
    question_containers = WebDriverWait(driver, 10).until(
         EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.test-question.question"))
    )
    
    answer_dict9 = {
        "แบ็คอัพข้อมูลสมาร์ทโฟน": "เพื่อป้องกันการสูญหายของข้อมูลในกรณีที่โทรศัพท์หาย",
        "ดาวน์โหลดแอพพลิเคชันจากแหล่งที่น่าเชื่อถือ": "เพื่อป้องกันไวรัส มัลแวร์ และได้ใช้งานแอพพลิเคชันที่มีคุณภาพดี",
        "ข้อควรระวังในการใช้งาน WiFi สาธารณะ": "อาจมีผู้ไม่หวังดีแอบดักข้อมูลของคุณ",
        "การตั้งรหัสผ่านบนสมาร์ทโฟนมีรูปแบบใดบ้าง": "แบบ PIN Code และ แบบ Pattern",
        "รหัสผ่านที่ยากต่อการคาดเดา": "เพื่อป้องกันการเข้าถึงข้อมูลโดยไม่ได้รับอนุญาต",
        "อัปเดตซอฟต์แวร์สมาร์ทโฟน": "ช่วยแก้ไขช่องโหว่และป้องกันภัยคุกคามใหม่ๆ",
        "เพิ่มความปลอดภัยให้กับสมาร์ทโฟน": "หมั่น Back up ข้อมูล และ ปิด WiFi สาธารณะเมื่อไม่ได้ใช้งาน",
        "https:// มีความสำคัญ": "เป็นเว็บไซต์ที่มีความปลอดภัยในการรับส่งข้อมูล"
    }
    
    for i, container in enumerate(question_containers):
        if i == 0:
            time.sleep(2)
        question_text = container.find_element(By.CSS_SELECTOR, "div[data-qa='question-desc']").text
        print(f"Course 9 - Processing question: {question_text}")
        
        expected_answer = None
        for key, answer in answer_dict9.items():
            if key in question_text:
                expected_answer = answer
                break
        if not expected_answer:
            print("Course 9 - No matching question found. Skipping.")
            continue
        
        choices = container.find_elements(By.CSS_SELECTOR, "label[role='radio']")
        selected = False
        for choice in choices:
            full_choice = choice.text.strip()
            if len(full_choice) > 2 and full_choice[1] == '.':
                full_choice = full_choice[2:].strip()  # Remove prefix
            if full_choice.lower() == expected_answer.lower():
                driver.execute_script("arguments[0].scrollIntoView(true);", choice)
                for _ in range(2):  # force click twice
                    driver.execute_script("arguments[0].click();", choice)
                    time.sleep(0.1)
                selected = True
                break
        if not selected:
            print(f"Course 9 - No valid choice found for: {expected_answer}")
    # Submit answers for course 9
    submit_button1 = WebDriverWait(driver, 10).until(
         EC.element_to_be_clickable((By.XPATH, "(//button[@data-qa='btn-submit'])[1]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button1)
    submit_button1.click()
    time.sleep(1)
    submit_button2 = WebDriverWait(driver, 10).until(
         EC.element_to_be_clickable((By.XPATH, "(//button[@data-qa='btn-submit'])[1]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button2)
    driver.execute_script("arguments[0].click();", submit_button2)

def answer_questions_ten(driver):
    # Navigate to course 10 page
    driver.get("https://learndiaunjaicyber.ais.co.th/course/88/playlist/2116?learningpath_id=145&learningpath_sectionid=180")
    progress_button = WebDriverWait(driver, 10).until(
         EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa='btn-progress']"))
    )
    progress_button.click()
    question_containers = WebDriverWait(driver, 10).until(
         EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.test-question.question"))
    )
    # Fixed answer mapping for course 10 (using full answer texts)
    answer_dict10 = {
        "ข้อมูลที่โพสต์หรือแชร์ไปแล้ว": "Cloud Storage",
        "ข้อใด คือ Passive Digital Footprint": "ประวัติการค้นหาบนอินเทอร์เน็ต",
        "การตั้งค่าความเป็นส่วนตัวในโซเชียลมีเดียมีประโยชน์อย่างไร": "ป้องกันการเข้าถึงข้อมูลจากผู้ที่ไม่ได้รับอนุญาต",
        "ข้อใด ไม่ใช่ วิธีการป้องกันการทิ้งรอยดิจิทัลที่ไม่ปลอดภัย": "แชร์ข้อมูลส่วนตัวกับทุกคน",
        "การตั้งค่าความเป็นส่วนตัวไม่ให้เป็นสาธารณะช่วยป้องกันอะไร?": "การเข้าถึงข้อมูลส่วนตัวจากบุคคลที่ไม่เกี่ยวข้อง",
        "เพราะเหตุใดการเปิดเผยข้อมูลส่วนตัวมากเกินไปในโลกดิจิทัลจึงเป็นอันตราย": "ทำให้ผู้ไม่หวังดีสามารถสืบค้นและปลอมแปลงตัวตนได้ง่ายขึ้น",
        "Digital Footprint คือ": "การบันทึกข้อมูลทางดิจิทัลที่เกิดจากการโพสต์ แชร์ หรือป้อนข้อมูลเข้าสู่ระบบออนไลน์",
        "ข้อใดเป็นลักษณะของ Active Digital Footprint": "การกดไลก์โพสต์ของเพื่อน"
    }
    for container in question_containers:
        # Use a standard short sleep to allow animations to complete
        time.sleep(1)
        question_text = container.find_element(By.CSS_SELECTOR, "div[data-qa='question-desc']").text
        print(f"Course 10 - Processing question: {question_text}")
        expected_answer = None
        for key, answer in answer_dict10.items():
            if key in question_text:
                expected_answer = answer
                break
        if not expected_answer:
            print("Course 10 - No matching question found. Skipping.")
            continue
        choices = container.find_elements(By.CSS_SELECTOR, "label[role='radio']")
        selected = False
        for choice in choices:
            full_choice = choice.text.strip()
            if len(full_choice) > 2 and full_choice[1] == '.':
                full_choice = full_choice[2:].strip()  # Remove prefix
            if full_choice.lower() == expected_answer.lower():
                driver.execute_script("arguments[0].scrollIntoView(true);", choice)
                for _ in range(2):  # force click twice
                    driver.execute_script("arguments[0].click();", choice)
                    time.sleep(0.1)
                selected = True
                break
        if not selected:
            print(f"Course 10 - No matching choice found for: {expected_answer}")
    submit_button1 = WebDriverWait(driver, 10).until(
         EC.element_to_be_clickable((By.XPATH, "(//button[@data-qa='btn-submit'])[1]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button1)
    submit_button1.click()
    time.sleep(1)
    submit_button2 = WebDriverWait(driver, 10).until(
         EC.element_to_be_clickable((By.XPATH, "(//button[@data-qa='btn-submit'])[1]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button2)
    # Wait for the loading overlay to disappear before clicking the submit button
    WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "div[data-qa='loading']")))
    driver.execute_script("arguments[0].click();", submit_button2)

def answer_questions_eleven(driver):
    # Navigate to course 11 page
    driver.get("https://learndiaunjaicyber.ais.co.th/course/89/playlist/2118?learningpath_id=145&learningpath_sectionid=180")
    progress_button = WebDriverWait(driver, 20).until(  # increased timeout to 20 seconds
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa='btn-progress']"))
    )
    progress_button.click()  # Fixed: now invoking the click
    
    # ...existing code to wait for question containers...
    question_containers = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.test-question.question"))
    )
    
    # Updated answer mapping with questions and their correct answer text
    answer_dict11 = {
        "WiFi ย่อมาจากอะไร": "Wireless Fidelity",
        "เทคโนโลยี WiFi ทำงานอย่างไร": "ใช้คลื่นวิทยุในการติดต่อสื่อสารระหว่างอุปกรณ์",
        "วิธีใดที่แฮกเกอร์ใช้ในการดักข้อมูล WiFi ปลอม": "การตั้งชื่อ WiFi ให้คล้ายกับ WiFi จริง",
        "เพราะเหตุใดการใช้ WiFi สาธารณะจึงเสี่ยงต่อการถูกแฮกข้อมูล": "เพราะ ข้อมูลสามารถถูกดักฟังหรือเปลี่ยนแปลงโดยแฮกเกอร์ได้ง่าย",
        "ข้อใดเป็นวิธีการป้องกันภัยจาก WiFi สาธารณะที่ถูกต้อง": "ตรวจสอบชื่อ WiFi Network Name และรหัสผ่านก่อนเชื่อมต่อ",
        "Man in the middle (MITM) คืออะไร": "รูปแบบการโจมตีที่แฮกเกอร์แทรกกลางการรับส่งข้อมูล",
        "เมื่อเชื่อมต่อ WiFi สาธารณะควรหลีกเลี่ยงการทำสิ่งใด": "การทำธุรกรรมออนไลน์",
        "War Driver คืออะไร": "การขับรถวนหาสัญญาณ WiFi ที่ไม่ปลอดภัย"
    }

    for i, container in enumerate(question_containers):
        if i == 0:
            time.sleep(2)
            
        question_text = container.find_element(By.CSS_SELECTOR, "div[data-qa='question-desc']").text
        print(f"Course 11 - Processing question: {question_text}")
        
        expected_answer = None
        for key, answer in answer_dict11.items():
            if key in question_text:
                expected_answer = answer
                break
                
        if not expected_answer:
            print("Course 11 - No matching question found. Skipping.")
            continue
            
        choices = container.find_elements(By.CSS_SELECTOR, "label[role='radio']")
        selected = False
        
        for choice in choices:
            # Get the full text of the choice without the letter prefix
            full_choice = choice.text.strip()
            if len(full_choice) > 2:  # Make sure it's not just the letter
                full_choice = full_choice[2:].strip()  # Remove the letter prefix (ก., ข., etc.)
                
            if full_choice.lower() == expected_answer.lower():
                driver.execute_script("arguments[0].scrollIntoView(true);", choice)
                for _ in range(2):  # force click twice
                    driver.execute_script("arguments[0].click();", choice)
                    time.sleep(0.1)
                selected = True
                break
                
        if not selected:
            print(f"Course 11 - No matching answer found for: {expected_answer}")
            
    submit_button1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//button[@data-qa='btn-submit'])[1]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button1)
    submit_button1.click()
    
    time.sleep(1)
    
    submit_button2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//button[@data-qa='btn-submit'])[1]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button2)
    submit_button2.click()

def answer_questions_twelve(driver):
    # Navigate to test page 14
    driver.get("https://learndiaunjaicyber.ais.co.th/test/14/?learningpath_id=145&learningpath_sectionid=180")
    # Wait longer for the loading overlay to disappear and force-remove if needed
    WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.ID, "full-loading")))
    driver.execute_script("if(document.getElementById('full-loading')) { document.getElementById('full-loading').remove(); }")
    progress_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-qa='btn-progress']"))
    )
    # Use JavaScript click to bypass overlay interception
    driver.execute_script("arguments[0].click();", progress_button)
    # Wait for question containers to load
    question_containers = WebDriverWait(driver, 10).until(
         EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.test-question.question"))
    )
    # Mapping question snippets to expected answer texts for course 12 (40 items)
    answer_dict12 = {
        "ท่านคิดว่าข้อใดต่อไปนี้เป็นรหัสผ่าน (password) ที่ยากต่อการคาดเดามากที่สุด": "ดรุนัย ตั้งรหัสผ่านเป็น Skb300125@21",#1
        "antivirus software is out of date": "ธยาดา รีบดำเนินการอัพเดทซอฟต์แวร์ต้านไวรัสให้เป็นเวอร์ชันล่าสุด",#2
        "พฤติกรรมในข้อใดเป็นการใช้ทักษะการวิเคราะห์เพื่อรู้เท่าทันสื่อ": "อะตอมตัดสินคุณค่าของข้อมูลบนพื้นฐานของหลักการต่าง ๆ",#3
        "ข้อใดมีความเสี่ยงในการจัดการความเป็นส่วนตัวน้อยที่สุด": "ตั้งค่าในอินสตราแกรมให้เพื่อนเท่านั้นที่เห็นกิจกรรมของตนเอง",
        "ข้อใด ไม่ใช่ ประโยชน์ของการจัดการร่องรอยทางไซเบอร์": "ช่วยให้ผู้ใช้งานบนระบบอินเทอร์เน็ตเข้าถึงข้อมูลส่วนตัวและข้อมูลบัญชี ผู้อื่นทางไซเบอร์",#4
        "ข้อใดเป็นการสร้างอัตลักษณ์พลเมืองไซเบอร์": "การแสดงตัวตนในโลกออนไลน์ให้ตรงกับโลกความเป็นจริง",#5
        "บุคคลในข้อใดแสดงถึงการทิ้งร่องรอยทางไซเบอร์ แบบมีเจตนาบันทึกไว้ในโลกออนไลน์": "ใบเตย แชร์ที่อยู่ของตนเองผ่านสื่อสังคมออนไลน์",#6
        "ข้อใด ไม่ใช่ แนวทางการป้องกันภัยคุกคามและลดร่องรอยทางไซเบอร์": "การเก็บข้อมูลไว้ที่เครื่องคอมพิวเตอร์อย่างเดียวโดยไม่สำรองไว้ที่แหล่งอื่น",#7
        "พฤติกรรมข้อใดใช้ทักษะการมีส่วนร่วมเพื่อรู้เท่าทันสื่อ": "พราวนำคลิปของเทรนเนอร์ในต่างประเทศมาดัดแปลงให้เหมาะกับคนไทย",#8
        "คุณธรรมในข้อใดสำคัญที่สุดในการสร้างอัตลักษณ์พลเมืองไซเบอร์": "ความซื่อสัตย์",#9
        "เมื่อพบข่าวเกี่ยวกับความลับด้านไม่ดีของดาราในสังคมออนไลน์": "ไม่ต้องดำเนินการใดๆ",#10
        "ข้อใดหมายถึงการรู้เท่าทันสื่อในเรื่องมิติเวลา (Time)": "การรู้ตัวว่าเวลาใดควรใช้หรือควรใส่ใจกับกิจกรรมอื่น ๆ บ้าง",#11
        "ข้อใดเป็นการใช้เวลาหน้าจอแบบ ไม่มี การโต้ตอบ": "การดูโทรทัศน์",#12
        "นฤบดีถูกเพื่อนแฮ็กเฟซบุ๊กแล้วใช้แอบอ้างเพื่อยืมเงิน เป็นการกลั่นแกล้งทางไซเบอร์แบบใด": "แบบที่ 5) การโจรกรรมอัตลักษณ์ดิจิทัลของผู้อื่นเพื่อนำไปใช้แอบอ้าง",#13
        "ข้อใดเป็นผลจากการมีทักษะการเอาใจเขามาใส่ใจเราทางไซเบอร์": "เกิดพฤติกรรมอันพึงประสงค์ทางไซเบอร์",#14
        "บุคคลในข้อใดแสดงถึงการใช้ทักษะการจัดการร่องรอยทางไซเบอร์ไม่ถูกต้อง": "อุทัย สมัครแอปพลิเคชัน โดยกดยอมรับทุกข้อตกลงในการให้ข้อมูลและยินยอมให้ข้อมูลส่วนบุคคล",#15
        "เมื่อได้รับข้อความติเตียนเพื่อนที่ไม่เป็นความจริง ควรทำอย่างไร": "แจ้งให้คุณครู ผู้ปกครอง หรือคนที่ใกล้ชิดกับสุเชาว์ และสุรัตน์ทราบ เพื่อหาทางแก้ไข",#16
        "หากเพื่อนโพสต์ข้อความต่อว่าให้เกิดความเสียหายที่ไม่เป็นความจริง ควรทำอย่างไร": "โพสต์ชี้แจงว่าไม่ใช่เรื่องจริง",#17
        "ข้อใด ไม่ใช่ ผลกระทบจากการรั่วไหลของข้อมูลในบัญชีโซเชียลมีเดีย": "ทุกข้อเป็นผลกระทบที่อาจจะเกิดขึ้น",#18
        "การถูกบล็อกไม่ให้เข้ากลุ่มเพื่อนร่วมรุ่น เป็นการกลั่นแกล้งทางไซเบอร์แบบใด": "แบบที่ 3) การกีดกันออกจากกลุ่ม",#19
        "การพิมพ์ username และ password เพื่อเข้าใช้อีเมล เป็นการแสดงตัวตนทางไซเบอร์แบบใด": "การยืนยันว่า ""นี่ฉันเอง""",#
        "บุคคลในข้อใดแสดงถึงการใช้ทักษะการจัดการร่องรอยทางไซเบอร์ไม่ถูกต้อง": "อุทัย สมัครแอปพลิเคชัน โดยกดยอมรับทุกข้อตกลงในการให้ข้อมูลและยินยอมให้ข้อมูลส่วนบุคคล",#20
        "การแอบดูเฟซบุ๊กและไลน์ของผู้อื่นเป็นการทำผิดจริยธรรมทางเทคโนโลยีสารสนเทศด้านใด": "ความเป็นส่วนตัว (Privacy)",#21
        "ข้อใด คือ ความหมายของร่องรอยทางไซเบอร์": "ข้อมูลที่ผู้ใช้งานออนไลน์กระทําไว้ สามารถติดตามได้ หากผู้ใช้กระทําผิดกฎหมายหรือศีลธรรมจะมีผลกระทบต่อชื่อเสียงและภาพลักษณะได้",#22
        "นลินีถูกขู่ว่าจะทำร้ายถ้าเปิดเผยเรื่องเสพยา เป็นการกลั่นแกล้งทางไซเบอร์แบบใด": "แบบที่ 6) การก่อกวน คุกคาม และข่มขู่ โดยการสอดแนมบนโลกออนไลน์",#23
        "ข้อใดแสดงการปฏิบัติต่อเพื่อนเหมือนที่ต้องการให้เพื่อนปฏิบัติต่อเราทางไซเบอร์": "ภีม แสดงความคิดเห็นที่เฟซบุ๊กของเพื่อนด้วยถ้อยคำสุภาพ",#24
        "ข้อใดไม่ใช่องค์ประกอบของทักษะการรู้เท่าทันสื่อ?": "ทักษะการแก้ปัญหา",#25
        "ผลกระทบที่จะเกิดขึ้นกับผู้ที่เล่นเกมออนไลน์นานๆ มากที่สุดเป็นลำดับแรก คือข้อใด": "ความเมื่อยล้าของนิ้วมือ คอ หลัง",#26
        "การดาวน์โหลดแอปพลิเคชัน ควรปฏิบัติอย่างไรให้ปลอดภัยที่สุด": "อ่านข้อตกลงและเงื่อนไขการใช้งานว่าจะอนุญาตให้แอปพลิเคชันเข้าถึงข้อมูลส่วนบุคคลใดได้บ้าง",#27
        "ในช่วงโควิด-19 ข้อใดแสดงอัตลักษณ์พลเมืองไซเบอร์ไม่เหมาะสม": "โพสต์ภาพผู้เสียชีวิตจากการฉีดวัคซีนโดยไม่ปิดบังใบหน้า",#28
        "ข้อใดเป็นผลกระทบทางด้านสังคมจากการใช้เวลาหน้าจอมากเกินไป": "มีพฤติกรรมก้าวร้าวขึ้น",#29
        "ข้อใดถือเป็นมารยาททางไซเบอร์": "ใช้ถ้อยคำสุภาพในการติดต่อสื่อสารกับผู้อื่นทางไซเบอร์",#30
        "เครือข่ายอินเทอร์เน็ตจากแหล่งใดปลอดภัยที่สุดสำหรับการโอนเงิน": "เครือข่ายอินเทอร์เน็ตของโทรศัพท์มือถือ",#31
        "การเปิดเผยข้อมูลส่วนบุคคลของผู้อื่นในข้อใดถือว่าเป็นการกระทำความผิด": "มดโพสต์ภาพแอบถ่ายขณะที่เพื่อนเผลอ",#32
        "การใช้ชื่อล็อกอินและรหัสผ่านเดียวกันสำหรับทุกแอคเคาท์ควรทำอย่างไร": "ไม่ควรใช้รหัสผ่านเดียวกันกับทุกแอคเคาท์ของตัวเอง",#33
        "การจัดการความเป็นส่วนตัวในข้อใดมีความเสี่ยงมากที่สุด": "บอกรหัสผ่านให้เพื่อนสนิททราบ",#34
        "พฤติกรรมในข้อใดที่ใช้หน้าจออย่างมีเป้าหมายได้เหมาะสมที่สุด": "ส้มปิดการแจ้งเตือนจากไลน์ขณะเรียนออนไลน์",#35
        "ข้อใด ไม่ ถือว่าเป็นการใช้เวลาหน้าจอ (Screen Time)": "การอ่านหนังสือด้านเทคโนโลยี",#36
        "ข้อมูลใดต่อไปนี้ ไม่ ควรเผยแพร่ไปในเครือข่ายสังคมออนไลน์": "ทุกข้อไม่ควรเผยแพร่",#37

        "ในช่วงสถานการณ์การแพร่ระบาดของโควิด-19 ข้อใดแสดงอัตลักษณ์พลเมืองไซเบอร์ไม่เหมาะสม": "โพสต์ภาพผู้เสียชีวิตจากการฉีดวัคซีนโดยไม่ปิดบังใบหน้า",#38
        "สุริวิภา ได้รับข้อความจากสุเชาว์ทางไลน์ในเชิงติเตียนว่า สุรัตน์ เพื่อนของเธออีกคน มีพฤติกรรมยืมเงินแล้วไม่คืน ทั้งที่ความจริงหาเป็นเช่นนั้นไม่": "แจ้งให้คุณครู ผู้ปกครอง หรือคนที่ใกล้ชิดกับสุเชาว์ และสุรัตน์ทราบ เพื่อหาทางแก้ไข" ,#added
        "ถ้าหากท่านอ่านเจอข่าวเกี่ยวกับความลับด้านไม่ดีของดารา นักกีฬา หรือ คนดังในวงการต่างๆ ในสังคมออนไลน์ ท่านจะปฏิบัติตัวอย่างไร": "ไม่ต้องดำเนินการใดๆ",#added
        "นฤบดี ถูกเพื่อนแฮ็กเฟซบุ๊กแล้วใช้แอบอ้างเพื่อยืมเงินของเพื่อนอีกคนหนึ่งเป็นการถูกกลั่นแกล้งทางไซเบอร์แบบใด?": "แบบที่ 5)",#added
        "“ต้นกล้าชอบเล่นเกมออนไลน์กับเพื่อนมาก และใช้เวลาในการเล่นเกมแต่ละครั้งเป็นชั่วโมง” จากข้อความดังกล่าว ผลกระทบที่จะเกิดขึ้นกับต้นกล้ามากที่สุดเป็นลำดับแรก คือข้อใด": "ความเมื่อยล้าของนิ้วมือ คอ หลัง",#added
        "เมื่อต้องการดาวน์โหลดแอปพลิเคชันบนโทรศัพท์มือถือ ท่านควรปฏิบัติตนตามข้อใดจึงจะทำให้ข้อมูลส่วนบุคคลมีความปลอดภัยมากที่สุด": "อ่านข้อตกลงและเงื่อนไขการใช้งานว่าจะอนุญาตให้แอปพลิเคชันเข้าถึงข้อมูลส่วนบุคคลใดได้บ้าง",#added
        "ข้อใด ไม่ใช่ ผลกระทบที่เกิดจากการรั่วไหลของข้อมูลที่ละเอียดอ่อนในบัญชีโซเชียลมีเดียของท่าน ทั้งโดยไม่ได้ตั้งใจหรือโดยเจตนา": "ทุกข้อเป็นผลกระทบที่อาจจะเกิดขึ้น",#added
        "ข้อใดอธิบายความหมายของความสามารถในการเข้าถึงสื่อได้ถูกต้อง": "ความสามารถในการตระหนักถึงผลกระทบของเนื้อหา",#added
        "หากเพื่อนโพสต์ข้อความทางเฟซบุ๊กต่อว่าท่านให้เกิดความเสียหาย ทั้งที่เรื่องเหล่านั้นไม่ใช่ความจริง ท่านควรปฏิบัติตนตามข้อใดจึงจะเหมาะสมที่สุด": "โพสต์ชี้แจงว่าไม่ใช่เรื่องจริง",#added
        "นลินี ถูกเพื่อนผู้ชายต่างโรงเรียนส่งข้อความในอินบอกซ์เฟซบุ๊กของเธอ โดยขู่ว่าจะทำร้าย ถ้าหากเธอนำเรื่องที่เขากับเพื่อนเสพยาเสพติด": "แบบที่ 6)",#added
        "บุคคลในข้อใดแสดงให้เห็นว่าได้ปฏิบัติต่อเพื่อนเหมือนที่ต้องการให้เพื่อนปฏิบัติต่อเราทางไซเบอร์": "ภีม แสดงความคิดเห็นที่เฟซบุ๊กของเพื่อนด้วยถ้อยคำสุภาพ",#added
        "นุ่นกำลังซื้อของที่ห้างสรรพสินค้า และต้องการโอนเงินผ่านแอปพลิเคชันของธนาคาร นุ่นควรเลือกใช้เครือข่ายอินเตอร์เน็ตจากแหล่งใดจึงจะปลอดภัยที่สุด": "เครือข่ายอินเทอร์เน็ตของโทรศัพท์มือถือ",#added
        "ข้อใดเป็นผลกระทบทางด้านสังคมที่เกิดขึ้นจากการใช้เวลาหน้าจอมากเกินไป": "มีพฤติกรรมก้าวร้าวขึ้น",#added
        "การพิมพ์ชื่อผู้ใช้ (username) และรหัสผ่าน (password) เพื่อเข้าใช้งานอีเมล เป็นการแสดงตัวตนทางไซเบอร์ในรูปแบบใด": "การยืนยันว่า “นี่ฉันเอง”",#added
        "ท่านคิดเห็นอย่างไรกับการใช้ชื่อล็อกอินและรหัสผ่านเดียวกันสำหรับเข้าสู่ระบบทุกแอคเคาท์ของท่าน?": "ไม่ควรใช้รหัสผ่านเดียวกันกับทุกแอคเคาท์ของตัวเอง",#added
        "นายเอกขอใช้คอมพิวเตอร์ของนายบอยแต่ถือโอกาสเข้าไปดูเฟซบุ๊ก ไลน์และรูปส่วนตัวที่นายบอยที่บันทึกในเครื่องคอมพิวเตอร์ การกระทำของนายเอกถือเป็นการทำผิดจริยธรรมทางเทคโนโลยีสารสนเทศด้านใด": "ความเป็นส่วนตัว (Privacy)",#added
        # "Other__": "Other__",#added
        # "Other__": "Other__",#added
        # "Other__": "Other__",#added
    }
    for i, container in enumerate(question_containers):
        if i == 0:
            time.sleep(2)
        question_text = container.find_element(By.CSS_SELECTOR, "div[data-qa='question-desc']").text
        print(f"Course 12 - Processing question: {question_text}")
        expected_answer = None
        for key, answer in answer_dict12.items():
            if key in question_text:
                expected_answer = answer
                break
        if not expected_answer:
            print("Course 12 - No matching key found. Skipping.")
            continue
        choices = container.find_elements(By.CSS_SELECTOR, "label[role='radio']")
        selected = False
        for choice in choices:
            full_choice = choice.text.strip()
            if len(full_choice) > 2 and full_choice[1] == '.':
                full_choice = full_choice[2:].strip()
            if full_choice.lower() == expected_answer.lower():
                driver.execute_script("arguments[0].scrollIntoView(true);", choice)
                for _ in range(2):
                    driver.execute_script("arguments[0].click();", choice)
                    time.sleep(0.1)
                selected = True
                break
        if not selected:
            print(f"Course 12 - No valid choice found for question matching {expected_answer}")
        time.sleep(3)  # Add delay after processing each question
    # Submit answers for course 12
    submit_button1 = WebDriverWait(driver, 10).until(
         EC.element_to_be_clickable((By.XPATH, "(//button[@data-qa='btn-submit'])[1]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button1)
    submit_button1.click()
    time.sleep(1)
    submit_button2 = WebDriverWait(driver, 10).until(
         EC.element_to_be_clickable((By.XPATH, "(//button[@data-qa='btn-submit'])[1]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button2)
    submit_button2.click()

def main():
    driver = webdriver.Chrome()  # Make sure you have ChromeDriver installed
    try:
        # your username and password 
        username = "YOUR_USERNAME"
        password = "YOUR PASSWORD"
        
        login_and_navigate(driver, username, password)

        answer_questions(driver)
        answer_questions_second(driver)
        answer_questions_third(driver)
        answer_questions_four(driver)
        answer_questions_five(driver)
        answer_questions_six(driver)
        answer_questions_seven(driver)
        answer_questions_eight(driver)
        answer_questions_nine(driver)
        answer_questions_ten(driver)
        answer_questions_eleven(driver)
        answer_questions_twelve(driver)
        
        time.sleep(5)  # Wait to see results
    finally:
        driver.quit()

if __name__ == "__main__":
    main()