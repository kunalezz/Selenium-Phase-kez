# from selenium.webdriver import Chrome, ChromeOptions
# o = ChromeOptions()
# o.add_experimental_option("detach", True)
# driver = Chrome(options=o)

# driver.get("https://demoqa.com/text-box")
# driver.maximize_window()
# sleep(2)
# username =driver.find_element(By.ID,'userName')
# username.send_keys('Sarvesh')
# driver.quit()
# driver.get("https://www.amazon.in")
# driver.maximize_window()
# sleep(3)
#
# search_box = driver.find_element(By.ID, "")
# search_box.send_keys("laptop")
# sleep(2)
# search_button = driver.find_element(By.ID, "nav-search-submit-button")
# search_button.click()

# from selenium.webdriver import Chrome
# from selenium.webdriver.common.by import By
# sleep(3)
# search = driver.find_element(By.CLASS_NAME, "nav-input")
# search.send_keys("laptop")
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep
driver = Chrome(options=0)
# driver.get("https://www.amazon.in")
# driver.maximize_window()
# sleep(3)
# driver.find_element(by.TAG_NAME, "input").send_keys("laptop")

driver.get("https://www.amazon.in")
driver.maximize_window()
sleep(3)
driver.find_element(By.LINK_TEXT,SSSSSSSSSSSSSSSSSSSSSSSSSSSSS
SSSSSSSSSSSSSStoday's Deal").click()
