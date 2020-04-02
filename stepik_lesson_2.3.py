from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector(".trollface.btn")
    time.sleep(1)
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_value = browser.find_element_by_id("input_value")
    x = x_value.text
    res = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(res)

    button1 = browser.find_element_by_css_selector("button.btn")
    button1.click()


finally:
    time.sleep(10)
    browser.quit()
