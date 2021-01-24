from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
link = "http://suninjuly.github.io/math.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)
    people_radio = browser.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value", people_checked)
    assert people_checked is not None, "People radio is not selected by defaut"
    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(y)
    I_M_Robot = browser.find_element_by_css_selector("#robotCheckbox")
    I_M_Robot.click()
    Robot_Rules = browser.find_element_by_css_selector("#robotsRule")
    Robot_Rules.click()
    Submit = browser.find_element_by_css_selector(".btn")
    Submit.click()

finally:
    time.sleep(3)
    browser.quit()
