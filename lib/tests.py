from main import *
from config import *

print("CREATING NEW USER")

user=create_user("Jammie", "Bravo")
print(f"User:{user.first_name}{user.last_name}")

print("")
print("***** FETCHING A USER BY THIER ID *****")
user=get_user(7)
print(f"User:{user}")

print("")
print("***** UPDATING USERS BY THEIR ID *****")
new_data={"first_name":"Keanu", "last_name":"Reeves"}
user=update_user(7, new_data)
print(f"Updated Name:{user.first_name} SurName:{user.last_name}")

print("")
print("***** DELETING A USER BY IS*****")
user=delete_user(5)
print(f"User No longer Available")
# print(f"User:{user.first_name}") # When You try to Run this query the line outputs an error

print("")
print("***** FETCHING A USER'S GUN REVIEWS BY ID *****")
review=get_gun_user_reviews(8)
print(f"Review:{review}")

print("")
print("***** CREATING NEW GUN REVIEWS *****")
review=create_review(7, 11, "Shocking and Choking")
print(f"New Gun ID:{review.gun_id}, Reviewed by User ID:{review.user_id},and the review is:{review.review_text}")

print("")
print("***** RETREIVING A GUN BY ID*****")
gun=get_gun(6)
print(f"Here is:{gun}")

print("")
print("***** UPDATING GUN'S DETAILS****")
new_data={'gun_name':"Black King", 'gun_price':750,'gun_info':"Fast killing sniper rifle"}
new_gun=update_gun(8, new_data)
print(f"The New gun is called the {new_gun.gun_name},the Gun's Price is {new_gun.gun_price} and it is a {new_gun.gun_info}")
 
print("")
print("***** DELETING GUN DETAILS****")
gun=delete_gun(1)
print("Gun data succesfully deleted")

print("")
print("***** RETREIVING A GUN'S REVIEWS****")
reviews=get_gun_reviews(11)
print(f"Here are the reviews:{reviews}")
