from main import add_user, get_all_users, get_all_guns, get_gun_by_id, get_user_by_id, gun_user
from main import delete_gun, delete_user, session
from models import Gun
# Create a new user

# Read all users
print("All Users:")
for user in get_all_users():
    print(f"User ID: {user.id}, First Name: {user.first_name}, Last Name: {user.last_name}")

# Read user by ID
user_id_to_query = 3  # Replace with the desired user ID
user_to_query = get_user_by_id(user_id_to_query)
if user_to_query:
    print(f"User with ID {user_id_to_query}:")
    print(f"User ID: {user_to_query.id}, First Name: {user_to_query.first_name}, Last Name: {user_to_query.last_name}")

# Read all guns
print("All Guns:")
for gun in get_all_guns():
    print(f"Gun ID: {gun.id}, Gun Name: {gun.gun_name}, Gun Price: {gun.gun_price}, Gun Info: {gun.gun_info}")

# Read gun by ID
gun_id_to_query = 1  # Replace with the desired gun ID
gun_to_query = get_gun_by_id(gun_id_to_query)
if gun_to_query:
    print(f"Gun with ID {gun_id_to_query}:")
    print(f"Gun ID: {gun_to_query.id}, Gun Name: {gun_to_query.gun_name}, Gun Price: {gun_to_query.gun_price}, Gun Info: {gun_to_query.gun_info}")

# Delete a user by ID
user_id_to_delete = 1  # Replace with the desired user ID to delete
delete_user(user_id_to_delete)
print(f"Deleted user with ID {user_id_to_delete}")

# Delete a gun by ID
gun_id_to_delete = 1  # Replace with the desired gun ID to delete
delete_gun(gun_id_to_delete)
print(f"Deleted gun with ID {gun_id_to_delete}")
