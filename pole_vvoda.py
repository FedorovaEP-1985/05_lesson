from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Инициализация драйвера для Firefox с использованием webdriver_manager
browser = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))

try:
    # Шаг 1: Открыть страницу
    browser.get('http://the-internet.herokuapp.com/inputs')

    # Ожидание появления поля ввода
    input_field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,
                                        'input[type="number"]'))
    )

    # Шаг 2: Ввести в поле текст "1000"
    input_field.send_keys("1000")

    # Пауза для наглядности
    time.sleep(5)

    # Шаг 3: Очистить поле
    input_field.clear()

    # Шаг 4: Ввести в это же поле текст "999"
    input_field.send_keys("999")

    # Пауза для визуальной проверки (необязательно)
    time.sleep(5)

finally:
    # Закрыть браузер
    browser.quit()
