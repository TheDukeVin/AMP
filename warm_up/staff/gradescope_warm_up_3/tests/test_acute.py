import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from warm_up_3 import classify_triangle

class TestAcute(unittest.TestCase):
    @weight(1)
    @number("1.1")
    def test_eval_equilateral(self):
        """Acute- Equilateral"""
        val = classify_triangle(3,3,3)
        self.assertEqual(val, "acute")

    @weight(1)
    @number("1.2")
    def test_eval_isoceles(self):
        """Acute- Isosceles"""
        val = classify_triangle(3,3,4)
        self.assertEqual(val, "acute")

    @weight(1)
    @number("1.3")
    def test_eval_decimal(self):
        """Acute- Decimal Side Lengths"""
        val = classify_triangle(.5,.5,.5)
        self.assertEqual(val, "acute")

    @weight(1)
    @number("1.4")
    def test_eval_general(self):
        """Acute- General"""
        val = classify_triangle(4, 5, 6)
        self.assertEqual(val, "acute")
