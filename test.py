from selenium import webdriver
import time
import Download_the_solution


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    time.sleep(1)
    browser.find_element_by_id("book").click()
    browser.switch_to.alert.accept()
    time.sleep(2)
    Download_the_solution.Dts("https://stepik.org/lesson/181384/step/8?auth=registration&unit=156009",browser, "459")

finally:
    time.sleep(3)
    browser.quit()