class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} {self.cuisine_type} restaurant .")

    def open_restaurant(self):

        print(f"{self.restaurant_name} is now open!")

restaurant = Restaurant("Big Booty Judy", "Soul Food")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

