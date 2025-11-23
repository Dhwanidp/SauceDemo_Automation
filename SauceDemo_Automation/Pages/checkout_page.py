from SauceDemo_Automation.utils.locators_util import CheckoutPageLocators

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def click_continue(self):
        self.driver.find_element(*CheckoutPageLocators.continue_button).click()

    def get_error(self):
        return self.driver.find_element(*CheckoutPageLocators.error_message).text

    def fill_first_name(self, value):
        self.driver.find_element(*CheckoutPageLocators.first_name).send_keys(value)

    def fill_last_name(self, value):
        self.driver.find_element(*CheckoutPageLocators.last_name).send_keys(value)

    def fill_postal_code(self, value):
        self.driver.find_element(*CheckoutPageLocators.postal_code).send_keys(value)
