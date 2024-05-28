from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

# Ваш токен
token = 'eyJhbGciOiJIUzM4NCJ9.eyJzdWIiOiIzOCIsImlhdCI6MTcxNjQ2MTQ1NCwiZXhwIjoxNzE2NTQ3ODU0LCJ1c2VySWQiOjM4LCJjdXN0b21lcnMiOltdLCJhc3NldHMiOltdLCJ1c2VyTmFtZSI6Ik1hcmluYTEgQWRtaW4xIiwidXNlck1haWwiOiJta2FyYXZhZXZhQHByb2R1Y3RzYXZ2eS5jb20iLCJyb2xlIjoiU0tZWF9BRE1JTiIsImlzU2t5WCI6dHJ1ZSwiYWNjZXNzQWxsQ3VzdG9tZXJzIjp0cnVlLCJhY2Nlc3NBbGxBc3NldHMiOnRydWUsInBlcm1pc3Npb25zIjpbeyJuYW1lIjoiVVNFUl9NQU5BR0VNRU5UIiwibGV2ZWwiOiJXUklURSJ9LHsibmFtZSI6IkNVU1RPTUVSX01BTkFHRU1FTlQiLCJsZXZlbCI6IldSSVRFIn0seyJuYW1lIjoiRkxJR0hUX01BTkFHRU1FTlQiLCJsZXZlbCI6IldSSVRFIn0seyJuYW1lIjoiSU1BR0VfTUFOQUdFTUVOVCIsImxldmVsIjoiV1JJVEUifSx7Im5hbWUiOiJJTUFHRV9SRVZJRVciLCJsZXZlbCI6IldSSVRFIn0seyJuYW1lIjoiQU9JX01PTklUT1JJTkciLCJsZXZlbCI6IldSSVRFIn0seyJuYW1lIjoiQU9JX0FQUFJPVkFMX0lOVEVSTkFMIiwibGV2ZWwiOiJXUklURSJ9LHsibmFtZSI6IkFPSV9BUFBST1ZBTF9FWFRFUk5BTCIsImxldmVsIjoiV1JJVEUifSx7Im5hbWUiOiJEQVRBX0VYUE9SVCIsImxldmVsIjoiV1JJVEUifSx7Im5hbWUiOiJBT0lfSU5TUEVDVElPTiIsImxldmVsIjoiV1JJVEUifSx7Im5hbWUiOiJBU1NFVF9aT05FIiwibGV2ZWwiOiJXUklURSJ9XSwidW5pdCI6Ik1FVFJJQyJ9.pkhP5Ry-omNoAqO4cYf79YH17C0lfDMddH-BrAmWpL9-CnKZ9Yw4tkqWwO0T0r2f'

# Настройки для Chrome
chrome_options = Options()
chrome_options.add_argument("--disable-web-security")

# Запуск Chrome с заданными настройками
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://staging.skyx-internal.com/dashboard')

# Убедитесь, что страница загрузилась
assert "staging.skyx-internal.com" in driver.current_url

# Установить токен в LocalStorage
script = f"""
window.localStorage.setItem('jwtToken', '{token}');
"""
driver.execute_script(script)

# Перезагрузить страницу после установки токена
driver.refresh()
sleep(3)

# Проверьте, действительно ли токен установлен и работает
def is_logged_in():
    # Попробуйте найти элемент, который доступен только для авторизованных пользователей
    try:
        element = driver.find_element(By.CSS_SELECTOR, '.aside-manage a')
        return True
    except:
        return False

# Проверка успешности авторизации
if is_logged_in():
    print("Успешно авторизован")
    # Выполните дальнейшие действия после успешной авторизации
    system_administration = driver.find_element(By.CSS_SELECTOR, '.aside-manage a')
    system_administration.click()
    filters = driver.find_element(By.XPATH, '//div[@class="button-01 button-filters ng-star-inserted"]')
    filters.click()
else:
    print("Не удалось авторизоваться. Проверьте токен или процесс авторизации.")

# Закрыть браузер
driver.quit()
