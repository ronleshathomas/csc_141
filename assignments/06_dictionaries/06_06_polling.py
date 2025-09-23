favorite_number = {
     'miya': '5',
    'minah': '14',
    'mir': '23',
    'lee': '3',
    'rai': '22',
}

people_to_poll = ['miya', 'minah', 'michael', 'sarah', 'anna']

for person in people_to_poll:
    if person in favorite_number:
        print(f"Thank you, {person.title()}, for responding to the poll!")
    else:
        print(f"{person.title()}, you are invited to take the favorite number poll!")

