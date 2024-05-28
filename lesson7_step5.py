from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://suninjuly.github.io/math.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)

    x_tag = browser.find_element(By.ID, "input_value")
    x = x_tag.text
    y = calc(x)


    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(y)

    robot = browser.find_element(By.ID,"robotCheckbox")
    robot.click()

    robots_rule = browser.find_element(By.ID, "robotsRule")
    robots_rule.click()

    submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()