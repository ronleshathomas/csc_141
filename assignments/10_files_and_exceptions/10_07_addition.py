print("Welcome to the Addition Calculator!")
print("Type 'quit' anytime to exit.\n")

while True:
    first_number = input("Enter the first number: ")
    if first_number.lower() == 'quit':
        print("Goodbye!")
        break

    second_number = input("Enter the second number: ")
    if second_number.lower() == 'quit':
        print("Goodbye!")
        break

    try:
        result = int(first_number) + int(second_number)
    except ValueError:
        print("Oops! Please enter valid numbers only.\n")
    else:
        print(f"The sum of {first_number} and {second_number} is {result}.\n")

