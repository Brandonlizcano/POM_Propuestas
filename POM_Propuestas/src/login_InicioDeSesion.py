from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
 



USERNAME = "Brandon.lizcano"
PASSWORD = "456789**"
 

driver = webdriver.Edge()



driver.get('https://propuestas.andesscd.com.co/')
 
 
USario_Ingresar = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, 'usuario'))
)
USario_Ingresar.click()
USario_Ingresar.send_keys(USERNAME)
 
Contraseña_ingresar = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, 'contraseña'))
)
Contraseña_ingresar.click()
Contraseña_ingresar.send_keys(PASSWORD)
Contraseña_ingresar.send_keys(Keys.RETURN)
 
 
time.sleep(15)
 
 
driver.quit()
 