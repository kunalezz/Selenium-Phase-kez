from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.maximize_window()

# Open Naukri website
driver.get("https://www.naukri.com/registration/createAccount")


time.sleep(3)


name = driver.find_element(By.ID, "name")
name.send_keys("Kunal Soni")


email = driver.find_element(By.ID, "email")
email.send_keys("kunal123@gmail.com")


password = driver.find_element(By.ID, "password")
password.send_keys("Password@123")


time.sleep(5)


driver.quit()