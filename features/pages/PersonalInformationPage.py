from selenium.webdriver.common.by import By
from features.pages.BasePage import BasePage

class PersonalInformationPage(BasePage):
    test = (By.ID, "user-name")

    FIRST_NAME_INPUT = (By.XPATH, "//input[@id='first-name']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@id='last-name']")
    ZIP_POSTAL_CODE_INPUT = (By.XPATH, "//input[@id='postal-code']")
    CONTINUE_BUTTON = (By.XPATH, "//input[@id='continue']")


    def enter_username(self, first_name):
        self.enter_text(*self.FIRST_NAME_INPUT, first_name)

    def enter_last_name(self, password):
        self.enter_text(*self.LAST_NAME_INPUT, password)

    def enter_code_postal(self, password):
        self.enter_text(*self.ZIP_POSTAL_CODE_INPUT, password)

    def click_continue(self):
        self.click_element(*self.CONTINUE_BUTTON)

