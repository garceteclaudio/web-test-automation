
from behave import given, when, then
from selenium import webdriver
from features.pages.CheckoutOverviewPage import CheckoutOverviewPage

@then('shows checkout overview')
def step_impl(context):
    context.checkout_overview_page = CheckoutOverviewPage(context.driver)
    text = context.checkout_overview_page.get_checkout_overview_text()
    print("Texto: ",text)
    assert "Checkout: Overview" in text

@when('the user click finish')
def step_impl(context):
    context.checkout_overview_page.click_finish()