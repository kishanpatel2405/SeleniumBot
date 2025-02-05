from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver with an increased timeout
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open Facebook login page
driver.get("https://www.facebook.com/")

# Wait for the page to load
time.sleep(3)

# Locate the email/phone input field and the password input field
email_input = driver.find_element(By.ID, "email")
password_input = driver.find_element(By.ID, "pass")

# Enter your credentials
email_input.send_keys("your_email@example.com")  # Replace with your email
password_input.send_keys("your_password")  # Replace with your password

# Press the 'Enter' key to submit the login form
password_input.send_keys(Keys.RETURN)

# Wait for the login process to complete (you can also use explicit waits here)
time.sleep(5)

# Optional: Close the browser after a few seconds
driver.quit()
