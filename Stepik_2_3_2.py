"""
Задание: переход на новую вкладку
В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно переключить WebDriver на новую вкладку и решить в ней задачу.

Сценарий для реализации выглядит так:

Открыть страницу http://suninjuly.github.io/redirect_accept.html
Нажать на кнопку
Переключиться на новую вкладку
Пройти капчу для робота и получить число-ответ
"""

from selenium import webdriver
import math
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    browser.find_element_by_css_selector(".btn").click()
    new_window = browser.window_handles
    browser.switch_to.window(new_window[1])
    x = browser.find_element_by_css_selector("#input_value").text
    browser.find_element_by_id("answer").send_keys(str(math.log(abs(12 * math.sin(int(x))))))
    browser.find_element_by_css_selector(".btn").click()
    ans = browser.switch_to.alert.text.split(": ")
    browser.switch_to.alert.accept()
    browser.get('https://stepik.org/course/575/promo?auth=login')
    time.sleep(2)
    browser.find_element_by_css_selector("#id_login_email").send_keys("goosts@mail.ru")
    browser.find_element_by_css_selector("#id_login_password").send_keys("4242564dichenchimdi")
    browser.find_element_by_css_selector(".sign-form__btn").click()
    time.sleep(3)
    browser.get('https://stepik.org/lesson/184253/step/6?unit=158843')
    time.sleep(3)
    browser.execute_script("window.scrollBy(0, 300);")
    browser.find_element_by_css_selector("textarea").send_keys(ans[1])
    browser.find_element_by_css_selector(".submit-submission").click()

finally:
    time.sleep(30)
    browser.quit()

