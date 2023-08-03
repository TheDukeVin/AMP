import py_compile
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from AnagramExplorer import AnagramExplorer
from valid_word_list import get_valid_word_list

explorer = AnagramExplorer(get_valid_word_list())

class TestEx1(unittest.TestCase):
  @weight(1)
  @number("3.1")
  def test_1(self):
      """explorer.is_valid_anagram_pair -  Basic True"""
      pair =("pot", "top")
      letters = ["p", "o", "t", "s", "r", "i", "a"]
      val = explorer.is_valid_anagram_pair(pair, letters)
      self.assertEqual(val, True)

  @weight(1)
  @number("3.2")
  def test_2(self):
      """explorer.is_valid_anagram_pair -  Basic True with mixed Capitalization"""
      pair =("pot", "Top")
      letters = ["p", "o", "t", "s", "r", "i", "a"]
      val = explorer.is_valid_anagram_pair(pair, letters)
      self.assertEqual(val, True)

  @weight(1)
  @number("3.3")
  def test_3(self):
      """explorer.is_valid_anagram_pair -  Basic False"""
      pair =("pot", "rat")
      letters = ["p", "o", "t", "s", "r", "i", "a"]
      val = explorer.is_valid_anagram_pair(pair, letters)
      self.assertEqual(val, False)

  @weight(1)
  @number("3.4")
  def test_4(self):
      """explorer.is_valid_anagram_pair -  Identical Words"""
      pair =("pot", "pot")
      letters = ["p", "o", "t", "s", "r", "i", "a"]
      val = explorer.is_valid_anagram_pair(pair, letters)
      self.assertEqual(val, False)

  @weight(1)
  @number("3.5")
  def test_5(self):
     """explorer.is_valid_anagram_pair -  Identical Words with Mixed Capitalization"""
     pair =("pot", "POT")
     letters = ["p", "o", "t", "s", "r", "i", "a"]
     val = explorer.is_valid_anagram_pair(pair, letters)
     self.assertEqual(val, False)

  @weight(1)
  @number("3.6")
  def test_6(self):
        """explorer.is_valid_anagram_pair -  Nearly Identical Words"""
        pair =("pot", "pit")
        letters = ["p", "o", "t", "s", "r", "i", "a"]
        val = explorer.is_valid_anagram_pair(pair, letters)
        self.assertEqual(val, False)

  @weight(1)
  @number("3.7")
  def test_7(self):
      """explorer.is_valid_anagram_pair -  Valid anagrams, but not in letters"""
      pair =("baste", "beast")
      letters = ["p", "o", "t", "s", "r", "i", "a"]
      val = explorer.is_valid_anagram_pair(pair, letters)
      self.assertEqual(val, False)

  @weight(1)
  @number("3.8")
  def test_8(self):
        """explorer.is_valid_anagram_pair -  1 letter words"""
        pair =("t", "t")
        letters = ["p", "o", "t", "s", "r", "i", "a"]
        val = explorer.is_valid_anagram_pair(pair, letters)
        self.assertEqual(val, False)

  @weight(1)
  @number("3.9")
  def test_9(self):
        """explorer.is_valid_anagram_pair -  Almost Anagrams: Plural"""
        pair =("pot", "pots")
        letters = ["p", "o", "t", "s", "r", "i", "a"]
        val = explorer.is_valid_anagram_pair(pair, letters)
        self.assertEqual(val, False)

  @weight(1)
  @number("3.10")
  def test_10(self):
        """explorer.is_valid_anagram_pair -  Two Empty Strings"""
        pair =("", "")
        letters = ["p", "o", "t", "s", "r", "i", "a"]
        val = explorer.is_valid_anagram_pair(pair, letters)
        self.assertEqual(val, False)

  @weight(1)
  @number("3.10")
  def test_10(self):
        """explorer.is_valid_anagram_pair - Anagrams, but not in valid_word_list()"""
        pair =("sria", "airs")
        letters = ["p", "o", "t", "s", "r", "i", "a"]
        val = explorer.is_valid_anagram_pair(pair, letters)
        self.assertEqual(val, False)

  @weight(1)
  @number("3.11")
  def test_11(self):
        """explorer.is_valid_anagram_pair - Double letter in word but not letters list"""
        pair =("loop", "pool")
        letters = ["p", "o", "l", "s", "r", "i", "a"]
        val = explorer.is_valid_anagram_pair(pair, letters)
        self.assertEqual(val, False)

  @weight(1)
  @number("3.12")
  def test_12(self):
        """explorer.is_valid_anagram_pair - Double letter in word and also letters list"""
        pair =("loop", "pool")
        letters = ["p", "o", "l", "s", "r", "i", "o"]
        val = explorer.is_valid_anagram_pair(pair, letters)
        self.assertEqual(val, True)
