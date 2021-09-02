from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:

    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("[id='num2']").text
    y_element = browser.find_element_by_css_selector("[id='num1']").text

    sum = int(x_element)+int(y_element)
    sum_str = str(sum)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum_str)
    submit_button = browser.find_element_by_css_selector("[type='submit']").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
