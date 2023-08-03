import py_compile
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from review_python_practice import fizz_buzz

class TestEx1(unittest.TestCase):
  @weight(1)
  @number("1.1")
  def test_0(self):
      """fizz_buzz -  FizzBuzz with 0 numbers"""
      val = fizz_buzz(0)
      self.assertEqual(val, [])

  @weight(1)
  @number("1.2")
  def test_15(self):
      """fizz_buzz -  FizzBuzz with 15 numbers"""
      val = fizz_buzz(15)
      self.assertEqual(val, [1, 2, "fizz", 4, "buzz", "fizz", 7, 8, "fizz", "buzz", 11, "fizz", 13, 14, "fizzbuzz"])