def car_profile(manufacturer, model, **car_info):
    """Build a dictionary containing information about each car."""
    profile = {}
    profile['manufacturer'] = manufacturer
    profile['model'] = model
    for key, value in car_info.items():
        profile[key] = value
    return profile


def print_car_profile(cars_profile):
    """Print out the key/values in the car profile dictionary."""
    for key, value in cars_profile.items():
        print(key.title(), ' = ', value.title())


my_car_profile = car_profile(
    'ford', 'mustang', doors='2', color='red', cylinders='4-turbo')

print_car_profile(my_car_profile)
