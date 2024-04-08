from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install() 
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://tomspizzeria.b4a.app/")
ortaBoy = driver.find_element(By.CSS_SELECTOR, value="input[value='Orta']")
zeytin = driver.find_element(By.CSS_SELECTOR, value="input[value='zeytin']")
mantar = driver.find_element(By.CSS_SELECTOR, value="input[value='mantar']")	
ortaBoy.click()
print(ortaBoy.is_selected())
print(zeytin.is_selected())
print(mantar.is_selected())
time.sleep(2)
driver.quit()