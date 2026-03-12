from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Launch Chrome browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open a website
driver.get("https://www.google.com")

# Print the current URL
print("Current URL:", driver.current_url)

# Close the browser
driver.quit()