import pyperclip as pyperclip
from selenium import webdriver
import time
import math

try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser.get(link)
    submit = browser.find_element_by_css_selector("[type='submit']").click()
    alert = browser.switch_to.alert
    alert.accept()
    x = browser.find_element_by_css_selector('#input_value')
    field = browser.find_element_by_css_selector("#answer").send_keys(calc(int(x.text)))
    submit = browser.find_element_by_css_selector("[type='submit']").click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)


    alert_text = alert.accept()

finally:
    time.sleep(1)
    browser.close()
