import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from selenium import webdriver

link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()

try:

    browser.get(link)

    num1 = browser.find_element(By.ID, "num1")
    num2 = browser.find_element(By.ID, "num2")
    result = int(num1.text) + int(num2.text)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(result))

    browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

    print(result)

finally:
    time.sleep(10)
    browser.quit()
