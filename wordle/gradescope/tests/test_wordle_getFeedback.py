import py_compile
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from wordle import get_feedback

class TestEx1(unittest.TestCase):

  @weight(1)
  @number("1.1")
  def test_1(self):
      """get_feedback - AMBER presentation example"""
      secret_word = "AMBER"
      guess = "BRAKE"
      print(f"Guess:{guess} Secret Word:{secret_word}")
      val = get_feedback(guess, secret_word)
      self.assertEqual(val, "bra-e")

  @weight(1)
  @number("1.2")
  def test_2(self):
      """get_feedback - MOTTO presentation example"""
      secret_word = "MOTTO"
      guess = "TOOTH"
      print(f"Guess:{guess} Secret Word:{secret_word}")
      val = get_feedback(guess, secret_word)
      self.assertEqual(val, "tOoT-")

  @weight(1)
  @number("1.3")
  def test_3(self):
      """get_feedback - Documentation example #1"""
      secret_word = "EATEN"
      guess = "LEVER"
      val = get_feedback(guess, secret_word)
      self.assertEqual(val, "-e-E-")

  @weight(1)
  @number("1.4")
  def test_4(self):
       """get_feedback - Documentation example #2"""
       secret_word = "LOWER"
       guess = "LEVER"
       val = get_feedback(guess, secret_word)
       self.assertEqual(val, "L--ER")

  @weight(1)
  @number("1.5")
  def test_5(self):
      """get_feedback - Documentation example #3"""
      secret_word = "MADAM"
      guess = "MOMMY"
      val = get_feedback(guess, secret_word)
      self.assertEqual(val, "M-m--")

  @weight(1)
  @number("1.6")
  def test_6(self):
      """get_feedback - Documentation example #4"""
      secret_word = "ARGUE"
      guess = "MOTTO"
      val = get_feedback(guess, secret_word)
      self.assertEqual(val, "-----")

  @weight(1)
  @number("1.7")
  def test_7(self):
        """get_feedback - Guess is secret word"""
        secret_word = "MOTTO"
        guess = "MOTTO"
        val = get_feedback(guess, secret_word)
        self.assertEqual(val, "MOTTO")

  @weight(1)
  @number("1.8")
  def test_8(self):
        """get_feedback - Guess is lowercase"""
        secret_word = "MADAM"
        guess = "mommy"
        val = get_feedback(guess, secret_word)
        self.assertEqual(val, "M-m--")

  @weight(1)
  @number("1.9")
  def test_9(self):
        """get_feedback - Guess and secret word are anagrams"""
        secret_word = "CRATE"
        guess = "TRACE"
        val = get_feedback(guess, secret_word)
        self.assertEqual(val, "tRAcE")

  @weight(1)
  @number("1.10")
  def test_10(self):
        """get_feedback - Guess and secret word are anagrams with no shared letter positions"""
        secret_word = "ANGLE"
        guess = "GLEAN"
        val = get_feedback(guess, secret_word)
        self.assertEqual(val, "glean")