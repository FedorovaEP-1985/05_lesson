from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Инициализация драйвера (например, для Chrome)
driver = webdriver.Chrome()

try:
    # Шаг 1: Открыть страницу
    driver.get("http://the-internet.herokuapp.com/inputs")

    # Шаг 2: Найти поле ввода и ввести текст "1000"
    input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
    input_field.send_keys("1000")

    # Пауза для наглядности
    time.sleep(2)

    # Шаг 3: Очистить поле ввода
    input_field.clear()

    # Пауза для наглядности
    time.sleep(2)

    # Шаг 4: Ввести текст "999" в то же поле
    input_field.send_keys("999")

    # Пауза для наглядности
    time.sleep(2)

finally:
    # Закрыть браузер
    driver.quit()

    # Пауза для наглядности
    time.sleep(2)

    # Закрыть браузер
    driver.quit()
