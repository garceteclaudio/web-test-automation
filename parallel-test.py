#Parallel test with selenium library and pytest-xdist
import random
import pytest
from selenium import webdriver
import time


@pytest.mark.parametrize("variant", range(2))
def test_parallel(variant):
    num = random.random()
    print("Random number: ",num)
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get('https://www.saucedemo.com/')
    time.sleep(2)
    driver.close()
    
    
#Ejecuciones de a 2, hasta un range de 5
# pytest parallel-test.py -n 2