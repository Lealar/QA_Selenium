"""Задание: поиск сокровища с помощью get_attribute
В данной задаче вам нужно с помощью роботов решить ту же математическую задачу, как и в прошлом задании. Но теперь значение переменной х спрятано в "сундуке", точнее, значение хранится в атрибуте valuex у картинки с изображением сундука.

Ваша программа должна:

Открыть страницу http://suninjuly.github.io/get_attribute.html.
Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
Посчитать математическую функцию от x (сама функция остаётся неизменной).
Ввести ответ в текстовое поле.
Отметить checkbox "I'm the robot".
Выбрать radiobutton "Robots rule!".
Нажать на кнопку "Submit".
Для вычисления значения выражения в п.4 используйте функцию calc(x) из предыдущей задачи.

Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. Скопируйте его в поле ниже и нажмите кнопку "Submit", чтобы получить баллы за задание."""

from selenium import webdriver
import math
import time

def calsulate(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    Links = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(Links)
    val = browser.find_element_by_id("treasure")
    val = val.get_attribute("valuex")
    answer = browser.find_element_by_id("answer")
    answer.send_keys(calsulate(val))
    imRobots = browser.find_element_by_id("robotCheckbox")
    imRobots.click()
    RobotsRules = browser.find_element_by_id("robotsRule")
    RobotsRules.click()
    submit = browser.find_element_by_class_name("btn")
    submit.click()

finally:
    time.sleep(20)
    browser.quit()