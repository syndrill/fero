import os
import sys

from flask import (
    Flask, render_template, abort
)

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'fero.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/404')
    def four_o_four():
        return abort(404)

    @app.route('/403')
    def four_o_three():
        return abort(403)

    # blueprint
    from fero.scrapper import scrapper
    from fero.auth import auth
    
    # error
    from fero.errors import page_not_found, forbidden

    # hacky plugin systems
    from fero.plugins import init_plugins

    app.register_blueprint(scrapper)
    app.register_blueprint(auth)

    app.register_error_handler(404, page_not_found)
    app.register_error_handler(403, forbidden)

    plugins.init_plugins(app)

    app.add_url_rule('/', endpoint='index')

    return app
