from behave import given, when, then
from selenium import webdriver
from features.pages.HomePage import HomePage


@then('shows home page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    product_texts = context.home_page.get_products_text()
    print("Texto: ",product_texts)
    assert "Products" in product_texts
