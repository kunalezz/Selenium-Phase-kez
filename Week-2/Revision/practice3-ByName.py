from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

assert "Facebook" in driver.title, "Naah!"

el = driver.find_element(By.NAME, "email")
el.clear()
el.send_keys("kunal.ez")
time.sleep(5)

driver.close()
driver.quit()