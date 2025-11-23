from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from SauceDemo_Automation.utils.locators_util import LoginPageLocators


class LoginPage:
    def __init__(self, driver, timeout=8):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def login(self, username, password):
        self.wait.until(EC.presence_of_element_located(LoginPageLocators.usernameid))

        user_el = self.driver.find_element(*LoginPageLocators.usernameid)
        pass_el = self.driver.find_element(*LoginPageLocators.passwordid)

        user_el.clear()
        pass_el.clear()

        user_el.send_keys(username)
        pass_el.send_keys(password)
        self.driver.find_element(*LoginPageLocators.login_button).click()
