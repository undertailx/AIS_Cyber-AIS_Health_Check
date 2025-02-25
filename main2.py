# WORKING 99.88%
# https://digitalhealthcheck.ais.th/th/home  # AUTO 3 STRAS ALL STAGES

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# setting cookie for login
def set_login_cookie(driver):
    driver.get("https://aunjaicheck.ais.th")
    cookie1 = {
        'name': 'XSRF-TOKEN',
        'value': 'YOUR_COOKIE_HERE',
        'domain': 'aunjaicheck.ais.th',
        'path': '/'
    }
    cookie2 = {
        'name': 'aisdigitalhealthcheck_session',
        'value': 'YOUR_COOKIE_HERE',
        'domain': 'aunjaicheck.ais.th',
        'path': '/'
    }
    driver.add_cookie(cookie1)
    driver.add_cookie(cookie2)

def answer_questions(driver):
    # ตั้งค่าพื้นฐาน
    answer_sequence = "ynyyyyyyyyyyynnyyyyyy"
    
    # เข้าสู่หน้าแบบทดสอบ
    set_login_cookie(driver)
    driver.get("https://aunjaicheck.ais.th/th/member/query/1/cyber-security-and-safety")
    time.sleep(1)
    
    for q_num, answer in enumerate(answer_sequence, 1):
        try:
            # เลือกคำตอบ yes หรือ no
            value = "no" if answer.lower() == 'n' else "yes"
            
            # ใช้ JavaScript ค้นหาและคลิกตัวเลือก
            script = f"""
                // หาตัวเลือกทั้งหมดที่กำลังแสดงอยู่
                var choices = Array.from(document.querySelectorAll('label.game-options__choice'));
                var targetChoice = choices.find(el => {{
                    var input = el.querySelector('input[value="{value}"]');
                    return input && el.offsetParent !== null;
                }});
                
                // คลิกตัวเลือกถ้าพบ
                if (targetChoice) {{
                    targetChoice.click();
                    console.log("คลิกตัวเลือก {value} สำเร็จ");
                }}
                return targetChoice !== null;
            """
            clicked = driver.execute_script(script)
            
            if not clicked:
                print(f"ไม่พบตัวเลือก {value} สำหรับคำถามที่ {q_num}")
            
            time.sleep(0.5)
            
            # คลิกปุ่ม Next ด้วย JavaScript
            next_script = """
                var nextBtn = document.getElementById('next');
                if (nextBtn) {
                    nextBtn.style.display = 'block';
                    nextBtn.style.opacity = '1';
                    nextBtn.disabled = false;
                    nextBtn.click();
                    return true;
                }
                return false;
            """
            next_clicked = driver.execute_script(next_script)
            
            if not next_clicked:
                print(f"ไม่พบปุ่ม Next สำหรับคำถามที่ {q_num}")
            
            time.sleep(0.5)
            
        except Exception as e:
            print(f"เกิดข้อผิดพลาดที่คำถามที่ {q_num}: {str(e)}")
    
    # คลิกปุ่มส่งคำตอบเมื่อตอบครบทุกข้อ
    try:
        submit_script = """
            // หาปุ่มส่งคำตอบ
            var submitBtn = Array.from(document.querySelectorAll('button')).find(el => 
                el.textContent.includes('ส่งคำตอบ') && el.offsetParent !== null
            );
            
            if (submitBtn) {
                submitBtn.click();
                console.log("คลิกปุ่มส่งคำตอบสำเร็จ");
                return true;
            }
            return false;
        """
        submit_clicked = driver.execute_script(submit_script)
        
        if not submit_clicked:
            print("ไม่พบปุ่มส่งคำตอบ")
    except Exception as e:
        print(f"ไม่สามารถคลิกปุ่มส่งคำตอบ: {str(e)}")

