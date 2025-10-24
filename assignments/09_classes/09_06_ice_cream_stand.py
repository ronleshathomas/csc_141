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


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type="Ice Cream"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["vanilla bean", "chocolate", "cookies&cream", "butter pecan"]

    def display_flavors(self):
        print(f"\n{self.restaurant_name} offers the following flavors:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")


ice_cream_stand = IceCreamStand("The creamery")

ice_cream_stand.describe_restaurant()
ice_cream_stand.display_flavors()

