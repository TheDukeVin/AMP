import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from warm_up_2 import calculate_area

class TestAcute(unittest.TestCase):
    @weight(1)
    @number("1.1")
    def test_area_1(self):
        """Area- radius: 1"""
        actual = calculate_area(1)
        expected = 3.14159 
        self.assertLess(abs(expected - actual), 0.001)

    @weight(1)
    @number("1.2")
    def test_area_2(self):
        """Area- radius: 4"""
        actual = calculate_area(4)
        expected = 50.26548
        self.assertLess(abs(expected - actual), 0.001)

    @weight(1)
    @number("1.3")
    def test_area_3(self):
        """Area- radius: 2.5"""
        actual = calculate_area(2.5)
        expected = 19.63495
        self.assertLess(abs(expected - actual), 0.001)

    @weight(1)
    @number("1.4")
    def test_area_4(self):
        """Area- radius: 10"""
        actual = calculate_area(10)
        expected = 314.15927
        self.assertLess(abs(expected - actual), 0.001)