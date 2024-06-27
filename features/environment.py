from behave import *
from selenium import webdriver


def before_all(context):
   print('Before all executed')


def before_scenario(context, scenario):
   context.driver = webdriver.Chrome()




def after_scenario(context, scenario):
   context.driver.quit()


def after_feature(scenario, context):
   print('After feature executed')


def after_all(context):
   print('After all executed')