import json

filename = 'user_info.json'

try:
    with open(filename) as f:
        user_info = json.load(f)
except FileNotFoundError:
    user_info = {}
    user_info['username'] = input("Enter your username: ")
    user_info['favorite_number'] = input("Enter your favorite number: ")
    user_info['favorite_color'] = input("Enter your favorite color: ")

    
    with open(filename, 'w') as f:
        json.dump(user_info, f)
    print("\nThanks! Your information has been saved.\n")
else:
    print("\nI already know your information! Here's what I remember:\n")
print(f"Username: {user_info['username']}")
print(f"Favorite number: {user_info['favorite_number']}")
print(f"Favorite color: {user_info['favorite_color']}")

