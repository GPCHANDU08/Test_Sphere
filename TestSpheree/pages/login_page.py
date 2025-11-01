from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        print(f"[INFO] Opening SauceDemo and trying login: {username}")
        self.open()
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def is_logged_in(self):
        return "inventory" in self.driver.current_url
