import math
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = 'https://suninjuly.github.io/redirect_accept.html'

browser = webdriver.Chrome()

try:
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, "button")

    button.click()

    new_tab = browser.window_handles[1]
    browser.switch_to.window(new_tab)

    x = browser.find_element(By.ID, "input_value")
    y = calc(x.text)

    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.TAG_NAME, "button").click()

finally:
    sleep(5)
    browser.quit()




