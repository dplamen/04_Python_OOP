class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if price <= self.__budget and self.__animal_capacity > 0:
            self.animals.append(animal)
            self.__budget -= price
            self.__animal_capacity -= 1
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        if price > self.__budget and self.__animal_capacity > 0:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                self.__workers_capacity += 1
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries = 0
        for worker in self.workers:
            salaries += worker.salary
        if salaries <= self.__budget:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        cost = 0
        for animal in self.animals:
            cost += animal.money_for_care
        if cost <= self.__budget:
            self.__budget -= cost
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return f"You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f'You have {len(self.animals)} animals'
        lion_list = []
        cheetah_list = []
        tiger_list = []
        for animal in self.animals:
            if type(animal).__name__ == 'Lion':
                lion_list.append(animal.__repr__())
            elif type(animal).__name__ == 'Cheetah':
                cheetah_list.append(animal.__repr__())
            elif type(animal).__name__ == 'Tiger':
                tiger_list.append(animal.__repr__())

        result += f'\n----- {len(lion_list)} Lions:\n' + '\n'.join(lion_list)
        result += f'\n----- {len(tiger_list)} Tigers:\n' + '\n'.join(tiger_list)
        result += f'\n----- {len(cheetah_list)} Cheetahs:\n' + '\n'.join(cheetah_list)
        return result

    def workers_status(self):
        result = f'You have {len(self.workers)} workers'
        keeper_list = []
        caretaker_list = []
        vets_list = []
        for worker in self.workers:
            if type(worker).__name__ == 'Keeper':
                keeper_list.append(worker.__repr__())
            elif type(worker).__name__ == 'Caretaker':
                caretaker_list.append(worker.__repr__())
            elif type(worker).__name__ == 'Vet':
                vets_list.append(worker.__repr__())

        result += f'\n----- {len(keeper_list)} Keepers:\n' + '\n'.join(keeper_list)
        result += f'\n----- {len(caretaker_list)} Caretakers:\n' + '\n'.join(caretaker_list)
        result += f'\n----- {len(vets_list)} Vets:\n' + '\n'.join(vets_list)
        return result

