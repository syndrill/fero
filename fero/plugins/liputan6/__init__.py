from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

_header_get = {
    'Connection': 'close',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'DNT': '1',
    'Cookie': 'js_enabled=false;'
}

def _get_search_url(q, page=1):
    '''
    param:
        - q, queries/lewords for searching
        - page, select specific page to fetch
    return:
        - a string for URL query used for search with google
    '''
    q = q.replace(' ', '+')
    url = 'https://www.liputan6.com/search?q='
    return url + q

def fetch(keyword):
    data = []
    page = 1
    has_next = True
    while has_next:
        url = _get_search_url(keyword, page)
        req = Request(url, headers=_header_get)
        html = urlopen(req)
        soup = BeautifulSoup(html)
        for article in soup.findAll('a', {'class': 'articles--iridescent-list--text-item__title-link'}):
            data.append({
                'title': article['title'],
                'url': article['href']
            })
        # page += 1
        has_next = False
    return data

def load(app):
    pass