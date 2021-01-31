"""Задание: ждем нужный текст на странице
Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха по строго заданной цене. Более высокая цена нас не устраивает, а по более низкой цене объект успеет забронировать кто-то другой.

В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/explicit_wait2.html
Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
Нажать на кнопку "Book"
Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
Чтобы определить момент, когда цена аренды уменьшится до $100, используйте метод text_to_be_present_in_element из библиотеки expected_conditions."""

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    button = WebDriverWait(browser, 500).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    browser.find_element_by_id("book").click()
    submit_btn = browser.find_element_by_id("solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);",submit_btn)
    x = browser.find_element_by_id("input_value").text
    browser.find_element_by_id("answer").send_keys(str(math.log(abs(12 * math.sin(int(x))))))
    submit_btn.click()
finally:
    time.sleep(5)
    browser.quit()


