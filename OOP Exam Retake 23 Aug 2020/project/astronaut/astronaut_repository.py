from project.astronaut.astronaut import Astronaut


class AstronautRepository:
    def __init__(self):
        self.astronauts = []

    def add(self, astronaut: Astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        for astro in self.astronauts:
            if astro is astronaut:
                self.astronauts.remove(astro)

    def find_by_name(self, name):
        for astro in self.astronauts:
            if astro.name == name:
                return astro
