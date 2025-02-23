from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException

# Инициализация драйвера
driver = webdriver.Chrome()

try:
    # Открываем страницу
    driver.get("http://uitestingplayground.com/classattr")

    # Кликаем на синюю кнопку
    try:
        button = driver.find_element(By.CLASS_NAME, "btn-primary")
        button.click()
        print("Клик по кнопке выполнен успешно!")
    except NoSuchElementException:
        print("Ошибка: Кнопка не найдена на странице.")
    except Exception as e:
        print(f"Ошибка при клике по кнопке: {e}")

except WebDriverException as e:
    print(f"Ошибка при открытии страницы: {e}")

finally:
    # Закрываем браузер
    driver.quit()
