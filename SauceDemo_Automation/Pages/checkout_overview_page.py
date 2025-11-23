from SauceDemo_Automation.utils.locators_util import CheckoutOverviewLocators
from selenium.webdriver.common.by import By

class CheckoutOverviewPage:
    def __init__(self, driver):
        self.driver = driver

    def get_item_prices(self):
        elems = self.driver.find_elements(*CheckoutOverviewLocators.inventory_item_price)
        return [float(e.text.replace("$", "")) for e in elems]

    def get_subtotal(self):
        text = self.driver.find_element(*CheckoutOverviewLocators.summary_subtotal_label).text
        return float(text.split("$")[-1])

    def get_tax(self):
        text = self.driver.find_element(*CheckoutOverviewLocators.summary_tax_label).text
        return float(text.split("$")[-1])

    def get_total(self):
        text = self.driver.find_element(*CheckoutOverviewLocators.summary_total_label).text
        return float(text.split("$")[-1])

    def click_finish(self):
        self.driver.find_element(*CheckoutOverviewLocators.finish_button).click()
