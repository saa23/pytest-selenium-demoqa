import time
from datetime import datetime, timezone
from . import driver, wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from commons.logger import logger_instance as logger

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

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

def text_box(target_url):
        # =====================
        ### Loc in Home Page
        # =====================
        # ELEMENTS_DIV = '//*[@id="app"]/div/div/div[2]/div/div[1]/div/div[3]/h5'
        # FORMS_DIV = '//*[@id="app"]/div/div/div[2]/div/div[2]/div/div[3]/h5'
        # ALERTS_DIV = '//*[@id="app"]/div/div/div[2]/div/div[3]/div/div[3]/h5'
        # WIDGETS_DIV = '//*[@id="app"]/div/div/div[2]/div/div[4]/div/div[3]/h5'
        # INTERACTIONS_DIV = '//*[@id="app"]/div/div/div[2]/div/div[5]/div/div[3]/h5'
        # BOOK_STORE_DIV = '//*[@id="app"]/div/div/div[2]/div/div[6]/div/div[3]/h5'

        # =====================
        ### Loc in Text Box
        # =====================
        TEXT_BOX = '//*[@id="item-0"]/span'
        INPUT_FULLNAME = '//input[@id="userName"]'
        INPUT_EMAIL = '//input[@id="userEmail"]'
        INPUT_CURRENT_ADDRESS = '//textarea[@id="currentAddress"]'
        INPUT_PERMANENT_ADDRESS = '//textarea[@id="permanentAddress"]'
        BUTTON_SUBMIT = '//button[@id="submit"]'


        driver.get(target_url)
        driver.maximize_window()

        wait.until(EC.visibility_of_element_located((By.XPATH, TEXT_BOX))).click()
        time.sleep(3)

        loc_fullname = wait.until(EC.visibility_of_element_located((By.XPATH, INPUT_FULLNAME)))
        loc_fullname.send_keys("Saadi Saadi")
        time.sleep(2)

        loc_email = wait.until(EC.visibility_of_element_located((By.XPATH, INPUT_EMAIL)))
        loc_email.send_keys("Saadi_DataScientist@gmail.com")
        time.sleep(2)

        loc_current_addr = wait.until(EC.visibility_of_element_located((By.XPATH, INPUT_CURRENT_ADDRESS)))
        loc_current_addr.send_keys("Kota Tangsel")
        time.sleep(2)

        loc_current_addr = wait.until(EC.visibility_of_element_located((By.XPATH, INPUT_PERMANENT_ADDRESS)))
        loc_current_addr.send_keys("Kota Jaksel")
        time.sleep(2)

        wait.until(EC.visibility_of_element_located((By.XPATH, BUTTON_SUBMIT))).click()

        time.sleep(5)

        message = "text_box"
        now_utc = datetime.now(timezone.utc).strftime("%d_%m_%Y_%H_%M_%S")
        driver.save_screenshot(f'./reports/{message}-{now_utc}.png')

        driver.quit()

