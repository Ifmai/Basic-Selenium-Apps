import time

from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert

chromedriver_autoinstaller.install() 
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/javascript_alerts")

firstAlert = driver.find_element(By.XPATH, value="//button[contains(text(), 'Click for JS Alert')]")
secondAlert = driver.find_element(By.XPATH, value="//button[contains(text(), 'Click for JS Confirm')]")
thirdAlert = driver.find_element(By.XPATH, value="//button[contains(text(), 'Click for JS Prompt')]")

#firstAlert.click()
#secondAlert.click()
thirdAlert.click()

WebDriverWait(driver, 10).until(expected_conditions.alert_is_present())
alert = Alert(driver)
alert.send_keys("Hello World") #3. alert için
time.sleep(2)

print(alert.text) # alert mesajını alır.
alert.accept()
#alert.dismiss() # 2. ve 3. alert için
print(driver.find_element(By.ID, value="result").text)

time.sleep(2)
driver.quit()