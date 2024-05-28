from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os

link = 'https://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements(By.CSS_SELECTOR, "[type='text")
    for element in elements:
        element.send_keys("test")
    file_attach = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname("lesson8_step7_upload_file.py"))
    file = os.path.join(current_dir, "text.txt")
    file_attach.send_keys(file)
    browser.find_element(By.TAG_NAME, "button").click()
finally:
    sleep(5)
    browser.quit()
