from codecs import make_encoding_map
from time import sleep #импортировали метод из пакета
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


Edge = webdriver.Edge(
service = EdgeService(EdgeChromiumDriverManager().install()))
Chrome = webdriver.Chrome(
service=ChromeService(ChromeDriverManager().install()))

def make_screenshot(browser): #определили единый метод
	browser.maximize_window()
	browser.get("https://vk.com/")
	sleep(5)
	browser.save_screenshot("./vk.png")
	browser.quit()

make_screenshot(Edge)
make_screenshot(Chrome)
