cities = {
    'team': {
        'country': 'America',
        'population': '500,000',
        'fact': '3rd largest city in America',
    },
    'weight': {
        'country': 'France',
        'population': '1,500,000',
        'fact': 'home of the Eiffel Tower',
    },
    'superbowls': {
        'country': 'England',
        'population': '3,000,000',
        'fact': 'home of James Bond',
    },
    'position': {
        'country': 'America',
        'population': '500,000',
        'fact': '3rd largest city in America',
    },
}


for city, information in cities.items():
    print(city.title() + ":")
    for category, fact in information.items():
        print("\t" + category.title() + ": " + fact)
    print()
