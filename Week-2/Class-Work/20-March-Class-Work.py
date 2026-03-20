# from selenium  import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# import time
#
# driver = webdriver.Chrome()
# driver.get("file:///Users/kunalsoni/Library/Containers/net.whatsapp.WhatsApp/Data/tmp/documents/713A86E7-7C44-45FC-94A7-72049A8EA3A9/E22_Dropdowns.html")
# #Single Select DropDown
# dropdown = driver.find_element(By.ID, 'state')
# option = Select(dropdown)
#
#
# option.select_by_visible_text("Bihar")
# time.sleep(2)
#
# option.select_by_value('MH')
# time.sleep(2)
#
# option.select_by_index(0)
# time.sleep(2)
#
# # multi-select DropDown
# driver.find_element(By.XPATH, '//option[@value="dance"]').click()
# time.sleep(2)
# driver.find_element(By.XPATH, '//option[@value="music"]').click()
# time.sleep(2)
#
#
#
# driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# driver = webdriver.Chrome()
# driver.get("https://www.amazon.in/")
#
# wait = WebDriverWait(driver, 10)
#
# # Step 1: Find search box
# search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
#
# # Step 2: Type query
# search_box.send_keys("nike shoes")
#
# time.sleep(2)
# # Step 3: Wait for suggestions to appear
# suggestions = wait.until(
#     EC.presence_of_all_elements_located((By.XPATH, "//div[@role='row']"))
# )
#
# time.sleep(2)
#
# # Step 4: Print all suggestions
# for s in suggestions:
#     print(s.text)
#
# suggestions[0].click()
#
#
# driver.quit()




