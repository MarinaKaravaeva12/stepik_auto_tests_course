from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep



browser = webdriver.Chrome()
browser.get('https://staging.skyx-internal.com/login')
sleep(3)

email = browser.find_element(By.XPATH, '//input[@name="name"]')
email.send_keys("mkaravaeva@productsavvy.com")
password = browser.find_element(By.XPATH, '//input[@name="password"]')
password.send_keys("Test$123456")
sleep(3)
login_button = browser.find_element(By.XPATH, '//input[@class="button-03 button-03-a"]')
login_button.click()
sleep(3)

two_f_a = browser.find_element(By.XPATH, '//input[@class="otp-input ng-untouched ng-pristine ng-valid"]')
two_f_a.send_keys('2')
two_f_a2 = browser.find_element(By.XPATH, '//input[@class="otp-input ng-untouched ng-pristine ng-valid"]')
two_f_a2.send_keys('4')
two_f_a3 = browser.find_element(By.XPATH, '//input[@class="otp-input ng-untouched ng-pristine ng-valid"]')
two_f_a3.send_keys('1')
two_f_a4 = browser.find_element(By.XPATH, '//input[@class="otp-input ng-untouched ng-pristine ng-valid"]')
two_f_a4.send_keys('2')
two_f_a5 = browser.find_element(By.XPATH, '//input[@class="otp-input ng-untouched ng-pristine ng-valid"]')
two_f_a5.send_keys('3')
two_f_a6 = browser.find_element(By.XPATH, '//input[@class="otp-input ng-untouched ng-pristine ng-valid"]')
two_f_a6.send_keys('1')
sleep(3)