import unittest
from gradescope_utils.autograder_utils.decorators import weight, number

from automathic import fibonacci_sequence

class TestFibonacciSequence(unittest.TestCase):
    @weight(1)
    @number("6.1")
    def test_neg(self):
        """Fibonacci Sequences- Negative Terms"""
        actual = fibonacci_sequence(-2)
        self.assertEqual(actual, [])

    @weight(1)
    @number("6.2")
    def test_zero(self):
        """Fibonacci Sequences- Zero Terms"""
        actual = fibonacci_sequence(0)
        self.assertEqual(actual, [])

    @weight(1)
    @number("6.3")
    def test_one(self):
        """Fibonacci Sequences- One Term"""
        actual = fibonacci_sequence(1)
        self.assertEqual(actual, [1])

    @weight(1)
    @number("6.4")
    def test_many(self):
        """Fibonacci Sequences- Many Terms"""
        actual = fibonacci_sequence(19)
        self.assertEqual(actual, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181])
