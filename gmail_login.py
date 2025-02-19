from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
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

    print("Waiting for 'Sign in' button to be clickable...")
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@aria-label='Sign into Gmail']"))).click()
    print("Clicked 'Sign in' button.")

    print("Waiting for page to load...")
    WebDriverWait(driver, 20).until(EC.url_contains("https://accounts.google.com"))

    print("Waiting for email input field...")
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "identifierId")))

    driver.find_element(By.ID, "identifierId").send_keys(username)
    print("Entered username.")

    print("Clicking 'Next' button after entering username...")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "identifierNext"))).click()

    print("Waiting for password field to be present...")
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "password")))

    driver.find_element(By.NAME, "password").send_keys(password)
    print("Entered password.")

    print("Clicking 'Next' button after entering password...")
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "passwordNext"))).click()

    print("Logged in successfully.")

except TimeoutException as e:
    print(f"Timeout occurred: {e}")
    print("Page source at timeout:")
    print(driver.page_source)

except NoSuchElementException as e:
    print(f"Element not found: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")















