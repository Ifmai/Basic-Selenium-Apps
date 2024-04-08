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
print(driver.title)
#print(driver.current_window_handle)
#hangi sekmede olduğumuzu görmek için current_window_handle kullanılır.
#selenium her bir sekme için bir id oluşturur ve bu id'yi current_window_handle ile alabiliriz.
#bu id'yi alarak hangi sekmede olduğumuzu görebiliriz. işlemlerimizi buna göre kontrol ederek yapabiliriz.
time.sleep(2)
driver.switch_to.new_window('tab')
driver.get("http://www.google.com")
print(driver.title)
#print(driver.current_window_handle)
time.sleep(2)
apple = driver.window_handles[0] # 0 da olduğunu biliyoruz ilk açılan sekme.
#window_handles ile açık olan tüm sekmelerin id'lerini alabiliriz.
driver.switch_to.window(apple)
#switch_to.window bizden bir name paremetresi bekler ve bu name paremetresi o sekmenin id'si olmalıdır.
#bu şekilde pencereler arasında geçiş yapabiliriz.
time.sleep(2)
driver.quit()