def answer_questions_page2(driver):
    # ตั้งค่าพื้นฐานสำหรับหน้าที่สอง
    answer_sequence = "ynynnn"
    # เข้าสู่หน้าแบบทดสอบหน้าที่สอง
    set_login_cookie(driver)
    driver.get("https://aunjaicheck.ais.th/th/member/query/2/digital-use")
    time.sleep(1)
    
    for q_num, answer in enumerate(answer_sequence, 1):
        try:
            value = "no" if answer.lower() == 'n' else "yes"
            script = f"""
                // หาตัวเลือกทั้งหมดที่กำลังแสดงอยู่
                var choices = Array.from(document.querySelectorAll('label.game-options__choice'));
                var targetChoice = choices.find(el => {{
                    var input = el.querySelector('input[value="{value}"]');
                    return input && el.offsetParent !== null;
                }});
                if (targetChoice) {{
                    targetChoice.click();
                    console.log("คลิกตัวเลือก {value} สำเร็จ");
                }}
                return targetChoice !== null;
            """
            clicked = driver.execute_script(script)
            if not clicked:
                print(f"ไม่พบตัวเลือก {value} สำหรับคำถามที่ {q_num}")
            time.sleep(0.5)
            # คลิกปุ่ม Next ด้วย JavaScript
            next_script = """
                var nextBtn = document.getElementById('next');
                if (nextBtn) {
                    nextBtn.style.display = 'block';
                    nextBtn.style.opacity = '1';
                    nextBtn.disabled = false;
                    nextBtn.click();
                    return true;
                }
                return false;
            """
            next_clicked = driver.execute_script(next_script)
            if not next_clicked:
                print(f"ไม่พบปุ่ม Next สำหรับคำถามที่ {q_num}")
            time.sleep(0.5)
        except Exception as e:
            print(f"เกิดข้อผิดพลาดที่คำถามที่ {q_num}: {str(e)}")
    try:
        submit_script = """
            // หาปุ่มส่งคำตอบ
            var submitBtn = Array.from(document.querySelectorAll('button')).find(el => 
                el.textContent.includes('ส่งคำตอบ') && el.offsetParent !== null
            );
            if (submitBtn) {
                submitBtn.click();
                console.log("คลิกปุ่มส่งคำตอบสำเร็จ");
                return true;
            }
            return false;
        """
        submit_clicked = driver.execute_script(submit_script)
        if not submit_clicked:
            print("ไม่พบปุ่มส่งคำตอบในหน้าที่สอง")
    except Exception as e:
        print(f"ไม่สามารถคลิกปุ่มส่งคำตอบในหน้าที่สอง: {str(e)}")

def answer_questions_page3(driver):
    # ตั้งค่าพื้นฐานสำหรับหน้าที่สาม
    answer_sequence = "yyyyyyyyyyyyyyyyyy"
    set_login_cookie(driver)
    driver.get("https://aunjaicheck.ais.th/th/member/query/5/digital-literacy")
    time.sleep(1)
    
    for q_num, answer in enumerate(answer_sequence, 1):
        try:
            value = "no" if answer.lower()=='n' else "yes"
            script = f"""
                // หาตัวเลือกทั้งหมดที่กำลังแสดงอยู่
                var choices = Array.from(document.querySelectorAll('label.game-options__choice'));
                var targetChoice = choices.find(el => {{
                    var input = el.querySelector('input[value="{value}"]');
                    return input && el.offsetParent !== null;
                }});
                if (targetChoice) {{
                    targetChoice.click();
                    console.log("คลิกตัวเลือก {value} สำเร็จ");
                }}
                return targetChoice !== null;
            """
            clicked = driver.execute_script(script)
            if not clicked:
                print(f"ไม่พบตัวเลือก {value} สำหรับคำถามที่ {q_num}")
            time.sleep(0.5)
            
            next_script = """
                var nextBtn = document.getElementById('next');
                if (nextBtn) {
                    nextBtn.style.display='block';
                    nextBtn.style.opacity='1';
                    nextBtn.disabled=false;
                    nextBtn.click();
                    return true;
                }
                return false;
            """
            next_clicked = driver.execute_script(next_script)
            if not next_clicked:
                print(f"ไม่พบปุ่ม Next สำหรับคำถามที่ {q_num}")
            time.sleep(0.5)
        except Exception as e:
            print(f"เกิดข้อผิดพลาดที่คำถามที่ {q_num}: {str(e)}")
    
    try:
        submit_script = """
            // หาปุ่มส่งคำตอบ
            var submitBtn = Array.from(document.querySelectorAll('button')).find(el =>
                el.textContent.includes('ส่งคำตอบ') && el.offsetParent !== null
            );
            if (submitBtn) {
                submitBtn.click();
                console.log("คลิกปุ่มส่งคำตอบสำเร็จ");
                return true;
            }
            return false;
        """
        submit_clicked = driver.execute_script(submit_script)
        if not submit_clicked:
            print("ไม่พบปุ่มส่งคำตอบในหน้าที่สาม")
    except Exception as e:
        print(f"ไม่สามารถคลิกปุ่มส่งคำตอบในหน้าที่สาม: {str(e)}")

