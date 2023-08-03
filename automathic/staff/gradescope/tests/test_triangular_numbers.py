import unittest
from gradescope_utils.autograder_utils.decorators import weight, number

from automathic import triangle_numbers

class TestTriangleNumbers(unittest.TestCase):
    @weight(1)
    @number("4.1")
    def test_neg(self):
        """Triangle Numbers- Negative Terms"""
        actual = triangle_numbers(-2)
        self.assertEqual(actual, [])

    @weight(1)
    @number("4.2")
    def test_zero(self):
        """Triangle Numbers- 0 Terms"""
        actual = triangle_numbers(0)
        self.assertEqual(actual, [])

    @weight(1)
    @number("4.3")
    def test_neg2(self):
       """Triangle Numbers- 1 Term"""
       actual = triangle_numbers(1)
       self.assertEqual(actual, [1])

    @weight(1)
    @number("4.4")
    def test_zero2(self):
       """Triangle Numbers- 4 Terms"""
       actual = triangle_numbers(4)
       self.assertEqual(actual, [1, 3, 6, 10])

    @weight(1)
    @number("4.5")
    def test_one(self):
        """Triangle Numbers- 10 Terms"""
        actual = triangle_numbers(10)
        self.assertEqual(actual, [1, 3, 6, 10, 15, 21, 28, 36, 45, 55])