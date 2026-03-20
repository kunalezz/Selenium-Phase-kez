from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.ID, "name").send_keys("Kunal")


driver.find_element(By.ID, "email").send_keys("kez@gmail.com")


driver.find_element(By.ID, "phone").send_keys("9928700174")

driver.find_element(By.ID, "textarea").send_keys("34-A shivpuri Jhotwara, Jaipur 302012")

driver.find_element(By.ID, "male").click()

driver.find_element(By.XPATH, '//*[@id="sunday"]').click()
driver.find_element(By.XPATH, '//*[@id="friday"]').click()
driver.find_element(By.XPATH, '//*[@id="saturday"]').click()

driver.find_element(By.ID, "country").send_keys("India")

driver.find_element(By.ID, "colors").send_keys("Blue")

driver.find_element(By.ID, "animals").send_keys("Lion")


time.sleep(2)

driver.quit()
