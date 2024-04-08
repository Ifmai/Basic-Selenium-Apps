import time

from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chromedriver_autoinstaller.install() 
driver = webdriver.Chrome()
driver.maximize_window()
#imlicit wait - gizli bekleme
driver.implicitly_wait(20)
# driver nesnesi ile kullanmamız bu waiting yönteminin güzel olan yanıdır.
# bu wait tüm driver nesnesi kapanana kadar geçerlidir.
# herhangi bir elementi bulamadığında sayfanın yüklenmesini bekliyoruz 20 saniye kadar.

driver.get("https://www.amazon.com")
driver.implicitly_wait(30)
#böyle bir şey yaparsak ilkini override yapar. 
#başta dediğimiz gibi tüm program için bu bir kez yeterlidir.

# şimdi bu bekleme türü şunun için kullanılır eğer
# bu sayfa 20-30 saniye içerisinde yüklenmezse test driverımız kapanır.
# bizde bu sayfanın yüklenmesinde sorun olduğunu anlarız.
# bu beklemede spesifik bir şeyi beklemeyiz. sadece sleep gibi bekleriz ancak sleep kullanmaktan daha mantıklıdır.
# çünkü total program boyu geçerlidir bu kod bir defa tanımlandığında.
# sayfa yüklendiğinde işlem yapılır ve devam edilir.
# sleepde ise o süre geçene kadar kod akışı sağlanamaz.
# bu yüzden hiç bir zaman sleep kullanmaktan yana olmayacağız.
# ve kodumuzda her yerde time.sleep(10) görmek çok terchimiz değil.
# ayrıca çok kirli gözükmektedir.
driver.quit()