def answer_questions_page4(driver):
    # ตั้งค่าพื้นฐานสำหรับหน้าที่ 4
    answer_sequence = "yyyyyyyyy"
    set_login_cookie(driver)
    driver.get("https://aunjaicheck.ais.th/th/member/query/6/digital-rights")
    time.sleep(1)
    for q_num, answer in enumerate(answer_sequence, 1):
        try:
            value = "no" if answer.lower()=='n' else "yes"
            script = f"""
                // หาตัวเลือกทั้งหมดที่กำลังแสดงอยู่
                var choices = Array.from(document.querySelectorAll('label.game-options__choice'));
                var targetChoice = choices.find(el => {{
                    var input = el.querySelector('input[value="{value}"]');
                    return input && el.offsetParent !== null;
                }});
                if (targetChoice) {{
                    targetChoice.click();
                    console.log("คลิกตัวเลือก {value} สำเร็จ");
                }}
                return targetChoice !== null;
            """
            clicked = driver.execute_script(script)
            if not clicked:
                print(f"ไม่พบตัวเลือก {value} สำหรับคำถามที่ {q_num}")
            time.sleep(0.5)
            next_script = """
                var nextBtn = document.getElementById('next');
                if (nextBtn) {
                    nextBtn.style.display='block';
                    nextBtn.style.opacity='1';
                    nextBtn.disabled=false;
                    nextBtn.click();
                    return true;
                }
                return false;
            """
            next_clicked = driver.execute_script(next_script)
            if not next_clicked:
                print(f"ไม่พบปุ่ม Next สำหรับคำถามที่ {q_num}")
            time.sleep(0.5)
        except Exception as e:
            print(f"เกิดข้อผิดพลาดที่คำถามที่ {q_num}: {str(e)}")
    try:
        submit_script = """
            // หาปุ่มส่งคำตอบ
            var submitBtn = Array.from(document.querySelectorAll('button')).find(el =>
                el.textContent.includes('ส่งคำตอบ') && el.offsetParent !== null
            );
            if (submitBtn) {
                submitBtn.click();
                console.log("คลิกปุ่มส่งคำตอบสำเร็จ");
                return true;
            }
            return false;
        """
        submit_clicked = driver.execute_script(submit_script)
        if not submit_clicked:
            print("ไม่พบปุ่มส่งคำตอบในหน้าที่ 4")
    except Exception as e:
        print(f"ไม่สามารถคลิกปุ่มส่งคำตอบในหน้าที่ 4: {str(e)}")

