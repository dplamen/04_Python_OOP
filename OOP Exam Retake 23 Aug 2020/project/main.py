from project.space_station import SpaceStation

space = SpaceStation()
space.add_astronaut("Biologist", "Peter")
space.add_astronaut("Geodesist", "John")
space.add_astronaut("Meteorologist", "Asen")
space.add_planet("Earth", "Item1, Item2, Item3, Item1, Item1, Item2, Item3, Item1")
space.add_planet("Mars", "Item11, Item21, Item31, Item11")
space.add_planet("Venera", "Item11, Item21, Item31, Item11 , Item21, Item31, Item1, , Item21, Item31, Item1, Item31, Item1")
space.recharge_oxygen()
print(space.send_on_mission("Earth"))
print(space.send_on_mission("Mars"))
print(space.send_on_mission("Venera"))
print(space.report())
