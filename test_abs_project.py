from selenium import webdriver
import time
import math

def ans():
    return str(math.log(int(time.time())))

try:
    browser = webdriver.Chrome()

    browser.get("https://stepik.org/lesson/236898/step/1")
    browser.implicitly_wait(10)
    browser.find_element_by_css_selector(".textarea").send_keys(ans())
    browser.find_element_by_css_selector(".submit-submission").click()
    check = browser.find_element_by_css_selector(".smart-hints__hint").text
    print(check)
finally:
    browser.quit()