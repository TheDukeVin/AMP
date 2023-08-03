import py_compile
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from fake import find_lighter_or_heavier_egg
import math


class TestEx1(unittest.TestCase):
    @weight(1)
    @number("3.1")
    def test_1(self):
        """find_lighter_or_heavier_egg -  basket1 (given in starter code) -- 9 eggs"""
        basket = [10, 10, 10, 10, 10, 10, 11, 10, 10]
        type, index = find_lighter_or_heavier_egg(basket)
        desiredtype = "heavier"
        desiredIndex = 6
        expected = (desiredtype, desiredIndex)
        actual = (type, index)
        self.assertEqual(actual, expected)

    @weight(1)
    @number("3.2")
    def test_2(self):
        """find_lighter_or_heavier_egg -  basket2 (given in starter code) -- 27 eggs"""
        basket = [10,10,10,10,10,10,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
        type, index = find_lighter_or_heavier_egg(basket)
        desiredtype = "heavier"
        desiredIndex = 6
        expected = (desiredtype, desiredIndex)
        actual = (type, index)
        self.assertEqual(actual, expected)

    @weight(1)
    @number("3.3")
    def test_3(self):
        """find_lighter_or_heavier_egg -  basket1 (given in starter code) but fake is light -- 9 eggs"""
        basket = [10, 10, 10, 10, 10, 10, 9, 10, 10]
        type, index = find_lighter_or_heavier_egg(basket)
        desiredtype = "lighter"
        desiredIndex = 6
        expected = (desiredtype, desiredIndex)
        actual = (type, index)
        self.assertEqual(actual, expected)

    @weight(1)
    @number("3.4")
    def test_4(self):
        """find_lighter_or_heavier_egg -  basket2 (given in starter code) but fake is light -- 27 eggs"""
        basket = [10,10,10,10,10,10,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
        type, index = find_lighter_or_heavier_egg(basket)
        desiredtype = "lighter"
        desiredIndex = 6
        expected = (desiredtype, desiredIndex)
        actual = (type, index)
        self.assertEqual(actual, expected)

    @weight(1)
    @number("3.5")
    def test_5(self):
        """find_lighter_or_heavier_egg -  Empty list"""
        basket = []
        type, index = find_lighter_or_heavier_egg(basket)
        desiredtype = "no fake"
        desiredIndex = -1
        expected = (desiredtype, desiredIndex)
        actual = (type, index)
        self.assertEqual(actual, expected)

    @weight(1)
    @number("3.6")
    def test_6(self):
        """find_lighter_or_heavier_egg -  No fake eggs -- 81 eggs"""
        basket = [5] * 81
        type, index = find_lighter_or_heavier_egg(basket)
        expected = ("no fake", -1)
        self.assertEqual((type, index), expected)

    @weight(1)
    @number("3.7")
    def test_7(self):
        """find_lighter_or_heavier_egg -  Fake egg (heavy) at end of list -- 81 eggs"""
        basket = [10] * 80 + [11]
        type, index = find_lighter_or_heavier_egg(basket)
        desiredtype = "heavier"
        desiredIndex = 80
        expected = (desiredtype, desiredIndex)
        actual = (type, index)
        # expected = (True, 81, 5)
        self.assertEqual(actual, expected)

    @weight(1)
    @number("3.8")
    def test_8(self):
        """find_lighter_or_heavier_egg -  Fake egg (light) at end of list -- 81 eggs"""
        basket = [10] * 80 + [9]
        type, index = find_lighter_or_heavier_egg(basket)
        desiredtype = "lighter"
        desiredIndex = 80
        expected = (desiredtype, desiredIndex)
        actual = (type, index)
        self.assertEqual(actual, expected)

    @weight(1)
    @number("3.9")
    def test_9(self):
        """find_lighter_or_heavier_egg -  Fake egg (heavy) at beginning of list -- 81 eggs"""
        basket = [11] + [10] * 80
        type, index = find_lighter_or_heavier_egg(basket)
        desiredtype = "heavier"
        desiredIndex = 0
        expected = (desiredtype, desiredIndex)
        actual = (type, index)
        self.assertEqual(actual, expected)

    @weight(1)
    @number("3.10")
    def test_10(self):
        """find_lighter_or_heavier_egg -  Fake egg (light) at beginning of list -- 81 eggs"""
        basket = [9] + [10] * 80
        type, index = find_lighter_or_heavier_egg(basket)
        desiredtype = "lighter"
        desiredIndex = 0
        expected = (desiredtype, desiredIndex)
        actual = (type, index)
        self.assertEqual(actual, expected)

    @weight(1)
    @number("3.11")
    def test_11(self):
        """find_lighter_or_heavier_egg -  Fake egg (heavy) in middle of list -- 81 eggs"""
        basket = [10] * 40 + [11] + [10] * 40
        type, index = find_lighter_or_heavier_egg(basket)
        desiredtype = "heavier"
        desiredIndex = 40
        expected = (desiredtype, desiredIndex)
        actual = (type, index)
        self.assertEqual(actual, expected)

    @weight(1)
    @number("3.12")
    def test_12(self):
        """find_lighter_or_heavier_egg -  Fake egg (light) in middle of list -- 81 eggs"""
        basket = [10] * 40 + [9] + [10] * 40
        type, index = find_lighter_or_heavier_egg(basket)
        desiredtype = "lighter"
        desiredIndex = 40
        expected = (desiredtype, desiredIndex)
        actual = (type, index)
        self.assertEqual(actual, expected)

    @weight(1)
    @number("3.13")
    def test_13(self):
        """find_lighter_or_heavier_egg - Heavier egg in a list of 3 eggs"""
        basket = [11, 10, 10]
        type, index1 = find_lighter_or_heavier_egg(basket)
        self.assertEqual(index1, 0)
        self.assertEqual(type, "heavier")

    @weight(1)
    @number("3.14")
    def test_14(self):
        """find_lighter_or_heavier_egg - No fakes in a variety of lengths and positions"""
        for i in range(1, 5):
            length = int(math.pow(3, i))
            basket = [5] * length
            type, index = find_lighter_or_heavier_egg(basket)
            self.assertEqual(index, -1)
            self.assertEqual(type, "no fake")

    @weight(1)
    @number("3.15")
    def test_15(self):
        """find_lighter_or_heavier_egg - Lighter egg in a list of 3 eggs"""
        basket = [10, 9, 10]
        type, index1 = find_lighter_or_heavier_egg(basket)
        self.assertEqual(index1, 1)
        self.assertEqual(type, "lighter")
