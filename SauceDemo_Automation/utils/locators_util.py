from selenium.webdriver.common.by import By

class LoginPageLocators:
    usernameid = (By.ID, "user-name")
    passwordid = (By.ID, "password")
    login_button = (By.ID, "login-button")

class ProductsPageLocators:
    product_sort_container = (By.CLASS_NAME, "product_sort_container")
    inventory_item = (By.CLASS_NAME, "inventory_item")
    inventory_item_name = (By.CLASS_NAME, "inventory_item_name")
    inventory_item_price = (By.CLASS_NAME, "inventory_item_price")
    shopping_cart_link = (By.CLASS_NAME, "shopping_cart_link")
    shopping_cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
    pricebar_button = (By.XPATH, ".//div[@class='pricebar']/button")

class CartPageLocators:
    cart_items = (By.CLASS_NAME, "inventory_item_name")
    checkout_button = (By.ID, "checkout")

class CheckoutPageLocators:
    title = (By.CLASS_NAME, "title")
    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    postal_code = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")
    error_message = (By.XPATH, "//h3[@data-test='error']")

class CheckoutOverviewLocators:
    inventory_item_price = (By.CLASS_NAME, "inventory_item_price")
    summary_subtotal_label = (By.CLASS_NAME, "summary_subtotal_label")
    summary_tax_label = (By.CLASS_NAME, "summary_tax_label")
    summary_total_label = (By.CLASS_NAME, "summary_total_label")
    finish_button = (By.ID, "finish")

class FinishPageLocators:
    complete_header = (By.CLASS_NAME, "complete-header")
    complete_text = (By.CLASS_NAME, "complete-text")
    back_to_products = (By.ID, "back-to-products")
