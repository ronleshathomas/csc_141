rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'mississippi': 'united states'
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print() 

print("Rivers included in the dictionary:")
for river in rivers.keys():
    print(f"- {river.title()}")

print()

print("Countries included in the dictionary:")
for country in rivers.values():
    print(f"- {country.title()}")

