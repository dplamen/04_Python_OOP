from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.isspace() or value == '':
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type, name, price):
        if name in [x.name for x in self.food_menu]:
            raise Exception(f"{food_type} {name} is already in the menu!")
        if food_type == "Bread":
            self.food_menu.append(Bread(name, price))
        elif food_type == "Cake":
            self.food_menu.append(Cake(name, price))
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type, name, portion, brand):
        if name in [x.name for x in self.drinks_menu]:
            raise Exception(f"{drink_type} {name} is already in the menu!")
        if drink_type == "Tea":
            self.drinks_menu.append(Tea(name, portion, brand))
        elif drink_type == "Water":
            self.drinks_menu.append(Water(name, portion, brand))
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type, table_number, capacity):
        if table_number in [x.table_number for x in self.tables_repository]:
            raise Exception(f"Table {table_number} is already in the bakery!")
        if table_type == "InsideTable":
            self.tables_repository.append(InsideTable(table_number, capacity))
        elif table_type == "OutsideTable":
            self.tables_repository.append(OutsideTable(table_number, capacity))
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people):
        for t in self.tables_repository:
            if not t.is_reserved and t.capacity >= number_of_people:
                t.reserve(number_of_people)
                return f"Table {t.table_number} has been reserved for {number_of_people} people"

        return f"No available table for {number_of_people} people"

    def order_food(self, table_number, *food_names):
        ordered_food = []
        not_ordered = []
        table = [t for t in self.tables_repository if t.table_number == table_number]
        if table:
            table = table[0]
            for food in food_names:
                found = False
                for x in self.food_menu:
                    if x.name == food:
                        table.order_food(x)
                        ordered_food.append(repr(x))
                        found = True
                        break
                if not found:
                    not_ordered.append(food)

            result = f"Table {table_number} ordered:\n"
            result += '\n'.join(ordered_food)
            if not_ordered:
                result += f"\n{self.name} does not have in the menu:\n"
                result += '\n'.join(not_ordered)
            return result
        return f"Could not find table {table_number}"

    def order_drink(self, table_number, *drink_names):
        ordered_drink = []
        not_ordered = []
        table = [t for t in self.tables_repository if t.table_number == table_number]
        if table:
            table = table[0]
            for drink in drink_names:
                found = False
                for x in self.drinks_menu:
                    if x.name == drink:
                        table.order_drink(x)
                        ordered_drink.append(repr(x))
                        found = True
                        break
                if not found:
                    not_ordered.append(drink)

            result = f"Table {table_number} ordered:\n"
            result += '\n'.join(ordered_drink)
            if not_ordered:
                result += f"\n{self.name} does not have in the menu:\n"
                result += '\n'.join(not_ordered)
            return result
        return f"Could not find table {table_number}"

    def leave_table(self, table_number):
        table = [t for t in self.tables_repository if t.table_number == table_number]
        if table:
            table = table[0]
            bill = table.get_bill()
            table.clear()
            self.total_income += bill

            result = f"Table: {table_number}\n"
            result += f"Bill: {bill:.2f}"

            return result

    def get_free_tables_info(self):
        result = ""
        for table in self.tables_repository:
            result += f"{table.free_table_info()}\n"

        return result

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
