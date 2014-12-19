from flask import redirect, url_for
from app import app


@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('static', filename='index.html'))
