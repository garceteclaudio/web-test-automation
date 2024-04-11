import pysikuli as sik
from pysikuli import Key, Button, Region, config
import time


sik.mouseMove((100,100))

configuracionAvanzadaPicture="C:/proyecots_personales/web-test-automation/imageAutomation/configuracionAvanzada.png"
accederAwww="C:/proyecots_personales/web-test-automation/imageAutomation/accederAwww.png"

findd = sik.find(image=configuracionAvanzadaPicture, max_search_time=5)
print("valor: ",findd)


sik.click(configuracionAvanzadaPicture)
time.sleep(1)
sik.click(accederAwww)
time.sleep(4)
#Click "Activar advertencias"