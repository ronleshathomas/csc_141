def make_sandwich(*items):
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")
    print("Your sandwich is ready!\n")

make_sandwich("ham", "cheese", "lettuce")
make_sandwich("turkey", "bacon")
make_sandwich("peanut butter", "jelly", "banana", "honey")

