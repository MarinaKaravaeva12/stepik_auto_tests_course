from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# browser = webdriver.Chrome()
# browser.get('https://www.qa-practice.com/elements/button/simple')
# clickButton = browser.find_element(By.ID, 'submit-id-submit')
# clickButton.click()
# sleep(5)
# clickButton2 = browser.find_element(By.CLASS_NAME, 'btn-primary')
# clickButton2.click()
# sleep(5)
#
# browser.find_element(By.LINK_TEXT, 'Contact').click()
# sleep(5)

# click_button3 = browser.find_element(By.CSS_SELECTOR, 'input[class="btn btn-primary"]')
# click_button3.click()
# sleep(5)
# click_button4 = browser.find_element(By.XPATH, '//input[@class="btn btn-primary"]')
# click_button4.click()
# sleep(5)


# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
sleep(5)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://suninjuly.github.io/text_input_task.html")
sleep(5)

# Метод find_element позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Метод принимает в качестве аргументов способ поиска и значение, по которому мы будем искать
# Ищем поле для ввода текста
textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")

# Напишем текст ответа в найденное поле
textarea.send_keys("get()")
sleep(5)

# Найдем кнопку, которая отправляет введенное решение
submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()
sleep(5)

# После выполнения всех действий мы должны не забыть закрыть окно браузера
driver.quit()