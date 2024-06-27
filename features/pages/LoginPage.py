from selenium.webdriver.common.by import By
from features.pages.BasePage import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def enter_username(self, username):
        self.enter_text(*self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.enter_text(*self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click_element(*self.LOGIN_BUTTON)