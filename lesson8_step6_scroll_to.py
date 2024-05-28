from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import math



def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'https://SunInJuly.github.io/execute_script.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_text = browser.find_element(By.ID, "input_value")
    x = x_text.text

    y = calc(x)
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()
    sleep(1)
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.TAG_NAME, "button").click()
    sleep(5)
finally:
    browser.quit()
