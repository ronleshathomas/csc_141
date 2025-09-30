sandwich_orders = ['tuna', 'turkey', 'ham', 'veggie', 'chicken']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)  
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich) 

print("\nAll sandwiches that were made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")

