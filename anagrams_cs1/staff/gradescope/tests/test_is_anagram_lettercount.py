import py_compile
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from anagrams import is_anagram_lettercount

class TestEx1(unittest.TestCase):
  @weight(1)
  @number("2.1")
  def test_1(self):
      """is_anagram_lettercount -  Basic True"""
      val = is_anagram_lettercount("baste", "beast")
      self.assertEqual(val, True)

  @weight(1)
  @number("2.2")
  def test_2(self):
      """is_anagram_lettercount -  Basic True with mixed Capitalization"""
      val = is_anagram_lettercount("Allergy", "reGaLLy")
      self.assertEqual(val, True)

  @weight(1)
  @number("2.3")
  def test_3(self):
      """is_anagram_lettercount -  Basic False"""
      val = is_anagram_lettercount("baste", "beaft")
      self.assertEqual(val, False)

  @weight(1)
  @number("2.4")
  def test_4(self):
      """is_anagram_lettercount -  Identical Words"""
      val = is_anagram_lettercount("road", "road")
      self.assertEqual(val, False)

  @weight(1)
  @number("2.5")
  def test_5(self):
     """is_anagram_lettercount -  Identical Words with Mixed Capitalization"""
     val = is_anagram_lettercount("road", "Road")
     self.assertEqual(val, False)

  @weight(1)
  @number("2.6")
  def test_6(self):
        """is_anagram_lettercount -  Nearly Identical Words"""
        val = is_anagram_lettercount("abed", "abet")
        self.assertEqual(val, False)

  @weight(1)
  @number("2.7")
  def test_7(self):
        """is_anagram_lettercount -  Nearly Anagram: repeated letters"""
        val = is_anagram_lettercount("odd", "do")
        self.assertEqual(val, False)

  @weight(1)
  @number("2.8")
  def test_8(self):
        """is_anagram_lettercount -  1 letter words"""
        val = is_anagram_lettercount("a", "a")
        self.assertEqual(val, False)

  @weight(1)
  @number("2.9")
  def test_9(self):
        """is_anagram_lettercount -  Almost Anagrams: Plural"""
        val = is_anagram_lettercount("castor", "costars")
        self.assertEqual(val, False)

  @weight(1)
  @number("2.10")
  def test_10(self):
        """is_anagram_lettercount -  Two Empty Strings"""
        val = is_anagram_lettercount("", "")
        self.assertEqual(val, False)
  
  @weight(1)
  @number("2.11")
  def test_11(self):
      """is_anagram_lettercount -  1 word not in valid word list"""
      val = is_anagram_lettercount("baste", "bteas")
      self.assertEqual(val, False)

  @weight(1)
  @number("2.12")
  def test_12(self):
      """is_anagram_lettercount -  2 words not in valid word list"""
      val = is_anagram_lettercount("ftvx", "xvtf")
      self.assertEqual(val, False)

  @weight(1)
  @number("2.13")
  def test_13(self):
      """is_anagram_lettercount - 2 near-anagrams"""
      val = is_anagram_lettercount("rattles", "realist")
      self.assertEqual(val, False)