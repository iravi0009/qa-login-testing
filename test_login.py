from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize browser
driver = webdriver.Chrome()

# Open demo login page
driver.get("https://example.com/login")

# Maximize window
driver.maximize_window()

try:
    # Locate username and password fields
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")

    # Enter test data
    username.send_keys("testuser")
    password.send_keys("123456")

    # Click login button
    login_btn = driver.find_element(By.XPATH, "//button")
    login_btn.click()

    # Wait to observe result
    time.sleep(3)

    print("Test Executed Successfully")

except Exception as e:
    print("Error occurred:", e)

finally:
    driver.quit()
