import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestRegistration(unittest.TestCase):
    def test_reg1(self):
        link = "https://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element(By.CSS_SELECTOR, '.first_block .first_class .first')
        first_name.send_keys("Marina")
        last_name = browser.find_element(By.CSS_SELECTOR, '.first_block .second_class .second')
        last_name.send_keys("Karavaeva")
        email = browser.find_element(By.CSS_SELECTOR, '.first_block .third_class .third')
        email.send_keys("test@gmail.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Incorrect message")
        browser.quit()

    def test_reg2(self):
        link = "https://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element(By.CSS_SELECTOR, '.first_block .first_class .first')
        first_name.send_keys("Marina")
        last_name = browser.find_element(By.CSS_SELECTOR, '.first_block .second_class .second')
        last_name.send_keys("Karavaeva")
        email = browser.find_element(By.CSS_SELECTOR, '.first_block .third_class .third')
        email.send_keys("test@gmail.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Incorrect message")
        browser.quit()
if __name__ == "__main__":
    unittest.main()