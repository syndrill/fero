from urllib.parse import urlencode
from urllib.request import Request, urlopen

import json

GOOGLE_CSE_API_KEY = 'REDACTED' # DO NOT PUSH TO GIT

def _get_search_url(q, page=1):
    '''
    param:
        - q, queries/lewords for searching
        - page, select specific page to fetch
    return:
        - a string for URL query used for search with google
    '''
    url = 'https://www.googleapis.com/customsearch/v1?'
    q = q.replace(' ', '+') # no space here. humph.
    params = { 'q'  : q.encode('utf8'),
               'cx' : '018212539862037696382:-xa61bkyvao',
               'key': GOOGLE_CSE_API_KEY }
    return url + urlencode(params)

def fetch(keyword):
    url = _get_search_url(keyword)
    req = Request(url)
    res = urlopen(req)
    res = json.load(html)

    data = []
    for item in res['items']:
        data.append({'title': item['pagemap']['metatags'][0]['og:title'],
                     'url': item['pagemap']['metatags'][0]['og:url']})

    return data


def load(app):
    pass