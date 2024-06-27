from selenium.webdriver.common.by import By
from features.pages.BasePage import BasePage

class CheckoutOverviewPage(BasePage):
    test = (By.ID, "user-name")

    CHECKOUT_OVERVIEW_TEXT = (By.XPATH, "//span[contains(text(),'Checkout: Overview')]")
    FINISH_BUTTON = (By.XPATH, "//button[@id='finish']")

    def get_checkout_overview_text(self):
        return self.get_text(*self.CHECKOUT_OVERVIEW_TEXT)

    def click_finish(self):
        self.click_element(*self.FINISH_BUTTON)

