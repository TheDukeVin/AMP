import py_compile
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from anagrams import top_level_checks

class TestEx1(unittest.TestCase):
  @weight(1)
  @number("1.1")
  def test_1(self):
      """top_level_checks -  Returns lowercased words"""
      _, lower1, _ = top_level_checks("ATE", "eAt")
      self.assertEqual(lower1, "ate")

  @weight(1)
  @number("1.2")
  def test_2(self):
      """top_level_checks -  Returns False if words are identical"""
      result, _, _ = top_level_checks("banana", "banana")
      self.assertEqual(result, False)

  @weight(1)
  @number("1.3")
  def test_3(self):
      """top_level_checks -  Returns False if words are identical but with mixed capitalization"""
      result, _, _ = top_level_checks("aTe", "ATE")
      self.assertEqual(result, False)

  @weight(1)
  @number("1.4")
  def test_4(self):
      """top_level_checks -  Returns False if words are different lengths"""
      result, _, _ = top_level_checks("banana", "bana")
      self.assertEqual(result, False)