from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация драйвера
driver = webdriver.Chrome()

try:
    # Открываем страницу

    driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

    # Кликаем на кнопку "Add Element" 5 раз

    for _ in range(5):
        driver.find_element(By.XPATH, "//button[text()='Add Element']").click()
    # Собираем список кнопок "Delete"

    delete_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")

    # Выводим размер списка

    print(f"Количество кнопок 'Delete': {len(delete_buttons)}")
finally:
    # Закрываем браузер

    driver.quit()
