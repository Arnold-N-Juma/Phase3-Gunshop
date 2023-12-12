from sqlalchemy import create_engine
from sqlalchemy import Column, Text, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func

engine=create_engine('sqlite:///guns.db',  echo=True)

Base=declarative_base()

class Review(Base):
    __tablename__="reviews"
    id=Column(Integer(),primary_key=True)
    review_text=Column(String())
    user_id = Column(Integer, ForeignKey("users.id"))
    gun_id = Column(Integer(), ForeignKey("guns.id"))
    
    
    
    users = relationship('User', back_populates='reviews')
    guns = relationship('Gun', back_populates='reviews')
    

class User(Base):
    __tablename__="users"
    id=Column(Integer(),primary_key=True)
    first_name=Column(String())
    last_name=Column(String())
    
    reviews = relationship("Review", back_populates='users')

class Gun(Base):
    __tablename__="guns"
    id=Column(Integer(),primary_key=True)
    gun_name=Column(String())
    gun_price=Column(String())
    gun_info=Column(String())
   
    reviews=relationship("Review", back_populates="guns")