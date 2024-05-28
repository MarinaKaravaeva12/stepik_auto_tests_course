import math
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    button = browser.find_element(By.ID,"book")
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100'))
    button.click()

    title = browser.find_element(By.ID, "simple_text")
    browser.execute_script("return arguments[0].scrollIntoView(true)", title)

    x = browser.find_element(By.ID, "input_value")
    y = calc(x.text)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    browser.find_element(By.ID, "solve").click()
finally:
    sleep(5)
    browser.quit()
