# Challenge QA

Este es un proyecto de pruebas automatizadas de la pagina web https://www.saucedemo.com/, los cuales se encuantran desarrollados por Claudio Rodolfo Garcete, principalmente con WebdriverIO y Cucumber. Los test se ejecutan de forma local.

## Comenzando

Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.

### Pre-requisitos


- Es necesario tener instalado [node](https://www.python.org/downloads/) para instalar y ejecutar el proyecto.
- 

### Instalacion

- Clonar el proyecto - `https://github.com/garceteclaudio/web-test-automation.git`.

- Para utilizar el proyecto, se debe abrir una consola bash, situarnos en el directorio raiz del proyecto e instalar las dependencias de la siguiente manera:


```
npm install
```


### Ejecutando las pruebas

Las pruebas son ejecutadas localmente.

- Ubicacarse en la raiz del proyecto.

- Ejecutar el siguiente script:

```
behave features/login.feature
```

### Reporte de pruebas

- Ubicarse en el archivo reports/html/index.html

![Screenshot](reports.png)


## Construido con
* [Python](https://www.python.org/downloads/) - Programming language
* [Selenium WebDriver](https://www.selenium.dev/documentation/webdriver/) - Framework E2E utilizado
* [Behave](https://behave.readthedocs.io/en/latest/) - Framework para escribir los escenarios de prueba en lenguaje GHERKIN


## Autor
* **Claudio Rodolfo Garcete** - *Automation Tester* 

## Consultas
* garcete.claudio@gmail.com