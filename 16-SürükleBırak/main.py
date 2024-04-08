import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
driver.implicitly_wait(30)

driver.get("https://demoqa.com/droppable/")

kaynak = driver.find_element(By.CSS_SELECTOR, "div#simpleDropContainer div")
hedef = driver.find_element(By.CSS_SELECTOR, "div#simpleDropContainer div.drop-box")

print("Once: "+hedef.text)
action = ActionChains(driver)
action.drag_and_drop(kaynak, hedef).perform()
time.sleep(2)
print("Sonra: "+hedef.text)
time.sleep(2)
driver.quit()