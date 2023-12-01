import json
import time

import logging

from flask import request, render_template

import create_app, database
from models import Book


time.sleep(5)
app = create_app.create_app()
logging.basicConfig(level=logging.DEBUG)

@app.route('/', methods=['GET'])
def homepage():
    books = database.get_all(Book)
    return render_template('main.html', all_books=books)

if __name__ == '__main__':
       app.run(host='0.0.0.0', port=30006, debug=True)


