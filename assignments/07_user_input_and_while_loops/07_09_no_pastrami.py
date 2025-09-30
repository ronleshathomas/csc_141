sandwich_orders = ['tuna', 'pastrami', 'ham', 'pastrami', 'veggie', 'pastrami', 'chicken']
finished_sandwiches = []

print("Sorry, the deli has run out of pastrami.\n")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)


print("\nAll sandwiches that were made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")

