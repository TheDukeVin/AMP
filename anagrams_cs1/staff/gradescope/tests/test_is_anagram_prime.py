import py_compile
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from anagrams import is_anagram_prime

class TestEx1(unittest.TestCase):
  @weight(1)
  @number("3.1")
  def test_1(self):
      """is_anagram_prime -  Basic True"""
      val = is_anagram_prime("baste", "beast")
      self.assertEqual(val, True)

  @weight(1)
  @number("3.2")
  def test_2(self):
      """is_anagram_prime -  Basic True with mixed Capitalization"""
      val = is_anagram_prime("Allergy", "reGaLLy")
      self.assertEqual(val, True)

  @weight(1)
  @number("3.3")
  def test_3(self):
      """is_anagram_prime -  Basic False"""
      val = is_anagram_prime("baste", "beaft")
      self.assertEqual(val, False)

  @weight(1)
  @number("3.4")
  def test_4(self):
      """is_anagram_prime -  Identical Words"""
      val = is_anagram_prime("road", "road")
      self.assertEqual(val, False)

  @weight(1)
  @number("3.5")
  def test_5(self):
     """is_anagram_prime -  Identical Words with Mixed Capitalization"""
     val = is_anagram_prime("road", "Road")
     self.assertEqual(val, False)

  @weight(1)
  @number("3.6")
  def test_6(self):
        """is_anagram_prime -  Nearly Identical Words"""
        val = is_anagram_prime("abed", "abet")
        self.assertEqual(val, False)

  @weight(1)
  @number("3.7")
  def test_7(self):
        """is_anagram_prime -  Nearly Anagram: repeated letters"""
        val = is_anagram_prime("odd", "do")
        self.assertEqual(val, False)

  @weight(1)
  @number("3.8")
  def test_8(self):
        """is_anagram_prime -  1 letter words"""
        val = is_anagram_prime("a", "a")
        self.assertEqual(val, False)

  @weight(1)
  @number("3.9")
  def test_9(self):
        """is_anagram_prime -  Almost Anagrams: Plural"""
        val = is_anagram_prime("castor", "costars")
        self.assertEqual(val, False)

  @weight(1)
  @number("3.10")
  def test_10(self):
        """is_anagram_prime -  Two Empty Strings"""
        val = is_anagram_prime("", "")
        self.assertEqual(val, False)

  @weight(1)
  @number("3.11")
  def test_11(self):
      """is_anagram_prime -  1 word not in valid word list"""
      val = is_anagram_prime("baste", "bteas")
      self.assertEqual(val, False)

  @weight(1)
  @number("3.12")
  def test_12(self):
      """is_anagram_prime -  2 words not in valid word list"""
      val = is_anagram_prime("ftvx", "xvtf")
      self.assertEqual(val, False)

  @weight(1)
  @number("3.13")
  def test_13(self):
      """is_anagram_prime - 2 near-anagrams"""
      val = is_anagram_prime("rattles", "realist")
      self.assertEqual(val, False)