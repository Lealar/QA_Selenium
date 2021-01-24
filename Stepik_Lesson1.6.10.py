from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    box1 = browser.find_element_by_css_selector(".first_block .first")
    box1.send_keys("abc")
    box2 = browser.find_element_by_css_selector(".first_block .second")
    box2.send_keys("abc2")
    box3 = browser.find_element_by_css_selector(".first_block .third")
    box3.send_keys("abc3")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(3)

    welcome = browser.find_element_by_tag_name("h1")

    welcome = welcome.text
    assert "Congratulations! You have successfully registered!" == welcome

finally:
    time.sleep(10)
    browser.close()
