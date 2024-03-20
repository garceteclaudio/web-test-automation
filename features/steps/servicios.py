#!/usr/bin/env python3
from behave import *
import requests

url = ""
response = None

@given('un endpoint publico "https://api.sampleapis.com/futurama/info"')
def step_impl(context):
    print("Ejecutando servicio........")
    global url
    url = "https://api.sampleapis.com/futurama/info"

@when('el usuario realiza un get')
def step_impl(context):
    global response
    response = requests.get(url)

@then('el usuario obtiene un codigo "{codigo}"')
def step_impl(context, codigo):
    print(response.json())
    assert response.status_code == int(codigo), f"El código de estado esperado era {codigo}, pero se obtuvo {response.status_code}"
