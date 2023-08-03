import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from conform import please_flip_streamlined


class TestStreamlined(unittest.TestCase):
    @weight(1)
    @number("2.1")
    def test_caps_1(self):
        """Please Flip Streamlined-  Basic Caps 1"""
        caps = ["F", "F", "B", "B", "B", "F", "B", "B", "B", "F", "F", "B", "F"]
        val = please_flip_streamlined(caps)
        self.assertEqual(val, ['People in positions 2 through 4 flip your caps!',
                                'People in positions 6 through 8 flip your caps!',
                                'Person in position 11 flip your cap!'])

    @weight(1)
    @number("2.2")
    def test_caps_2(self):
        """Please Flip Streamlined-  Basic Caps 2"""
        caps = ["F", "F", "B", "B", "B", "F", "B", "B", "B", "F", "F", "F", "F"]
        val = please_flip_streamlined(caps)
        self.assertEqual(val, ['People in positions 2 through 4 flip your caps!',
                                'People in positions 6 through 8 flip your caps!'])

    @weight(1)
    @number("2.3")
    def test_caps_3(self):
        """Please Flip Streamlined-  Alternating Caps, Even List length"""
        caps = ["F", "B", "F", "B", "F", "B"]
        val = please_flip_streamlined(caps)
        self.assertTrue(val in (['Person in position 0 flip your cap!',
                                'Person in position 2 flip your cap!',
                                'Person in position 4 flip your cap!'],
                                ['Person in position 1 flip your cap!',
                                'Person in position 3 flip your cap!',
                                'Person in position 5 flip your cap!']))

    @weight(1)
    @number("2.4")
    def test_caps_4(self):
        """Please Flip Streamlined-  Alternating Caps, Odd List length"""
        caps = ["F", "B", "F", "B", "F"]
        val = please_flip_streamlined(caps)
        self.assertEqual(val, ['Person in position 1 flip your cap!',
                               'Person in position 3 flip your cap!'])

    @weight(1)
    @number("2.5")
    def test_caps_5(self):
        """Please Flip Streamlined-  Same Caps"""
        caps = ["F", "F", "F", "F", "F"]
        val = please_flip_streamlined(caps)
        self.assertEqual(len(val), 0)

    @weight(1)
    @number("2.6")
    def test_caps_6(self):
        """Please Flip Streamlined-  Same Caps"""
        caps = ["B", "B", "B", "B", "B"]
        val = please_flip_streamlined(caps)
        self.assertEqual(len(val), 0)

    @weight(1)
    @number("2.7")
    def test_caps_7(self):
        """Please Flip Streamlined-  Empty List"""
        caps = []
        val = please_flip_streamlined(caps)
        self.assertEqual(len(val), 0)
