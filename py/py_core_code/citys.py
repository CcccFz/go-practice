cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(state, themap):
    if state in themap:
        return themap[state]
    else:
        return 'Not found.'

cities['_find'] = find_city

while True:
    print('State? (ENTER to quit)')
    state = input('> ')
    if not state:
        break

    city_found = cities['_find'](state, cities)
    print(city_found)
