import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from warm_up_3 import classify_triangle

class TestDoesNotExist(unittest.TestCase):

    @weight(1)
    @number("4.1")
    def test_eval_negative1(self):
        """Does Not Exist- Negative Side Length 1"""
        val = classify_triangle(5, -4, 3)
        self.assertEqual(val, "does not exist")

    @weight(1)
    @number("4.2")
    def test_eval_negative2(self):
        """Does Not Exist- Negative Side Length 1"""
        val = classify_triangle(-3, 8, 4)
        self.assertEqual(val, "does not exist")

    @weight(1)
    @number("4.3")
    def test_eval_too_small1(self):
        """Does Not Exist- Sides Too Small 1"""
        val = classify_triangle(1, 2, 3)
        self.assertEqual(val, "does not exist")

    @weight(1)
    @number("4.4")
    def test_eval_too_small2(self):
        """Does Not Exist- Sides Too Small 2"""
        val = classify_triangle(1, 1, 4)
        self.assertEqual(val, "does not exist")

    @weight(1)
    @number("4.5")
    def test_eval_too_small3(self):
        """Does Not Exist- Sides Too Small 3"""
        val = classify_triangle(3, 3, 6)
        self.assertEqual(val, "does not exist")

    @weight(1)
    @number("4.6")
    def test_eval_zero(self):
        """Does Not Exist- Side length 0"""
        val = classify_triangle(0, 0, 0)
        self.assertEqual(val, "does not exist")
