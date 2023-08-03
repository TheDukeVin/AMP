import py_compile
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from anagram_race import is_anagram_checkoff

class TestEx1(unittest.TestCase):
  @weight(1)
  @number("2.1")
  def test_1(self):
      """is_anagram_checkoff -  Basic True"""
      val = is_anagram_checkoff("baste", "beast")
      self.assertEqual(val, True)

  @weight(1)
  @number("2.2")
  def test_2(self):
      """is_anagram_checkoff -  Basic True with mixed Capitalization"""
      val = is_anagram_checkoff("Allergy", "reGaLLy")
      self.assertEqual(val, True)

  @weight(1)
  @number("2.3")
  def test_3(self):
      """is_anagram_checkoff -  Basic False"""
      val = is_anagram_checkoff("baste", "beaft")
      self.assertEqual(val, False)

  @weight(1)
  @number("2.4")
  def test_4(self):
      """is_anagram_checkoff -  Identical Words"""
      val = is_anagram_checkoff("road", "road")
      self.assertEqual(val, False)

  @weight(1)
  @number("2.5")
  def test_5(self):
     """is_anagram_checkoff -  Identical Words with Mixed Capitalization"""
     val = is_anagram_checkoff("road", "Road")
     self.assertEqual(val, False)

  @weight(1)
  @number("2.6")
  def test_6(self):
        """is_anagram_checkoff -  Nearly Identical Words"""
        val = is_anagram_checkoff("abed", "abet")
        self.assertEqual(val, False)

  @weight(1)
  @number("2.7")
  def test_7(self):
        """is_anagram_checkoff -  Nearly Anagrams: repeated letter"""
        val = is_anagram_checkoff("odd", "do")
        self.assertEqual(val, False)

  @weight(1)
  @number("2.8")
  def test_8(self):
        """is_anagram_checkoff -  1 letter words"""
        val = is_anagram_checkoff("a", "a")
        self.assertEqual(val, False)

  @weight(1)
  @number("2.9")
  def test_9(self):
        """is_anagram_checkoff -  Almost Anagrams: Plural"""
        val = is_anagram_checkoff("castor", "costars")
        self.assertEqual(val, False)

  @weight(1)
  @number("2.10")
  def test_10(self):
        """is_anagram_checkoff -  Two Empty Strings"""
        val = is_anagram_checkoff("", "")
        self.assertEqual(val, False)

  @weight(1)
  @number("2.11")
  def test_11(self):
      """is_anagram_checkoff -  1 word not in valid word list"""
      val = is_anagram_checkoff("baste", "bteas")
      self.assertEqual(val, False)

  @weight(1)
  @number("2.12")
  def test_12(self):
      """is_anagram_checkoff -  2 words not in valid word list"""
      val = is_anagram_checkoff("ftvx", "xvtf")
      self.assertEqual(val, False)

  @weight(1)
  @number("2.13")
  def test_13(self):
      """is_anagram_checkoff - 2 near-anagrams"""
      val = is_anagram_checkoff("rattles", "realist")
      self.assertEqual(val, False)
