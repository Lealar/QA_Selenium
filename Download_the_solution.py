import time


def Dts(link, browser,ans, email, password ):
    browser.get('https://stepik.org/course/575/promo?auth=login')
    time.sleep(2)
    browser.find_element_by_css_selector("#id_login_email").send_keys(email)
    browser.find_element_by_css_selector("#id_login_password").send_keys(password)
    browser.find_element_by_css_selector(".sign-form__btn").click()
    time.sleep(3)
    browser.get(link)
    time.sleep(3)
    browser.execute_script("window.scrollBy(0, 300);")
    browser.find_element_by_css_selector("textarea").send_keys(ans[1])
    browser.find_element_by_css_selector(".submit-submission").click()