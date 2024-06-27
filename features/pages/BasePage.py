from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def sleep(self, secss):
        time.sleep(secss)

    def fluent_wait(self, by, value, timeout=10, poll_frequency=1, ignored_exceptions=None):
        if ignored_exceptions is None:
            ignored_exceptions = [NoSuchElementException]

        wait = WebDriverWait(self.driver, timeout, poll_frequency=poll_frequency, ignored_exceptions=ignored_exceptions)
        element = wait.until(EC.presence_of_element_located((by, value)))
        return element

    def find_element(self, by, value, timeout=10):
        return self.fluent_wait(by, value, timeout)

    def find_elements(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located((by, value)))

    def click_element(self, by, value, timeout=10):
        element = self.find_element(by, value, timeout)
        element.click()

    def enter_text(self, by, value, text, timeout=10):
        element = self.find_element(by, value, timeout)
        element.clear()
        element.send_keys(text)

    def get_text(self, by, value, timeout=10):
        element = self.find_element(by, value, timeout)
        return element.text
