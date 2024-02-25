from Scrapers import HackerNewsScraper, TourScraper

if __name__ == '__main__':
    scraper = TourScraper()
    scraper.check_and_send_email()
    dataframe = scraper.create_dataframe()
    dataframe.to_csv('data/tours.csv', index=False)
    print("DataFrame with time and index:")
    print(dataframe)
