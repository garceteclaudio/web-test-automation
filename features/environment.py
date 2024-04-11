from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def before_scenario(context, scenario):
    print("En ejecucion: " + scenario.name)
    # inicializar el navegador Chrome
    #chrome_options = Options()
    #chrome_options.add_argument("--headless")  # Ejecución en modo headless (sin interfaz gráfica)
    #chrome_options.add_argument("--no-sandbox")  # CI
    #chrome_options.add_argument("--disable-dev-shm-usage")  # CI
    #river_path = "C:\\bancorTM\\drivers\\chromedriver.exe"
    #context.driver = webdriver.Chrome(options=chrome_options)
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(5)


def after_scenario(context, scenario):
    try:
        if scenario.status == "failed":
            context.driver.get_screenshot_as_file(context.evidence_path + '/' + scenario.name + '.png')

    except:
        print(f"No fue posible adjuntar una imagen de error. Escenario '{scenario.name}'")
    # Cerrar el navegador al finalizar pruebas
    context.driver.quit()

def before_step(context, step):
    print(f"Ejecutando step: {step.name}")

def after_step(context, step):
    print(f"Finaliza step: {step.name}")