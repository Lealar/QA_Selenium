"""Напишите код, который реализует следующий сценарий:

Открыть страницу http://suninjuly.github.io/selects1.html
Посчитать сумму заданных чисел
Выбрать в выпадающем списке значение равное расчитанной сумме
Нажать кнопку "Submit"
Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени), вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания."""

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/selects1.html')
    chose = Select(browser.find_element_by_tag_name("select"))
    chose.select_by_value(str(int(browser.find_element_by_id("num1").text) + int(browser.find_element_by_id("num2").text)))
    Submit = browser.find_element_by_css_selector(".btn").click()
finally:
    time.sleep(3)
    browser.quit()

""" ВТОРОЙ СПОСОБ 

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/selects1.html')
    number = int((browser.find_element_by_id("num1")).text )+ int((browser.find_element_by_id("num2")).text)
    print(number)
    browser.find_element_by_tag_name("select").click()
    browser.find_element_by_css_selector("[value='"+ str(number) + "']").click()
    time.sleep(2)
    Submit = browser.find_element_by_css_selector(".btn").click()
finally:
    time.sleep(3)
    browser.quit()"""

