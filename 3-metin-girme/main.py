from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
import time

# Chrome'u otomatik olarak indirir ve yükler
chromedriver_autoinstaller.install() 

#driver = webdriver.Chrome(executable_path="C:/Users/pc/Desktop/chromedriver.exe")
#Driver oluşturuldu (Tarayıcı açıldı)
driver = webdriver.Chrome()

#get metodu bizi belirtilen siteye yönlendirir
driver.get("https://google.com")
driver.maximize_window()

arama_kutusu_id = driver.find_element(By.ID, value="APjFqb") # id üzerinden Arama kutusunu bulur
arama_kutusu_name = driver.find_element(By.NAME, value="q") # name üzerinden Arama kutusunu bulur
arama_kutusu_name.send_keys("Python") # id ilede aynı şekilde yapıyoruz. 
arama_kutusu_name.send_keys(Keys.ENTER) # Keys sınıfı içerisinden ENTER tuşuna basmak için kullanılır.

time.sleep(5)
driver.quit() # Tarayıcıyıda açık olan tüm sekmeleri kapatır