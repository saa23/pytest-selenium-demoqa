from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait


service = Service(executable_path='./utilities/chromedriver.exe')
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-software-rasterizer")
driver = webdriver.Chrome(service= service, options= chrome_options)  # Optional argument, if not specified will search path.
wait = WebDriverWait(driver, 5)


