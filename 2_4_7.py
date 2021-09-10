from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

browser = webdriver.Chrome(executable_path="C:/chromedriver/chromedriver.exe")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
#button = WebDriverWait(browser, 5).until(
#        EC.element_to_be_clickable((By.ID, "verify"))
#    )
#button.click()
button_2 = browser.find_element_by_id("book")

browser.execute_script("return arguments[0].scrollIntoView(true);", button_2)

WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

button_3 = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "book"))
    )
button_3.click()

check_1 = browser.find_element_by_css_selector("[id='input_value']")
browser.execute_script("return arguments[0].scrollIntoView(true);", check_1)
num_1 = check_1.text


y = calc(num_1)

answer = browser.find_element_by_css_selector("[id='answer']")
answer.send_keys(y)

check_4 = browser.find_element_by_css_selector("[id='solve']")
browser.execute_script("return arguments[0].scrollIntoView(true);", check_4)
check_4.click()

time.sleep(5)

browser.quit()