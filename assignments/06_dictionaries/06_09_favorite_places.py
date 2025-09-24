favorite_places = {
    'miya': ['paris', 'new york', 'tokyo'],
    'lee': ['london', 'rome'],
    'ray': ['egypt']
}
for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f" - {place.title()}")
    print() 

