class Country:
    def __init__(self, name):
        self.name = name
        self.cities = []

    def add_city(self, city):
        self.cities.append(city)

class City:
    def __init__(self, name, country):
        self.name = name
        self.country = country

philippines = Country(name="The Philippines")
cebu = City(name="Cebu City", country=philippines)
lapu_lapu = City(name="Lapu-Lapu City", country=philippines)

philippines.add_city(cebu)
philippines.add_city(lapu_lapu)

print("Country Name:", philippines.name)
print("Cities:")
for city in philippines.cities:
    print(f" - {city.name}")




