from flask import render_template

def page_not_found(err):
    return render_template('errors/404.html', error=err.description), 404

def forbidden(err):
    return render_template('errors/403.html', error=err.description), 403
