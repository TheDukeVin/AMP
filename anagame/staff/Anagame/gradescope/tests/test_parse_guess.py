import py_compile
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from anagame import parse_guess

class TestEx1(unittest.TestCase):
  @weight(1)
  @number("5.1")
  def test_1(self):
      """parse_guess -  Basic Correct"""
      guess = "eat,tea"
      val = parse_guess(guess)
      self.assertEqual(val, ("eat", "tea"))

  @weight(1)
  @number("5.2")
  def test_2(self):
      """parse_guess - Correct, 1 space after comma"""
      guess = "eat, tea"
      val = parse_guess(guess)
      self.assertEqual(val, ("eat", "tea"))

  @weight(1)
  @number("5.3")
  def test_3(self):
      """parse_guess - Correct, Many spaces"""
      guess = " eat , tea "
      val = parse_guess(guess)
      self.assertEqual(val, ("eat", "tea"))

  @weight(1)
  @number("5.4")
  def test_4(self):
       """parse_guess - Incorrect, no comma"""
       guess = "eat tea"
       val = parse_guess(guess)
       self.assertEqual(val, ("", ""))

  @weight(1)
  @number("5.5")
  def test_5(self):
      """parse_guess - Incorrect, multiple commas"""
      guess = "eat, tea,"
      val = parse_guess(guess)
      self.assertEqual(val, ("", ""))

  @weight(1)
  @number("5.6")
  def test_6(self):
      """parse_guess - Incorrect, one word"""
      guess = "eattea"
      val = parse_guess(guess)
      self.assertEqual(val, ("", ""))

  @weight(1)
  @number("5.7")
  def test_7(self):
      """parse_guess - Incorrect, three words"""
      guess = "eat, tea, ate"
      val = parse_guess(guess)
      self.assertEqual(val, ("", ""))

  @weight(1)
  @number("5.8")
  def test_8(self):
      """parse_guess - Basic Correct 2"""
      guess = "stop, pots"
      val = parse_guess(guess)
      self.assertEqual(val, ("stop", "pots"))

  @weight(1)
  @number("5.9")
  def test_9(self):
      """parse_guess - Mystery Correct 1"""
      guess = " stop ,pots"
      val = parse_guess(guess)
      self.assertEqual(val, ("stop", "pots"))

  @weight(1)
  @number("5.10")
  def test_10(self):
      """parse_guess - Mystery Correct 2"""
      guess = "stop    ,pots   "
      val = parse_guess(guess)
      self.assertEqual(val, ("stop", "pots"))
