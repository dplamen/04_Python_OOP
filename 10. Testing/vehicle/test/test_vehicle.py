from project.vehicle import Vehicle
from unittest import TestCase, main


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(15.4, 100.9)
    
    def test_initialization(self):
        self.assertEqual(15.4, self.vehicle.fuel)
        self.assertEqual(15.4, self.vehicle.capacity)
        self.assertEqual(100.9, self.vehicle.horse_power)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_if_enough_fuel(self):
        self.vehicle.drive(10)
        self.assertEqual(2.9000000000000004, self.vehicle.fuel)

    def test_drive_if_not_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_if_enough_capacity(self):
        self.vehicle.capacity = 100
        self.vehicle.refuel(30)
        self.assertEqual(45.4, self.vehicle.fuel)

    def test_refuel_if_not_enough_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(20)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_print_vehicle(self):
        result = str(self.vehicle)
        self.assertEqual("The vehicle has 100.9 horse power "
                         "with 15.4 fuel left and 1.25 fuel consumption", result)
        
         
if __name__ == '__main__':
    main()
