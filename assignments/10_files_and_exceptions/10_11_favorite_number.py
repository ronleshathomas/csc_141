import json
favorite_number = input("What is your favorite number? ")

filename = 'favorite_number.json'
with open(filename, 'w') as f:
    json.dump(favorite_number, f)

print(f"Your favorite number {favorite_number} has been saved!")


import json

filename = 'favorite_number.json'
try:
    with open(filename) as f:
        favorite_number = json.load(f)
except FileNotFoundError:
    print("No favorite number found. Please run favorite_number.py first.")
else:
    print(f"I know your favorite number! It's {favorite_number}.")

