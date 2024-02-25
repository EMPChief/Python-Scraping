import pandas as pd
from bs4 import BeautifulSoup
import cloudscraper
import selectorlib
from .class_EmailSender import EmailSender
from datetime import datetime

class TourScraper:
    def __init__(self, data_file='data/tours.txt'):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
            "Referer": "https://www.google.com/",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Pragma": "no-cache",
        }
        self.base_url = 'http://programmer100.pythonanywhere.com/tours/'
        self.scraper = cloudscraper.create_scraper()
        self.data_file = data_file

    def get_tours_page(self, url):
        response = self.scraper.get(url, headers=self.headers)
        return response

    def get_soup(self):
        tours_page = self.get_tours_page(self.base_url)
        soup = BeautifulSoup(tours_page.text, 'html.parser')
        return soup

    def extract_data(self):
        soup_obj = self.get_soup()
        extractor = selectorlib.Extractor.from_yaml_file('some_yaml/tours.yaml')
        tour_data = extractor.extract(str(soup_obj))['tours']
        return tour_data
    
    def store_data(self):
        scraped_data = self.extract_data()

        if scraped_data != 'No upcoming tours' and scraped_data:
            with open(self.data_file, 'r') as file:
                existing_data = [line.strip() for line in file.readlines()]

            if scraped_data not in existing_data:
                with open(self.data_file, 'a') as file:
                    file.write(scraped_data + '\n')
                return scraped_data
            else:
                return None
        return None

    def check_and_send_email(self):
        scraped_data = self.store_data()
        
        if scraped_data is not None:
            print('New Upcoming Tour Found')
            print('Sending Email')
            EmailSender().send_email(subject="Upcoming Tour", body=f"Upcoming tour by a random band\n{scraped_data}", recipient_email="support@empchief.com")
            print('Email Sent')
        else:
            print('No Upcoming Tours found')
    
    def create_dataframe(self):
        scraped_data = self.extract_data()
        if scraped_data != 'No upcoming tours' and scraped_data:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            band, city, date = scraped_data.split(', ')
            dataframe = pd.DataFrame({
                'ScrapeDate': [current_time],
                'Band': [band],
                'City': [city],
                'Date': [date]
            })
            return dataframe
        else:
            return pd.DataFrame()

if __name__ == '__main__':
    scraper = TourScraper()
    scraper.check_and_send_email()
    dataframe = scraper.create_dataframe()
    dataframe.to_csv('data/tours.csv', index=False)
    print("DataFrame with time and index:")
    print(dataframe)
