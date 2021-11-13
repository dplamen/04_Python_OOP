from worker import Worker
import unittest


class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("Test", 100, 10)

    def test_worker_is_initialized_correctly(self):
        # Assert
        self.assertEqual("Test", self.worker.name)
        self.assertEqual(100, self.worker.salary)
        self.assertEqual(10, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_worker_energy_increased_after_rest(self):
        # Act
        self.worker.rest()
        # Assert
        self.assertEqual(11, self.worker.energy)

    def test_worker_works_with_negative_energy(self):
        # Arrange
        worker = Worker("Test", 100, 0)
        # Act
        with self.assertRaises(Exception) as ex:
            worker.work()
        # Assert
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_worker_money_increase_with_salary(self):
        self.assertEqual(0, self.worker.money)
        # Act
        self.worker.work()
        # Assert
        self.assertEqual(100, self.worker.money)

    def test_worker_energy_decreased_after_work(self):
        self.assertEqual(10, self.worker.energy)
        # Act
        self.worker.work()
        # Assert
        self.assertEqual(9, self.worker.energy)

    def test_worker_get_info_method(self):
        # Act
        result = self.worker.get_info()
        # Assert
        self.assertEqual('Test has saved 0 money.', result)


if __name__ == '__main__':
    unittest.main()
