from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

class TemperatureScraper:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument("disable-infobars")
        self.chrome_options.add_argument("start-maximized")
        self.chrome_options.add_argument("disable-dev-shm-usage")
        self.chrome_options.add_argument("no-sandbox")
        self.chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.chrome_options.add_argument("disable-blink-features=AutomationControlled")
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def get_temperature(self):
        self.driver.get("http://automated.pythonanywhere.com")
        time.sleep(2)
        try:
            element = self.driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
            temperature = self.clean_text(element.text)
            return temperature
        except NoSuchElementException as e:
            print("Temperature element not found.")
            return None

    @staticmethod
    def clean_text(text):
        try:
            temperature = float(text.split(": ")[1])
            return temperature
        except (IndexError, ValueError) as e:
            print("Error extracting temperature:", e)
            return None

    def close_driver(self):
        self.driver.quit()


def main():
    scraper = TemperatureScraper()
    temperature = scraper.get_temperature()
    if temperature is not None:
        print("Temperature:", temperature)
    scraper.close_driver()

if __name__ == "__main__":
    main()
