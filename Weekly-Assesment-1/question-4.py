from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.maximize_window()

# Open Myntra website
driver.get("https://www.myntra.com")


time.sleep(3)


search_box = driver.find_element(By.CLASS_NAME, "desktop-searchBar")


search_box.send_keys("shoes")


time.sleep(5)


driver.quit()