from project.appliances.fridge import Fridge
from project.people.child import Child
from project.rooms.room import Room
from unittest import TestCase, main


class TestRoom(TestCase):
    def setUp(self):
        self.room = Room("Test", 100, 2)

    def test_room_initialisation(self):
        self.assertEqual("Test", self.room.family_name)
        self.assertEqual(100, self.room.budget)
        self.assertEqual(2, self.room.members_count)
        self.assertEqual([], self.room.children)
        self.assertEqual(0, self.room.expenses)

    def test_expenses_property_if_negative(self):
        with self.assertRaises(ValueError) as ex:
            self.room.expenses = -10
        self.assertEqual("Expenses cannot be negative", str(ex.exception))

    def test_expenses_property_if_acceptable(self):
        self.room.expenses = 10
        self.assertEqual(10, self.room.expenses)

    def test_calculate_expenses_method(self):
        appliances = [Fridge()]
        children = [Child(3, 2, 5), Child(2, 2, 5)]
        self.room.calculate_expenses(appliances, children)
        self.assertEqual(606, self.room.expenses)


if __name__ == '__main__':
    main()
