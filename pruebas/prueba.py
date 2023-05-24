from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import time
import pandas as pd

Options = webdriver.ChromeOptions()
Options.add_argument('--start-maximized')
Options.add_argument('--disable-extensions')

#driver_path= 'C:/Users/algiv/OneDrive/Escritorio/Chillvacc/ChilVacc/pruebas/chromedriver.exe'
driver= webdriver.Chrome(options=Options)
driver.get('http://localhost:3000')


WebDriverWait(driver, 5)\
    .until(ec.element_to_be_clickable((By.XPATH,'/html/body/div/div/header/div[2]/div/div/div/div[3]/form/input')))\
    .send_keys("hola")

WebDriverWait(driver, 5)\
    .until(ec.element_to_be_clickable((By.XPATH,'/html/body/div/div/header/div[2]/div/div/div/div[3]/form/button')))\
    .click()

time.sleep(10)