from selenium.webdriver.common.by import By
from features.pages.BasePage import BasePage

class HomePage(BasePage):
    test = (By.ID, "user-name")

    TEXT_PRODUCTS = (By.XPATH, "//span[contains(text(),'Products')]")

    def get_products_text(self):
        return self.get_text(*self.TEXT_PRODUCTS)
