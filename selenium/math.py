from selenium import webdriver
import time
import math

try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("[id='input_value']")
    x = x_element.text
    y = calc(x)
    input= browser.find_element_by_id("answer")
    input.send_keys(y)
    checkbox=browser.find_element_by_css_selector("[for='robotCheckbox']").click()
    radio_button=browser.find_element_by_css_selector("[for='robotsRule']").click()
    submit_button = browser.find_element_by_css_selector("[type='submit']").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
