from selenium.webdriver.common.by import By
from features.pages.BasePage import BasePage

class CheckoutCompletePage(BasePage):
    test = (By.ID, "user-name")

    THANK_YOU_FOR_ORDER_TEXT = (By.XPATH, "//h2[contains(text(),'Thank you for your order!')]")


    def get_thank_your_for_order_text(self):
        return self.get_text(*self.THANK_YOU_FOR_ORDER_TEXT)



