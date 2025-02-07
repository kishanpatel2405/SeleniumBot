import json
from pathlib import Path

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


class SeleniumDriver(object):
    def __init__(
            self,
            driver_path='chromedriver.exe',  # chromedriver path
            cookies_file_path='cookies/cookies.txt',
            website="https://facebook.com"
    ):
        self.driver_path = Path(driver_path).as_posix()
        self.cookies_file_path = Path(cookies_file_path).as_posix()
        self.website = website

        # Chrome options setup
        options = Options()
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        options.add_argument(f'user-agent={user_agent}')
        options.add_argument("--disable-notifications")

        # Use the Service class to specify the driver
        service = Service(self.driver_path)

        # Initialize the webdriver with the service object
        self.driver = webdriver.Chrome(service=service, options=options)

        try:
            # Load cookies for given websites
            with open(self.cookies_file_path) as cookie_file:
                cookies = json.load(cookie_file)
            self.driver.get(self.website)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
        except Exception as e:
            print(str(e))
            print("Error loading cookies")

    def save_cookies(self):
        cookies = self.driver.get_cookies()
        with open(self.cookies_file_path, 'w') as outfile:
            json.dump(cookies, outfile, indent=4)

    def close_all(self):
        if len(self.driver.window_handles) < 1:
            return
        for window_handle in self.driver.window_handles[:]:
            self.driver.switch_to.window(window_handle)
            self.driver.close()

    def quit(self):
        self.save_cookies()
        self.close_all()
        self.driver.quit()











