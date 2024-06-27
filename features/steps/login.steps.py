from behave import given, when, then
from features.pages.LoginPage import LoginPage

@given('the user is on the login page')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.driver.get('https://www.saucedemo.com/')


@when('the user enters a valid username')
def step_impl(context):
    context.login_page.enter_username('standard_user')

@when('the user enters a valid password')
def step_impl(context):
    context.login_page.enter_password('secret_sauce')

@when('the user clicks the login button')
def step_impl(context):
    context.login_page.click_login()



