# Tour Scraper Script

The tour_scraper_script.py script is designed to continuously scrape upcoming tour data, store it in a SQLite database, and send an email notification if new tour information is found.

## Usage

```bash
python main_tutorial.py
```

## Overview

This script performs the following actions:

- Initialize TourScraper:

  - Creates an instance of TourScraper to scrape tour data from a specific website.

- Check and Send Email:

  - Checks for new tour data.
  - If new data is found, sends an email notification using the EmailSender class.
    - Email includes details of the upcoming tour.

- Create DataFrame:

  - Creates a Pandas DataFrame from the scraped tour data.

- Initialize Database:

  - Creates or connects to a SQLite database named database.db.
  - Creates a table named tourevent with columns: id, ScrapeDate, band, city, date.

- Insert New Data:

  - Compares the new tour data with existing data in the database.
  - Inserts new data into the tourevent table if it is not already present.

- Sleep and Repeat:

  - Sleeps for 5 seconds to wait for the next scrape.
  - Continues this process in an infinite loop.

## Requirements

- Python 3.x
- pandas library
- time module
- TourScraper class from Scrapers.py
- My_Database class from dbs.py
- EmailSender class from class_EmailSender.py
- Existing some_yaml/tours.yaml for data extraction

## Important Notes

- Ensure the required Python dependencies are installed.
- The Scrapers.py file contains the TourScraper class for scraping tour data.
- The dbs.py file contains the My_Database class for database operations.
- The class_EmailSender.py file contains the EmailSender class for sending email notifications.
- The script continuously runs in an infinite loop, checking for new tour data.
- It uses a SQLite database named database.db to store the tour data.
- The TourScraper class scrapes tour data, My_Database manages the database, and EmailSender sends email notifications.
