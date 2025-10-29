print("Let's add two numbers!")
print("Type 'quit' at any time to stop.\n")

while True:
    first_number = input("Enter the first number: ")
    if first_number.lower() == 'quit':
        break

    second_number = input("Enter the second number: ")
    if second_number.lower() == 'quit':
        break

    try:
        
        result = int(first_number) + int(second_number)
    except ValueError:
        
        print("Oops! You must enter numbers, not text. Please try again.\n")
    else:
        print(f"The sum of {first_number} and {second_number} is {result}.\n")

