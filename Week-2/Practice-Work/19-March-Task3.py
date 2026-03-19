from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demowebshop.tricentis.com/register")

# Gender
driver.find_element(By.ID, "gender-male").click()
time.sleep(1)

# First Name
driver.find_element(By.ID, "FirstName").send_keys("Kunal")
time.sleep(1)

# Last Name
driver.find_element(By.ID, "LastName").send_keys("Soni")
time.sleep(1)

# Email
driver.find_element(By.ID, "Email").send_keys("abc@gdhasgd.com")
time.sleep(1)

# Password
driver.find_element(By.ID, "Password").send_keys("23123123")
time.sleep(1)

# Confirm Password
driver.find_element(By.ID, "ConfirmPassword").send_keys("23123123")
time.sleep(1)

# Register
driver.find_element(By.ID, "register-button").click()
time.sleep(2)

driver.quit()