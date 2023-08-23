import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('http://selenium.dev/')

time.sleep(5) # Let the user actually see something!

search_box = browser.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()

time.sleep(5) # Let the user actually see something!

browser.quit()