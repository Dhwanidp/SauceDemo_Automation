import os
import json
import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from SauceDemo_Automation.Pages.login_page import LoginPage
from SauceDemo_Automation.Pages.Products_page import ProductsPage
from SauceDemo_Automation.Pages.cart_page import CartPage
from SauceDemo_Automation.Pages.checkout_page import CheckoutPage
from SauceDemo_Automation.Pages.checkout_overview_page import CheckoutOverviewPage
from SauceDemo_Automation.Pages.finish_page import FinishPage

TESTS_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.dirname(TESTS_DIR)
user_path = os.path.join(PROJECT_ROOT, "user_data", "users.json")

with open(user_path, "r", encoding="utf-8") as f:
    users = json.load(f)
    test_list = users["UserData"]

@pytest.mark.parametrize("test_list_item", test_list)
class TestE2ECheckout:

    def test_full_checkout_flow(self, setup, test_list_item, product_map, items_to_buy):
        driver = setup
        wait = WebDriverWait(driver, 5)

        login_page = LoginPage(driver)
        products_page = ProductsPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)
        overview_page = CheckoutOverviewPage(driver)
        finish_page = FinishPage(driver)

        login_page.login(test_list_item["username"], test_list_item["password"])

        products_page.sort_by_text("Name (A to Z)")
        names_az = products_page.get_product_names()
        assert names_az == sorted(names_az), "Sorting of A-Z FAIL"

        products_page.sort_by_text("Name (Z to A)")
        wait.until(lambda d: products_page.get_product_names() == sorted(products_page.get_product_names(), reverse=True))
        names_za = products_page.get_product_names()
        assert names_za == sorted(names_za, reverse=True), "Sorting of Z-A FAIL"

        products_page.sort_by_text("Price (low to high)")
        prices_low = products_page.get_product_prices()
        assert prices_low == sorted(prices_low), "Sorting of Low to High FAIL"

        products_page.sort_by_text("Price (high to low)")
        prices_high = products_page.get_product_prices()
        assert prices_high == sorted(prices_high, reverse=True), "Sorting of High to Low FAIL"

        products_page.add_items(product_map, items_to_buy)
        products_page.open_cart()

        cart_items = cart_page.get_items_in_cart()
        for item in items_to_buy:
            assert item in cart_items, f"{item} is missing from cart"

        cart_page.click_checkout()

        checkout_page.click_continue()
        error = checkout_page.get_error()
        assert "First Name is required" in error, "Without Name it continued"

        checkout_page.fill_first_name("Test")
        checkout_page.click_continue()
        error = checkout_page.get_error()
        assert "Last Name is required" in error, "No error for missing Last Name"

        checkout_page.fill_last_name("User")
        checkout_page.fill_postal_code("abc")
        checkout_page.click_continue()

        prices = overview_page.get_item_prices()
        calculated_total = round(sum(prices), 2)
        subtotal_shown = round(overview_page.get_subtotal(), 2)
        assert calculated_total == subtotal_shown, f"Subtotal mismatch! calc={calculated_total}, shown={subtotal_shown}"

        tax_shown = round(overview_page.get_tax(), 2)
        total_shown = round(overview_page.get_total(), 2)
        assert round(subtotal_shown + tax_shown, 2) == total_shown, "Final total mismatch!"

        overview_page.click_finish()

        success_header = finish_page.get_header()
        success_text = finish_page.get_complete_text()
        assert success_header == "Thank you for your order!", "Order not completed!"
        print(success_text)
