import unittest
from gradescope_utils.autograder_utils.decorators import weight, number

from automathic import positive_multiples

class TestPositiveMultiples(unittest.TestCase):
    @weight(1)
    @number("2.1")
    def test_neg(self):
        """Positive Multiples- Negative Terms"""
        actual = positive_multiples(-2, 3)
        self.assertEqual(actual, [])

    @weight(1)
    @number("2.2")
    def test_zero(self):
        """Positive Multiples- 0 Terms"""
        actual = positive_multiples(0, 2)
        self.assertEqual(actual, [])

    @weight(1)
    @number("2.3")
    def test_neg2(self):
        """Positive Multiples- Negative Multiple"""
        actual = positive_multiples(3, -2)
        self.assertEqual(actual, [])

    @weight(1)
    @number("2.4")
    def test_zero2(self):
        """Positive Multiples- 0 Multiple"""
        actual = positive_multiples(2, 0)
        self.assertEqual(actual, [])

    @weight(1)
    @number("2.5")
    def test_one(self):
        """Positive Multiples- 1 Term"""
        actual = positive_multiples(1, 2)
        self.assertEqual(actual, [2])

    @weight(1)
    @number("2.6")
    def test_four(self):
        """Positive Multiples- Many Terms"""
        actual = positive_multiples(4, 1)
        self.assertEqual(actual, [1, 2, 3, 4])

    @weight(1)
    @number("2.7")
    def test_four(self):
        """Positive Multiples- Many Terms"""
        actual = positive_multiples(5, 3)
        self.assertEqual(actual, [3, 6, 9, 12, 15])
