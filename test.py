from bs4 import BeautifulSoup
import cloudscraper
import selectorlib
import pandas as pd
from EmailSender import EmailSender

class TourScraper():
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
            "Referer": "https://www.google.com/",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Pragma": "no-cache",
        }
        self.base_url = 'http://programmer100.pythonanywhere.com/tours/'
        self.scraper = cloudscraper.create_scraper()
        self.data_file = 'data/tours.txt'

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
        scraped = self.extract_data()

        if scraped != 'No upcoming tours' and scraped:
            with open(self.data_file, 'r') as f:
                existing_data = [line.strip() for line in f.readlines()]

            if scraped not in existing_data:
                with open(self.data_file, 'a') as f:
                    f.write(scraped + '\n')
                return scraped
            else:
                return None
        return None




    def check_and_send_email(self):
        scraped = self.store_data()
        
        if scraped is not None:
            print('New Upcoming Tour Found')
            print('Sending Email')
            EmailSender().send_email(subject="Upcoming Tour", body=f"Upcoming tour by a random band\n{scraped}", recipient_email="support@empchief.com")
            print('Email Sent')
        else:
            print('No Upcoming Tours found')



if __name__ == '__main__':
    tour_scraper = TourScraper()
    tour_scraper.check_and_send_email()
