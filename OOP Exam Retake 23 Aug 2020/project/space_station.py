from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_missions = 0
        self.missions_not_completed = 0

    def add_astronaut(self, astronaut_type, name):
        if astronaut_type == 'Biologist':
            astro = Biologist(name)
        elif astronaut_type == 'Geodesist':
            astro = Geodesist(name)
        elif astronaut_type == 'Meteorologist':
            astro = Meteorologist(name)
        else:
            raise Exception("Astronaut type is not valid!")

        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.name == name:
                return f"{name} is already added."

        self.astronaut_repository.add(astro)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name, items):
        planet = Planet(name)
        items = items.split(', ')
        for item in items:
            planet.items.append(item)
        for pl in self.planet_repository.planets:
            if pl.name == name:
                return f"{name} is already added."

        self.planet_repository.planets.append(planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name):
        astro = self.astronaut_repository.find_by_name(name)
        if astro:
            self.astronaut_repository.remove(astro)
            return f"Astronaut {name} was retired!"
        raise Exception(f"Astronaut {name} doesn't exists!")

    def recharge_oxygen(self):
        for astro in self.astronaut_repository.astronauts:
            astro.increase_oxygen(10)

    def send_on_mission(self, planet_name):
        planet = self.planet_repository.find_by_name(planet_name)
        if not planet:
            raise Exception("Invalid planet name!")

        astro = [x for x in self.astronaut_repository.astronauts if x.oxygen > 30]
        if not astro:
            raise Exception("You need at least one astronaut to explore the planet!")

        suitable_astro = sorted(astro, key=lambda x: x.oxygen, reverse=True)
        astro_count = 1
        for astronaut in suitable_astro:
            flag = False
            while planet.items:
                astronaut.breathe()
                astronaut.backpack.append(planet.items.pop())
                if astronaut.oxygen < 0:
                    astronaut.oxygen = 0
                    flag = True
                    break

            if flag:
                astro_count += 1
                continue
        if planet.items:
            self.missions_not_completed += 1
            return "Mission is not completed."
        self.successful_missions += 1
        return f"Planet: {planet_name} was explored. {astro_count} astronauts participated in collecting items."

    def report(self):
        result = f"{self.successful_missions} successful missions!\n"
        result += f"{self.missions_not_completed} missions were not completed!\n"
        result += f"Astronauts' info:\n"
        for astro in self.astronaut_repository.astronauts:
            result += f"Name: {astro.name}\n"
            result += f"Oxygen: {astro.oxygen}\n"
            if astro.backpack:
                result += f"Backpack items: {', '.join(astro.backpack)}\n"
            else:
                result += 'Backpack items: "none"\n'

        return result.rstrip('\n')

