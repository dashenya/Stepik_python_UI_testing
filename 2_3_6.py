import os
from selenium import webdriver
import math
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome(executable_path="C:/chromedriver/chromedriver.exe")
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

check_1 = browser.find_element_by_css_selector("button.trollface")
#browser.execute_script("return arguments[0].scrollIntoView(true);", check_1)
#time.sleep(2)
check_1.click()

new_window = browser.window_handles[1]
first_w = browser.window_handles[0]
browser.switch_to.window(new_window)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

check_2 = browser.find_element_by_css_selector("[id='input_value']")
num_1 = check_2.text

y = calc(num_1)

answer = browser.find_element_by_css_selector("[id='answer']")
answer.send_keys(y)

button = browser.find_element_by_css_selector("[type='submit']")
button.click()

time.sleep(2)

