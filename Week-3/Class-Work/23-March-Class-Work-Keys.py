# 1- Basics of Keysq
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("https://www.amazon.in")
# driver.maximize_window()
#
# wait = WebDriverWait(driver, 10)
#
# el = wait.until(EC.presence_of_element_located((By.NAME, "field-keywords")))
# el.send_keys("Shoes")
# el.send_keys(Keys.RETURN)
#
# import time
# time.sleep(5)
#
# driver.quit()
import time

# 2-Drag and Drop using Keys
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Chrome()
# driver.get("https://demoqa.com/text-box")
#
# el = driver.find_element(By.ID, "currentAddress")
# el.send_keys("34-A RPN")
# el.send_keys(Keys.CONTROL + 'c')
# el.send_keys(Keys.RETURN)
# el2
#
#
# driver.quit()



# 3 - Action-Chains-Clicks
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# import time
#
# driver = webdriver.Chrome()
# driver.get('https://demoqa.com/buttons')
#
# actions = ActionChains(driver)
#
# # Double Click
# el = driver.find_element(By.ID, "doubleClickBtn")
# actions.double_click(el).perform()
#
# time.sleep(2)
#
# # Right Click
# el2 = driver.find_element(By.ID, "rightClickBtn")
# actions.context_click(el2).perform()
#
# time.sleep(2)
#
# driver.quit()

# 4 - Action-Chains-Clicks
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.get("https://www.amazon.in")
#
# action = ActionChains(driver)
#
# # Example: click on "Mobiles" link (stable element)
# el = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Mobiles')]"))
# )
#
# action.move_to_element(el).click().perform()
#
# driver.quit()


# # 5 - Action-Chain-Class-Scroll-by-amount
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.get("https://www.amazon.in")
#
# action = ActionChains(driver)
#
# # Example: click on "Mobiles" link (stable element)
# el = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Mobiles')]"))
# )
# action.move_to_element(el).click().perform()
# time.sleep(3)
# action.scroll_by_amount(0,1000).perform()
# time.sleep(3)
#
#
# driver.quit()

# 6 Scroll-By-Origin
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.get("https://www.amazon.in")
#
# action = ActionChains(driver)
#
# el = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Mobiles')]"))
# )
#
# action.scroll_to_element(el).perform()
#
# time.sleep(3)
#
# # scroll from element
# origin = ScrollOrigin.from_element(el)
# action.scroll_from_origin(origin, 0, 1000).perform()
#
# time.sleep(3)
#
# driver.quit()

# 7 Move to element
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.get("https://www.amazon.in")
#
# action = ActionChains(driver)
#
# el = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Mobiles')]"))
# )
#
# action.move_to_element(el).perform()
#
# time.sleep(3)
#
#
# driver.quit()

# 8 CLick and Hold
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.get("https://yonobusiness.sbi.bank.in/yonobusinesslogin")
# time.sleep(2)
# action = ActionChains(driver)
#
# el = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.ID, "password"))
# )
# el.send_keys('kneegrow')
# el2 = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]'))
# )
# action.move_to_element(el2).click_and_hold().pause(3).release().perform()
# time.sleep(3)
#
# driver.quit()


# 9 Drag and Drop
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://demoqa.com/droppable")
time.sleep(2)
action = ActionChains(driver)

el = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "draggable"))
)

el2 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "droppable"))
)

action.drag_and_drop(el, el2).perform()
time.sleep(3)

driver.quit()
