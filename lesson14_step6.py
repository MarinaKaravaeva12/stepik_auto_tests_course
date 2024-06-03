# import math
# assert abs(-2) == 3, "should be absolute value of a number"


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

link = 'https://suninjuly.github.io/registration1.html'
browser = webdriver.Chrome()
try:
    browser.get(link)
    title = browser.find_element(By.TAG_NAME, "h1").text
    assert title == "Hello", \
        f"Wrong title, got {title} instead of Hello"

finally:
    browser.quit()
