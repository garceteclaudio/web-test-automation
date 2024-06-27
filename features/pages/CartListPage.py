from selenium.webdriver.common.by import By
from features.pages.BasePage import BasePage

class CartListPage(BasePage):
    test = (By.ID, "user-name")

    CHECKOUT_BUTTON = (By.XPATH, "//button[@id='checkout']")



    def click_checkout(self):
        self.click_element(*self.CHECKOUT_BUTTON)

