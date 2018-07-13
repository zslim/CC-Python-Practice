import unittest
from datetime import datetime
from years_module import years


# Here's our "unit tests".


class YearsTestCase(unittest.TestCase):
    def test_100years(self):
        current_year = datetime.now().year
        age = 35
        self.assertEqual(years(age), current_year + 100 - age)
        age = 2
        self.assertEqual(years(age), current_year + 100 - age)
        age = 99
        self.assertEqual(years(age), current_year + 100 - age)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
