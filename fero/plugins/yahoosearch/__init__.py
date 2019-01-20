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
    url = 'https://id.search.yahoo.com/search?'
    q = q.replace(' ', '+') # no space here. humph.
    params = { 'p' : q.encode('utf8'), 'b' : (page - 1) * 10 + 1 }
    return url + urlencode(params)

def fetch(keyword):
    url = _get_search_url(keyword)
    req = Request(url)
    html = urlopen(req)
    soup = BeautifulSoup(html, 'html.parser')

    # TODO        

    return soup

def load(app):
    pass