import time

from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def changeWindow(driver, title):
	i = 0
	windows = driver.window_handles
	for window in windows:
		i += 1
		driver.switch_to.window(window)
		if driver.title == title:
			print("Bulundu : " + str(i) )
			break

chromedriver_autoinstaller.install() 
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("http://www.apple.com")
driver.switch_to.new_window('tab')
driver.get("http://www.google.com")
driver.switch_to.new_window('tab')
driver.get("http://www.amazon.com")


changeWindow(driver, "Google")

#bu kullanmamız gereken yöntem.
#driver.switch_to.window(driver.window_handles[1]) bunda rastgele yerleştirebildiği için
#id leri bu şekilde kullanmak daha mantıklıdır.
#ilk örnekte 2 sekme ile işlem yaptımız için 1. sekme 0. index 2. sekme 1. index'dir.
# ancak 3 ve üstü sekmeyle işlem yaptığımızda indexler değişebilir. Bunun bir garantisi yoktur.
print(driver.title)

time.sleep(5)
driver.quit()