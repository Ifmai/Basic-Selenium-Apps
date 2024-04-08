from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install() 

driver = webdriver.Chrome()

driver.get("https://tr.wikipedia.org/wiki/Anasayfa")
driver.maximize_window()
text = driver.find_element(By.ID, value="mp-tfa")
print(text.text)

time.sleep(5)
driver.quit() # Tarayıcıyıda açık olan tüm sekmeleri kapatır