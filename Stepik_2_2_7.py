import os
from selenium import webdriver
import time


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    browser.find_element_by_name("firstname").send_keys("Ivan")
    browser.find_element_by_name("lastname").send_keys("Kozhedub")
    browser.find_element_by_name("email").send_keys("Logitech@mail.ru")
    send = browser.find_element_by_id("file")
    curen = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(curen,"file.txt")
    send.send_keys(file_path)
    browser.find_element_by_css_selector(".btn").click()



finally:
    time.sleep(3)
    browser.quit()