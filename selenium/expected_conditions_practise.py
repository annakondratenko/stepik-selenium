import math

import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)
    price_button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    book_button = browser.find_element(By.ID, "book").click()

    x = browser.find_element_by_css_selector('#input_value')
    field = browser.find_element_by_css_selector("#answer").send_keys(calc(int(x.text)))
    submit = browser.find_element_by_css_selector("[type='submit']").click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)
    alert_text = alert.accept()



finally:
    browser.close()
