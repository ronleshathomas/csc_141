print("Enter pizza toppings (type 'quit' to stop):")

while True:
    topping = input("Topping: ")

    if topping.lower() == 'quit':
        print("Finished making your pizza!")
        break
    else:
        print(f"I'll add {topping} to your pizza.")