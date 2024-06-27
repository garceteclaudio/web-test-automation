
from behave import given, when, then
from selenium import webdriver
from features.pages.CheckoutCompletePage import CheckoutCompletePage

@then('shows than your for your order')
def step_impl(context):
    context.checkout_overview_page = CheckoutCompletePage(context.driver)
    text = context.checkout_overview_page.get_thank_your_for_order_text()
    print("Texto: ",text)
    ## se utiliza para visual la pantalla final
    context.home_page.sleep(3)
    assert "Thank you for your order!" in text