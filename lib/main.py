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