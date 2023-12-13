from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Gun,Review,User

if __name__ == '__main__':
    engine = create_engine('sqlite:///guns.sqlite')
    Session = sessionmaker(bind=engine)
    session = Session()
    
    fake = Faker()
    
    gun_names = [
    "Thunderstrike",
    "Shadow Reaper",
    "Inferno Fury",
    "Rapid Blaster",
    "Nightshade Viper",
    "Stormbreaker",
    "Spectre Magnum",
    "Hellfire Annihilator",
    "Widowmaker",
    "Vortex Destroyer",
    "Venomous Fang",
    "Frostbite Crusher",
    "Solar Eclipse",
    "Steel Serpent",
    "Lunar Avenger",
    "Silent Assassin",
    "Doomsday Devastator",
    "Mystic Guardian",
    "Nebula Blaster",
    "Phantom Ghost" 
]
    gun_infos = [
    "Assault Rifle",
    "Sniper Rifle",
    "Shotgun",
    "Submachine Gun",
    "Pistol",
    "Heavy Machine Gun",
    "Magnum Revolver",
    "Flamethrower",
    "Sniper Rifle",
    "Rocket Launcher",
    "Poison Dart Gun",
    "Freeze Ray",
    "Solar Beam Emitter",
    "Railgun",
    "Laser Pistol",
    "Silenced Submachine Gun",
    "BFG (Big Freaking Gun)",
    "Enchanted Crossbow",
    "Energy Pistol",
    "Stealth SMG"
]
    reviewtext = [
    "Absolutely amazing product! It exceeded all my expectations.",
    "Terrible experience. I regret purchasing this item.",
    "Five stars! This is a game-changer.",
    "Not worth the price. Poor quality and functionality.",
    "Highly recommend! Quality craftsmanship and excellent performance.",
    "Worst purchase ever. Broke after just a few uses.",
    "Exceptional customer service. They went above and beyond to help me.",
    "Average product. It gets the job done but nothing special.",
    "Incredible value for the money. I'm impressed!",
    "The design is stylish and modern. A perfect addition to my collection.",
    "I love it! The features are fantastic, and it's so easy to use.",
    "Disappointed. The product did not live up to the hype.",
    "Great for beginners. Simple and user-friendly.",
    "Awful customer support. They were unhelpful and unresponsive.",
    "Beautiful packaging. The presentation alone is worth it.",
    "Not recommended. Flimsy construction and unreliable.",
    "Efficient and effective. This product saved me a lot of time.",
    "Poorly designed. The ergonomics are uncomfortable.",
    "Top-notch quality. I would buy from this brand again.",
    "Mixed feelings. Some aspects are great, others not so much."
]
    #create guns
    guns = []
    for i in range(25):
        gun = Gun(
            gun_name = random.choice(gun_names),
            gun_price = random.randint(500,1000),
            gun_info = random.choice(gun_infos)
        )
         # add and commit individually to get IDs back
        session.add(gun)
        session.commit()
        #append the gun to our guns list
        guns.append(gun)
        
    #create users
    users = []
    for i in range(25):
        user = User(
            first_name = fake.first_name(),
            last_name = fake.last_name(),
        )
        # add and commit individually to get IDs back
        session.add(user)
        session.commit()
        #append the user to our users list
        users.append(user)
        
    #create reviews
    reviews = []
    for gun in guns:
        for item in range(random.randint(1,5)):
            user = random.choice(users)
            if gun not in user.guns:
                user.guns.append(gun)
                session.add(user)
                session.commit()
            
            review = Review(
                review_text = random.choice(reviewtext),
                gun_id = gun.id,
                user_id = user.id,
            )
            #append the review to our reviews list
            reviews.append(review)
           
           
    #bulk save, commit then close the session 
    session.bulk_save_objects(reviews)
    session.commit()
    session.close()