import py_compile
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from fake import find_heavier_egg_recursive
import math

class TestEx1(unittest.TestCase):
    @weight(1)
    @number("2.1")
    def test_1(self):
        """find_heavier_egg_recursive -  eggsList1 (given in starter code) -- 9 eggs"""
        eggsList = [10, 10, 10, 10, 10, 10, 11, 10, 10]
        actual = find_heavier_egg_recursive(eggsList)
        expected = (6, 2)
        self.assertEqual(actual[0], expected[0])
        self.assertLessEqual(actual[1], expected[1])

    @weight(1)
    @number("2.2")
    def test_2(self):
        """find_heavier_egg_recursive -  eggsList2 (given in starter code) -- 27 eggs"""
        eggsList = [10,10,10,10,10,10,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
        actual = find_heavier_egg_recursive(eggsList)
        expected = (6, 3)
        self.assertEqual(actual[0], expected[0])
        self.assertLessEqual(actual[1], expected[1])


    @weight(1)
    @number("2.3")
    def test_3(self):
        """find_heavier_egg_recursive -  Empty list"""
        eggsList = []
        actual = find_heavier_egg_recursive(eggsList)
        expected = (-1, 0)
        self.assertEqual(actual[0], expected[0])
        self.assertLessEqual(actual[1], expected[1])

    @weight(1)
    @number("2.4")
    def test_4(self):
        """find_heavier_egg_recursive -  No fake eggs -- 81 eggs"""
        eggsList = [5] * 81
        actual = find_heavier_egg_recursive(eggsList)
        expected = (-1, 5)
        self.assertEqual(actual[0], expected[0])
        self.assertLessEqual(actual[1], expected[1])

    @weight(1)
    @number("2.5")
    def test_5(self):
        """find_heavier_egg_recursive -  Fake egg at end of list -- 81 eggs"""
        eggsList = [10] * 80 + [11]
        actual = find_heavier_egg_recursive(eggsList)
        expected = (80, 5)
        self.assertEqual(actual[0], expected[0])
        self.assertLessEqual(actual[1], expected[1])

    @weight(1)
    @number("2.6")
    def test_6(self):
        """find_heavier_egg_recursive -  Fake egg at beginning of list -- 81 eggs"""
        eggsList = [11] + [10] * 80
        actual = find_heavier_egg_recursive(eggsList)
        expected = (0, 4)
        self.assertEqual(actual[0], expected[0])
        self.assertLessEqual(actual[1], expected[1])

    @weight(1)
    @number("2.7")
    def test_7(self):
        """find_heavier_egg_recursive -  Fake egg in middle of list -- 81 eggs"""
        eggsList = [10] * 40 + [11] + [10] * 40
        actual = find_heavier_egg_recursive(eggsList)
        expected = (40, 4)
        self.assertEqual(actual[0], expected[0])
        self.assertLessEqual(actual[1], expected[1])

    @weight(1)
    @number("2.8")
    def test_8(self):
        """find_heavier_egg_recursive - Fake in variety of different lengths and positions"""
        for i in range(1, 5):
            length = int(math.pow(3, i))
            for j in [0, length//2, length-1]:
                basket = [10] * length
                basket[j] = 11
                index, numWeighings = find_heavier_egg_recursive(basket)
                if j == length-1:
                    expectedWeighings = i+1
                else:
                    expectedWeighings = i
                self.assertEqual(index, j)
                self.assertLessEqual(numWeighings, expectedWeighings)

    @weight(1)
    @number("2.9")
    def test_9(self):
        """find_heavier_egg_recursive - No fake in variety of different lengths"""
        for i in range(1, 5):
            length = int(math.pow(3, i))
            basket = [10] * length
            index, numWeighings = find_heavier_egg_recursive(basket)
            self.assertEqual(index, -1)
            self.assertLessEqual(numWeighings, i+1)
