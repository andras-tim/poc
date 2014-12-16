#!flask/bin/python
import os

pybabel = 'flask/bin/pybabel'
os.system(pybabel + ' compile -d app/translations')
