#!flask/bin/python
# http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

from app import app

app.run(host='0.0.0.0', debug=True)
