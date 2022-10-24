import random




class City:
    def __init__(self, city_name: str = 'default city'):
        self.city_name = city_name
        self.streets = []

    @property
    def population(self):
        population = 0
        for street in self.streets:
            for building in street.buildings:
                population += building.population
        return population

    def create_city(self, streets_number: int = 5):
        for street in range(streets_number):
            self.streets.append(Street(len(self.streets) + 1, random.randint(5, 20)))

    def add_street(self):
        self.streets.append(Street(len(self.streets) + 1, random.randint(5, 20)))

    def delete_street(self, street_num: int):
        self.streets.pop(street_num - 1)

    def info(self):
        print('Street', 'Building', 'Population')
        for street in self.streets:
            for building in street.buildings:
                print(street.street_num, building.building_number, building.population, sep='\t'*2)



class Street:
    def __init__(self, street_num: int, num_of_buildings: int):
        self.buildings = []
        self.num_of_buildings = num_of_buildings
        self.street_num = street_num

        for building in range(self.num_of_buildings):
            self.buildings.append(Building(len(self.buildings) + 1))


class Building:
    def __init__(self, building_number: int):
        self.population = random.randint(1, 100)
        self.building_number = building_number



if __name__ == '__main__':
    city = City('Antwerp')
    city.add_street()
    city.add_street()
    print(city.population)
    city.info()
    city.delete_street(1)
    city.info()
    city.add_street()
    city.add_street()
    city.add_street()
    city.add_street()
    city.info()
    city.delete_street(2)
    city.info()
    print(f' {city.city_name} population = {city.population}')



