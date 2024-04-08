import time

from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chromedriver_autoinstaller.install() 
driver = webdriver.Chrome()
driver.maximize_window()

# bu sayfada 3 saniye beklediğimiz de bir buton oluşacak bir template site.
driver.get("https://pynishant.github.io/Selenium-python-waits.html")
# explicit wait - açıktan bekleme

#driver.implicitly_wait(10)# bunu koyarsak sayfa yüklenmesi için bekliyor olacağız.
# çalışır mı çalışır ama biz burada bir buton var 
# ve o butonun geri dönüt süresi net 3 saniye biz onu bekleyeceğiz.
# ayrıca her zaman kaç saniye olacağını bilemezsiniz bu yüzden az süre verirsek test patlar.
tryit = driver.find_element(By.XPATH, value="//button[contains(text(), 'Try it')]")
tryit.click()
#şimdi burada wait fonksiyonunu yorum satırına alıp denerseniz hata vericek selenium
#selenium gerçekten çok hızlı çalışıyor bu yüzden 3 saniye geçmeden clıck me butonuna basmaya
#çalışcaktır ancak 1 saniye bile geçmeden gözükmeyen bir butona basmaya çalıştığında hata alırsınız.

#WebDriverWait şimdi burada bu arkadaş nasıl çalışıyor
# 1. Paremetre hangi driver ile işlem yapılacağı. 2. Paremetre Max kaç saniye bekleyeceği.
# sonrasında ona until bir şart sağlanana kadar bekle diyeceğiz.
# ona bir expected conditions vericez. bir şart veriyoruz.
# burada bir element olduğu için şartıız presence_of_element_located bu element var mı diye bakıyoruz.
# bu element oluştuğu an kod çalışmaya devam edicektir.
# bu element koşulunu ise her yarım saniyede bir kontrol ediyor.
# yaklaşık 6. kontrolünden sonra işlemi yapıcak demektir.
# bu bekleme süresini override edebilirsiniz. 3. paremetre float değer tipinde kaç saniyede bir kontrol edeceğini alır.
WebDriverWait(driver, 45).until(expected_conditions.presence_of_element_located((By.XPATH, "//button[contains(text(), 'CLICK ME')]")))
#buradaki expected_conditions ile
#radio butonların çıkmasını, seçilebilir olmasını vb. bir çok şeyi bekleyebilirsiniz.
#sayfa değişiyorsa url bile değişip değişmediğini şart olarak verebilirsin.
#title da var. xd
#burayı detaylı incele dostum.
clickMe = driver.find_element(By.XPATH, value="//button[contains(text(), 'CLICK ME')]")
clickMe.click()

#son dikkatini çekiceğim durum
#presence vs visibility
#buradaki durum presence durumu başta CLICK ME butonu sayfa html içerisinde yok.
#bir fonksiyon ile üretiliyor. html içerisinde presence olan her şey görünür olucak diye bir durum yok.
#bunu kullanırken buna dikkat etmeyi unutma. eğer html içerisinde yoksa beklediğin şey presence
#eğer var ancak görünür olmasını bekliyorsan visibility durumunu kontrol etmeyi unutma.
driver.quit()