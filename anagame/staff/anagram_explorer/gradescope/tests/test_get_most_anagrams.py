import py_compile
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from anagram_explorer import get_most_anagrams

class TestEx1(unittest.TestCase):
    @weight(1)
    @number("3.1")
    def test_1(self):
        """get_most_anagrams -  Short list (2 sets of anagrams)"""
        words = ["abed", "abled", "bade", "baled", "bead", "blade"]
        actual_val = get_most_anagrams(words)
        expected_val = ["abed", "abled"]
        self.assertEqual(actual_val, expected_val)

    @weight(1)
    @number("3.2")
    def test_2(self):
        """get_most_anagrams -  Long list given in the starter code"""
        words = ['abed', 'bade', 'bead', 'acme', 'came', 'mace', 'abet', 'beat', 'beta', 'acre', 'care', 'race', 'apt', 'pat', 'tap', 'abut', 'tabu', 'tuba', 'amen', 'mane', 'mean', 'name', 'ales', 'leas', 'sale', 'seal', 'anew', 'wane', 'wean', 'abets', 'baste', 'beast', 'beats', 'betas', 'acres', 'cares', 'races', 'scare', 'angel', 'angle', 'glean', 'alert', 'alter', 'later', 'airmen', 'marine', 'remain', 'aligned', 'dealing', 'leading', 'actors', 'castor', 'costar', 'antler', 'learnt', 'rental', 'alerted', 'altered', 'related', 'treadle', 'actress', 'casters', 'recasts', 'allergy', 'gallery', 'largely', 'regally']
        actual_val = get_most_anagrams(words)
        expected_val = ["abets"]
        self.assertEqual(actual_val, expected_val)

    @weight(1)
    @number("3.3")
    def test_3(self):
        """get_most_anagrams -  Empty corpus"""
        words = []
        actual_val = get_most_anagrams(words)
        expected_val = []
        self.assertEqual(actual_val, expected_val)

    @weight(1)
    @number("3.4")
    def test_4(self):
        """get_most_anagrams -  No anagrams in corpus"""
        words = ["abed", "allergy", "amen", "anew", "angel", "tap", "treadle"]
        actual_val = get_most_anagrams(words)
        expected_val = []
        self.assertEqual(actual_val, expected_val)

    @weight(1)
    @number("3.5")
    def test_5(self):
        """get_most_anagrams -  Tie for most anagrams and several no anagrams"""
        words = ["rat", "mouse", "tar", "art", "chicken", "stop", "pots", "tops" ]
        actual_val = get_most_anagrams(words)
        expected_val = ['art', 'pots']
        self.assertEqual(actual_val, expected_val)