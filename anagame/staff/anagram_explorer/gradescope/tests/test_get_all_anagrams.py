import py_compile
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from anagram_explorer import get_all_anagrams

class TestEx1(unittest.TestCase):
    @weight(1)
    @number("4.1")
    def test_1(self):
        """get_all_anagrams -  Short list (2 sets of anagrams)"""
        words = ["abed", "abled", "bade", "baled", "bead", "blade"]
        val = get_all_anagrams(words)
        expected_val = {"abed", "bade", "bead","abled", "baled", "blade"}
        self.assertEqual(val, expected_val)

    @weight(1)
    @number("4.2")
    def test_2(self):
        """get_all_anagrams -  Long list (20 sets of anagrams); given in the starter code"""
        words = [
            "abed",
            "abet",
            "abets",
            "abut",
            "acme",
            "acre",
            "acres",
            "actors",
            "actress",
            "airmen",
            "alert",
            "alerted",
            "ales",
            "aligned",
            "allergy",
            "alter",
            "altered",
            "amen",
            "anew",
            "angel",
            "angle",
            "antler",
            "apt",
            "bade",
            "baste",
            "bead",
            "beast",
            "beat",
            "beats",
            "beta",
            "betas",
            "came",
            "care",
            "cares",
            "casters",
            "castor",
            "costar",
            "dealing",
            "gallery",
            "glean",
            "largely",
            "later",
            "leading",
            "learnt",
            "leas",
            "mace",
            "mane",
            "marine",
            "mean",
            "name",
            "pat",
            "race",
            "races",
            "recasts",
            "regally",
            "related",
            "remain",
            "rental",
            "sale",
            "scare",
            "seal",
            "tabu",
            "tap",
            "treadle",
            "tuba",
            "wane",
            "wean",
        ]
        val = get_all_anagrams(words)
        expected_val = {
            "abed", "bade", "bead","abet", "beat", "beta",
            "abets", "baste", "beast", "beats", "betas",
            "abut", "tabu", "tuba",
            "acme", "came", "mace",
            "acre", "care", "race",
            "acres", "cares", "races", "scare",
            "actors", "castor", "costar",
            "actress", "casters", "recasts",
            "airmen", "marine", "remain",
            "alert", "alter", "later","alerted", "altered", "related", "treadle","ales", "leas", "sale", "seal","aligned", "dealing", "leading","allergy", "gallery", "largely", "regally","amen", "mane", "mean", "name","anew", "wane", "wean","angel", "angle", "glean","antler", "learnt", "rental","apt", "pat", "tap",
        }
        self.assertEqual(val, expected_val)

    @weight(1)
    @number("4.3")
    def test_3(self):
        """get_all_anagrams -  Empty words list"""
        words = []
        val = get_all_anagrams(words)
        expected_val=set()
        self.assertEqual(val, expected_val)

    @weight(1)
    @number("4.4")
    def test_4(self):
        """get_all_anagrams -  No anagrams (each list has length 1)"""
        words = ["abed", "allergy", "amen", "anew", "angel", "tap", "treadle"]
        val = get_all_anagrams(words)
        expected_val=set()
        self.assertEqual(val, expected_val)

    @weight(1)
    @number("4.5")
    def test_5(self):
        """get_all_anagrams -  Mix of many anagrams and no anagrams"""
        words = [
            "abc",
            "abcd",
            "abce",
            "abdc",
            "acb",
            "acbd",
            "acdb",
            "acc",
            "bac",
            "bacd",
            "badc",
            "bca",
            "bcad",
            "bcda",
            "cab",
            "cabd",
            "cadb",
            "cac",
            "cba",
            "cbad",
            "cbda",
            "cca",
        ]
        val = get_all_anagrams(words)
        expected_val = {
            "abc", "acb", "bac", "bca", "cab", "cba",
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
                "cbda","acc", "cac", "cca"
        }
        self.assertEqual(val, expected_val)

    @weight(1)
    @number("4.6")
    def test_6(self):
        """get_all_anagrams -  corpus with 1 word"""
        words = ["rat"]
        val = get_all_anagrams(words)
        expected_val=set()

        self.assertEqual(val, expected_val)

