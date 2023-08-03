import py_compile
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from anagram_explorer import get_prime_hash_dict

class TestEx1(unittest.TestCase):
    @weight(1)
    @number("2.1")
    def test_1(self):
        """get_prime_hash_dict -  Short list (2 sets of anagrams)"""
        words = ["abed", "abled", "bade", "baled", "bead", "blade"]
        val = get_prime_hash_dict(words)
        desired_val = {
            462: ["abed", "bade", "bead"],
            17094: ["abled", "baled", "blade"],
        }
        self.assertEqual(val, desired_val)

    @weight(1)
    @number("2.2")
    def test_2(self):
        """get_prime_hash_dict -  Long list (20 sets of anagrams); given in the starter code"""
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
        val = get_prime_hash_dict(words)
        desired_val = {
            462: ["abed", "bade", "bead"],
            4686: ["abet", "beat", "beta"],
            313962: ["abets", "baste", "beast", "beats", "betas"],
            31098: ["abut", "tabu", "tuba"],
            4510: ["acme", "came", "mace"],
            6710: ["acre", "care", "race"],
            449570: ["acres", "cares", "races", "scare"],
            136383190: ["actors", "castor", "costar"],
            2138604490: ["actress", "casters", "recasts"],
            54416758: ["airmen", "marine", "remain"],
            3525434: ["alert", "alter", "later"],
            271458418: ["alerted", "altered", "related", "treadle"],
            54538: ["ales", "leas", "sale", "seal"],
            95800474: ["aligned", "dealing", "leading"],
            3029539502: ["allergy", "gallery", "largely", "regally"],
            38786: ["amen", "mane", "mean", "name"],
            78518: ["anew", "wane", "wean"],
            595034: ["angel", "angle", "glean"],
            151593662: ["antler", "learnt", "rental"],
            7526: ["apt", "pat", "tap"],
        }
        self.assertEqual(val, desired_val)

    @weight(1)
    @number("2.3")
    def test_3(self):
        """get_prime_hash_dict -  Empty words list"""
        words = []
        val = get_prime_hash_dict(words)
        self.assertEqual(val, {})

    @weight(1)
    @number("2.4")
    def test_4(self):
        """get_prime_hash_dict -  No anagrams (each list has length 1)"""
        words = ["abed", "allergy", "amen", "anew", "angel", "tap", "treadle"]
        val = get_prime_hash_dict(words)
        desired_val = {
            462: ["abed"],
            3029539502: ["allergy"],
            38786: ["amen"],
            78518: ["anew"],
            595034: ["angel"],
            7526: ["tap"],
            271458418: ["treadle"],
        }
        self.assertEqual(val, desired_val)

    @weight(1)
    @number("2.5")
    def test_5(self):
        """get_prime_hash_dict -  Mix of many anagrams and no anagrams"""
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
        val = get_prime_hash_dict(words)
        desired_val = {
            30: ["abc", "acb", "bac", "bca", "cab", "cba"],
            210: [
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
            330: ["abce"],
            50: ["acc", "cac", "cca"],
        }
        self.assertEqual(val, desired_val)

    @weight(1)
    @number("2.6")
    def test_6(self):
        """get_prime_hash_dict -  corpus with 1 word"""
        words = ["rat"]
        val = get_prime_hash_dict(words)
        self.assertEqual(val, {8662: ["rat"]})