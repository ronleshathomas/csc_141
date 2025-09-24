person1 = {
  'first_name': 'Namier',
    'last_name': 'Dukes',
    'age': 20,
    'city': 'Philadelphia'
}
person2 = {
    'first_name': 'Tamiya',
    'last_name': 'Anderson',
    'age': 21,
    'city': 'Philadelphia'
}

person3 = {
    'first_name': 'Nasier',
    'last_name': 'Williams',
    'age': 23,
    'city': 'Allentown'
}

people = [person1, person2, person3]

for person in people:
    print(f"First name: {person['first_name'].title()}")
    print(f"Last name: {person['last_name'].title()}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city'].title()}")
    print()  

