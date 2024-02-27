# TourScraper Class

The `TourScraper` class is designed to scrape upcoming tour data from a specific website, store the data, and send an email notification if new tour information is found. It also creates a Pandas DataFrame from the scraped data.

## Initialization

To use the `TourScraper` class, you need to initialize it with a data file path where the scraped data will be stored.

Example Initialization:

```python
# Initialize with default data file path 'data/tours.txt'
scraper = TourScraper()

# Alternatively, specify a custom data file path
# scraper = TourScraper(data_file='custom/path/tours.txt')
```

## Methods

`get_tours_page(url)`

- Retrieves the HTML content of the tours page from the specified URL.
  - url (str): The URL of the tours page.
  - Returns: Response object from the request.

`get_soup()`

- Parses the HTML content of the tours page into a BeautifulSoup object.
  - Returns: BeautifulSoup object of the tours page.

`extract_data()`

- Extracts tour data from the BeautifulSoup object using a SelectorLib YAML file.
  - Returns: List of tour data.

`store_data()`

- Stores the extracted tour data into a file (default data/tours.txt).
  - Returns: The newly added tour data if it's new, otherwise None.

`check_and_send_email()`

- Checks for new tour data, sends an email notification using the EmailSender class if new data is found.

`create_dataframe()`

- Creates a Pandas DataFrame from the extracted tour data.
  - Returns: Pandas DataFrame with columns ['ScrapeDate', 'Band', 'City', 'Date'].

## Example Usage:

```python
scraper.check_and_send_email()
dataframe = scraper.create_dataframe()
dataframe.to_csv('data/tours.csv', index=False)
```

## Important Notes

- This class relies on the cloudscraper, pandas, beautifulsoup4, selectorlib, and a custom EmailSender class.
- The EmailSender class is expected to be in a module named class_EmailSender.py in the same directory.
- Ensure the existence of the some_yaml/tours.yaml file for data extraction.
- Before running, make sure to set up the necessary environment variables for the EmailSender class.
