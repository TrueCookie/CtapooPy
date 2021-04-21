
cities_guide = {}

N = int(input())
count = 0
while count < N:
    country_cities = input()

    space_index = country_cities.find(' ')
    country = country_cities[:space_index]
    cities = country_cities[space_index:]

    for city in str.split(cities, ' '):
        cities_guide[city] = country

    count = count + 1


M = int(input())
count = 0
while count < M:
    print(cities_guide[input()])
