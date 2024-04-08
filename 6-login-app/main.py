from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install() 

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()
userNameBox = driver.find_element(By.ID, value="username")
passwordBox = driver.find_element(By.ID, value="password")

userNameBox.send_keys("tomsmith")
passwordBox.send_keys("SuperSecretPassword")
element = driver.find_element(By.CSS_SELECTOR, value="button[type='submit']")
#element = driver.find_element(By.XPATH, value="//button[@type='submit']")
element.click()

nowUrl = driver.current_url
if nowUrl == "https://the-internet.herokuapp.com/secure":
	print("Giriş başarılı")
else:
	errorText = driver.find_element(By.ID, value="flash").text
	print("Hata: ", errorText)
	print("Giriş başarısız")

#element.click()
time.sleep(2)
driver.quit() # Tarayıcıyıda açık olan tüm sekmeleri kapatır