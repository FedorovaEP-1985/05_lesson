from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

Firefox = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))
Edge = webdriver.Edge(
    service = EdgeService(EdgeChromiumDriverManager().install()))
Chrome = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

# определили единый способ:


def make_screenshot(browser):
    browser.maximize_window()
    browser.get("https://vk.com/")
    sleep(5)
    browser.save_screenshot("./vk.png")
    browser.quit()


make_screenshot(Edge)
make_screenshot(Chrome)
make_screenshot(Firefox)
