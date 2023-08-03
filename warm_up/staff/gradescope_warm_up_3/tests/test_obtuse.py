import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from warm_up_3 import classify_triangle

class TestObtuse(unittest.TestCase):
    @weight(1)
    @number("2.1")
    def test_eval_isoceles1(self):
        """Obtuse- Isosceles 1"""
        val = classify_triangle(7,4,4)
        self.assertEqual(val, "obtuse")

    @weight(1)
    @number("2.2")
    def test_eval_isoceles2(self):
        """Obtuse- Isosceles 2"""
        val = classify_triangle(4,7,4)
        self.assertEqual(val, "obtuse")

    @weight(1)
    @number("2.3")
    def test_eval_isoceles3(self):
        """Obtuse- Isosceles 3"""
        val = classify_triangle(4,4,7)
        self.assertEqual(val, "obtuse")

    @weight(1)
    @number("2.4")
    def test_eval_general(self):
        """Obtuse- General"""
        val = classify_triangle(3, 4, 6)
        self.assertEqual(val, "obtuse")
