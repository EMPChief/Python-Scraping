import requests as rq
from bs4 import BeautifulSoup as bs
import pprint as pp
import time


def sort_hackernews_list(hm_list):
    return sorted(hm_list, key=lambda k: k['points'], reverse=True)


def scrape_hn_page(url):
    res = rq.get(url)
    soup = bs(res.text, 'html.parser')
    links = soup.select('.titleline')
    votes = soup.select('.score')

    hn_list = []
    for idx, link in enumerate(links):
        title = link.get_text()
        href = link.get('href', None)
        points_text = votes[idx].get_text() if idx < len(votes) else '0 points'
        points = int(points_text.replace(' points', ''))

        if points > 100:
            hn_list.append({'title': title, 'href': href, 'points': points})

    return hn_list


def create_custom_news_df(pages=1):
    base_url = 'https://news.ycombinator.com/'
    hn_full_list = []
    url = base_url

    for _ in range(pages):
        hn_list = scrape_hn_page(url)
        hn_full_list.extend(hn_list)

        res = rq.get(url)
        soup = bs(res.text, 'html.parser')
        more_link = soup.select('.morelink')
        if more_link:
            more_href = more_link[0].get('href')
            if not more_href.startswith('http'):
                more_href = base_url + more_href
            url = more_href
        else:
            break

        if _ < pages - 1:
            time.sleep(30)

    return sort_hackernews_list(hn_full_list)


pp.pprint(create_custom_news_df(5))
