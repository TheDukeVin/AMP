import py_compile
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from review_python_practice import fizz_buzz, alternating, xor, alphabetize, reverse

class TestEx1(unittest.TestCase):
  @weight(1)
  @number("3.1")
  def test_TrueTrue(self):
      """xor -  xor both True"""
      val = xor(True, True)
      self.assertEqual(val, False)

  @weight(1)
  @number("3.2")
  def test_FalseFalse(self):
      """xor -  xor both False"""
      val = xor(False, False)
      self.assertEqual(val, False)

  @weight(1)
  @number("3.3")
  def test_TrueFalse(self):
      """xor -  xor True False"""
      val = xor(True, False)
      self.assertEqual(val, True)

  @weight(1)
  @number("3.4")
  def test_FalseTrue(self):
      """xor -  xor False True"""
      val = xor(False, True)
      self.assertEqual(val, True)