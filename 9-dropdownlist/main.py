from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
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
zeytin.click()

odeme = Select(driver.find_element(By.ID, value="odeme-tipi"))
odemeTypes = odeme.options #web element listesi döndürür. her bir option için.

for odemeType in odemeTypes:
	print(odemeType.text)

odeme.select_by_value("Kredi Kartı")
# odeme.select_by_index(3) #index vererek seçme
#odeme.deselect_all # tüm seçenekleri kaldırıır
#odeme.deselect_by_value()
#odeme.deselect_by_index()
time.sleep(2)
driver.quit()