from bs4 import BeautifulSoup
from urllib.parse import urlencode
from urllib.request import Request, urlopen

def _get_search_url(q, page=1):
    '''
    param:
        - q, queries/lewords for searching
        - page, select specific page to fetch
    return:
        - a string for URL query used for search with google
    '''
    url = 'https://www.detik.com/search/searchall?'
    q = q.replace(' ', '+') # no space here. humph.
    params = { 'query' : q.encode('utf8'), 'page' : page}
    return url + urlencode(params)

def fetch(keyword):
    data = []
    page = 1

    has_next = True
    while has_next:

        url = _get_search_url(keyword, page)
        req = Request(url)
        html = urlopen(req)
        soup = BeautifulSoup(html)

        for article in soup.findAll('article'):
            data.append({'title': article.a['href'], 'url': article.a.h2.text})

        pae += 1
        has_next = soup.findAll('a', {'class' : 'last'})

    return data

def load(app):
    pass