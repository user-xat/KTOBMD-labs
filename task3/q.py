# Q. Страны и города
if __name__ == '__main__':
    FILENAME = '!countries_and_cities.txt'
    cities_dict = dict()

    with open(FILENAME) as fin:
        n = int(fin.readline().strip())
        for _ in range(n):
            country_and_cities = fin.readline().split()
            country = country_and_cities[0]
            for city in country_and_cities[1:]:
                cities_dict[city] = country

        m = int(fin.readline().strip())
        for _ in range(m):
            city = fin.readline().strip()
            print(cities_dict[city])
