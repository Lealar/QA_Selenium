"""

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!! ВАЖНО: ФУНЦММ НАЗЫВАЙ КАК: test_ ЭТО ОЧЕНЬ ВАЖНО, ЧЕРЕЗ ВРЕМЯ Я ПОДУМАЮ  ЧТО ЭТО НЕ ВАЖНО НО НА ЭТОМ Я ПОТРАТИЛ 30 МИНУТ!!! ЭТО ВАЖНО!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Задание: оформляем тесты в стиле unittest
Попробуйте оформить тесты из первого модуля в стиле unittest.

Возьмите тесты из шага — https://stepik.org/lesson/138920/step/11?unit=196194
Создайте новый файл
Создайте в нем класс с тестами, который должен наследоваться от unittest.TestCase по аналогии с предыдущим шагом
Перепишите в стиле unittest тест для страницы http://suninjuly.github.io/registration1.html
Перепишите в стиле unittest второй тест для страницы http://suninjuly.github.io/registration2.html
Оформите финальные проверки в тестах в стиле unittest, например, используя проверочный метод assertEqual
Запустите получившиеся тесты из файла
Просмотрите отчёт о запуске и найдите последнюю строчку
Отправьте эту строчку в качестве ответа на это задание
Обратите внимание, что по задумке должно выбрасываться исключение NoSuchElementException во втором тесте. Если вы использовали конструкцию try/except, здесь нужно запустить тест без неё. Ловить исключения не надо (во всяком случае, здесь)!

Это всё для иллюстрации того, что unittest выполнит тесты и обобщит результаты даже при наличии неожиданного исключения.

"""
import unittest
from selenium import webdriver
import time

class TestChek(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
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
        self.assertEqual("Congratulations! You have successfully registered!", welcome, "REGISTRATION FAIL EXCELENT SELECTORS")

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
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
        self.assertEqual("Congratulations! You have successfully registered!", welcome, "REGISTRATION FAIL EXCELENT SELECTORS")

if __name__ == '__main__':
    unittest.main()