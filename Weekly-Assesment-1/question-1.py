from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.maximize_window()


driver.get("https://www.facebook.com")


wait = WebDriverWait(driver, 10)


email_field = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='email']"))
)
email_field.send_keys("sampleemail@gmail.com")


password_field = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='pass']"))
)
password_field.send_keys("samplepassword123")


login_button = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='login']"))
)
login_button.click()


import time
time.sleep(5)


driver.quit()