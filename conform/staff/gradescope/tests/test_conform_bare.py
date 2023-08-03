import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from conform import please_flip_bare


class TestBare(unittest.TestCase):
    @weight(1)
    @number("4.1")
    def test_barehead_caps_1(self):
        """Bareheaded - Barehead and Caps 1"""
        caps = ["F", "F", "B", "H", "B", "F", "B", "B", "B", "F", "H", "F", "F"]
        val = please_flip_bare(caps)
        self.assertEqual(val, ['Person in position 2 flip your cap!',
                               'Person in position 4 flip your cap!',
                               'People in positions 6 through 8 flip your caps!'])

    @weight(1)
    @number("4.2")
    def test_barehead_caps_2(self):
        """Bareheaded - Barehead and Caps 2"""
        caps = ["B", "B", "F", "H", "F", "B", "F", "F", "F", "B", "H", "B", "H"]
        val = please_flip_bare(caps)
        self.assertEqual(val, ['Person in position 2 flip your cap!',
                               'Person in position 4 flip your cap!',
                               'People in positions 6 through 8 flip your caps!'])

    @weight(1)
    @number("4.3")
    def test_barehead_caps_3(self):
        """Bareheaded - Just F and H"""
        caps = ["F", "H", "H", "H", "F"]
        val = please_flip_bare(caps)
        self.assertEqual(len(val), 0)

    @weight(1)
    @number("4.4")
    def test_barehead_caps_4(self):
        """Bareheaded - Barehead and Caps 3"""
        caps = ["F", "F", "B", "H", "B", "B", "H", "F", "F"]
        val = please_flip_bare(caps)
        self.assertTrue(val in (['People in positions 0 through 1 flip your caps!',
                                 'People in positions 7 through 8 flip your caps!'],
                                ['Person in position 2 flip your cap!',
                                 'People in positions 4 through 5 flip your caps!']))

    @weight(1)
    @number("4.5")
    def test_barehead_caps_5(self):
        """Bareheaded - Just Bareheaded People"""
        caps = ["H", "H", "H", "H", "H", "H", "H"]
        val = please_flip_bare(caps)
        self.assertEqual(len(val), 0)

    @weight(1)
    @number("4.6")
    def test_barehead_caps_6(self):
        """Bareheaded - Same Caps"""
        caps = ["F", "F", "F", "F", "F"]
        val = please_flip_bare(caps)
        self.assertEqual(len(val), 0)

    @weight(1)
    @number("4.7")
    def test_barehead_caps_7(self):
        """Bareheaded - Same Caps"""
        caps = ["B", "B", "B", "B", "B"]
        val = please_flip_bare(caps)
        self.assertEqual(len(val), 0)

    @weight(1)
    @number("4.8")
    def test_barehead_caps_8(self):
        """One Bareheaded amongst Same Caps"""
        caps = ["F", "H", "F", "F", "F"]
        val = please_flip_bare(caps)
        self.assertEqual(len(val), 0)

    @weight(1)
    @number("4.9")
    def test_barehead_caps_9(self):
        """One Bareheaded amongst Same Caps"""
        caps = ["B", "B", "H", "B", "B"]
        val = please_flip_bare(caps)
        self.assertEqual(len(val), 0)

    @weight(1)
    @number("4.10")
    def test_barehead_caps_10(self):
        """One Alt"""
        caps = ["F", "F", "B", "H", "B"]
        val = please_flip_bare(caps)
        self.assertEqual(val, ['People in positions 0 through 1 flip your caps!'])

    @weight(1)
    @number("4.11")
    def test_barehead_caps_11(self):
        """Bareheaded changes"""
        caps = ["F", "B", "F", "B", "H", "B", "F"]
        val = please_flip_bare(caps)
        self.assertTrue(val in (['Person in position 0 flip your cap!',
                                 'Person in position 2 flip your cap!',
                                 'Person in position 6 flip your cap!'],
                                ['Person in position 1 flip your cap!',
                                 'Person in position 3 flip your cap!',
                                 'Person in position 5 flip your cap!']))

    @weight(1)
    @number("4.12")
    def test_barehead_caps_12(self):
        """Difficult Bareheaded"""
        caps = ["F", "B", "B", "B", "H", "H", "B", "B", "B", "H", "B", "F"]
        val = please_flip_bare(caps)
        self.assertEqual(val, ['Person in position 0 flip your cap!',
                               'Person in position 11 flip your cap!'])

    @weight(1)
    @number("4.13")
    def test_barehead_caps_13(self):
        """Difficult Bareheaded"""
        caps = ["F", "H", "F", "B", "B", "B", "H", "H", "B", "F", "F", "H", "B", "F"]
        val = please_flip_bare(caps)
        self.assertEqual(val, ['People in positions 3 through 5 flip your caps!',
                               'Person in position 8 flip your cap!',
                               'Person in position 12 flip your cap!'])
