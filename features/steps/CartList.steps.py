from behave import given, when, then
from selenium import webdriver
from features.pages.CartListPage import CartListPage


@when('the user click checkout')
def step_impl(context):
    context.cart_list = CartListPage(context.driver)
    context.cart_list.click_checkout()

    #assert "Products" in product_texts