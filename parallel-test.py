from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from concurrent.futures import ThreadPoolExecutor
import time


def seleniumGrid():
    chrome_options = Options()
    chrome_options.set_capability('browserName', 'chrome')
    chrome_options.set_capability('platformName', 'mac')
    chrome_options.set_capability('gsg:customcap', True)
    chrome_options.set_capability('se:name', 'test esto!')

    # URL del hub
    hub_url = 'http://localhost:4444'
    # Crear la instancia del navegador remoto
    driver =  webdriver.Remote(command_executor=hub_url, options=chrome_options)
    return driver

def selenium_alone():
    driver = webdriver.Chrome()
    return driver

def run_test(instance_name, browser_name):
    driver = selenium_alone()
    try:
        # Abrir una página web
        driver.get('https://selenium.dev')

        # Realizar alguna acción (por ejemplo, obtener el título de la página)
        print(f"{instance_name} ({browser_name}) - Page title is: {driver.title}")

    finally:
        # Cerrar el navegador
        driver.quit()

def main():
    # Lista de pruebas con nombres de instancia y nombres de navegador
    tests = [
        ('Test 1', 'chrome'),
        ('Test 2', 'chrome'),
        ('Test 3', 'chrome'),
        ('Test 4', 'chrome'),
        ('Test 5', 'chrome'),
        ('Test 6', 'chrome'),
        ('Test 7', 'chrome'),
        ('Test 8', 'chrome'),
    ]

    # Ejecutar las pruebas en paralelo usando ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=9) as executor:
        for instance_name, browser_name in tests:
            executor.submit(run_test, instance_name, browser_name)

if __name__ == '__main__':
    main()