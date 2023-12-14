from models import *
from config import *


#Create a new user with a first name,  and last name
def create_user(first_name,last_name):
    if len(first_name) < 5 or len(last_name) < 5:
        print("name must be 5 or more characters")
    else:
        new_user = User(
            first_name=first_name,
            last_name = last_name
        )
        #save it to the database
        session.add(new_user)
        session.commit() 
        return new_user
    
#Retrieve a user's information by providing their user ID.
def get_user(id):
    user = session.query(User).filter(User.id == id).first()
    return f'{user.first_name}'+ " " +f'{user.last_name}'

#Update a user's information by providing their user ID and new data.
def update_user(user_id, new_data):
    user = session.query(User).get(user_id)
    if user:
        for key, value in new_data.items():
            setattr(user, key, value)
        session.commit()
    return user

#Delete a user by providing their user ID.
def delete_user(id):
    user = session.query(User).get(id)
    if user:
        #delete from the database
        session.delete(user)
        #save the database
        session.commit()

#Retrieve all gun reviews related to a specific user by providing their user ID.
def get_gun_user_reviews(user_id):
    collection = []
    gun_reviews = session.query(Review).filter(Review.user_id == user_id).all()
    for review in gun_reviews:
        collection.append(f'Gun ID:{review.gun_id}, Gun review: "{review.review_text}".')
    return collection

# Fetch all users along with their associated gun reviews.
def fetch_all_users_with_gun_reviews():
    users_with_reviews = (
        session.query(User)
        .options(joinedload(User.reviews).joinedload(Review.gun))
        .all()
    )
    return users_with_reviews

#Create a new gun review with a gun id, user ID, and review.
def create_review(gun_id,user_id,review_text):
    new_review = Review(
        gun_id = gun_id,
        user_id = user_id,
        review_text = review_text
    )
    #save it to the database
    session.add(new_review)
    session.commit() 
    return new_review

#Retrieve a guns information by providing its gun ID.
def get_gun(id):
    gun = session.query(Gun).filter(Gun.id == id).first()
    return f'Gun name: {gun.gun_name}, Gun price: {gun.gun_price}, Gun info: {gun.gun_info}'

#Update a guns information by providing its gun ID and new data.
def update_gun(gun_id, new_data):
    gun = session.query(Gun).get(gun_id)
    if gun:
        for key, value in new_data.items():
            setattr(gun, key, value)
        session.commit()
    return gun

#Delete a gun by providing its gun ID.
def delete_gun(id):
    gun = session.query(Gun).get(id)
    if gun:
        #delete from the database
        session.delete(gun)
        #save the database
        session.commit()
        
#Fetch all gun reviews related to a specific gun by providing a specific gun ID
def get_gun_reviews(gun_id):
    collection = []
    reviews = session.query(Review).filter(Review.gun_id == gun_id)
    for review in reviews:
        collection.append(review.review_text)
    return collection