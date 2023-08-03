import py_compile
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from anagram_race import is_anagram_sort

class TestEx1(unittest.TestCase):
  @weight(1)
  @number("4.1")
  def test_1(self):
      """is_anagram_sort -  Basic True"""
      val = is_anagram_sort("baste", "beast")
      self.assertEqual(val, True)

  @weight(1)
  @number("4.2")
  def test_2(self):
      """is_anagram_sort -  Basic True with mixed Capitalization"""
      val = is_anagram_sort("Allergy", "reGaLLy")
      self.assertEqual(val, True)

  @weight(1)
  @number("4.3")
  def test_3(self):
      """is_anagram_sort -  Basic False"""
      val = is_anagram_sort("baste", "beaft")
      self.assertEqual(val, False)

  @weight(1)
  @number("4.4")
  def test_4(self):
      """is_anagram_sort -  Identical Words"""
      val = is_anagram_sort("road", "road")
      self.assertEqual(val, False)

  @weight(1)
  @number("4.5")
  def test_5(self):
     """is_anagram_sort -  Identical Words with Mixed Capitalization"""
     val = is_anagram_sort("road", "Road")
     self.assertEqual(val, False)

  @weight(1)
  @number("4.6")
  def test_6(self):
        """is_anagram_sort -  Nearly Identical Words"""
        val = is_anagram_sort("abed", "abet")
        self.assertEqual(val, False)

  @weight(1)
  @number("4.7")
  def test_7(self):
        """is_anagram_sort -  Nearly Anagrams: repeated letter"""
        val = is_anagram_sort("odd", "do")
        self.assertEqual(val, False)

  @weight(1)
  @number("4.8")
  def test_8(self):
        """is_anagram_sort -  1 letter words"""
        val = is_anagram_sort("a", "a")
        self.assertEqual(val, False)

  @weight(1)
  @number("4.9")
  def test_9(self):
        """is_anagram_sort -  Almost Anagrams: Plural"""
        val = is_anagram_sort("castor", "costars")
        self.assertEqual(val, False)

  @weight(1)
  @number("4.10")
  def test_10(self):
        """is_anagram_sort -  Empty Words"""
        val = is_anagram_sort("", "")
        self.assertEqual(val, False)

  @weight(1)
  @number("4.11")
  def test_11(self):
      """is_anagram_sort -  1 word not in valid word list"""
      val = is_anagram_sort("baste", "bteas")
      self.assertEqual(val, False)

  @weight(1)
  @number("4.12")
  def test_12(self):
      """is_anagram_sort -  2 words not in valid word list"""
      val = is_anagram_sort("ftvx", "xvtf")
      self.assertEqual(val, False)

  @weight(1)
  @number("4.13")
  def test_13(self):
      """is_anagram_sort - 2 near-anagrams"""
      val = is_anagram_sort("rattles", "realist")
      self.assertEqual(val, False)