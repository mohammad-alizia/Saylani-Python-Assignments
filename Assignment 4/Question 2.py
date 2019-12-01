cities = {
    'Karachi': {
        'country': 'Pakistan',
        'population': 6158080,
        'fact': 'mazar e quaid',
        },
    'Agra': {
        'country': 'India',
        'population': 876,
        'fact': 'Taj Mahal',
        },
    'Paris': {
        'country': 'France',
        'population': 1003285,
        'fact': 'Eifel Tower',
        }
    }

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    fact = city_info['fact'].title()

    print("\n" + city.title() + " is in " + country + ".")
    print("  It has a population of about " + str(population) + ".")
    print("  The " + fact + " is a famous architect")