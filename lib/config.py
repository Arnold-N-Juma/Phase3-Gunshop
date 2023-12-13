# config.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database configuration
DATABASE_URI = 'sqlite:///guns.sqlite'

# Create a database engine
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()