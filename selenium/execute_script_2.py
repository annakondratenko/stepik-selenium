# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.execute_script("alert('Robots at work');")
# browser.execute_script("document.title='Script executing';alert('Robots at work');")
import math

from selenium import webdriver
import time

try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)
    x_element = browser.find_element_by_css_selector("[id='input_value']")
    x_value = int(x_element.text)
    result = calc(x_value)
    browser.execute_script("window.scrollBy(0, 100);")
    enter_field = browser.find_element_by_css_selector("[id='answer']")
    enter_field.send_keys(result)
    checkbox = browser.find_element_by_css_selector("[id='robotCheckbox']").click()
    radiobutton = browser.find_element_by_css_selector('[for="robotsRule"]').click()
    submit = browser.find_element_by_css_selector("[type='submit']").click()


finally:
    time.sleep(10)
    browser.close()
