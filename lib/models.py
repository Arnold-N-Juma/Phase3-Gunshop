from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine=create_engine('sqlite:///guns.db',  echo=True)

Base=declarative_base()

class Review(Base):
    __tablename__="reviews"
    id=column(Integer(),primary_key=True)
    review=column(string())
    user_id = Column(Integer, ForeignKey("users.id"))
    gun_id = Column(Integer(), ForeignKey("guns.id"))
    
    
    
    users = relationship('User', back_populates='reviews')
    guns = relationship('Gun', back_populates='reviews')
    

class User(Base):
    __tablename__="users"
    id=column(Integer(),primary_key=True)
    first_name=column(String())
    last_name=column(String())
    
    reviews = relationship("Review", back_populates='users')

class Gun(Base):
    __tablename__="guns"
    id=column(Integer(),primary_key=True)
    gun_name=column(String())
    gun_price=column(String())
    gun_info=column(String())
   
    reviews=relationship("Review", back_populates="guns")