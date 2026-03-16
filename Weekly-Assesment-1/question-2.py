from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.maximize_window()


driver.get("https://www.youtube.com")


time.sleep(3)

# Locate search box using NAME locator and type text
search_box = driver.find_element(By.NAME, "search_query")
search_box.send_keys("melody hits")


time.sleep(5)


driver.quit()