import py_compile
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from anagram_explorer import get_sorted_hash_dict

class TestEx1(unittest.TestCase):
    @weight(1)
    @number("1.1")
    def test_1(self):
        """get_sorted_hash_dict -  Short list (2 sets of anagrams)"""
        words = ["abed", "abled", "bade", "baled", "bead", "blade"]
        val = get_sorted_hash_dict(words)
        desired_val = {
            ("a", "b", "d", "e"): ["abed", "bade", "bead"],
            ("a", "b", "d", "e", "l"): ["abled", "baled", "blade"],
        }
        self.assertEqual(val, desired_val)

    @weight(1)
    @number("1.2")
    def test_2(self):
        """get_sorted_hash_dict -  Long list (20 sets of anagrams); given in the starter code"""
        words = ['abed', 'bade', 'bead', 'acme', 'came', 'mace', 'abet', 'beat', 'beta', 'acre', 'care', 'race', 'apt', 'pat', 'tap', 'abut', 'tabu', 'tuba', 'amen', 'mane', 'mean', 'name', 'ales', 'leas', 'sale', 'seal', 'anew', 'wane', 'wean', 'abets', 'baste', 'beast', 'beats', 'betas', 'acres', 'cares', 'races', 'scare', 'angel', 'angle', 'glean', 'alert', 'alter', 'later', 'airmen', 'marine', 'remain', 'aligned', 'dealing', 'leading', 'actors', 'castor', 'costar', 'antler', 'learnt', 'rental', 'alerted', 'altered', 'related', 'treadle', 'actress', 'casters', 'recasts', 'allergy', 'gallery', 'largely', 'regally']

        val = get_sorted_hash_dict(words)
        desired_val = {
            ("a", "b", "d", "e"): ["abed", "bade", "bead"],
            ("a", "b", "e", "t"): ["abet", "beat", "beta"],
            ("a", "b", "e", "s", "t"): ["abets", "baste", "beast", "beats", "betas"],
            ("a", "b", "t", "u"): ["abut", "tabu", "tuba"],
            ("a", "c", "e", "m"): ["acme", "came", "mace"],
            ("a", "c", "e", "r"): ["acre", "care", "race"],
            ("a", "c", "e", "r", "s"): ["acres", "cares", "races", "scare"],
            ("a", "c", "o", "r", "s", "t"): ["actors", "castor", "costar"],
            ("a", "c", "e", "r", "s", "s", "t"): ["actress", "casters", "recasts"],
            ("a", "e", "i", "m", "n", "r"): ["airmen", "marine", "remain"],
            ("a", "e", "l", "r", "t"): ["alert", "alter", "later"],
            ("a", "d", "e", "e", "l", "r", "t"): ["alerted", "altered","related","treadle",],
            ("a", "e", "l", "s"): ["ales", "leas", "sale", "seal"],
            ("a", "d", "e", "g", "i", "l", "n"): ["aligned", "dealing", "leading"],
            ("a", "e", "g", "l", "l", "r", "y"): ["allergy", "gallery", "largely","regally",],
            ("a", "e", "m", "n"): ["amen", "mane", "mean", "name"],
            ("a", "e", "n", "w"): ["anew", "wane", "wean"],
            ("a", "e", "g", "l", "n"): ["angel", "angle", "glean"],
            ("a", "e", "l", "n", "r", "t"): ["antler", "learnt", "rental"],
            ("a", "p", "t"): ["apt", "pat", "tap"],
        }
        self.assertEqual(val, desired_val)

    @weight(1)
    @number("1.3")
    def test_3(self):
        """get_sorted_hash_dict -  Empty words list"""
        words = []
        val = get_sorted_hash_dict(words)
        self.assertEqual(val, {})

    @weight(1)
    @number("1.4")
    def test_4(self):
        """get_sorted_hash_dict -  No anagrams (each list has length 1)"""
        words = ["abed", "allergy", "amen", "anew", "angel", "tap", "treadle"]
        val = get_sorted_hash_dict(words)
        desired_val = {
            ("a", "b", "d", "e"): ["abed"],
            ("a", "e", "g", "l", "l", "r", "y"): ["allergy"],
            ("a", "e", "m", "n"): ["amen"],
            ("a", "e", "n", "w"): ["anew"],
            ("a", "e", "g", "l", "n"): ["angel"],
            ("a", "p", "t"): ["tap"],
            ("a", "d", "e", "e", "l", "r", "t"): ["treadle"],
        }
        self.assertEqual(val, desired_val)

    @weight(1)
    @number("1.5")
    def test_5(self):
        """get_sorted_hash_dict -  Mix of many anagrams and no anagrams"""
        words = ["abc","abcd","abce","abdc","acb","acbd","acdb","acc","bac","bacd","badc","bca","bcad","bcda","cab","cabd","cadb","cac","cba","cbad","cbda","cca"]

        val = get_sorted_hash_dict(words)
        desired_val = {
            ("a", "b", "c"): ["abc", "acb", "bac", "bca", "cab", "cba"],
            ("a", "b", "c", "d"): [
                "abcd",
                "abdc",
                "acbd",
                "acdb",
                "bacd",
                "badc",
                "bcad",
                "bcda",
                "cabd",
                "cadb",
                "cbad",
                "cbda",
            ],
            ("a", "b", "c", "e"): ["abce"],
            ("a", "c", "c"): ["acc", "cac", "cca"],
        }
        self.assertEqual(val, desired_val)

    @weight(1)
    @number("1.6")
    def test_6(self):
        """get_sorted_hash_dict -  corpus with 1 word"""
        words = ["rat"]
        val = get_sorted_hash_dict(words)
        self.assertEqual(val, {("a", "r", "t"): ["rat"]})