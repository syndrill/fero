from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def _get_search_url(q, page=1):
    '''
    param:
        - q, queries/lewords for searching
        - page, select specific page to fetch
    return:
        - a string for URL query used for search with google
    '''
    q = q.replace(' ', '-')
    url = 'https://www.antaranews.com/search/{}/{}'.format(q, page)
    return url

def fetch(keyword):
    data = []
    page = 1

    has_next = True
    while has_next:

        url = _get_search_url(keyword, page)
        req = Request(url)
        html = urlopen(req)
        soup = BeautifulSoup(html, 'html.parser')

        for article in soup.findAll('article', {'class': 'simple-post'}):
            data.append({
                'title': article.header.h3.a['title'],
                'url': article.header.h3.a['href']
            })

        page += 1
        has_next = soup.findAll('a', {'aria-label': 'Next'}) != None

    return data

def load(app):
    pass