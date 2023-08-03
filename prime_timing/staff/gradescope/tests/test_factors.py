import py_compile
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from prime_timing import get_factors

class TestEx1(unittest.TestCase):
  @weight(1)
  @number("0.1")
  def test_1(self):
      """get_factors: Composite Number"""
      factorList = get_factors(12)
      self.assertEqual(factorList, [1, 2, 3, 4, 6, 12])

  @weight(1)
  @number("0.2")
  def test_2(self):
      """get_factors: Prime Number"""
      factorList = get_factors(17)
      self.assertEqual(factorList, [1, 17])

  @weight(1)
  @number("0.3")
  def test_3(self):
      """get_factors: 1"""
      factorList = get_factors(1)
      self.assertEqual(factorList, [1])

  @weight(1)
  @number("0.4")
  def test_4(self):
      """get_factors: 0"""
      factorList = get_factors(0)
      self.assertEqual(factorList, [])

  @weight(1)
  @number("0.5")
  def test_5(self):
     """get_factors: Negative Number"""
     factorList = get_factors(-12)
     self.assertEqual(factorList, [])

  @weight(1)
  @number("0.6")
  def test_6(self):
        """get_factors: Composite Number with Duplicate Factor"""
        factorList = get_factors(36)
        self.assertEqual(factorList, [1, 2, 3, 4, 6, 9, 12, 18, 36])