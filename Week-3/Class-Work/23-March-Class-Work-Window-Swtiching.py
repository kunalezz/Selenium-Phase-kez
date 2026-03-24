from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

# Store main window
main_window = driver.current_window_handle

# Open new tab
driver.execute_script("window.open('https://www.youtube.com');")
time.sleep(2)

# Get all windows
all_windows = driver.window_handles

# Switch to new tab
for window in all_windows:
    if window != main_window:
        driver.switch_to.window(window)
        break

print(all_windows)
print("Current URL:", driver.current_url)