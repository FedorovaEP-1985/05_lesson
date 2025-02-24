from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Запуск браузера в headless-режиме
    browser = p.chromium.launch(headless=False)  # headless=False для визуального отображения
    page = browser.new_page()

    # Открываем страницу
    page.goto("http://the-internet.herokuapp.com/entry_ad")

    # Ожидаем появления модального окна
    page.wait_for_selector("div.modal", state="visible")  # Ждем, пока модальное окно станет видимым

    # Нажимаем кнопку "Close" в модальном окне
    page.click("div.modal-footer p")  # Используем CSS-селектор для кнопки "Close"

    # Ждем 2 секунды, чтобы увидеть результат
    page.wait_for_timeout(2000)

    # Закрываем браузер
    browser.close()