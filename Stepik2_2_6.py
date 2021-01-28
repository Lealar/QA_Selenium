"""
1. Открыть страницу http://SunInJuly.github.io/execute_script.html.
2. Считать значение для переменной x.
3. Посчитать математическую функцию от x.
4. Проскроллить страницу вниз.
5. Ввести ответ в текстовое поле.
6. Выбрать checkbox "I'm the robot".
7. Переключить radiobutton "Robots rule!".
8. Нажать на кнопку "Submit"."""

from selenium import webdriver
import time
import math

def func(x):
    return (math.log(abs(12 * math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/execute_script.html")
    x = browser.find_element_by_id("input_value").text
    print(func(x))
    send_keys = browser.find_element_by_id("answer")
    send_keys.send_keys(str(func(x)))
    browser.find_element_by_id("robotCheckbox").click()
    button = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    browser.find_element_by_css_selector(".btn").click()

finally:
    time.sleep(3)
    browser.quit()