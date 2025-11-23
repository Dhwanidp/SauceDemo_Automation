from SauceDemo_Automation.utils.locators_util import ProductsPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver

    def sort_by_text(self, text):
        dropdown = Select(self.driver.find_element(*ProductsPageLocators.product_sort_container))
        dropdown.select_by_visible_text(text)

    def get_product_names(self):
        return [n.text for n in self.driver.find_elements(*ProductsPageLocators.inventory_item_name)]

    def get_product_prices(self):
        prices = self.driver.find_elements(*ProductsPageLocators.inventory_item_price)
        return [float(p.text.replace("$", "")) for p in prices]

    def add_items(self, product_map, items_to_buy):
        for item in items_to_buy:
            if item in product_map:
                self.driver.find_element(By.ID, product_map[item]).click()

    def open_cart(self):
        self.driver.find_element(*ProductsPageLocators.shopping_cart_badge).click()
