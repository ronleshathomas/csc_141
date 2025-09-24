cities = {
    'paris': {
        'country': 'france',
        'population': '2.1 million',
        'fact': 'Known as the City of Light and home to the Eiffel Tower.',
        'language': 'french',
        'landmark': 'eiffel tower'
    },
    'tokyo': {
        'country': 'japan',
        'population': '13.9 million',
        'fact': 'The most populous metropolitan area in the world.',
        'language': 'japanese',
        'landmark': 'tokyo tower'
    },
    'cairo': {
        'country': 'egypt',
        'population': '10 million',
        'fact': 'Famous for its proximity to the Pyramids of Giza.',
        'language': 'arabic',
        'landmark': 'pyramids of giza'
    }
}
for city, info in cities.items():
    print(f"\n {city.title()}")
    print(f"{city.title()} is in {info['country'].title()} and has a population of about {info['population']}.")
    print(f"People there primarily speak {info['language'].title()}.")
    print(f"A famous landmark is the {info['landmark'].title()}.")
    print(f"Fun fact: {info['fact']}")

