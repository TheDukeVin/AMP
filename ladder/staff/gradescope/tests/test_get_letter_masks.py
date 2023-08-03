import unittest
from gradescope_utils.autograder_utils.decorators import weight, number

import random 

from valid_word_list import get_valid_word_list
from ladder_solution import get_letter_masks

class TestLetterMasks(unittest.TestCase):
    @weight(1)
    @number("1.1")
    def test_1(self):
        """get_letter_masks- cat"""
        actual = get_letter_masks("cat")
        expected = ["*at","c*t","ca*"]
        self.assertEqual(sorted(actual), sorted(expected))

    @weight(1)
    @number("1.2")
    def test_2(self):
        """get_letter_masks- HELP"""
        actual = get_letter_masks("HELP")
        expected = ["*elp","h*lp","he*p","hel*"]
        self.assertEqual(sorted(actual), sorted(expected))

    @weight(1)
    @number("1.3")
    def test_3(self):
        """get_letter_masks- empty string"""
        actual = get_letter_masks("")
        expected = []
        self.assertEqual(sorted(actual), sorted(expected))

    @weight(1)
    @number("1.4")
    def test_4(self):
        """get_letter_masks- no"""
        actual = get_letter_masks("no")
        expected = ["*o","n*"]
        self.assertEqual(sorted(actual), sorted(expected))

    @weight(1)
    @number("1.5")
    def test_5(self):
        """get_letter_masks- Mystery 1"""
        actual = get_letter_masks("story")
        expected = ["*tory","s*ory","st*ry", "sto*y", "stor*"]
        self.assertEqual(sorted(actual), sorted(expected))

    @weight(1)
    @number("1.6")
    def test_6(self):
        """get_letter_masks- Mystery 2"""
        actual = get_letter_masks("LatTE")
        expected = ["*atte","l*tte","la*te", "lat*e", "latt*"]
        self.assertEqual(sorted(actual), sorted(expected))

    def mask_matches(self, mask, word):
        self.assertEqual(len(mask), len(word))
        for mask_char, word_char in zip(mask, word):
            if mask_char == '*':
                continue
            else:
                self.assertEqual(mask_char, word_char)

    # @weight(1)
    # @number("1.7")
    # def test_sound_generation(self):
    #    """get_letter_masks- Every mask matches the original word"""
    #    valid_words = get_valid_word_list()
    #    for _ in range(100):
    #        word = random.choice(valid_words)
    #        print("checking masks for word", word)
    #        for mask in get_letter_masks(word):
    #            self.mask_matches(mask, word)

    # @weight(1)
    # @number("1.8")
    # def test_well_formed_generation(self):
    #     """get_letter_masks- Every mask has one wild card"""
    #     valid_words = get_valid_word_list ()
    #     for _ in range(100):
    #        word = random.choice(valid_words)
    #        print("Counting number of * in masks for", word)
    #        for mask in get_letter_masks(word):
    #            self.assertEqual(1, mask.count("*"))

    # @weight(1)
    # @number("1.9")
    # def test_complete_generation(self):
    #     """get_letter_masks- Wild card occurs in each position once"""
    #     ## checks that the wild card occurs in every position once
    #     valid_words = get_valid_word_list()
    #     for _ in range(100):
    #         word = random.choice(valid_words)
    #         print(word, "generates", get_letter_masks(word))
    #         positions = set(mask.find("*") for mask in get_letter_masks(word))
    #         if -1 in positions: print("-1 indicates not in word")
    #         self.assertEqual(set(range(len(word))), set(positions))

if __name__ == "__main__":
    unittest.main(verbosity=2)