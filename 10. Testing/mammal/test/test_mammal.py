from project.mammal import Mammal
from unittest import TestCase, main


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("Test", "TestType", "Rrrr")

    def test_init_mammal(self):
        self.assertEqual("Test", self.mammal.name)
        self.assertEqual("TestType", self.mammal.type)
        self.assertEqual("Rrrr", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)
        
    def test_make_sound(self):
        result = self.mammal.make_sound()
        self.assertEqual("Test makes Rrrr", result)

    def test_get_kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual("animals", result)

    def test_info_method(self):
        result = self.mammal.info()
        self.assertEqual("Test is of type TestType", result)


if __name__ == '__main__':
    main()




