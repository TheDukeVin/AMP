import unittest
from gradescope_utils.autograder_utils.decorators import weight, number

from automathic import arithmetic_sequence

class TestArithmeticSequence(unittest.TestCase):
    @weight(1)
    @number("5.1")
    def test_neg(self):
        """Arithmetic Sequences- Negative Number of Terms"""
        actual = arithmetic_sequence(-1, 1, 2)
        self.assertEqual(actual, [])

    @weight(1)
    @number("5.2")
    def test_zero(self):
        """Arithmetic Sequences- Zero Number of Terms"""
        actual = arithmetic_sequence(0, 1, 2)
        self.assertEqual(actual, [])

    @weight(1)
    @number("5.3")
    def test_one(self):
        """Arithmetic Sequences- One Term"""
        actual = arithmetic_sequence(1, 1, 2)
        self.assertEqual(actual, [1])

    @weight(1)
    @number("5.4")
    def test_three(self):
        """Arithmetic Sequences- General"""
        actual = arithmetic_sequence(3, 1, 2)
        self.assertEqual(actual, [1, 2, 3])

    @weight(1)
    @number("5.5")
    def test_five(self):
        """Arithmetic Sequences- General"""
        actual = arithmetic_sequence(5, 0, 2)
        self.assertEqual(actual, [0, 2, 4, 6, 8])

    @weight(1)
    @number("5.6")
    def test_five_neg(self):
        """Arithmetic Sequences- Two Negative Terms"""
        actual = arithmetic_sequence(5, -1, -3)
        self.assertEqual(actual, [-1, -3, -5, -7, -9])

    @weight(1)
    @number("5.7")
    def test_seven(self):
        """Arithmetic Sequences- One Negative Term"""
        actual = arithmetic_sequence(7, 1, -2)
        self.assertEqual(actual, [1, -2, -5, -8, -11, -14, -17])
