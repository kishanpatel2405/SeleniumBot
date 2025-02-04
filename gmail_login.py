from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

username = "kishan.vaghasiya122822@marwadiuniversity.ac.in"
password = "Ynnb@898"

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
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='button button__label']"))).click()
    print("Clicked 'Sign in' button.")

    print("Waiting for username field to be present...")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "identifierId")))
    driver.find_element(By.ID, "identifierId").send_keys(username)
    print("Entered username.")

    # Click the "Next" button after entering the username
    print("Clicking 'Next' button after entering username...")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "identifierNext"))).click()

    # Wait for the password field to be present and enter the password
    print("Waiting for password field to be present...")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
    driver.find_element(By.NAME, "password").send_keys(password)
    print("Entered password.")

    # Click the "Next" button after entering the password
    print("Clicking 'Next' button after entering password...")
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "passwordNext"))).click()

    print("Logged in successfully.")

except TimeoutException as e:
    print(f"Timeout occurred: {e}")
except NoSuchElementException as e:
    print(f"Element not found: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
