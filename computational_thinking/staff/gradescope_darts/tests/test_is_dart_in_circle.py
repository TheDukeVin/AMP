import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from darts import is_dart_in_circle

class TestIsDartInCircle(unittest.TestCase):
    @weight(1)
    @number("3.1")
    def test_dart_in_circle_1(self):
        """Dart is in center of the circle"""
        actual = is_dart_in_circle(
            200, 200, 200, 200, 3)
        expected = True
        self.assertEqual(actual, expected)

    @weight(1)
    @number("3.2")
    def test_dart_in_circle_2(self):
        """Dart is near edge of circle"""
        actual = is_dart_in_circle(
            105, 108, 100, 100, 10
        )
        expected = True
        self.assertEqual(actual, expected)

    @weight(1)
    @number("3.3")
    def test_dart_not_in_circle_1(self):
        """Dart not within circle"""
        actual = is_dart_in_circle(
            3, 4, 0, 0, 1)
        expected = False
        self.assertEqual(actual, expected)