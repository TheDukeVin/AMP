import py_compile
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from fake import find_heavier_egg_nonrecursive
import math

class TestEx1(unittest.TestCase):
    @weight(1)
    @number("1.1")
    def test_1(self):
        """find_heavier_egg_nonrecursive -  eggsList1 (given in starter code) -- 9 eggs"""
        basket = [10, 10, 10, 10, 10, 10, 11, 10, 10]
        actual = find_heavier_egg_nonrecursive(basket)
        expected = (6, 2)
        self.assertEqual(actual[0], expected[0])
        self.assertLessEqual(actual[1], expected[1])
        
    @weight(1)
    @number("1.2")
    def test_2(self):
        """find_heavier_egg_nonrecursive -  eggsList2 (given in starter code) -- 27 eggs"""
        basket = [10,10,10,10,10,10,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
        actual = find_heavier_egg_nonrecursive(basket)
        expected = (6, 3)
        self.assertEqual(actual[0], expected[0])
        self.assertLessEqual(actual[1], expected[1])

    @weight(1)
    @number("1.3")
    def test_3(self):
        """find_heavier_egg_nonrecursive -  Empty list"""
        basket = []
        actual = find_heavier_egg_nonrecursive(basket)
        expected = (-1, 0)
        self.assertEqual(actual[0], expected[0])
        self.assertLessEqual(actual[1], expected[1])

    @weight(1)
    @number("1.4")
    def test_4(self):
        """find_heavier_egg_nonrecursive -  No fake eggs -- 81 eggs"""
        basket = [5] * 81
        actual = find_heavier_egg_nonrecursive(basket)
        expected = (-1, 5)
        self.assertEqual(actual[0], expected[0])
        self.assertLessEqual(actual[1], expected[1])

    @weight(1)
    @number("1.5")
    def test_5(self):
        """find_heavier_egg_nonrecursive -  Fake egg at end of list -- 81 eggs"""
        basket = [10] * 80 + [11]
        actual = find_heavier_egg_nonrecursive(basket)
        expected = (80, 5)
        self.assertEqual(actual[0], expected[0])
        self.assertLessEqual(actual[1], expected[1])

    @weight(1)
    @number("1.6")
    def test_6(self):
        """find_heavier_egg_nonrecursive -  Fake egg at beginning of list -- 81 eggs"""
        basket = [11] + [10] * 80
        actual = find_heavier_egg_nonrecursive(basket)
        expected = (0, 4)
        self.assertEqual(actual[0], expected[0])
        self.assertLessEqual(actual[1], expected[1])

    @weight(1)
    @number("1.7")
    def test_7(self):
        """find_heavier_egg_nonrecursive -  Fake egg in middle of list -- 81 eggs"""
        basket = [10] * 40 + [11] + [10] * 40
        actual = find_heavier_egg_nonrecursive(basket)
        expected = (40, 4)
        self.assertEqual(actual[0], expected[0])
        self.assertLessEqual(actual[1], expected[1])

    @weight(1)
    @number("1.8")
    def test_8(self):
        """find_heavier_egg_nonrecursive - Fake in variety of different lengths and positions"""
        for i in range(1, 5):
            length = int(math.pow(3, i))
            for j in [0, length//2, length-1]:
                basket = [10] * length
                basket[j] = 11
                if j == length-1:
                    expectedWeighings = i+1
                else:
                    expectedWeighings = i
                index, numWeighings = find_heavier_egg_nonrecursive(basket)
                self.assertEqual(index, j)
                self.assertLessEqual(numWeighings, expectedWeighings)

    @weight(1)
    @number("1.9")
    def test_9(self):
        """find_heavier_egg_nonrecursive - No fake in variety of different lengths"""
        for i in range(1, 5):
            length = int(math.pow(3, i))
            basket = [10] * length
            index, numWeighings = find_heavier_egg_nonrecursive(basket)
            self.assertEqual(index, -1)
            self.assertLessEqual(numWeighings, i+1)
