class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}".title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can’t roll back an odometer!")

    def increment_odometer(self, miles):
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can’t add negative miles!")


class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65
            print("Battery upgraded to 65 kWh!")
        else:
            print("Battery is already upgraded.")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class, then the battery."""
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model 3', 2025)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()

my_tesla.battery.get_range()

