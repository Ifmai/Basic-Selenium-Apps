from selenium import webdriver
import chromedriver_autoinstaller
import time

# Chrome'u otomatik olarak indirir ve yükler
chromedriver_autoinstaller.install() 

#driver = webdriver.Chrome(executable_path="C:/Users/pc/Desktop/chromedriver.exe")
#Driver oluşturuldu (Tarayıcı açıldı)
driver = webdriver.Chrome()

#get metodu bizi belirtilen siteye yönlendirir
driver.get("http://www.python.org")
now_url = driver.current_url # Şu anki url'yi bize string olarak geri döndürür.
print(now_url)
driver.maximize_window() # Tarayıcıyı tam ekran yapar
driver.get("http://www.google.com")
title = driver.title # Sayfanın başlığını bize string olarak geri döndürür.
driver.back() # Bir önceki sayfaya gitmek için kullanılır
#driver.forward() # Bir sonraki sayfaya gitmek için kullanılır
#driver.refresh() # Sayfayı yenilemek için kullanılır
print(title)
time.sleep(5)
driver.close() # Tarayıcıyıda şuan çalışılan sekmeyi kapatır
driver.quit() # Tarayıcıyıda açık olan tüm sekmeleri kapatır