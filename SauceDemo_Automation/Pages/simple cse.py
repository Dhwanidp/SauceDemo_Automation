import time
from selenium.webdriver.support import expected_conditions as EC
import pytest
import json
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService

driver = webdriver.Edge(service=EdgeService())
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
driver.implicitly_wait(5)
usernameid = (By.ID, "user-name")
passwordid = (By.ID, "password")
login_button = (By.ID, "login-button")
driver.find_element(*usernameid).send_keys("standard_user")
driver.find_element(*passwordid).send_keys("secret_sauce")
driver.find_element(*login_button).click()

#product page===================================ok
product_map = {
    "Sauce Labs Backpack": "add-to-cart-sauce-labs-backpack",
    "Sauce Labs Bike Light": "add-to-cart-sauce-labs-bike-light",
    "Sauce Labs Bolt T-Shirt": "add-to-cart-sauce-labs-bolt-t-shirt",
    "Sauce Labs Fleece Jacket": "add-to-cart-sauce-labs-fleece-jacket",
    "Sauce Labs Onesie": "add-to-cart-sauce-labs-onesie",
    "Test.allTheThings() T-Shirt (Red)": "add-to-cart-test.allthethings()-t-shirt-(red)"
}

Items_to_buy = [
    "Sauce Labs Backpack",
    "Sauce Labs Onesie",
    "Test.allTheThings() T-Shirt (Red)"
]

for item in Items_to_buy:
    if item in product_map:
        driver.find_element(By.ID, product_map[item]).click()
    else:
        print(f"{item} not found on site.")

from selenium.webdriver.support.ui import Select

def sort_by_text(text):
    dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    dropdown.select_by_visible_text(text)

def get_product_names():
    return [n.text for n in driver.find_elements(By.CLASS_NAME, "inventory_item_name")]

def get_product_prices():
    return [float(p.text.replace("$", "")) for p in driver.find_elements(By.CLASS_NAME, "inventory_item_price")]

sort_by_text("Name (A to Z)")
names_az = get_product_names()
assert names_az == sorted(names_az), "Sorting of A-Z FAIL"

sort_by_text("Name (Z to A)")
names_za = get_product_names()
assert names_za == sorted(names_za, reverse=True), "Sorting of Z-A FAIL"

sort_by_text("Price (low to high)")
prices_LowToHigh = get_product_prices()
assert prices_LowToHigh == sorted(prices_LowToHigh), "Sorting of Low to High FAIL"

sort_by_text("Price (high to low)")
prices_HighToLow = get_product_prices()
assert prices_HighToLow == sorted(prices_HighToLow, reverse=True), "Sorting of High to Low FAIL"


driver.find_element(By.XPATH, "//span[@class = 'shopping_cart_badge']").click()

#cart=====================ok
productsInCart = [p.text for p in driver.find_elements(By.XPATH, "//div[@class='inventory_item_name']")]

print("Items in Cart:", productsInCart)

for item in Items_to_buy:
    assert item in productsInCart, f"{item} is missing from cart"

driver.find_element(By.ID, "checkout").click()


#detailss of user==============
driver.find_element(By.ID, "continue").click()
error = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
assert "First Name is required" in error, "Without Name it continued"

driver.find_element(By.ID, "first-name").send_keys("Test")
driver.find_element(By.ID, "continue").click()
error = driver.find_element(By.XPATH, "//h3[@data-test='error']").text

assert "Last Name is required" in error, "No error for missing Last Name"

driver.find_element(By.ID, "last-name").send_keys("User")
driver.find_element(By.ID, "postal-code").send_keys("abc")

driver.find_element(By.ID, "continue").click()

if "checkout-step-two" in driver.current_url:
    print("BUG: Checkout continued even with invalid postal code.")
else:
    print("Error page shown (unexpected behavior).")

time.sleep(3)

#checkout page================ok
price_of_items = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
prices = [float(p.text.replace("$", "")) for p in price_of_items]

calculated_total = sum(prices)

subtotal_text = driver.find_element(By.CLASS_NAME, "summary_subtotal_label").text
subtotal_shown = float(subtotal_text.split("$")[-1])

assert calculated_total == subtotal_shown

tax_text = driver.find_element(By.CLASS_NAME, "summary_tax_label").text
tax_shown = float(tax_text.split("$")[-1])

final_text = driver.find_element(By.CLASS_NAME, "summary_total_label").text
final_shown = float(final_text.split("$")[-1])

assert (subtotal_shown + tax_shown) == final_shown, "Final total mismatch!"

driver.find_element(By.ID, "finish").click()
#================end text final page
Final_Message = driver.find_element(By.CLASS_NAME, "complete-text").text
print(Final_Message)
