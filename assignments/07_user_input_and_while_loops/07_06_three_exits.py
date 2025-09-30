age = 0
while age != -1:
    age = (input("Enter your age (-1 to stop): "))
    age = (age)
    if age == -1:
        print("Exiting program.")
        break
    if age < 3:
        print("Your ticket is free!")
    elif age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")

