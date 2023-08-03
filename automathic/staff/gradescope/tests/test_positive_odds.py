import unittest
from gradescope_utils.autograder_utils.decorators import weight, number

from automathic import positive_odds

class TestPositiveOdds(unittest.TestCase):
    @weight(1)
    @number("1.1")
    def test_neg(self):
        """Positive Odds- Negative Terms"""
        actual = positive_odds(-2)
        self.assertEqual(actual, [])

    @weight(1)
    @number("1.2")
    def test_zero(self):
        """Positive Odds- 0 Terms"""
        actual = positive_odds(0)
        self.assertEqual(actual, [])

    @weight(1)
    @number("1.3")
    def test_one(self):
        """Positive Odds- 1 Term"""
        actual = positive_odds(1)
        self.assertEqual(actual, [1])

    @weight(1)
    @number("1.4")
    def test_two(self):
        """Positive Odds- 2 Terms"""
        actual = positive_odds(2)
        self.assertEqual(actual, [1, 3])

    @weight(1)
    @number("1.5")
    def test_five(self):
        """Positive Odds- Many Terms"""
        actual = positive_odds(5)
        self.assertEqual(actual, [1, 3, 5, 7, 9])
