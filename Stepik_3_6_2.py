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

