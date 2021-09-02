# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.execute_script("alert('Robots at work');")
# browser.execute_script("document.title='Script executing';alert('Robots at work');")
import math

from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By


try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/file_input.html'
    browser.get(link)
    firstname = browser.find_element_by_css_selector('[name = "firstname"]').send_keys("Test")
    lasttname = browser.find_element_by_css_selector('[name ="lastname"]').send_keys("Test")
    email = browser.find_element_by_css_selector('[name = "email"]').send_keys("Test")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file_example.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(file_path)
    submit = browser.find_element_by_css_selector("[type='submit']").click()



finally:
    time.sleep(10)
    browser.close()
