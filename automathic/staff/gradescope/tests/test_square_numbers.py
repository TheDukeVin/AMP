import unittest
from gradescope_utils.autograder_utils.decorators import weight, number

from automathic import square_numbers

class TestSquareNumbers(unittest.TestCase):
    @weight(1)
    @number("3.1")
    def test_neg(self):
        """Square Numbers- Negative Terms"""
        actual = square_numbers(-2)
        self.assertEqual(actual, [])

    @weight(1)
    @number("3.2")
    def test_zero(self):
        """Square Numbers- 0 Terms"""
        actual = square_numbers(0)
        self.assertEqual(actual, [])

    @weight(1)
    @number("3.3")
    def test_neg2(self):
       """Square Numbers- 1 Term"""
       actual = square_numbers(1)
       self.assertEqual(actual, [0])

    @weight(1)
    @number("3.4")
    def test_zero2(self):
       """Square Numbers- 4 Terms"""
       actual = square_numbers(4)
       self.assertEqual(actual, [0, 1, 4, 9])

    @weight(1)
    @number("3.5")
    def test_one(self):
        """Square Numbers- 10 Terms"""
        actual = square_numbers(10)
        self.assertEqual(actual, [0, 1, 4, 9, 16, 25, 36, 49, 64, 81])