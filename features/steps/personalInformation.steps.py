


from behave import given, when, then
from selenium import webdriver
from features.pages.PersonalInformationPage import PersonalInformationPage

@when('the user complete personal information')
def step_impl(context):
    context.personal_information_page = PersonalInformationPage(context.driver)
    context.personal_information_page.enter_username("Pepe")
    context.personal_information_page.enter_last_name("pepo")
    context.personal_information_page.enter_code_postal("4600")
    context.personal_information_page.click_continue()
