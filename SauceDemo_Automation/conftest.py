import json
import os
import datetime
import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.options import Options as EdgeOptions
from SauceDemo_Automation.utils import locators_util

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="edge")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        drv = webdriver.Chrome(service=ChromeService())
    elif browser_name == "firefox":
        drv = webdriver.Firefox(service=FirefoxService())
    else:
        options = EdgeOptions()
        options.add_argument("--start-maximized")
        drv = webdriver.Edge(service=EdgeService(), options=options)
    return drv

@pytest.fixture(params=["on chrome", "on firefox", "on edge"])
def crossing(request):
    return request.param

@pytest.fixture(scope="function")
def setup(browser, request):
    browser.get("https://www.saucedemo.com/")
    browser.maximize_window()
    browser.implicitly_wait(5)
    request.cls.driver = browser
    yield browser
    try:
        browser.quit()
    except:
        pass

def load_json(file_name):
    path = os.path.join(BASE_DIR, "user_data", file_name)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

@pytest.fixture(scope="function")
def users():
    return load_json("users.json")

@pytest.fixture(scope="function")
def product_map():
    return load_json("product_map.json")

@pytest.fixture(scope="function")
def items_to_buy():
    data = load_json("items_to_buy.json")
    if isinstance(data, dict) and "items" in data:
        return data["items"]
    return data

@pytest.fixture(scope="function")
def LoginPageLocators():
    return locators_util.LoginPageLocators

@pytest.fixture(scope="function")
def ProductPageLocators():
    return locators_util.ProductsPageLocators

SCREENSHOT_DIR = os.path.join(BASE_DIR, "reports", "screenshots")
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.failed and rep.when in ("setup", "call"):
        driver = None
        if "setup" in item.funcargs:
            driver = item.funcargs.get("setup")
        elif "browser" in item.funcargs:
            driver = item.funcargs.get("browser")
        else:
            driver = getattr(getattr(item, "instance", None), "driver", None)

        path = None
        if driver:
            ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            name = f"{item.name}_{rep.when}_{ts}.png"
            path = os.path.join(SCREENSHOT_DIR, name)
            try:
                driver.save_screenshot(path)
            except Exception:
                path = None

        html_plugin = item.config.pluginmanager.getplugin("html")
        if html_plugin and path and os.path.exists(path):
            extra = getattr(rep, "extra", [])
            try:
                extra.append(html_plugin.extras.image(path))
            except Exception:
                rel = os.path.relpath(path, BASE_DIR).replace("\\", "/")
                extra.append(html_plugin.extras.html(f'<img src="{rel}" style="max-width:100%;">'))
            rep.extra = extra
        rel_path = os.path.relpath(path, os.path.dirname(item.config.option.htmlpath))
        extra.append(pytest_html.extras.image(rel_path))
