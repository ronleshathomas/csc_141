import json

filename = 'favorite_number.json'

try:
    with open(filename) as f:
        favorite_number = json.load(f)
except FileNotFoundError:
    
    favorite_number = input("I don't know your favorite number yet. What is it? ")
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
    print(f"Thanks! I'll remember that your favorite number is {favorite_number}.")
else:
    print(f"I know your favorite number! It's {favorite_number}.")

