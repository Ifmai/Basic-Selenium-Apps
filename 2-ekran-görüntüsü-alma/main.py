from selenium import webdriver
import chromedriver_autoinstaller
import time

# Chrome'u otomatik olarak indirir ve yükler
chromedriver_autoinstaller.install() 

#driver = webdriver.Chrome(executable_path="C:/Users/pc/Desktop/chromedriver.exe")
#Driver oluşturuldu (Tarayıcı açıldı)
driver = webdriver.Chrome()

driver.maximize_window() # Tarayıcıyı tam ekran yapar
driver.get("http://www.google.com")
title = driver.title # Sayfanın başlığını bize string olarak geri döndürür.
if title == "Google":
	print("Google'a yönlendirildiniz.")
else: # bunu genellikle hata olduğunda hangi saayfadayız anlamak için kullanırız
	driver.save_screenshot("screenshot.png") # Ekran görüntüsü alır ve belirtilen yere kaydeder

#driver.save_screenshot("screenshot.png") # Ekran görüntüsü alır ve belirtilen yere kaydeder

time.sleep(5)
driver.quit() # Tarayıcıyıda açık olan tüm sekmeleri kapatır