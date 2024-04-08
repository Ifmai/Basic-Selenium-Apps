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

# iframe dediğimiz şey sayfamızın içinde başka bir sayfa gibi çalışan bir yapıdır.
# selenium ile iframe geçişleri yapabilmek için switch_to.frame() fonksiyonunu kullanırız.
# iframe geçişleri yaparken iframe'in id'sini, name'ini veya index'ini kullanabiliriz.
# diğer türlü bu iframe içindeki elementlere ulaşamayız.
# daha sonrasında ana sayfaya dönmek için switch_to.default_content() fonksiyonunu kullanırız.
# bu fonksiyon sayfanın en üstüne çıkarak ana sayfaya geçiş yapar.

driver.get("https://tomspizzeria.herokuapp.com/iframe-demo.html")
time.sleep(2)
# switch_to.frame => iframe gecis yapar
# paremetre olarak 3 farkli deger alabilir
# 1. iframe id
# 2. iframe name
# 3 index (0'dan basliyor')
driver.switch_to.frame("email_frame")
driver.find_element(By.ID, "email").send_keys("brad.pitt@fil.com")
time.sleep(2)
# default_content => en ana sayfaya don,, sayfanin aslina don
# parent_frame => bir ustteki frame gecis icin
# 1. ana sayfa
#   2. frame 1
#      3 frame 2
driver.switch_to.default_content()
driver.find_element(By.ID, "isim").send_keys("angelina.jolie@film.com")
time.sleep(2)


driver.quit()