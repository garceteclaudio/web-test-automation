from behave import given, when, then
from selenium import webdriver
from features.pages.HomePage import HomePage


@then('shows home page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    product_texts = context.home_page.get_products_text()
    print("Texto: ",product_texts)
    assert "Products" in product_texts

@when('the user select an item')
def step_impl(context):
    context.home_page.select_product()

@when('the user click shopping cart')
def step_impl(context):
    context.home_page.click_shopping_cart()
    context.home_page.sleep(1)