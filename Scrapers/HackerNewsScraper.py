import cloudscraper
from bs4 import BeautifulSoup
import pandas as pd
import time


class HackerNewsScraper:
    def __init__(self):
        self.base_url = 'https://news.ycombinator.com/'
        self.scraper = cloudscraper.create_scraper()

    def sort_stories_by_points(self, hn_list):
        return sorted(hn_list, key=lambda k: k['points'], reverse=True)

    def scrape_hn_page(self, url):
        res = self.scraper.get(url)
        if not res.ok:
            return []  # Return an empty list if the request fails

        soup = BeautifulSoup(res.text, 'html.parser')

        # Find elements with the 'titleline' class
        links = soup.select('.titleline')
        votes = soup.select('.score')

        hn_list = []
        for idx, link in enumerate(links):
            try:
                title = link.get_text()
                href = link.find('a').get('href', None)

                points_text = votes[idx].get_text(
                ) if idx < len(votes) else '0 points'
                points = int(points_text.replace(' points', ''))

                if points > 100:
                    hn_list.append(
                        {'title': title, 'href': href, 'points': points})

            except IndexError:
                print(f"Error parsing item at index {idx}")
            except ValueError:
                print(f"Error parsing points for item at index {idx}")

        return hn_list

    def create_custom_news_df(self, pages=1):
        hn_full_list = []
        url = self.base_url

        for page_num in range(pages):
            print(f"\nScraping page {page_num + 1}...")
            hn_list = self.scrape_hn_page(url)
            hn_full_list.extend(hn_list)

            res = self.scraper.get(url)
            if not res.ok:
                break

            soup = BeautifulSoup(res.text, 'html.parser')
            more_link = soup.select('.morelink')
            if more_link:
                more_href = more_link[0].get('href')
                if not more_href.startswith('http'):
                    more_href = self.base_url + more_href
                url = more_href
            else:
                print("No more pages found.")
                break

            if page_num < pages - 1:
                print("Waiting for 30 seconds before next request...")
                time.sleep(30)

        return hn_full_list

    def create_custom_news_df_as_dataframe(self, pages=1):
        hn_list = self.create_custom_news_df(pages)
        df = pd.DataFrame(hn_list)
        return df


if __name__ == "__main__":
    hacker_news = HackerNewsScraper()
    hn_data = hacker_news.create_custom_news_df_as_dataframe(7)
    hn_data.to_csv('hn_data.csv', index=False)
    print(hn_data)
