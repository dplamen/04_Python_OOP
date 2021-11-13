from project.planet.planet import Planet


class PlanetRepository:
    def __init__(self):
        self.planets = []

    def add(self, planet: Planet):
        self.planets.append(planet)

    def remove(self, planet: Planet):
        for pl in self.planets:
            if pl is planet:
                self.planets.remove(pl)

    def find_by_name(self, name):
        for planet in self.planets:
            if planet.name == name:
                return planet
