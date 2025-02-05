from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

username = "kisasnd@gmail.com"
password = "9876534"

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

url = "https://workspace.google.com/intl/en-US/gmail/"

# Initialize the WebDriver
driver = webdriver.Chrome(options=options)

try:
    print("Navigating to the Google Workspace page...")
    driver.get(url)

    # Wait for the "Sign in" button to be clickable and click it
    print("Waiting for 'Sign in' button to be clickable...")
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='Sign into Gmail']"))).click()
    print("Clicked 'Sign in' button.")

    # Wait for the redirect to the Google login page and ensure it's loaded
    print("Waiting for page to load...")
    WebDriverWait(driver, 20).until(EC.url_contains("https://accounts.google.com"))

    # Ensure that the "Email or phone" input field is present
    print("Waiting for email input field...")
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "identifierId")))

    # Enter username
    driver.find_element(By.ID, "identifierId").send_keys(username)
    print("Entered username.")

    # Click the "Next" button after entering the username
    print("Clicking 'Next' button after entering username...")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "identifierNext"))).click()

    # Wait for the password field to be present and enter the password
    print("Waiting for password field to be present...")
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "password")))

    # Enter password
    driver.find_element(By.NAME, "password").send_keys(password)
    print("Entered password.")

    # Click the "Next" button after entering the password
    print("Clicking 'Next' button after entering password...")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "passwordNext"))).click()

    # Successfully logged in (this can be adjusted based on the next page or action needed)
    print("Logged in successfully.")

except TimeoutException as e:
    print(f"Timeout occurred: {e}")
    # Output page source for debugging
    print("Page source at timeout:")
    print(driver.page_source)  # Inspect the HTML content at timeout to check what was loaded

except NoSuchElementException as e:
    print(f"Element not found: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
