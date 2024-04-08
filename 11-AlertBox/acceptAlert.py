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

driver.get("https://pynishant.github.io/Selenium-python-waits.html")

tryit = driver.find_element(By.XPATH, value="//button[contains(text(), 'Try it')]")
tryit.click()

WebDriverWait(driver, 45).until(expected_conditions.presence_of_element_located((By.XPATH, "//button[contains(text(), 'CLICK ME')]")))
clickMe = driver.find_element(By.XPATH, value="//button[contains(text(), 'CLICK ME')]")
clickMe.click()

# alert bekliyoruz çünkü çok kısa sürede çıkıyor olsa bile selenium ondan daha hızlı
WebDriverWait(driver, 3).until(expected_conditions.alert_is_present()) 
alert = Alert(driver)
alert.accept()

driver.quit()