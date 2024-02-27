# Hacker News Scraper Script

The hacker_news_scraper_script.py script is designed to scrape Hacker News data, clean and store it in a SQLite database, and insert new data if it does not already exist.

## Usage

```bash
python hacker_news_scraper_script.py
```

## Overview

This script performs the following actions:

- Initialize HackerNewsScraper:

  - Creates an instance of HackerNewsScraper to scrape Hacker News data.

- Scrape Hacker News:

  - Scrapes Hacker News data from multiple pages (default 40 pages).
  - Creates a Pandas DataFrame containing the scraped data.

- Initialize Database:

  - Creates or connects to a SQLite database named database.db.
  - Creates a table named hackernews with columns: id, title, href, points.

- Clean and Insert New Data:

  - Compares the new Hacker News data with existing data in the database.
  - Cleans titles and checks for duplicates.
  - Inserts new data into the hackernews table if it is not already present.

- Batch Insertion:

  - Inserts data in batches of 5 rows at a time.

- Print DataFrame:

  - Displays the Pandas DataFrame containing the scraped Hacker News data with timestamps.


## Constants

- `TABLE_NAME`: Name of the table in the database (default: hackernews)
- `DATABASE_NAME`: Name of the SQLite database (default: database.db)
- `PAGE_NUMBER`: Number of pages to scrape (default: 40)

## Functions

```python
def clean_title(title):
  """Cleans the title by stripping whitespace and converting to lowercase."""
  return cleaned_title
```

```python
def insert_batch_data(db, data, columns):
  """Inserts data in batches into the database. Batch size is set to 5 rows."""
```

## Requirements

- Python 3.x
- pandas library
- time module
- HackerNewsScraper class from Scrapers.py
- My_Database class from dbs.py

## Important Notes

- Ensure the required Python dependencies are installed.
- The Scrapers.py file contains the HackerNewsScraper class for scraping Hacker News data.
- The dbs.py file contains the My_Database class for database operations.
- The script continuously runs in an infinite loop, scraping Hacker News data.
- It uses a SQLite database named database.db to store the Hacker News data.
- The HackerNewsScraper class scrapes Hacker News data, and My_Database manages the database.
