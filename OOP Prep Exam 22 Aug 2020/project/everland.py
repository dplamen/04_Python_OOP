class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += room.room_cost + room.expenses
        return f"Monthly consumptions: {total_consumption:.2f}$."

    def pay(self):
        result = []
        for room in self.rooms:
            total_cost = room.room_cost + room.expenses
            if room.budget >= total_cost:
                room.budget -= total_cost
                result.append(f"{room.family_name} paid {total_cost:.2f}$ and have {room.budget:.2f}$ left.")
            else:
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(room)
        return '\n'.join(result)

    def status(self):
        all_people = 0
        for room in self.rooms:
            all_people += room.members_count
        result = f'Total population: {all_people}\n'
        for room in self.rooms:
            result += f'{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, ' \
                      f'Expenses: {room.expenses:.2f}$\n'
            if hasattr(room, 'children'):
                n = 1
                for child in room.children:
                    result += f"--- Child {n} monthly cost: {child.cost * 30:.2f}$\n"
                    n += 1
            appliance_monthly_expenses = 0
            if hasattr(room, 'appliances'):
                for appliance in room.appliances:
                    appliance_monthly_expenses += appliance.get_monthly_expense()
                result += f'--- Appliances monthly cost: {appliance_monthly_expenses:.2f}$\n'

        return result

