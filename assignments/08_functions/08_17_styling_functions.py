def display_message():
    """Display a message about what you're learning."""
    print("I’m learning about functions in this chapter!")


def favorite_book(title):
    """Display a message about someone's favorite book."""
    print(f"One of my favorite books is {title}.")


def city_country(city, country):
    """Return a string formatted as 'City, Country'."""
    return f"{city}, {country}"



display_message()

favorite_book("Alice in Wonderland")

print(city_country("Santiago", "Chile"))
print(city_country("Paris", "France"))
print(city_country("Tokyo", "Japan"))

