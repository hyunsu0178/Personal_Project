from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Path to your ChromeDriver
CHROMEDRIVER_PATH = "/Users/hyunsupark/Project/Personal_Project/macro/chromedriver"

driver = webdriver.Chrome(CHROMEDRIVER_PATH)

try:
    # Navigate to the class registration page
    driver.get("https://saprod.emory.edu")

    # Wait for the page to load
    time.sleep(2)
    # Wait for login to complete
    # Locate and check the required checkboxes
    # Use appropriate selectors (e.g., ID, name, XPath, or class)
    checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
    for checkbox in checkboxes:
        if not checkbox.is_selected():
            checkbox.click()  # Check the box

    # Wait for a moment before clicking the register button
    time.sleep(2)

    # Locate and click the "Register" button
    # register_button = driver.find_element(By.ID, "register_button")  # Adjust selector as needed
    # register_button.click()

    # Wait for registration confirmation
    time.sleep(5)

finally:
    # Close the browser
    driver.quit()