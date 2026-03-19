# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# # 1. Open Amazon
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("https://www.amazon.com/")
#
# wait = WebDriverWait(driver, 10)
#
# # 2. Search "watch"
# search_box = wait.until(EC.presence_of_element_located((By.NAME, "field-keywords")))
# search_box.clear()
# search_box.send_keys("watch")
# search_box.send_keys(Keys.RETURN)
#
# driver.implicitly_wait(10)
# # 4. Get all product containers
# products = driver.find_elements(By.CLASS_NAME, "a-price-whole")
#
# for i in products:
#     print(i.text)
# # 5. Quit browser
# driver.quit()



# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Chrome()
# driver.get("https://www.facebook.com/")
#
# el = driver.find_element(By.CLASS_NAME, "x1i10hfl")
# el.send_keys("kunal.ez")
# driver.find_element(By.NAME, "pass").send_keys("123")
# time.sleep(5)
# driver.find_element(By.CLASS_NAME, "x1ja2u2z").click()
# time.sleep(5)
# driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup the webdriver (example for Chrome)
# driver = webdriver.Chrome()
# driver.get("") # Replace with the actual URL
#
# # Find the checkbox element (replace 'checkbox_id' with the actual ID, name, or other locator)
#
# checkbox_element = driver.find_element(By.ID, "checkbox_id")
#
# # Check the status of the checkbox
# if checkbox_element.is_selected():
#     print("The checkbox is already selected.")
# else:
#     print("The checkbox is not selected. Clicking it now.")
#     checkbox_element.click() # Select the checkbox
#
# # Verify the status again after potential interaction
# if checkbox_element.is_selected():
#     print("The checkbox is now selected.")
# else:
#     print("The checkbox is still not selected (something went wrong).")
#
#
#
#
#     # Optional: Keep the browser open for a few seconds to observe
#     time.sleep(5)
#     # Close the browser
#     driver.quit()
#
#


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")

name = driver.find_element(By.ID, "firstName")
name.send_keys("Kunal")
time.sleep(1)

surname = driver.find_element(By.ID, "lastName")
surname.send_keys("Soni")
time.sleep(1)

mail = driver.find_element(By.ID, "userEmail")
mail.send_keys("csgo@gamil.com")
time.sleep(1)

#radio button
driver.find_element(By.XPATH, "//label[text()='Male']").click()
time.sleep(1)

number = driver.find_element(By.ID, "userNumber")
number.send_keys("7412016565")
time.sleep(1)

sub = driver.find_element(By.XPATH, '//*[@id="subjectsInput"]')
sub.send_keys("English, Testing")
time.sleep(1)

driver.find_element(By.ID, "hobbies-checkbox-1").click()
driver.find_element(By.ID, "hobbies-checkbox-3").click()
time.sleep(1)

upFile = driver.find_element(By.ID, "uploadPicture")
upFile.send_keys("/Users/kunalsoni/Downloads/IMG_6384.HEIC") # in this we need to send the path address of the image/file
time.sleep(1)

add = driver.find_element(By.ID, "currentAddress")
add.send_keys("csgo has new updates")
time.sleep(1)

city = driver.find_element(By.XPATH, '//*[@id="react-select-3-input"]')
city.send_keys("NCR")
city.send_keys(Keys.ENTER)
time.sleep(1)

paaji = driver.find_element(By.ID, "submit")
paaji.click()

driver.close()
driver.quit()
