cities = {
    'paris': {
        'country': 'france',
        'population': '2.1 million',
        'fact': 'Known as the City of Light and home to the Eiffel Tower.'
    },
    'tokyo': {
        'country': 'japan',
        'population': '13.9 million',
        'fact': 'The most populous metropolitan area in the world.'
    },
    'cairo': {
        'country': 'egypt',
        'population': '10 million',
        'fact': 'Famous for its proximity to the Pyramids of Giza.'
    }
}

for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"  Country: {info['country'].title()}")
    print(f"  Population: {info['population']}")
    print(f"  Fact: {info['fact']}")

