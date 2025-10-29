def city_country(city, country):
    return f"{city.title()}, {country.title()}"


from city_functions import city_country 

def test_city_country():
    formatted = city_country('santiago', 'chile')
    assert formatted == 'Santiago, Chile'

