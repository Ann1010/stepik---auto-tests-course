from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
import os


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element_by_name("firstname")
    first_name.send_keys("Anna")
    first_name = browser.find_element_by_name("lastname")
    first_name.send_keys("Pogrebnik")
    first_name = browser.find_element_by_name("email")
    first_name.send_keys("apogrebnik30@gmail.com")
    element = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    element.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
