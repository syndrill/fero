from flask import current_app
from fero import plugins
from flask import (
    abort, Blueprint, request
)

import json

scrapper = Blueprint('scrapper', __name__, url_prefix='/api/scrapper')

'''
/api/scrapper/<>/
'''

@scrapper.route('/<plugin_name>/fetch', methods=('GET', 'POST'))
def fetch(plugin_name=None):
    if request.method == 'POST':
        module = getattr(plugins, plugin_name, None)
        if not module:
            return abort(404)
        return json.dumps(module.fetch(request.form['keywords'])), 200, { 'Content-type' : 'application/json' }
    return abort(403)
