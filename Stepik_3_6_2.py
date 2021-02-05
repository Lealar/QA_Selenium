"""
Задание: параметризация тестов
Инопланетяне оставляют загадочные сообщения на Stepik в фидбеке задач на правильное решение. Мы смогли локализовать несколько url-адресов задач, где появляются кусочки сообщений. Ваша задача — реализовать автотест со следующим сценарием действий:

открыть страницу
ввести правильный ответ
нажать кнопку "Отправить"
дождаться фидбека о том, что ответ правильный
проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"
Опциональный фидбек — это текст в черном поле, как показано на скриншоте:

Используйте маркировку pytest для параметризации и передайте в тест список ссылок в качестве параметров:

https://stepik.org/lesson/236895/step/1
https://stepik.org/lesson/236896/step/1
https://stepik.org/lesson/236897/step/1
https://stepik.org/lesson/236898/step/1
https://stepik.org/lesson/236899/step/1
https://stepik.org/lesson/236903/step/1
https://stepik.org/lesson/236904/step/1
https://stepik.org/lesson/236905/step/1

Используйте осмысленное сообщение об ошибке в проверке текста, а также настройте нужные ожидания, чтобы тесты работали стабильно.

В упавших тестах найдите кусочки послания. Тест должен падать, если текст в опциональном фидбеке не совпадает со строкой "Correct!" Соберите кусочки текста в одно предложение и отправьте в качестве ответа на это задание.
"""


import pytest
from selenium import webdriver
import time
import math

def ans():
    return str(math.log(int(time.time())))

final= ''


@pytest.fixture(scope="function")
def browser():
    print("\n start browser")
    browser = webdriver.Chrome()
    answer = []
    yield browser
    print("\close browser")
    browser.quit()
    print(final)


@pytest.mark.parametrize('uri',["236895", "236896",
                              "236897","236898","236899",
                              "236903","236904","236905"])
def test_optional_feedback(browser, uri):
    link = f"https://stepik.org/lesson/{uri}/step/1"
    global final
    browser.get(link)
    browser.implicitly_wait(10)
    browser.find_element_by_css_selector(".textarea").send_keys(ans())
    browser.find_element_by_css_selector(".submit-submission").click()
    check = browser.find_element_by_css_selector(".smart-hints__hint").text
    try:
        assert str(check) == "Correct!"
    except AssertionError:
        final += check

