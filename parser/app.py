import database_uri
import datetime
import time
from bs4 import BeautifulSoup
import requests
from models import Book
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


time.sleep(10)
engine = create_engine(database_uri.DATABASE_CONNECTION_URI)
engine.connect()
session = Session(engine)
while(True):
    now = datetime.datetime.today().date()
    print("Parsing website at " + str(now))
    html = requests.get("https://www.biblio-globus.ru/").text
    soup = BeautifulSoup(html, 'lxml')
    newitems = soup.find("div", {"class": "container bright_container bright_container_mobile"})
    products = newitems.find_all("div", {"class": "product"})
    for p in products:
        author = p.find("div", {"class": "author"}).text
        name = p.find("h3").find("a").text
        if (name[-3:] == "..."):
            newurl = "https://www.biblio-globus.ru" + p.find("a", href=True)['href']
            product_html = requests.get(newurl).text
            product_soup = BeautifulSoup(product_html, 'lxml')
            name = product_soup.find("meta", property="og:title")["content"]
        book = Book(author=author, name=name, time=now)
        result = session.query(Book).filter(Book.name == name).first()
        if (result == None):
            session.add(book)
            session.commit()
    time.sleep(10)
