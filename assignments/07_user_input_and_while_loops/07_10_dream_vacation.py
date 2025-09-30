responses = {}
polling_active = True

while polling_active:
    vacation = input("If you could vacation anywhere, where would you go? ")
    responses = vacation

print("\n--- Poll Results ---")
for name, vacation in responses.items():
    print(f"{name} would like to visit {vacation}.")

