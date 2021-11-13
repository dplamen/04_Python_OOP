from car_manager import Car
from unittest import TestCase, main


class TestCar(TestCase):
    def setUp(self):
        self.car = Car("Test", "TestModel", 5.6, 52)

    def test_init_creates_all_attributes(self):
        self.assertEqual("Test", self.car.make)
        self.assertEqual("TestModel", self.car.model)
        self.assertEqual(5.6, self.car.fuel_consumption)
        self.assertEqual(52, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_null_make_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = None
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))
        with self.assertRaises(Exception) as ex:
            self.car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))
        self.car.make = "Test2"
        self.assertEqual("Test2", self.car.make)

    def test_null_model_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = None
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))
        with self.assertRaises(Exception) as ex:
            self.car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))
        self.car.model = "TestModel2"
        self.assertEqual("TestModel2", self.car.model)

    def test_negative_fuel_consumption_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))
        self.car.fuel_consumption = 3.4
        self.assertEqual(3.4, self.car.fuel_consumption)

    def test_negative_fuel_capacity_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))
        self.car.fuel_capacity = 34
        self.assertEqual(34, self.car.fuel_capacity)

    def test_negative_fuel_amount_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -5
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))
        self.car.fuel_amount = 0
        self.assertEqual(0, self.car.fuel_amount)

    def test_refuel_adds_fuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-10)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_adds_fuel_up_to_fuel_capacity(self):
        self.car.refuel(10)
        self.assertEqual(10, self.car.fuel_amount)
        self.car.refuel(100)
        self.assertEqual(52, self.car.fuel_amount)

    def test_drive_if_enough_fuel(self):
        self.car.refuel(30)
        self.car.drive(100)
        self.assertEqual(24.4, self.car.fuel_amount)

    def test_drive_if_not_enough_fuel(self):
        self.car.refuel(30)
        with self.assertRaises(Exception) as ex:
            self.car.drive(1000)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))
        self.assertEqual(30, self.car.fuel_amount)


if __name__ == '__main__':
    main()
