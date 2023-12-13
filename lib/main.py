from config import *
from models import *

#Create a new user with a first name,  and last name
def add_user(first_name,last_name):
    new_user = User(
        first_name=first_name,
        last_name = last_name
    )
    #save it to the database
    session.add(new_user)
    session.commit()
# Read function to read details from the database 
def get_all_users():
    return session.query(User).all()

def get_user_by_id(user_id):
    return session.query(User).filter(User.id == user_id).first()

def get_all_guns():
    return session.query(Gun).all()

def get_gun_by_id(gun_id):
    return session.query(Gun).filter(Gun.id == gun_id).first()

    
# Delete a user and Gun 
def delete_user(user_id):
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        session.delete(user)
        session.commit()

def delete_gun(gun_id):
    gun = session.query(Gun).filter(Gun.id == gun_id).first()
    if gun:
        session.delete(gun)
        session.commit()
