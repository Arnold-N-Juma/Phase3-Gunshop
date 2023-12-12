# Import necessary SQLAlchemy modules

from sqlalchemy import create_engine
from sqlalchemy import ForeignKey, Table, Column, Integer, String
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.orm import declarative_base

# Create a base class for declarative models
Base = declarative_base()


# Create a SQLAlchemy database engine
engine = create_engine('sqlite:///guns.sqlite')
Session = sessionmaker(bind=engine)
session = Session()

""" # Define a many-to-many relationship table between guns and users
gun_user = Table(
    'guns_users',
    Base.metadata,
    Column('gun_id', ForeignKey('guns.id'), primary_key=True),
    Column('user_id', ForeignKey('users.id'), primary_key=True),
    extend_existing=True,
)
 """

# Define the Gun class with attributes and relationships
class Gun(Base):
    __tablename__ = 'guns'
    
    id = Column(Integer(), primary_key=True)
    gun_name = Column(String())
    gun_price = Column(Integer())
    gun_info = Column(String())
    
    #relationships
    #to reviews
    #NB: the cascade function uses all symbol as a synonym for save-update, merge, refresh-expire, expunge, delete , 
    # and using it in conjunction with delete-orphan indicates that the child object should follow along with its parent in all cases, and be deleted once it is no longer associated with that parent.
    reviews = relationship('Review', back_populates='gun', cascade='all, delete-orphan')
    
    """ #to customers
    users = relationship('User', secondary= gun_user, back_populates='guns') """
    


# Define the User class with attributes and relationships
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    
    #relationships
    #to reviews
    #NB: the cascade function uses all symbol as a synonym for save-update, merge, refresh-expire, expunge, delete , 
    # and using it in conjunction with delete-orphan indicates that the child object should follow along with its parent in all cases, and be deleted once it is no longer associated with that parent.
    reviews = relationship('Review', back_populates='user', cascade='all, delete-orphan')
    
    """  
    #to guns
    guns = relationship('Restaurant', secondary= gun_user, back_populates='users') """
    
    
# Define the Review class with attributes and relationships
class Review(Base):
    __tablename__ = 'reviews'
    
    id = Column(Integer(), primary_key=True)
    review_text = Column(String())
    
    gun_id = Column(Integer(), ForeignKey('guns.id'))
    user_id = Column(Integer(), ForeignKey('users.id'))
    
    #relationships
    gun = relationship ('Gun', back_populates= 'reviews' )
    user = relationship ('User', back_populates= 'reviews')
   