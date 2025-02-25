from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Запуск браузера в headless-режиме
    # headless=False для визуального отображения
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Открываем страницу
    page.goto("http://the-internet.herokuapp.com/entry_ad")

    # Ожидаем появления модального окна
    page.wait_for_selector("div.modal", state="visible")

    # Нажимаем кнопку "Close" в модальном окне
    # Используем CSS-селектор для кнопки "Close"
    page.click("div.modal-footer p")

    # Ждем 2 секунды, чтобы увидеть результат
    page.wait_for_timeout(2000)

    # Закрываем браузер
    browser.close()
