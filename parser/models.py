from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.orm import declarative_base
import datetime

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer(), primary_key=True)
    author = Column(String(100))
    name = Column(String(100))
    time = Column(DateTime())