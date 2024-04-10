import logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class PyAnyhowScrape:
    def __init__(self, service, executable_path):
        self.service = service
        self.executable_path = executable_path
        self.driver = None
        self.logger = logging.getLogger(__name__)

    def get_driver(self):
        try:
            options = webdriver.ChromeOptions()
            options.add_argument("disable-infobars")
            options.add_argument("start-maximized")
            options.add_argument("headless")
            options.add_argument("no-sandbox")
            options.add_argument("disable-dev-shm-usage")
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_argument("disable-blink-features=AutomationControlled")
            self.driver = webdriver.Chrome(service=self.service,
                                           options=options)
            self.driver.get("http://automated.pythonanywhere.com")
            return self.driver
        except Exception as e:
            self.logger.error(f"Error creating WebDriver: {e}")
            raise

    def find_element(self, by, value):
        try:
            return self.driver.find_element(by=by, value=value)
        except NoSuchElementException as e:
            self.logger.error(f"Element not found: {e}")
            return None
        except Exception as e:
            self.logger.error(f"An error occurred: {e}")
            return None

    def quit(self):
        if self.driver:
            self.driver.quit()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.quit()


if __name__ == "__main__":
    service = webdriver.chrome.service.Service(executable_path="path to chromedriver")
    with PyAnyhowScrape(service, "path to chromedriver") as driver_wrapper:
        result = driver_wrapper.find_element(by="xpath",
                                             value="/html/body/div[1]/div/h1[1]")
        if result:
            print("Text found:", result.text)
        else:
            print("Text not found or an error occurred. Check logs for details.")

