import unittest
from gradescope_utils.autograder_utils.decorators import weight, number

from envelope import to_binary_bin, to_binary_format, to_binary_divide, to_binary_subtract, to_binary_bitwise

inputs = [0, 1, 4, 43, 255, 123, 129, 1001 ]
expected = ["0", "1", "100", "101011", "11111111", "1111011", "10000001", "1111101001"]

class TestPositiveOdds(unittest.TestCase):
    @weight(1)
    @number("1.1")
    def test_bin(self):
        """Built-in Function: bin"""
        for i, n in enumerate(inputs):
            actual = to_binary_bin(n)
            self.assertEqual(actual, expected[i])

    @weight(1)
    @number("1.2")
    def test_format(self):
        """Built-in Function: format"""
        for i, n in enumerate(inputs):
            actual = to_binary_format(n)
            self.assertEqual(actual, expected[i])

    @weight(1)
    @number("1.3")
    def test_one(self):
        """Dividing by 2"""
        for i, n in enumerate(inputs):
            actual = to_binary_divide(n)
            self.assertEqual(actual, expected[i])

    @weight(1)
    @number("1.4")
    def test_two(self):
        """Subtracting powers of 2"""
        for i, n in enumerate(inputs):
            actual = to_binary_subtract(n)
            self.assertEqual(actual, expected[i])

    @weight(1)
    @number("1.5")
    def test_five(self):
        """Optional Challenge: Bitwise Operators"""
        for i, n in enumerate(inputs):
            actual = to_binary_bitwise(n)
            self.assertEqual(actual, expected[i])