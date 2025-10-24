class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0 

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        if number >= 0:
            self.number_served = number
        else:
            print("Number served cannot be negative!")

    def increment_number_served(self, additional_customers):
        if additional_customers >= 0:
            self.number_served += additional_customers
        else:
            print("Cannot increment by a negative number!")


restaurant = Restaurant("Big Booty Judy", "Soul Food")

print(f"Customers served: {restaurant.number_served}")

restaurant.number_served = 25
print(f"Customers served after update: {restaurant.number_served}")

restaurant.set_number_served(50)
print(f"Customers served after using set_number_served(): {restaurant.number_served}")

restaurant.increment_number_served(30)
print(f"Customers served after increment: {restaurant.number_served}")

