from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install() 
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.imdb.com/")
time.sleep(2)
driver.find_element(By.XPATH, "//button[@data-testid='accept-button']").click()
driver.find_element(By.ID, value="imdbHeader-navDrawerOpen").click()
time.sleep(1)
driver.find_element(By.XPATH , value="//span[text()='Top 250 Movies']").click()
time.sleep(2) # bekliyoruz çünkü liste yüklensin.

#bütün div'i alır.
#filmNameList = driver.find_elements(By.XPATH, value="//ul[@class='ipc-metadata-list ipc-metadata-list--dividers-between sc-a1e81754-0 eBRbsI compact-list-view ipc-metadata-list--base']//li//div[@class='ipc-metadata-list-summary-item__c']")

#bütün div'in içindeki h3'ü alır.
filmNameList = driver.find_elements(By.XPATH, value="//ul[@class='ipc-metadata-list ipc-metadata-list--dividers-between sc-a1e81754-0 eBRbsI compact-list-view ipc-metadata-list--base']//li//div[@class='ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-b0691f29-9 klOwFB cli-title']//h3")
for i in filmNameList :
	print(i.text)
time.sleep(2)
driver.quit() # Tarayıcıyıda açık olan tüm sekmeleri kapatır