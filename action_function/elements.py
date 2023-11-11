import time
from datetime import datetime, timezone
from . import driver, wait, platform
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from commons.logger import logger_instance as logger

# import os
# from dotenv import load_dotenv
# load_dotenv()

"""
    Click Elements button, then:
    1. Text Box: Fill up a form having fields: Full Name, Email, Current Address, Permanent Address
    2. Check Box: Click the dropdown and click all choices
    3. Radio Button: Try to click radio button: Yes, Impressive, or No
    4. Web Tables: edit an item, delete an item, and short by certain column
    5. Buttons: Double Click, Right Click, Click Me. If get following texts then succeed:
            - double click: "You have done a double click"
            - right click: "You have done a right click"
            - click me: "You have done a dynamic click"
    6. Links
    7. Broken Links - Images
    8. Upload and Download
    9. Dynamic Properties
    """

def text_box(base_url):
    ELEMENTS_DIV = '//*[@id="app"]/div/div/div[2]/div/div[1]'
    FORMS_DIV = '//*[@id="app"]/div/div/div[2]/div/div[2]'
    ALERTS_DIV = '//*[@id="app"]/div/div/div[2]/div/div[3]'
    WIDGETS_DIV = '//*[@id="app"]/div/div/div[2]/div/div[4]'
    INTERACTIONS_DIV = '//*[@id="app"]/div/div/div[2]/div/div[5]'
    BOOK_STORE_DIV = '//*[@id="app"]/div/div/div[2]/div/div[6]'

    driver.get(f"{base_url}")
    driver.maximize_window()

    wait.until(EC.visibility_of_element_located((By.XPATH, ELEMENTS_DIV))).click()

