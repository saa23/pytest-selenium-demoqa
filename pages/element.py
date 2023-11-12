import time

from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils
from pages import retailer_aauth_account, retailer_favourite, retailer_cart, retailer_collection, retailer_order, \
    retailer_profile, retailer_product, retailer_checkout
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from commons import *


class ElementPage(BaseDriver):
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

    log = Utils.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


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
    INPUT_FULLNAME = '//*[@id="userName"]'
    INPUT_EMAIL = '//*[@id="userEmail"]'
    INPUT_CURRENT_ADDRESS = '//*[@id="currentAddress"]'
    INPUT_PERMANENT_ADDRESS = '//*[@id="permanentAddress"]'
    BUTTON_SUBMIT = '//*[@id="submit"]'


    # =====================
    ### Loc in Check Box
    # =====================
    BUTTON_DROPDOWN = '//*[@id="tree-node"]/ol/li/span/button'
    DESKTOP_LABEL = '//*[@id="tree-node"]/ol/li/ol/li[1]/span/label'
    DOCUMENTS_LABEL = '//*[@id="tree-node"]/ol/li/ol/li[2]/span/label'
    DOWNLOADS_LABEL = '//*[@id="tree-node"]/ol/li/ol/li[3]/span/label'


    # =====================
    ### Loc in Radio Button
    # =====================
    YES_RADIO = '//*[@for="yesRadio"]'
    IMPRESSIVE_RADIO = '//*[@for="impressiveRadio"]'
    NO_RADIO = '//*[@for="noRadio"]'


    def text_box(self, fullname, email, current_address, permanent_address):
        self.driver.get(ELEMENTS_TEXTBOX_URL)
        self.driver.find_element(By.XPATH, self.INPUT_FULLNAME).send_key(fullname)
        self.driver.find_element(By.XPATH, self.INPUT_EMAIL).send_key(email)
        self.driver.find_element(By.XPATH, self.INPUT_CURRENT_ADDRESS).send_key(current_address)
        self.driver.find_element(By.XPATH, self.INPUT_PERMANENT_ADDRESS).send_key(permanent_address)

        submit_button =  self.wait_until_visibility_of_element_located(By.XPATH, self.BUTTON_SUBMIT)
        self.driver.execute_script("arguments[0].click();", submit_button)


    def check_box(self):
        self.driver.get(ELEMENTS_CHECKBOX_URL)
        el =  self.wait_until_visibility_of_element_located(By.XPATH, self.BUTTON_DROPDOWN)
        self.driver.execute_script("arguments[0].click();", el)

        el =  self.wait_until_visibility_of_element_located(By.XPATH, self.DESKTOP_LABEL)
        self.driver.execute_script("arguments[0].click();", el)

        el =  self.wait_until_visibility_of_element_located(By.XPATH, self.DOCUMENTS_LABEL)
        self.driver.execute_script("arguments[0].click();", el)

        el =  self.wait_until_visibility_of_element_located(By.XPATH, self.DOWNLOADS_LABEL)
        self.driver.execute_script("arguments[0].click();", el)


    def radio_button(self):
        self.driver.get(ELEMENTS_RADIO_URL)
        el =  self.wait_until_visibility_of_element_located(By.XPATH, self.YES_RADIO)
        el.click()

        el =  self.wait_until_visibility_of_element_located(By.XPATH, self.IMPRESSIVE_RADIO)
        el.click()

        el =  self.wait_until_visibility_of_element_located(By.XPATH, self.NO_RADIO)
        el.click()