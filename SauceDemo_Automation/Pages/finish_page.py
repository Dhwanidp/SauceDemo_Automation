from SauceDemo_Automation.utils.locators_util import FinishPageLocators

class FinishPage:
    def __init__(self, driver):
        self.driver = driver

    def get_complete_text(self):
        return self.driver.find_element(*FinishPageLocators.complete_text).text

    def get_header(self):
        return self.driver.find_element(*FinishPageLocators.complete_header).text

    def back_to_products(self):
        self.driver.find_element(*FinishPageLocators.back_to_products).click()
