favorites = {
    'miya': {
        'places': ['paris', 'new york', 'tokyo'],
        'numbers': [1, 5, 4]
    },
    'lee': {
        'places': ['london', 'rome'],
        'numbers': [3, 9]
    },
    'ray': {
        'places': ['sydney'],
        'numbers': [25]
    },
}

for name, info in favorites.items():
    print(f"{name.title()}'s favorite places are:")
    for place in info['places']:
        print(f" - {place.title()}")
    
    print(f"{name.title()}'s favorite numbers are:")
    for number in info['numbers']:
        print(f" - {number}")
    
    print() 

