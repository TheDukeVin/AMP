import py_compile
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from review_python_practice import alternating

class TestEx1(unittest.TestCase):
  @weight(1)
  @number("2.1")
  def test_0(self):
      """alternating -  Empty sequence"""
      val = alternating(0)
      self.assertEqual(val, [])

  @weight(1)
  @number("2.2")
  def test_one(self):
      """alternating -  One element sequence"""
      val = alternating(1)
      self.assertEqual(val, [1])

  @weight(1)
  @number("2.3")
  def test_10(self):
      """alternating -  General case"""
      val = alternating(10)
      self.assertEqual(val, [1, -2, 3, -4, 5, -6, 7, -8, 9, -10])

  @weight(1)
  @number("2.4")
  def test_odd(self):
      """alternating -  Odd number of terms"""
      val = alternating(3)
      self.assertEqual(val, [1, -2, 3])

  @weight(1)
  @number("2.5")
  def test_even(self):
      """alternating -  Even number of terms"""
      val = alternating(4)
      self.assertEqual(val, [1, -2, 3, -4])
