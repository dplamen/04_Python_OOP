from project.supply.supply import Supply
from project.medicine.medicine import Medicine
from project.survivor import Survivor


class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []
        
    @property
    def food(self):
        food_obj = [s for s in self.supplies if s.__class__.__name__ == 'FoodSupply']
        if not food_obj:
            raise IndexError("There are no food supplies left!")
        return food_obj

    @property
    def water(self):
        water_obj = [s for s in self.supplies if s.__class__.__name__ == 'WaterSupply']
        if not water_obj:
            raise IndexError("There are no water supplies left!")
        return water_obj

    @property
    def painkillers(self):
        painkillers_obj = [s for s in self.medicine if s.__class__.__name__ == 'Painkiller']
        if not painkillers_obj:
            raise IndexError("There are no painkillers left!")
        return painkillers_obj

    @property
    def salves(self):
        salves_obj = [s for s in self.medicine if s.__class__.__name__ == 'Salves']
        if not salves_obj:
            raise IndexError("There are no salves left!")
        return salves_obj

    def add_survivor(self, survivor: Survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply: Supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine: Medicine):
        self.medicine.append(medicine)

    def heal(self, survivor: Survivor, medicine_type: str):
        to_remove = [m for m in self.medicine if m.__class__.__name__ == medicine_type][-1]
        self.medicine.remove(to_remove)
        if survivor.needs_healing:
            to_remove.apply(survivor)
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor: Survivor, sustenance_type: str):
        to_remove = [m for m in self.supplies if m.__class__.__name__ == sustenance_type][-1]
        self.supplies.remove(to_remove)
        if survivor.needs_sustenance:
            to_remove.apply(survivor)
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= 2 * survivor.age

        for survivor in self.survivors:
            self.sustain(survivor, 'FoodSupply')
            self.sustain(survivor, 'WaterSupply')
