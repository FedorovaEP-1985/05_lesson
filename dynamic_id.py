from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация драйвера

driver = webdriver.Chrome()

try:
    # Открываем страницу

    driver.get("http://uitestingplayground.com/dynamicid")

    # Кликаем на синюю кнопку

    driver.find_element(
        By.XPATH, "//button[contains(text(), 'Button with Dynamic ID')]"
    ).click()

    # Выводим сообщение об успешном выполнении

    print("Клик по кнопке выполнен успешно!")
finally:
    # Закрываем браузер

    driver.quit()
