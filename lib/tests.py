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