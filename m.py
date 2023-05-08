class Planet:
    def __init__(self):
        self.characteristics = input().split("+")
        self.planets_num = int(input())
        self.planets = {}

    def input_ships(self):
        for i in range(self.planets_num):
            item = input().split(": ")
            features = item[1].split(", ")
            planet_type = item[0]
            self.planets[planet_type] = list(features)

    def solve_task(self):
        good_planets = list()
        for planet_type, features in self.planets.items():
            count = 0
            for i in range(len(features)):
                if features[i] == self.characteristics[i]:
                    count += 1

            if count >= (len(self.characteristics) // 3):
                good_planets.append(planet_type)
        return good_planets

    def print_ships(self):
        good_planets = self.solve_task()
        for planet in good_planets:
            print(planet)

task2 = Planet()

task2.input_ships()
task2.print_ships()
