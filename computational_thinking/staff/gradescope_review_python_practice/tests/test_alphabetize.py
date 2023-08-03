import py_compile
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from review_python_practice import alphabetize

class TestEx1(unittest.TestCase):
  @weight(1)
  @number("4.1")
  def test_amp(self):
      """alphabetize -  Basic message"""
      val = alphabetize([0, 12, 15])
      self.assertEqual(val, "amp")

  @weight(1)
  @number("4.2")
  def test_empty(self):
      """alphabetize -  Empty list"""
      val = alphabetize([])
      self.assertEqual(val, "")

  @weight(1)
  @number("4.3")
  def test_banana(self):
      """alphabetize - Message with repeated letters"""
      val = alphabetize([1, 0, 13, 0, 13, 0])
      self.assertEqual(val, "banana")

  @weight(1)
  @number("4.4")
  def test_a(self):
      """alphabetize - First index check"""
      val = alphabetize([0])
      self.assertEqual(val, "a")

  @weight(1)
  @number("4.5")
  def test_z(self):
      """alphabetize - Last index check"""
      val = alphabetize([25])
      self.assertEqual(val, "z")
