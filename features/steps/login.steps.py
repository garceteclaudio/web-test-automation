#!/usr/bin/env python3
from behave import *
import time
from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

@given(u'Launch chrome browser')
def step_impl(context):


    # Configurar las opciones de Chrome
    chrome_options = Options()
    chrome_options.set_capability('browserName', 'chrome')
    chrome_options.set_capability('platformName', 'mac')
    chrome_options.set_capability('gsg:customcap', True)
    chrome_options.set_capability('se:name', 'test esto!')

    # URL del hub
    hub_url = 'http://192.168.100.54:4444'
    # Crear la instancia del navegador remoto

    # nodos ???
    context.driver = webdriver.Remote(command_executor=hub_url, options=chrome_options)
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
    