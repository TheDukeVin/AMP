import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from warm_up_3 import classify_triangle

class TestRight(unittest.TestCase):
    @weight(1)
    @number("3.1")
    def test_eval_increasing(self):
        """Right- Increasing Order"""
        val = classify_triangle(3, 4, 5)
        self.assertEqual(val, "right")

    @weight(1)
    @number("3.2")
    def test_eval_mixed1(self):
        """Right- Mixed Order 1"""
        val = classify_triangle(3, 5, 4)
        self.assertEqual(val, "right")

    @weight(1)
    @number("3.3")
    def test_eval_mixed2(self):
        """Right- Mixed Order 2"""
        val = classify_triangle(4, 3, 5)
        self.assertEqual(val, "right")

    @weight(1)
    @number("3.4")
    def test_eval_mixed3(self):
        """Right- Mixed Order 3"""
        val = classify_triangle(4, 5, 3)
        self.assertEqual(val, "right")

    @weight(1)
    @number("3.5")
    def test_eval_mixed4(self):
        """Right- Mixed Order 4"""
        val = classify_triangle(5, 3, 4)
        self.assertEqual(val, "right")

    @weight(1)
    @number("3.6")
    def test_eval_mixed5(self):
        """Right- Mixed Order 5"""
        val = classify_triangle(5, 4, 3)
        self.assertEqual(val, "right")

    @weight(1)
    @number("3.7")
    def test_eval_general(self):
        """Right- General"""
        val = classify_triangle(5, 12, 13)
        self.assertEqual(val, "right")
