import time

from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


chromedriver_autoinstaller.install() 
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://the-internet.herokuapp.com/upload")

#şimdi upload penceresi açılacak ve dosya seçme işlemi yapılacak
#dosya seçme işlemi için send_keys() fonksiyonunu kullanıyoruz.
#o normalde açılan windows/mac/linux artık hangi işletim sistemini kullanıyorsanız
#o pencere selenium ile ulaşamayız. çünkü o bir javascript alert penceresi filan değil
# direk işletim sistemi tarafından açılan bir pencere. bu yüzden selenium ile ona ulaşamayız.
# ancak burada biz onu tamamen aradan kaldırıyoruz. çünkü send_keys() fonksiyonu ile
# input edilecek id ye direk biz absolute path veriyoruz. yani dosyanın yolunu veriyoruz.
# aslında o pencerenin de yaptığı işlem bu. bizim yaptığımız işlem ile aynı.
# sadece daha görsel xd

#burada ki en önemli detay dosyayı file-upload ediğicemiz html elemanın
# 1. input etiketine sahip olması. yani <input> olması gerekiyor. </input> olmamalı
# 2. type="file" olması gerekiyor. yani <input type="file"> olmalı </input> olmamalı
# buna dikkat etmeniz gerekiyor. doğru elemente ulaşamazsanız dosya yükleyemezsiniz.

driver.find_element(By.ID, "file-upload").send_keys("/Users/huseyinalpaslanozdemir/Documents/GitHub/Basic-Selenium-Apps/14-DosyaYükleme/main.py")
time.sleep(2) # burada görmek için bekliyoruz. dosyanın yüklendiğini görmek için
# diğer türlü direk yüklenecek ve sonuç sayfasına geçilecek. çünkü selenium çok hızlı
# ben kendim görmek istediğim için koydum xd.
driver.find_element(By.ID, "file-submit").click()

WebDriverWait(driver, 30).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id='content']//h3")))

print(driver.find_element(By.XPATH, "//div[@id='content']//h3").text)
fileName = driver.find_element(By.ID, "uploaded-files")
print(fileName.text)
time.sleep(2)

driver.quit()