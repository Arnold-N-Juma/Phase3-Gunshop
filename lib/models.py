from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine=create_engine('sqlite:///guns.db',  echo=True)

Base=declarative_base()

class Gun(Base):
    pass

class Buyer(Base):
    pass

class Review(Base):
    pass