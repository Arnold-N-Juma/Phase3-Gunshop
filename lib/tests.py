from main import *

print(" >>>>>>>>>> USER OPERATIONS <<<<<<<<< ")
print("<=====CREATING A NEW USER=====>")
user = create_user("Erling","Haaland")
print(f"Created User: {user.first_name} {user.last_name}")

 
print("")

print("<=====GETTING A USER BY ID=====>")
fetched_user = get_user(8)
print(f"Fetched User : {fetched_user}")

print("")

print("<=====UPDATING A USER INFORMATION=====>")
updated_user_data = {'first_name': "Cole", 'last_name': "Palmer"}
updated_user = update_user(1,updated_user_data)
print(f"Updated User: {updated_user.first_name} {updated_user.last_name}")

print("")

print("<=====DELETING A USER=====>")
deleted_user = delete_user(26)
print(f"Successfully deleted user.")

print("")

print(" >>>>>>>>>> REVIEW OPERATIONS <<<<<<<<< ")
"""print("<=====CREATING A NEW REVIEW=====>")
review = create_review(13,23,"The gun holds alot of ammo")
print(f" Gun ID: {review.gun_id}, by user ID: {review.user_id}, had the following review: {review.review_text}") """

print('')

print("<=====FETCHING ALL GUN REVIEWS BY USER=====>")
fetched_review = get_gun_user_reviews(13)
print(fetched_review)

print('')

print("<=====FETCHING ALL USERS WITH THE ASSOCIATED GUN REVIEWS =====>")
users_reviews = fetch_all_users_with_gun_reviews()
for user in users_reviews:
    print(f"User : {user.first_name} {user.last_name}")
    
    for review in user.reviews:
        print(f"  Gun Name: {review.gun.gun_name}, Review Text: {review.review_text}")
        print('')
    print("-" * 30)

print('')

print(" >>>>>>>>>> GUN OPERATIONS <<<<<<<<< ")
print("<=====FETCHING GUN BY ID=====>")
fetched_gun = get_gun(8)
print(fetched_gun)

print('')

print("<=====UPDATING A GUN'S INFORMATION=====>")
updated_gun_data = {'gun_name': "Glock", 'gun_price': 1000, 'gun_info':"Glock 9"}
updated_gun = update_gun(1,updated_gun_data)
print(f"Updated Gun: {updated_gun.gun_name}, Gun price: {updated_gun.gun_price}, Gun info: {updated_gun.gun_info}")

print("")

""" print("<=====DELETING A GUN=====>")
deleted_gun = delete_gun(25)
print(f"Successfully deleted gun.") """

print('')

print("<=====FETCHING ALL GUN REVIEWS FOR A SPECIFIC GUN=====>")
fetched_review = get_gun_reviews(13)
print(fetched_review)