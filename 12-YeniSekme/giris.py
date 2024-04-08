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
driver.get("http://www.apple.com")
time.sleep(2)
#window de yeni bir pencere açar.
#driver.switch_to.new_window('window')
#tab de yeni bir sekme açar.
driver.switch_to.new_window('tab')
driver.get("http://www.google.com")
time.sleep(2)
driver.quit()

#burada basit bir şekilde nasıl yeni sekme açıp orada bir sayfaya gideceğimizi gördük.
#unutmayın driver o an hangi sekmedeyse yapıcağı tüm işlemler o sekmede gerçekleşir.
#bir den fazla sekmeyle işlem yaparken hangi sekmede olduğunu unutmamak gerekir.