# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # 1. Initialize the WebDriver
# # Ensure the path to your driver executable is correct
# driver = webdriver.Chrome()
#
# # 2. Navigate to the webpage
# url = "https://example-url-with-datatable.com"  # Replace with your actual URL
# driver.get(url)
#
# # Wait for the table to be present (optional, but recommended for dynamic pages)
# try:
#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.TAG_NAME, "table"))
#     )
# except Exception as e:
#     print(f"Error waiting for table: {e}")
#
# # 3. Locate the table element
# # Use a specific locator if the page has multiple tables (e.g., By.ID, By.CLASS_NAME)
# table = driver.find_element(By.TAG_NAME, "table")
#
# # 4. Find all rows within the table (tbody/tr)
# # The first row is often a header row (th), so iteration may start from index 1
# rows = table.find_elements(By.TAG_NAME, "tr")
#
# names_list = []
#
# # 5. Iterate through rows and cells to extract names
# for index, row in enumerate(rows):
#     # Skip the header row if necessary (assuming the first row is the header)
#     if index == 0:
#         continue
#
#     # Find all data cells (td) in the current row
#     cells = row.find_elements(By.TAG_NAME, "td")
#
#     # Assuming the name is in the first column (index 0)
#     if cells:
#         name_element = cells[0]
#         name = name_element.text  # Use the .text attribute to get the visible text
#         names_list.append(name)
#
# # 6. Print the extracted names
# print("Extracted names:")
# for name in names_list:
#     print(f"* {name}")
#
# # 7. Close the browser
# driver.quit()
# Import required libraries



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
#
# driver = webdriver.Chrome()
#
# driver.get("https://www.amazon.in")
#
# driver.maximize_window()
#
#
# time.sleep(2)
#
#
# search_box = driver.find_element(By.ID, "twotabsearchtextbox")
#
#
#
# mobile_name = "iPhone 15"
# search_box.send_keys(mobile_name)
#
#
# search_button = driver.find_element(By.ID, "nav-search-submit-button")
# search_button.click()
#
# # Wait for results to load
# time.sleep(3)
#
# # fetch price of the mobile_name list
# price = driver.find_element(By.XPATH, "(//span[@class='a-price-whole'])[1]")
#
#
# print("Price of", mobile_name, ":", price.text)
#
# driver.quit()



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
#
# driver.get("https://www.flipkart.com/")
#
# driver.maximize_window()
#
# wait = WebDriverWait(driver, 10)
#
# # Close login popup
# try:
#     close_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'✕')]")))
#     close_btn.click()
# except:
#     pass
#
# # Find search box
# search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
#
# item_name = "Jordan shoes"
#
# search_box.send_keys(item_name)
# search_box.send_keys(Keys.ENTER)
#
# # Wait for product prices to load
# price = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'₹')])[1]")))
#
# print("Price of", item_name, ":", price.text)
#
# driver.quit()





from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)
driver.maximize_window()

driver.get("https://www.flipkart.com")
sleep(4)
driver.find_element(By.CLASS_NAME, "nw1UBF.v1zwn25").send_keys("iPhone 15")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
print(driver.find_element(By.XPATH, '//div[contains(@class, "RG5Slk")]/../..//div[@class="hZ3P6w DeU9vF"]').text)