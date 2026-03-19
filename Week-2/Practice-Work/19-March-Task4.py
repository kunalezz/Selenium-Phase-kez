# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time
#
#
# driver = webdriver.Chrome()
# driver.get("https://testautomationpractice.blogspot.com/")
#
# upFiles = driver.find_elements(By.ID,"singleFileInput")
# upFiles.send_Keys("/Users/kunalsoni/Downloads/harsh_certi.pdf")
# time.sleep(1)
#
# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

time.sleep(2)
single_file = driver.find_element(By.ID, "singleFileInput")
single_file.send_keys("/Users/kunalsoni/Downloads/harsh_certi.pdf")
time.sleep(1)


# Click upload button (optional)
driver.find_element(By.XPATH, "//button[text()='Upload Single File']").click()

time.sleep(2)


files = '/Users/kunalsoni/Downloads/IMG_6384.HEIC\n/Users/kunalsoni/Downloads/WhatsApp Image 2025-06-05 at 11.44.36.jpeg'

multi_file = driver.find_element(By.ID, "multipleFilesInput")
multi_file.send_keys(files)

time.sleep(1)

# Click upload button (optional)
driver.find_element(By.XPATH, "//button[text()='Upload Multiple Files']").click()

time.sleep(2)

driver.quit()