def answer_questions_page5(driver):
    # ตั้งค่าพื้นฐานสำหรับหน้าที่ 5
    answer_sequence = "nnnnnnnnnnnnnnnnnnn"
    set_login_cookie(driver)
    driver.get("https://aunjaicheck.ais.th/th/member/query/7/cyber-bullying")
    time.sleep(1)
    for q_num, answer in enumerate(answer_sequence, 1):
        try:
            value = "no" if answer.lower()=='n' else "yes"
            script = f"""
                // หาตัวเลือกทั้งหมดที่กำลังแสดงอยู่
                var choices = Array.from(document.querySelectorAll('label.game-options__choice'));
                var targetChoice = choices.find(el => {{
                    var input = el.querySelector('input[value="{value}"]');
                    return input && el.offsetParent !== null;
                }});
                if (targetChoice) {{
                    targetChoice.click();
                    console.log("คลิกตัวเลือก {value} สำเร็จ");
                }}
                return targetChoice !== null;
            """
            clicked = driver.execute_script(script)
            if not clicked:
                print(f"ไม่พบตัวเลือก {value} สำหรับคำถามที่ {q_num}")
            time.sleep(0.5)
            next_script = """
                var nextBtn = document.getElementById('next');
                if (nextBtn) {
                    nextBtn.style.display='block';
                    nextBtn.style.opacity='1';
                    nextBtn.disabled=false;
                    nextBtn.click();
                    return true;
                }
                return false;
            """
            next_clicked = driver.execute_script(next_script)
            if not next_clicked:
                print(f"ไม่พบปุ่ม Next สำหรับคำถามที่ {q_num}")
            time.sleep(0.5)
        except Exception as e:
            print(f"เกิดข้อผิดพลาดที่คำถามที่ {q_num}: {str(e)}")
    try:
        submit_script = """
            // หาปุ่มส่งคำตอบ
            var submitBtn = Array.from(document.querySelectorAll('button')).find(el =>
                el.textContent.includes('ส่งคำตอบ') && el.offsetParent !== null
            );
            if (submitBtn) {
                submitBtn.click();
                console.log("คลิกปุ่มส่งคำตอบสำเร็จ");
                return true;
            }
            return false;
        """
        submit_clicked = driver.execute_script(submit_script)
        if not submit_clicked:
            print("ไม่พบปุ่มส่งคำตอบในหน้าที่ 5")
    except Exception as e:
        print(f"ไม่สามารถคลิกปุ่มส่งคำตอบในหน้าที่ 5: {str(e)}")

def answer_questions_page6(driver):
    # ตั้งค่าพื้นฐานสำหรับหน้าที่ 6
    answer_sequence = "yyyyyyyyyyyyy"
    set_login_cookie(driver)
    driver.get("https://aunjaicheck.ais.th/th/member/query/3/digital-relationship")
    time.sleep(1)
    for q_num, answer in enumerate(answer_sequence, 1):
        try:
            value = "no" if answer.lower()=='n' else "yes"
            script = f"""
                // หาตัวเลือกทั้งหมดที่กำลังแสดงอยู่
                var choices = Array.from(document.querySelectorAll('label.game-options__choice'));
                var targetChoice = choices.find(el => {{
                    var input = el.querySelector('input[value="{value}"]');
                    return input && el.offsetParent !== null;
                }});
                if (targetChoice) {{
                    targetChoice.click();
                    console.log("คลิกตัวเลือก {value} สำเร็จ");
                }}
                return targetChoice !== null;
            """
            clicked = driver.execute_script(script)
            if not clicked:
                print(f"ไม่พบตัวเลือก {value} สำหรับคำถามที่ {q_num}")
            time.sleep(0.5)
            next_script = """
                var nextBtn = document.getElementById('next');
                if (nextBtn) {
                    nextBtn.style.display='block';
                    nextBtn.style.opacity='1';
                    nextBtn.disabled=false;
                    nextBtn.click();
                    return true;
                }
                return false;
            """
            next_clicked = driver.execute_script(next_script)
            if not next_clicked:
                print(f"ไม่พบปุ่ม Next สำหรับคำถามที่ {q_num}")
            time.sleep(0.5)
        except Exception as e:
            print(f"เกิดข้อผิดพลาดที่คำถามที่ {q_num}: {str(e)}")
    try:
        submit_script = """
            // หาปุ่มส่งคำตอบ
            var submitBtn = Array.from(document.querySelectorAll('button')).find(el =>
                el.textContent.includes('ส่งคำตอบ') && el.offsetParent !== null
            );
            if (submitBtn) {
                submitBtn.click();
                console.log("คลิกปุ่มส่งคำตอบสำเร็จ");
                return true;
            }
            return false;
        """
        submit_clicked = driver.execute_script(submit_script)
        if not submit_clicked:
            print("ไม่พบปุ่มส่งคำตอบในหน้าที่ 6")
    except Exception as e:
        print(f"ไม่สามารถคลิกปุ่มส่งคำตอบในหน้าที่ 6: {str(e)}")

