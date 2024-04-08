import unittest
from random_test_data_generator import generate_test_data
import datetime


class TestDataGeneratorTestCase(unittest.TestCase):
    def test_numeric_generation(self):
        data = generate_test_data('numeric', 10)
        self.assertEqual(len(data), 10)
        self.assertTrue(all(isinstance(item, int) for item in data))

    def test_string_generation(self):
        data = generate_test_data('string', 10)
        self.assertEqual(len(data), 10)
        self.assertTrue(all(isinstance(item, str) for item in data))

    def test_datetime_generation(self):
        data = generate_test_data('datetime', 10)
        self.assertEqual(len(data), 10)
        self.assertTrue(all(isinstance(item, datetime.datetime) for item in data))


if __name__ == '__main__':
    unittest.main()