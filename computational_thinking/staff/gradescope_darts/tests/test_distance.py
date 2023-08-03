import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from darts import distance

class TestDistance(unittest.TestCase):
    @weight(1)
    @number("1.1")
    def test_distance_1(self):
        """Distance- (0,0) to (3, 4)"""
        actual = distance(0, 0, 3, 4)
        expected = 5
        self.assertLess(abs(expected - actual), 0.001)

    @weight(1)
    @number("1.2")
    def test_distance_2(self):
        """Distance- (0,0) to (-3, 4)"""
        actual = distance(0, 0, -3, 4)
        expected = 5
        self.assertLess(abs(expected - actual), 0.001)

    @weight(1)
    @number("1.3")
    def test_distance_3(self):
        """Distance- (-4,3) to (0,0)"""
        actual = distance(-4, 3, 0, 0)
        expected = 5
        self.assertLess(abs(expected - actual), 0.001)

    @weight(1)
    @number("1.4")
    def test_distance_4(self):
        """Distance- (1,2) to (1,2)"""
        actual = distance(1, 2, 1, 2)
        expected =  0
        self.assertLess(abs(expected - actual), 0.001)

    @weight(1)
    @number("1.5")
    def test_distance_5(self):
        """Distance- (1,1) to (2,2)"""
        actual = distance(1, 1, 2, 2)
        expected =  1.41421356
        self.assertLess(abs(expected - actual), 0.001)