def answer_questions_page7(driver):
    # ตั้งค่าพื้นฐานสำหรับหน้าที่ 7
    answer_sequence = "yyyyyyyyyyyyyyyyy"
    set_login_cookie(driver)
    driver.get("https://aunjaicheck.ais.th/th/member/query/4/digital-communications")
    time.sleep(1)
    for q_num, answer in enumerate(answer_sequence, 1):
        try:
            value = "no" if answer.lower()=='n' else "yes"
            script = f"""
                // หาตัวเลือกทั้งหมดที่กำลังแสดงอยู่
                var choices = Array.from(document.querySelectorAll('label.game-options__choice'));
                var targetChoice = choices.find(el => {{
                    var input = el.querySelector('input[value="{value}"]');
                    return input && el.offsetParent !== null;
                }});
                if (targetChoice) {{
                    targetChoice.click();
                    console.log("คลิกตัวเลือก {value} สำเร็จ");
                }}
                return targetChoice !== null;
            """
            clicked = driver.execute_script(script)
            if not clicked:
                print(f"ไม่พบตัวเลือก {value} สำหรับคำถามที่ {q_num}")
            time.sleep(0.5)
            next_script = """
                var nextBtn = document.getElementById('next');
                if (nextBtn) {
                    nextBtn.style.display='block';
                    nextBtn.style.opacity='1';
                    nextBtn.disabled=false;
                    nextBtn.click();
                    return true;
                }
                return false;
            """
            next_clicked = driver.execute_script(next_script)
            if not next_clicked:
                print(f"ไม่พบปุ่ม Next สำหรับคำถามที่ {q_num}")
            time.sleep(0.5)
        except Exception as e:
            print(f"เกิดข้อผิดพลาดที่คำถามที่ {q_num}: {str(e)}")
    try:
        submit_script = """
            // หาปุ่มส่งคำตอบ
            var submitBtn = Array.from(document.querySelectorAll('button')).find(el =>
                el.textContent.includes('ส่งคำตอบ') && el.offsetParent !== null
            );
            if (submitBtn) {
                submitBtn.click();
                console.log("คลิกปุ่มส่งคำตอบสำเร็จ");
                return true;
            }
            return false;
        """
        submit_clicked = driver.execute_script(submit_script)
        if not submit_clicked:
            print("ไม่พบปุ่มส่งคำตอบในหน้าที่ 7")
    except Exception as e:
        print(f"ไม่สามารถคลิกปุ่มส่งคำตอบในหน้าที่ 7: {str(e)}")

def main():
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options)
    
    try:
        answer_questions(driver)
        answer_questions_page2(driver)
        answer_questions_page3(driver)
        answer_questions_page4(driver)
        answer_questions_page5(driver)
        answer_questions_page6(driver)
        answer_questions_page7(driver)
        time.sleep(3)
    except Exception as e:
        print(f"เกิดข้อผิดพลาดหลัก: {str(e)}")
    finally:
        time.sleep(5)
        driver.quit()

if __name__ == "__main__":
    main()