"""Задание: кликаем по checkboxes и radiobuttons (капча для роботов)
Продолжим использовать силу роботов 🤖 для решения повседневных задач. На данной странице мы добавили капчу для роботов, то есть тест, являющийся простым для компьютера, но сложным для человека.

Ваша программа должна выполнить следующие шаги:

Открыть страницу http://suninjuly.github.io/math.html.
Считать значение для переменной x.
Посчитать математическую функцию от x (код для этого приведён ниже).
Ввести ответ в текстовое поле.
Отметить checkbox "I'm the robot".
Выбрать radiobutton "Robots rule!".
Нажать на кнопку Submit."""

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
