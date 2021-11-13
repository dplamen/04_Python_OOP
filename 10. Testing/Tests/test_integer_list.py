from extended_list import IntegerList
from unittest import TestCase, main


class TestIntegerList(TestCase):
    def setUp(self):
        self.ext_list = IntegerList(1, 2, 3)

    def test_initialization(self):
        self.assertEqual([1, 2, 3], self.ext_list._IntegerList__data)
        other_list = IntegerList(1, 'a', 2, 'b')
        self.assertEqual([1, 2], other_list._IntegerList__data)

    def test_add_element(self):
        self.ext_list.add(4)
        self.assertEqual([1, 2, 3, 4], self.ext_list._IntegerList__data)
        with self.assertRaises(ValueError) as ex:
            self.ext_list.add('x')
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_remove_index(self):
        el = self.ext_list.remove_index(0)
        self.assertEqual(1, el)
        self.assertEqual([2, 3], self.ext_list._IntegerList__data)

    def test_remove_index_if_out_of_range(self):
        with self.assertRaises(IndexError) as ex:
            self.ext_list.remove_index(3)
        self.assertEqual('Index is out of range', str(ex.exception))

    def test_if_get_returns_element(self):
        el = self.ext_list.get(0)
        self.assertEqual(1, el)
        with self.assertRaises(IndexError) as ex:
            self.ext_list.get(3)
        self.assertEqual('Index is out of range', str(ex.exception))

    def test_insert_element(self):
        self.ext_list.insert(0, 3)
        self.assertEqual([3, 1, 2, 3], self.ext_list._IntegerList__data)
        with self.assertRaises(IndexError) as ex:
            self.ext_list.insert(4, 4)
        self.assertEqual('Index is out of range', str(ex.exception))
        with self.assertRaises(ValueError) as ex:
            self.ext_list.insert(1, '4')
        self.assertEqual('Element is not Integer', str(ex.exception))

    def test_get_biggest(self):
        biggest = self.ext_list.get_biggest()
        self.assertEqual(3, biggest)

    def test_get_index(self):
        el = self.ext_list.get_index(2)
        self.assertEqual(1, el)


if __name__ == '__main__':
    main()
