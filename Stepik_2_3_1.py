""" Задание: принимаем alert
В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/alert_accept.html
Нажать на кнопку
Принять confirm
На новой странице решить капчу для роботов, чтобы получить число с ответом"""

from selenium import webdriver
import math
import time


try:
    browser = webdriver.Chrome()
    time.sleep(6)
    browser.get("http://suninjuly.github.io/alert_accept.html")
    time.sleep(2)
    browser.find_element_by_css_selector(".btn").click()
    time.sleep(2)
    browser.switch_to.alert.accept()
    x = browser.find_element_by_id("input_value").text
    browser.find_element_by_id("answer").send_keys(str(math.log(abs(12 * math.sin(int(x))))))
    time.sleep(1)
    browser.find_element_by_css_selector(".btn").click()
    time.sleep(1)
    ans = browser.switch_to.alert.text.split(": ")
    print(ans)
    time.sleep(2)
    browser.switch_to.alert.accept()
    browser.get('https://stepik.org/course/575/promo?auth=login')
    time.sleep(2)
    browser.find_element_by_css_selector("#id_login_email").send_keys("goosts@mail.ru")
    browser.find_element_by_css_selector("#id_login_password").send_keys("4242564dichenchimdi")
    browser.find_element_by_css_selector(".sign-form__btn").click()
    time.sleep(3)
    browser.get('https://stepik.org/lesson/184253/step/4?unit=158843')
    time.sleep(3)
    browser.execute_script("window.scrollBy(0, 300);")
    browser.find_element_by_css_selector("textarea").send_keys(ans[1])
    browser.find_element_by_css_selector(".submit-submission").click()


finally:
    time.sleep(6)
    browser.quit()