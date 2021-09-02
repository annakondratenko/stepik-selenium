from selenium import webdriver
import time
import math

try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("[id='treasure']").get_attribute("valuex")
    print(type(x_element))
    y = calc(x_element)
    input= browser.find_element_by_id("answer").send_keys(y)
    checkbox=browser.find_element_by_css_selector("[type='checkbox']").click()
    radio_button=browser.find_element_by_css_selector("[id='robotsRule']").click()
    submit_button = browser.find_element_by_css_selector("[type='submit']").click()

   # elements_to_select = tuple(("[id = 'robotCheckbox']", "[id='robotsRule']",
# "button.btn.btn-default"))

   # for elem in elements_to_select:
        #browser.find_element_by_css_selector(elem).click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
