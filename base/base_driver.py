from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    def wait_until_presence_of_element_located(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.presence_of_element_located((locator_type, locator)))
        return element

    def wait_until_element_to_be_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element

    def wait_until_visibility_of_element_located(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.visibility_of_element_located((locator_type, locator)))
        return element

    def wait_until_presence_of_all_elements_located(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 5)
        list_of_elements = wait.until(EC.presence_of_all_elements_located((locator_type, locator)))
        return list_of_elements

    def wait_until_visibility_of_all_elements_located(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 5)
        list_of_elements = wait.until(EC.visibility_of_all_elements_located((locator_type, locator)))
        return list_of_elements