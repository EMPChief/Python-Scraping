import requests as rq
from bs4 import BeautifulSoup as bs
import pprint as pp
import time
# https://scrapy.org/


def sort_hackernews_list(hm_list):
    return sorted(hm_list, key=lambda k: k['points'], reverse=True)


def request_with_retry(url, max_retries=3, delay=5):
    for attempt in range(max_retries):
        try:
            response = rq.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            response.raise_for_status()
            return response
        except rq.exceptions.HTTPError as e:
            print(f"HTTP error on attempt {attempt+1}: {e}")
        except rq.exceptions.RequestException as e:
            print(f"Request error on attempt {attempt+1}: {e}")
        time.sleep(delay)
    return None


def scrape_hn_page(url):
    res = request_with_retry(url)
    if not res:
        return []

    soup = bs(res.text, 'html.parser')
    links = soup.select('.titleline')
    votes = soup.select('.score')

    hn_list = []
    for idx, link in enumerate(links):
        try:
            title = link.get_text()
            href = link.get('href', None)
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


def create_custom_news_df(pages=1):
    base_url = 'https://news.ycombinator.com/'
    hn_full_list = []
    url = base_url

    for page_num in range(pages):
        print(f"\nScraping page {page_num + 1}...")
        hn_list = scrape_hn_page(url)
        hn_full_list.extend(hn_list)

        res = request_with_retry(url)
        if not res:
            break

        soup = bs(res.text, 'html.parser')
        more_link = soup.select('.morelink')
        if more_link:
            more_href = more_link[0].get('href')
            if not more_href.startswith('http'):
                more_href = base_url + more_href
            url = more_href
        else:
            print("No more pages found.")
            break

        if page_num < pages - 1:
            print("Waiting for 30 seconds before next request...")
            time.sleep(30)

    return hn_full_list


hn_data = create_custom_news_df(2)
pprinter = pp.PrettyPrinter(indent=4)
pprinter.pprint(hn_data)
