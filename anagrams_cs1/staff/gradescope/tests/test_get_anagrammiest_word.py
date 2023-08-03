import py_compile
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from anagrams import find_anagrammiest_word

class TestEx1(unittest.TestCase):
    @weight(1)
    @number("5.1")
    def test_1(self):
        """find_anagrammiest_word -  Short list (2 sets of anagrams)"""
        words = ["abed", "abled", "bade", "baled", "bead", "blade"]
        actual_val = find_anagrammiest_word(words)
        expected_vals = ["abed", "abled"]
        self.assertIn(actual_val, expected_vals)

    @weight(1)
    @number("5.2")
    def test_2(self):
        """find_anagrammiest_word -  Long list given in the starter code"""
        words = ['abed', 'bade', 'bead', 'acme', 'came', 'mace', 'abet', 'beat', 'beta', 'acre', 'care', 'race', 'apt', 'pat', 'tap', 'abut', 'tabu', 'tuba', 'amen', 'mane', 'mean', 'name', 'ales', 'leas', 'sale', 'seal', 'anew', 'wane', 'wean', 'abets', 'baste', 'beast', 'beats', 'betas', 'acres', 'cares', 'races', 'scare', 'angel', 'angle', 'glean', 'alert', 'alter', 'later', 'airmen', 'marine', 'remain', 'aligned', 'dealing', 'leading', 'actors', 'castor', 'costar', 'antler', 'learnt', 'rental', 'alerted', 'altered', 'related', 'treadle', 'actress', 'casters', 'recasts', 'allergy', 'gallery', 'largely', 'regally']
        actual_val = find_anagrammiest_word(words)
        self.assertEqual(actual_val, "abets")

    @weight(1)
    @number("5.3")
    def test_3(self):
        """find_anagrammiest_word -  Empty corpus"""
        words = []
        actual_val = find_anagrammiest_word(words)
        self.assertEqual(actual_val, "")

    @weight(1)
    @number("5.4")
    def test_4(self):
        """find_anagrammiest_word -  No anagrams in corpus"""
        words = ["abed", "allergy", "amen", "anew", "angel", "tap", "treadle"]
        actual_val = find_anagrammiest_word(words)
        self.assertEqual(actual_val, "")

    @weight(1)
    @number("5.5")
    def test_5(self):
        """find_anagrammiest_word -  Tie for most anagrams and several no anagrams"""
        words = ["rat", "mouse", "tar", "art", "chicken", "stop", "pots", "tops" ]
        actual_val = find_anagrammiest_word(words)
        expected_vals = ['art', 'pots']
        self.assertIn(actual_val, expected_vals)