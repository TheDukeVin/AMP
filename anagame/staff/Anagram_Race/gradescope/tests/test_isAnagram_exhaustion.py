import py_compile
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from anagram_race import is_anagram_exhaustive

class TestEx1(unittest.TestCase):
  @weight(1)
  @number("1.1")
  def test_1(self):
      """is_anagram_exhaustive -  Basic True"""
      val = is_anagram_exhaustive("baste", "beast")
      self.assertEqual(val, True)

  @weight(1)
  @number("1.2")
  def test_2(self):
      """is_anagram_exhaustive -  Basic True with mixed Capitalization"""
      val = is_anagram_exhaustive("Allergy", "reGaLLy")
      self.assertEqual(val, True)

  @weight(1)
  @number("1.3")
  def test_3(self):
      """is_anagram_exhaustive -  Basic False"""
      val = is_anagram_exhaustive("baste", "beaft")
      self.assertEqual(val, False)

  @weight(1)
  @number("1.4")
  def test_4(self):
      """is_anagram_exhaustive -  Identical Words"""
      val = is_anagram_exhaustive("road", "road")
      self.assertEqual(val, False)

  @weight(1)
  @number("1.5")
  def test_5(self):
     """is_anagram_exhaustive -  Identical Words with Mixed Capitalization"""
     val = is_anagram_exhaustive("road", "Road")
     self.assertEqual(val, False)

  @weight(1)
  @number("1.6")
  def test_6(self):
        """is_anagram_exhaustive -  Nearly Identical Words"""
        val = is_anagram_exhaustive("abed", "abet")
        self.assertEqual(val, False)

  @weight(1)
  @number("1.7")
  def test_7(self):
        """is_anagram_exhaustive -  Nearly Anagrams: repeated letter"""
        val = is_anagram_exhaustive("odd", "do")
        self.assertEqual(val, False)

  @weight(1)
  @number("1.8")
  def test_8(self):
        """is_anagram_exhaustive -  1 letter words"""
        val = is_anagram_exhaustive("a", "a")
        self.assertEqual(val, False)

  @weight(1)
  @number("1.9")
  def test_9(self):
        """is_anagram_exhaustive -  Almost Anagrams: Plural"""
        val = is_anagram_exhaustive("castor", "costars")
        self.assertEqual(val, False)

  @weight(1)
  @number("1.10")
  def test_10(self):
        """is_anagram_exhaustive -  Empty Words"""
        val = is_anagram_exhaustive("", "")
        self.assertEqual(val, False)
 
  @weight(1)
  @number("1.11")
  def test_11(self):
      """is_anagram_exhaustive -  1 word not in valid word list"""
      val = is_anagram_exhaustive("baste", "bteas")
      self.assertEqual(val, False)

  @weight(1)
  @number("1.12")
  def test_12(self):
      """is_anagram_exhaustive -  2 words not in valid word list"""
      val = is_anagram_exhaustive("ftvx", "xvtf")
      self.assertEqual(val, False)

  @weight(1)
  @number("1.13")
  def test_13(self):
      """is_anagram_exhaustive - 2 near-anagrams"""
      val = is_anagram_exhaustive("rattles", "realist")
      self.assertEqual(val, False)