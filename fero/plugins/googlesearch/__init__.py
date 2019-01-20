from bs4 import BeautifulSoup
from urllib.parse import urlencode
from urllib.request import Request, urlopen

import json

_header_get = {
    'Connection': 'close',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'DNT': '1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ms;q=0.6,ru;q=0.5'
}

def _get_search_url(q, page=1):
    '''
    param:
        - q, queries/lewords for searching
        - page, select specific page to fetch
    return:
        - a string for URL query used for search with google
    '''
    url = 'http://www.google.com/search?'
    q = q.replace(' ', '+') # no space here. humph.
    params = { 'q' : q.encode('utf8'), 'start' : page * 10 }
    return url + urlencode(params)

def fetch(keyword):
    url = _get_search_url(keyword)
    req = Request(url, headers = _header_get)
    html = urlopen(req)
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def load(app):
    pass