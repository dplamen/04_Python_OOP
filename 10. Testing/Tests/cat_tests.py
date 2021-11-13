from cat import Cat

import unittest


class CatTests(unittest.TestCase):
    def setUp(self):
        self.cat = Cat('Peter')

    def test_cat_size_increased_after_eating(self):
        self.assertEqual(0, self.cat.size)
        self.cat.eat()
        self.assertEqual(1, self.cat.size)
        
    def test_cat_is_fed_after_eating(self):
        self.cat.eat()
        self.assertEqual(True, self.cat.fed)

    def test_cat_cannot_be_fed_after_eating(self):
        self.cat.eat()
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test_cat_cannot_be_sleep_before_eating(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_not_sleepy_after_sleeping(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertEqual(False, self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()
