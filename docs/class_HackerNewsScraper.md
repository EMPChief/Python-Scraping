# Hacker News Scraper Documentation

## Overview

This Python program is a web scraper designed to fetch and analyze data from Hacker News. It utilizes various libraries such as cloudscraper, BeautifulSoup, and pandas to extract information about top stories based on points.

## Requirements

- Python 3.x
- Required Python libraries:
  - cloudscraper
  - BeautifulSoup
  - pandas

## Usage

To use the Hacker News Scraper, follow these steps:

Initialize HackerNewsScraper:

- Create an instance of HackerNewsScraper.
  - This initializes the base URL for Hacker News and a cloudscraper session.

Sort Stories by Points:

- `sort_stories_by_points(hn_list)`: Method to sort a list of Hacker News stories by their points in descending order.

Scrape Hacker News Page:

- `scrape_hn_page(url)`: Method to scrape a single page of Hacker News.
  - Returns a list of dictionaries containing story titles, URLs, and points.
  - Utilizes BeautifulSoup to parse the HTML content.

Customize News List:

- `create_custom_news_list(pages=1)`: Method to create a custom news list from multiple pages.
  - Automatically navigates through pagination to gather data from multiple pages.
  - Provides an option to specify the number of pages to scrape.

Create DataFrame:

- `create_custom_news_df(pages=1)`: Method to create a pandas DataFrame from the custom news list.
  - Returns a DataFrame with columns for title, URL, and points.

Save Data to CSV:

- After creating the DataFrame, it is saved to a CSV file using `to_csv`.
- Specify the file path where the data will be saved.

## Example

```python
if __name__ == "__main__":
    hacker_news = HackerNewsScraper()
    hn_data = hacker_news.create_custom_news_df(20)
    hn_data.to_csv('data/hn_scraper_data.csv', index=False)
    print(hn_data)
```

In this example:

- An instance of HackerNewsScraper is created.
- The program scrapes 20 pages of Hacker News.
- The resulting DataFrame is saved to data/hn_scraper_data.csv.

## Important Notes

User-Agent and Headers:

- The scraper includes custom headers to mimic a web browser.
- These headers can be modified in the `headers` method.

Error Handling:

- The program includes basic error handling for parsing and network errors.
- It prints error messages for better debugging.
