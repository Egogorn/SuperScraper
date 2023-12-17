import database_uri
import datetime
import time
import logging
from bs4 import BeautifulSoup
import requests
from models import Book
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

time.sleep(20)
engine = create_engine(database_uri.DATABASE_CONNECTION_URI)
engine.connect()
session = Session(engine)
logging.basicConfig(level=logging.INFO)
while(True):
    now = datetime.datetime.today().date()
    logging.info("Parsing website at " + str(now))
    request = requests.get("https://www.biblio-globus.ru/")
    if (request.status_code != 200):
        #retry if request was unsuccessful
        logging.error("Server/parser error")
        continue
    html = request.text
    soup = BeautifulSoup(html, 'lxml')
    newitems = soup.find("div", {"class": "container bright_container bright_container_mobile"})
    products = newitems.find_all("div", {"class": "product"})
    for product in products:
        author = product.find("div", {"class": "author"}).text
        name = product.find("h3").find("a").text
        if (name[-3:] == "..."):
            #go to product page in case it's name is not displayed in full
            newurl = "https://www.biblio-globus.ru" + product.find("a", href=True)['href']
            product_html = requests.get(newurl).text
            product_soup = BeautifulSoup(product_html, 'lxml')
            name = product_soup.find("meta", property="og:title")["content"]
        book = Book(author=author, name=name, time=now)
        result = session.query(Book).filter(Book.name == name).first()
        if (result == None):
            session.add(book)
            session.commit()
    time.sleep(600)
