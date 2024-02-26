from Scrapers import HackerNewsScraper
from dbs import My_Database
import pandas as pd
import time


TABLE_NAME = 'hackernews'
DATABASE_NAME = 'database.db'
PAGE_NUMBER = 40


def clean_title(title):
    return title.strip().lower()


def insert_batch_data(db, data, columns):
    batch_size = 5
    for i in range(0, len(data), batch_size):
        batch = data.iloc[i:i+batch_size]
        db.insert_many_rows(batch.values.tolist(), columns[1:])
        print(f"Batch {i // batch_size + 1} inserted into database.")


if __name__ == '__main__':
    columns = ['id INTEGER PRIMARY KEY',
               'title TEXT', 'href TEXT', 'points INTEGER']

    try:
        hacker_news = HackerNewsScraper()
        hn_data = hacker_news.create_custom_news_df(PAGE_NUMBER)

        db = My_Database(db_name=DATABASE_NAME, tb=TABLE_NAME)
        db.create_table(columns)

        existing_data = db.select_all_data()

        if not existing_data or len(existing_data) == 0:
            existing_titles = set()
        else:
            existing_titles = set(
                map(lambda x: clean_title(x[1]), existing_data))

        new_data = hn_data[~hn_data['title'].apply(
            clean_title).isin(existing_titles)]

        if not new_data.empty:
            insert_batch_data(db, new_data, columns)
            print("New data inserted into database.")
        else:
            print("No new data to insert.")

        print("DataFrame with time and index:")
        print(hn_data)
    except Exception as e:
        print(e)
    finally:
        db.close_connection()
