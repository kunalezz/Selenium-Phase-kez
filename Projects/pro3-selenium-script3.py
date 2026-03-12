from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Launch Chrome browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open Wikipedia
driver.get("https://www.wikipedia.org")

# Refresh the page
driver.refresh()

# Fetch title of Wikipedia
print("Wikipedia Title:", driver.title)

# Open Amazon
driver.get("https://www.amazon.com")

# Fetch title of Amazon
print("Amazon Title:", driver.title)

# Go back to previous page
driver.back()

# Close the browser
driver.quit()