import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from stones import is_valid_move

class TestIsValidMove(unittest.TestCase):
    @weight(1)
    @number("2.1")
    def test_eval_1(self):
        """is_valid_move- 16 Stones, Guess in valid_guesses"""
        self.assertEqual(is_valid_move(1, 16, [1,2,3,4]), True)

    @weight(1)
    @number("2.2")
    def test_eval_2(self):
        """is_valid_move- 16 Stones, Guess not in valid_guesses"""
        self.assertEqual(is_valid_move(5, 16, [1,2,3,4]), False)

    @weight(1)
    @number("2.3")
    def test_eval_3(self):
        """is_valid_move- 3 Stones, Guess in valid_guesses That Takes Last Stone"""
        self.assertEqual(is_valid_move(3, 3, [1,2,3,4]), False)

    @weight(1)
    @number("2.4")
    def test_eval_4(self):
        """is_valid_move- 3 Stones, Guess not in valid_guesses"""
        self.assertEqual(is_valid_move(0, 3, [1,2,3,4]), False)

    @weight(1)
    @number("2.5")
    def test_eval_5(self):
            """is_valid_move- 3 Stones, Guess in valid_guesses, but Takes Too Many Stones"""
            self.assertEqual(is_valid_move(4, 3, [1,2,3,4]), False)

    @weight(1)
    @number("2.6")
    def test_eval_6(self):
        """is_valid_move- 11 Stones, Guess in non-standard valid_guesses"""
        self.assertEqual(is_valid_move(2, 11, [1,2]), True)

    @weight(1)
    @number("2.7")
    def test_eval_7(self):
        """is_valid_move- 11 Stones, Guess in non-standard valid_guesses"""
        self.assertEqual(is_valid_move(2, 11, [1,2]), True)

    @weight(1)
    @number("2.8")
    def test_eval_8(self):
        """is_valid_move- 11 Stones, Guess not in non-standard valid_guesses"""
        self.assertEqual(is_valid_move(3, 11, [1,2]), False)
