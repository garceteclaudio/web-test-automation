#!/usr/bin/env python3
from behave import *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

@given(u'Launch chrome browser')
def step_impl(context):
    context.driver.get('https://www.saucedemo.com/')
    


@when(u'I type my user "{user}"')
def step_impl(context, user):
    # Wait explicito
    wait = WebDriverWait(context.driver, timeout=5)
    elem = context.driver.find_element(By.ID, 'user-name')
    wait.until(lambda d : elem.is_displayed())
    elem.send_keys(user)


@when(u'my password')
def step_impl(context):
    elemPassword = context.driver.find_element(By.ID, 'password')  # Find the search box
    elemPassword.send_keys('secret_sauce')


@when(u'click login button')
def step_impl(context):
    login_button = context.driver.find_element(By.ID, 'login-button')  # Find the search box
    login_button.click()



@then(u'I enter to the app')
def step_impl(context):
    time.sleep(2)
    