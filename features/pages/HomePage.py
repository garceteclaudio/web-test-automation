from selenium.webdriver.common.by import By
from features.pages.BasePage import BasePage

class HomePage(BasePage):
    test = (By.ID, "user-name")

    TEXT_PRODUCTS = (By.XPATH, "//span[contains(text(),'Products')]")
    PRODUCTO = (By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
    SHOPPING_CART = (By.XPATH, "//body/div[@id='root']/div[@id='page_wrapper']/div[@id='contents_wrapper']/div[@id='header_container']/div[1]/div[3]/a[1]")

    def get_products_text(self):
        return self.get_text(*self.TEXT_PRODUCTS)

    def select_product(self):
        self.click_element(*self.PRODUCTO)

    def click_shopping_cart(self):
        self.click_element(*self.SHOPPING_CART)

