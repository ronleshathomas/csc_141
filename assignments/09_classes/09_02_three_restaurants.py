class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")


restaurant1 = Restaurant("Big Booty Judy", "Soul Food")
restaurant2 = Restaurant("Konpa Konpa", "Haitian Food")
restaurant3 = Restaurant("Mushu", "Chinese Food")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

