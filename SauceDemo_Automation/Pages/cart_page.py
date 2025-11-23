from SauceDemo_Automation.utils.locators_util import CartPageLocators

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def get_items_in_cart(self):
        return [p.text for p in self.driver.find_elements(*CartPageLocators.cart_items)]

    def click_checkout(self):
        self.driver.find_element(*CartPageLocators.checkout_button).click()
