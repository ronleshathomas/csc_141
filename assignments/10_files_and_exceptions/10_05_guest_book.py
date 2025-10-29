print("Enter your name (or type 'quit' to stop):")

with open('guest_book.txt', 'a') as file_object:
    while True:
        name = input("Name: ")

        if name.lower() == 'quit':
            print("Guest book closed. Goodbye!")
            break

    
        file_object.write(name + "\n")
        print(f"Welcome, {name}! Your name has been added to the guest book.")

