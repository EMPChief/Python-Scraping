from Scrapers import TourScraper
from dbs import My_Database
import pandas as pd
import time

if __name__ == '__main__':
    columns = ['id INTEGER PRIMARY KEY', 'ScrapeDate',
               'band TEXT', 'city TEXT', 'date TEXT']

    while True:
        try:
            scraper = TourScraper()
            scraper.check_and_send_email()
            dataframe = scraper.create_dataframe()

            db = My_Database(db_name='database.db', tb='tourevent')
            db.create_table(columns)

            existing_data = db.select_all_data()

            if not existing_data or len(existing_data) == 0:
                existing_band_city_date = set()
            else:
                existing_band_city_date = set(
                    map(lambda x: (x[1], x[2], x[3]), existing_data))

            new_data = dataframe[~dataframe.apply(lambda x: (
                x['Band'], x['City'], x['Date']), axis=1).isin(existing_band_city_date)]

            if not new_data.empty:
                new_data = new_data[['ScrapeDate', 'Band', 'City', 'Date']]
                db.insert_many_rows(new_data.values.tolist(), columns[1:])
                print("New data inserted into database.")
            else:
                print("No new data to insert.")
            time.sleep(5)

            print("DataFrame with time and index:")
            print(dataframe)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            db.close_connection()

