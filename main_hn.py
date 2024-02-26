from Scrapers import HackerNewsScraper
from dbs import My_Database
import pandas as pd
import time

if __name__ == '__main__':
    columns = ['id INTEGER PRIMARY KEY', 'title TEXT', 'href TEXT', 'points INTEGER']

    try:
        hacker_news = HackerNewsScraper()
        hn_data = hacker_news.create_custom_news_df(10)

        db = My_Database(db_name='database.db', tb='hackernews')
        db.create_table(columns)

        existing_data = db.select_all_data()

        if not existing_data or len(existing_data) == 0:
            existing_band_city_date = set()
        else:
            existing_band_city_date = set(
                map(lambda x: (x[1], x[2], x[3]), existing_data))

        new_data = hn_data[~hn_data.apply(lambda x: (
            x['title'], x['href'], x['points']), axis=1).isin(existing_band_city_date)]

        if not new_data.empty:
            new_data = new_data[['title', 'href', 'points']]
            db.insert_many_rows(new_data.values.tolist(), columns[1:])
            print("New data inserted into database.")
        else:
            print("No new data to insert.")

        print("DataFrame with time and index:")
        print(hn_data)
    except Exception as e:
        print(e)
    finally:
        db.close_connection()
