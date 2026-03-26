# import os
# from time import sleep
# import time
# from selenium.webdriver import Chrome, ChromeOptions
# from selenium.webdriver.common.by import By
#
# o = ChromeOptions()
# o.add_experimental_option('detach', True)
# o.add_experimental_option("prefs", {"safebrowsing.enabled":True})
# o.add_argument("--disable-notifications")
# driver = Chrome(options=o)
# driver.implicitly_wait(10)
#
# # driver.get("https://google.com")
# # # print(driver.title)
# #
# # expected='GOOGLE'
# # actual=driver.title
# # assert expected==actual, "title mismatchh"
#
# # driver.get("https://amazon.in")
# # driver.find_element(By.LINK_TEXT,"Bestsellers").click()
# # actual=driver.title
# # expected='Amazon.in Bestsellers: The most popular items on Amazon'
# # assert expected==actual, "title mismatchh"
# # driver.save_screenshot(f'{folder}/ss1.png')
#
# # driver.get("https://google.com")
# # folder=os.path.join(os.getcwd(),'ssz')
# # os.makedirs(folder,exist_ok=True)
# #
# #
# # ele=driver.find_element(By.XPATH,"//textarea[@title='Search']")
# # ele.screenshot(f'{folder}/ss_ele{time.strftime("%Y%m%d-%H%M%S")}.png')
#
#
#
#
#
# sleep(5)
# driver.quit()
#
#

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
#
# # Start browser
# driver = webdriver.Chrome()
#
# # Open website
# driver.get("https://www.saucedemo.com/")
#
# # Maximize window (optional)
# driver.maximize_window()
#
# # Enter valid username
# driver.find_element(By.ID, "user-name").send_keys("standard_user")
#
# # Enter WRONG password
# driver.find_element(By.ID, "password").send_keys("wrong_password")
#
# # Click login button
# driver.find_element(By.ID, "login-button").click()
#
# # Wait for response
# time.sleep(2)
#
# # method 1
# # # Check for error message
# # try:
# #     error = driver.find_element(By.XPATH, "//h3[@data-test='error']")
# #
# #     if error.is_displayed():
# #         print("Login failed - taking screenshot")
# #
#         # Take screenshot
#         driver.save_screenshot("login_error.png")
#
# except:
#     print("No error message found")

# Close browser
# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start browser
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

# Enter valid username
driver.find_element(By.ID, "user-name").send_keys("standard_user")

# Enter WRONG password
driver.find_element(By.ID, "password").send_keys("wrong_password")

# Click login
driver.find_element(By.ID, "login-button").click()

# Wait for error message
wait = WebDriverWait(driver, 10)
error_element = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']"))
)

# ASSERT: Check error message is displayed
assert error_element.is_displayed(), "Error message not displayed!"

print("Assertion Passed: Error message is visible")

# Take screenshot after assertion
driver.save_screenshot("login_error.png")

# Close browser
driver.quit()