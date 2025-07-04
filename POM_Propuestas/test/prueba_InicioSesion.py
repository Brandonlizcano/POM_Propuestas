import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




Base_URL = "https://propuestas.andesscd.com.co/"

#Credenciales

USERNAME = "Brandon.lizcano"
PASSWORD = "456789**"

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.NAME, USERNAME)
        self.password_field = (By.NAME, PASSWORD)
        self.login_button = (By.XPATH, '//button[@type="kt_sign_in_submit"]')

def get_username(self):
        return self.driver.find_element(*self.username_field)
def get_password(self):
        return self.driver.find_element(*self.password_field)
def get_login_button(self):
        return self.driver.find_element(*self.login_button) 

def Inicio_Sesion (self, username, password):
    self.get_username().send_keys(username)
    self.get_password().send_keys(password)

def click_Inicio_Sesion(self):
    self.get_login_button().click()

@staticmethod
def get_Base_URL():
    return Base_URL

