from sqlalchemy import create_engine
from faker import Faker
from sqlalchemy.orm import sessionmaker, relationship,joinedload
from models import Base, Gun, User, Review

fake=Faker()
engine = create_engine('sqlite:///guns.db', echo=True)
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()

print("GUN SECTION DETAILS")

def seed_users_and_reviews():
    for _ in range(4):
        user_details = User(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
        )
        session.add(user_details)
        
        
    for user in session.query(User).all():
        for i in range(4):
            review = Review(
                review_text=fake.text()
            )
            session.add(review)

def seed_guns():
    for _ in range(4):
        gun_instance = Gun(
            gun_name=fake.word(),
            gun_price=fake.random_int(min=100, max=10000),
            gun_info=fake.sentence()
        )
        session.add(gun_instance)

    session.commit()

seed_users_and_reviews()
seed_guns()  
session.close()