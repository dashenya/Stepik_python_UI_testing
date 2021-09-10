import os
from selenium import webdriver
import math
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome(executable_path="C:/chromedriver/chromedriver.exe")
#link = "http://suninjuly.github.io/wait1.html" - рабочая ссылка
#link = "http://suninjuly.github.io/cats.html"
browser.implicitly_wait(5)
browser.get(link)

button = browser.find_element_by_id("verify")
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text

browser.quit()