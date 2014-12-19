#!flask/bin/python
# http://blog.miguelgrinberg.com/post/writing-a-javascript-rest-client

from app import app

app.run(host='0.0.0.0', port=8000, debug=True)
