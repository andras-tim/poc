from flask import render_template, request, g, make_response
from app import app, babel
from config import LANGUAGES


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(LANGUAGES.keys())


@app.before_request
def before_request():
    g.locale = get_locale()


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/index.js', methods=['GET'])
def index_js():
    js = render_template('index.js')
    response = make_response(js)
    response.mimetype = 'application/javascript'
    return response
