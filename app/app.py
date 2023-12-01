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
    all_books = ""
    for book in books:
        all_books += book.author + '\n' + book.name + "\n" + str(book.time) + "<br>"
    return all_books, 200

if __name__ == '__main__':
       app.run(host='0.0.0.0', port=30006, debug=True)


