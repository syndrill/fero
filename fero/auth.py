from flask import current_app
from flask import (
    abort, Blueprint, request
)

import json

auth = Blueprint('auth', __name__, url_prefix='/api/auth')

# TODO: eta. neva.