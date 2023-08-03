import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from stones import format_pile

class TestFormatPile(unittest.TestCase):
    @weight(1)
    @number("1.1")
    def test_eval_1(self):
        """format_pile- 1 stone in the pile"""
        val = format_pile(1)
        self.assertEqual(val, "\n*\nThere is 1 stone in the pile.")

    @weight(1)
    @number("1.2")
    def test_eval_2(self):
        """format_pile- 2 stones in the pile"""
        val = format_pile(2)
        self.assertEqual(val, "\n**\nThere are 2 stones in the pile.")

    @weight(1)
    @number("1.3")
    def test_eval_3(self):
        """format_pile- 3 stones in the pile"""
        val = format_pile(3)
        self.assertEqual(val, "\n**\n*\nThere are 3 stones in the pile.")

    @weight(1)
    @number("1.4")
    def test_eval_6(self):
        """format_pile- 6 stones in the pile"""
        val = format_pile(6)
        self.assertEqual(val, "\n***\n***\nThere are 6 stones in the pile.")

    @weight(1)
    @number("1.5")
    def test_eval_7(self):
        """format_pile- 7 stones in the pile"""
        val = format_pile(7)
        self.assertEqual(val, "\n***\n***\n*\nThere are 7 stones in the pile.")

    @weight(1)
    @number("1.6")
    def test_eval_10(self):
        """format_pile- 9 stones in the pile"""
        val = format_pile(9)
        self.assertEqual(val, "\n****\n***\n***\nThere are 9 stones in the pile.")

    @weight(1)
    @number("1.7")
    def test_eval_10(self):
        """format_pile- 10 stones in the pile"""
        val = format_pile(10)
        self.assertEqual(val, "\n****\n****\n**\nThere are 10 stones in the pile.")

    @weight(1)
    @number("1.8")
    def test_eval_11(self):
        """format_pile- 11 stones in the pile"""
        val = format_pile(11)
        self.assertEqual(val, "\n****\n****\n***\nThere are 11 stones in the pile.")

    @weight(1)
    @number("1.9")
    def test_eval_15(self):
        """format_pile- 15 stones in the pile"""
        val = format_pile(15)
        self.assertEqual(val, "\n****\n****\n****\n***\nThere are 15 stones in the pile.")

    @weight(1)
    @number("1.10")
    def test_eval_16(self):
        """format_pile- 16 stones in the pile"""
        val = format_pile(16)
        self.assertEqual(val, "\n****\n****\n****\n****\nThere are 16 stones in the pile.")
