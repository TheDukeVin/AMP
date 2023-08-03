import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from stones import get_ai_guess

class TestGetAIGuess(unittest.TestCase):
    @weight(1)
    @number("3.1")
    def test_eval_1(self):
        """get_ai_guess- 2 Stones, allowableGuesses:[1,2,3,4]"""
        val = get_ai_guess(2, [1,2,3,4])
        self.assertEqual(val, 1)

    @weight(1)
    @number("3.2")
    def test_eval_2(self):
        """get_ai_guess- 3 Stones, allowableGuesses:[1,2,3,4]"""
        val = get_ai_guess(3, [1,2,3,4])
        self.assertEqual(val, 2)

    @weight(1)
    @number("3.3")
    def test_eval_3(self):
        """get_ai_guess- 4 Stones, allowableGuesses:[1,2,3,4]"""
        val = get_ai_guess(4, [1,2,3,4])
        self.assertEqual(val, 3)

    @weight(1)
    @number("3.4")
    def test_eval_4(self):
        """get_ai_guess- 5 Stones, allowableGuesses:[1,2,3,4]"""
        val = get_ai_guess(5, [1,2,3,4])
        self.assertEqual(val, 4)

    @weight(1)
    @number("3.5")
    def test_eval_5(self):
        """get_ai_guess- 6 Stones, allowableGuesses:[1,2,3,4]"""
        val = get_ai_guess(6, [1,2,3,4])
        self.assertEqual(val, 1)

    @weight(1)
    @number("3.6")
    def test_eval_6(self):
        """get_ai_guess- 7 Stones, allowableGuesses:[1,2,3,4]"""
        val = get_ai_guess(7, [1,2,3,4])
        self.assertEqual(val, 1)

    @weight(1)
    @number("3.7")
    def test_eval_7(self):
        """get_ai_guess- 8 Stones, allowableGuesses:[1,2,3,4]"""
        val = get_ai_guess(8, [1,2,3,4])
        self.assertEqual(val, 2)

    @weight(1)
    @number("3.8")
    def test_eval_8(self):
        """get_ai_guess- 9 Stones, allowableGuesses:[1,2,3,4]"""
        val = get_ai_guess(9, [1,2,3,4])
        self.assertEqual(val, 3)

    @weight(1)
    @number("3.9")
    def test_eval_9(self):
        """get_ai_guess- 10 Stones, allowableGuesses:[1,2,3,4]"""
        val = get_ai_guess(10, [1,2,3,4])
        self.assertEqual(val, 4)

    @weight(1)
    @number("3.10")
    def test_eval_10(self):
        """get_ai_guess- 11 Stones, allowableGuesses:[1,2,3,4]"""
        val = get_ai_guess(11, [1,2,3,4])
        self.assertEqual(val, 1)

    @weight(1)
    @number("3.11")
    def test_eval_11(self):
        """get_ai_guess- 12 Stones, allowableGuesses:[1,2,3,4]"""
        val = get_ai_guess(12, [1,2,3,4])
        self.assertEqual(val, 1)

    @weight(1)
    @number("3.12")
    def test_eval_12(self):
        """get_ai_guess- 13 Stones, allowableGuesses:[1,2,3,4]"""
        val = get_ai_guess(13, [1,2,3,4])
        self.assertEqual(val, 2)

    @weight(1)
    @number("3.13")
    def test_eval_13(self):
        """get_ai_guess- 14 Stones, allowableGuesses:[1,2,3,4]"""
        val = get_ai_guess(14, [1,2,3,4])
        self.assertEqual(val, 3)

    @weight(1)
    @number("3.14")
    def test_eval_14(self):
        """get_ai_guess- 15 Stones, allowableGuesses:[1,2,3,4]"""
        val = get_ai_guess(15, [1,2,3,4])
        self.assertEqual(val, 4)

    @weight(1)
    @number("3.15")
    def test_eval_15(self):
        """get_ai_guess- 16 Stones, allowableGuesses:[1,2,3,4]"""
        val = get_ai_guess(16, [1,2,3,4])
        self.assertEqual(val, 1)
