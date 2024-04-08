from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install() 

driver = webdriver.Chrome()

driver.get("https://google.com")
driver.maximize_window()

arama_kutusu_id = driver.find_element(By.ID, value="APjFqb") # id üzerinden Arama kutusunu bulur
arama_kutusu_name = driver.find_element(By.NAME, value="q") # name üzerinden Arama kutusunu bulur
arama_kutusu_name.send_keys("Python") # id ilede aynı şekilde yapıyoruz. 
time.sleep(1)## burada 1 saniye bekliyoruz çünkü googleda arama yaparken buton pozisyon değişiyor ve hata alıyoruz
driver.find_element(By.NAME, value="btnK").click() # Arama butonuna tıklamak için kullanılır.

#burada bir sonuca click atıyoruz ancak google'da arama sonuçları sürekli değiştiği için bu kod çalışmayabilir
#ve ekstra olarak adamlar name/id vermemişler. Bu yüzden css_selector ile yapıyoruz.
#element = driver.find_element(By.CSS_SELECTOR, 'a[href*="udemy.com/course/sifirdan-ileri-seviyeye-python"]')
#element.click()
time.sleep(5)
driver.quit() # Tarayıcıyıda açık olan tüm sekmeleri kapatır