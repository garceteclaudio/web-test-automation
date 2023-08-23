#!/usr/bin/env python3

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.

driver.get('https://www.saucedemo.com/')
time.sleep(3)

assert 'Swag Labs' in driver.title

elem = driver.find_element(By.ID, 'user-name')
elem.send_keys('standard_user')

elemPassword = driver.find_element(By.ID, 'password')  # Find the search box
elemPassword.send_keys('secret_sauce')

login_button = driver.find_element(By.ID, 'login-button')  # Find the search box
login_button.click()

time.sleep(2)


driver.quit()