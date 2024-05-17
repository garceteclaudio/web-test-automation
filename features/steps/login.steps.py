#!/usr/bin/env python3
from behave import *
import time
from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given(u'Launch chrome browser')
def step_impl(context):
    print("Holaaa")
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(5)
    context.driver.get('https://www.saucedemo.com/')





@when(u'I type my user "{user}"')
def step_impl(context, user):
    # Wait explicito
    wait = WebDriverWait(context.driver, timeout=15)
    element = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    element.send_keys(user)


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
    context.driver.quit()
    