import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from darts import is_dart_in_square

class TestIsDartInSquare(unittest.TestCase):
    @weight(1)
    @number("2.1")
    def test_dart_in_square_1(self):
        """Dart is in center of the square"""
        actual = is_dart_in_square(
            100, 100, 50, 50, 150, 150)
        expected = True
        self.assertEqual(actual, expected)

    @weight(1)
    @number("2.2")
    def test_dart_in_square_2(self):
        """Dart is near edge of square"""
        actual = is_dart_in_square(
            149, 149, 50, 50, 150, 150)
        expected = True
        self.assertEqual(actual, expected)

    @weight(1)
    @number("2.3")
    def test_dart_not_in_square_1(self):
        """Dart not within square"""
        actual = is_dart_in_square(
            152, 100, 50, 50, 150, 150)
        expected = False
        self.assertEqual(actual, expected)

    @weight(1)
    @number("2.4")
    def test_dart_not_in_square_2(self):
        """Dart definitely not within square"""
        actual = is_dart_in_square(
            120, 1000, 50, 20, 150, 120)
        expected = False
        self.assertEqual(actual, expected)