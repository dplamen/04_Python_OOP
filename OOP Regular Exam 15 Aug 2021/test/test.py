from unittest import TestCase, main
from project.pet_shop import PetShop


class TestPetShop(TestCase):
    def setUp(self):
        self.pet_shop = PetShop("Test")

    def test_init_pet_shop(self):
        self.assertEqual("Test", self.pet_shop.name)
        self.assertEqual({}, self.pet_shop.food)
        self.assertEqual([], self.pet_shop.pets)

    def test_add_invalid_quantity_food(self):
        with self.assertRaises(ValueError) as ex:
            self.pet_shop.add_food("Food1", 0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))
        
    def test_add_food_valid_in_pet_shop(self):
        result = self.pet_shop.add_food("Food1", 50)
        self.assertEqual("Successfully added 50.00 grams of Food1.", result)
        self.assertEqual(50, self.pet_shop.food["Food1"])

    def test_add_new_pet_to_shop(self):
        result = self.pet_shop.add_pet("Pesho")
        self.assertEqual("Pesho", self.pet_shop.pets[0])
        self.assertEqual("Successfully added Pesho.", result)

    def test_add_pet_with_same_name(self):
        self.pet_shop.add_pet("Pesho")
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet("Pesho")
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_feed_pet_not_in_shop(self):
        self.pet_shop.add_food("Food1", 10.2)
        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet("Food_1", "Test")
        self.assertEqual("Please insert a valid pet name", str(ex.exception))
        
    def test_feed_pet_with_food_not_available(self):
        self.pet_shop.add_pet("Test")
        result = self.pet_shop.feed_pet("Food_2", "Test")
        self.assertEqual("You do not have Food_2", result)

    def test_feed_pet_when_food_is_below_100(self):
        self.pet_shop.add_pet("Test")
        self.pet_shop.add_food("Food", 80)
        result = self.pet_shop.feed_pet("Food", "Test")
        self.assertEqual("Adding food...", result)
        self.assertEqual(1080, self.pet_shop.food["Food"])

    def test_feed_pet_when_food_is_equal_or_higher_than_100(self):
        self.pet_shop.add_pet("Test")
        self.pet_shop.add_food("Food", 180)
        result = self.pet_shop.feed_pet("Food", "Test")
        self.assertEqual("Test was successfully fed", result)
        self.assertEqual(80, self.pet_shop.food["Food"])

    def test_repr_method(self):
        self.pet_shop.add_pet("Test1")
        self.pet_shop.add_pet("Test2")
        self.assertEqual("Shop Test:\nPets: Test1, Test2", repr(self.pet_shop))


if __name__ == '__main__':
    main()
