def make_car(manufacturer, model, **options):
    """Build a dictionary containing information about a car."""
    car_info = {
        'manufacturer': manufacturer,
        'model': model
    }
    for key, value in options.items():
        car_info[key] = value
    return car_info

car1 = make_car('Tesla', 'Model S', color='red', autopilot=True)
car2 = make_car('Ford', 'Mustang', year=2023, color='blue')

print(car1)
print(car2)

