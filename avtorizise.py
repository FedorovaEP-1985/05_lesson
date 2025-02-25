from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
import time

# Инициализация драйвера для Firefox
# с использованием webdriver_manager
driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))

try:
    # Шаг 1: Открыть страницу авторизации
    driver.get("http://the-internet.herokuapp.com/login")

    # Шаг 2: Найти поле username и ввести значение "tomsmith"
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")

    # Шаг 3: Найти поле password и ввести значение "SuperSecretPassword!"
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")

    # Пауза для наглядности
    time.sleep(2)

    # Шаг 4: Найти кнопку Login и нажать на неё
    login_button = driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()

    # Пауза для наглядности
    time.sleep(2)

    # Проверка успешной авторизации (опционально)
    success_message = driver.find_element(By.ID, "flash")
    if "You logged into a secure area!" in success_message.text:
        print("Авторизация прошла успешно!")
    else:
        print("Ошибка авторизации.")

    # Пауза для наглядности
    time.sleep(2)
finally:
    # Закрыть браузер
    driver.quit()
