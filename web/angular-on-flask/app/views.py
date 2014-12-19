from flask import redirect, url_for
from app import app


@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('static', filename='index.html'))


@app.route('/app/bower_components/bootstrap/dist/css/bootstrap.css', methods=['GET'])
def bootstrap():
    return redirect("https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css")


@app.route('/app/bower_components/angular/angular.js', methods=['GET'])
def angular():
    return redirect("https://ajax.googleapis.com/ajax/libs/angularjs/1.2.28/angular.min.js")
