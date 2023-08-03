import py_compile
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number

from AnagramExplorer_solution import AnagramExplorer_solution
from valid_word_list import get_valid_word_list

explorer_solution = AnagramExplorer_solution(get_valid_word_list())

from AnagramExplorer import AnagramExplorer

letters1 = ["a","b","e","d","l"]
letters2 = ["p", "o", "t", "s", "r", "i", "a"]

class TestEx1(unittest.TestCase):
  @weight(1)
  @number("6.1")
  def test_1(self):
      """get_all_anagrams -  Basic Example in function comments"""
      corpus= ["abed", "mouse", "bead", "baled", "abled", "rat", "blade"]
      print(f"corpus: {corpus}")

      all_anagrams= {"abed",  "abled", "baled", "bead", "blade"}
      student_explorer = AnagramExplorer(corpus)
      val = student_explorer.get_all_anagrams(letters1)
      self.assertEqual(val, all_anagrams)

  @weight(1)
  @number("6.2")
  def test_2(self):
      """get_all_anagrams - No anagrams in corpus"""
      corpus= ["abed", "mouse", "rat", "cat", "tiger", "elephant", "stork"]
      print(f"corpus: {corpus}")
      all_anagrams= set()
      student_explorer = AnagramExplorer(corpus)
      val = student_explorer.get_all_anagrams(letters1)
      self.assertEqual(len(val.union(all_anagrams)), len(all_anagrams))

  @weight(1)
  @number("6.3")
  def test_3(self):
      """get_all_anagrams - Corpus with 6 anagrams from 2 anagram families"""
      corpus = ["abed", "bead", "baled", "bade", "blade", "abled"]
      print(f"corpus: {corpus}")
      all_anagrams = {"abed", "abled", "bade", "baled", "bead", "blade"}
      student_explorer = AnagramExplorer(corpus)
      val = student_explorer.get_all_anagrams(letters1)
      self.assertEqual(val, all_anagrams)

  @weight(1)
  @number("6.4")
  def test_4(self):
      """get_all_anagrams - Variety of word lengths, some anagrams not in letters"""
      corpus= ["bad", "abed", "mouse", "bead", "baled", "abled", "rat", "art", "blade", "dab"]
      print(f"corpus: {corpus}")
      print(f"letters: {letters1}")

      all_anagrams ={"abed",  "abled", "bad", "baled", "bead", "blade", "dab"}
      student_explorer = AnagramExplorer(corpus)
      val = student_explorer.get_all_anagrams(letters1)
      self.assertEqual(val, all_anagrams)

  @weight(1)
  @number("6.5")
  def test_5(self):
      """get_all_anagrams - Actual wordlist from valid_word_list, letter combo #1"""
      print(f"letters: {letters1}")

      all_anagrams = explorer_solution.get_all_anagrams(letters1)
      student_explorer = AnagramExplorer(get_valid_word_list())
      val = student_explorer.get_all_anagrams(letters1)
      self.assertEqual(val, all_anagrams)

  @weight(1)
  @number("6.6")
  def test_6(self):
      """get_all_anagrams - Actual wordlist from valid_word_list, letter combo #2"""
      print(f"letters: {letters2}")

      all_anagrams = explorer_solution.get_all_anagrams(letters2)
      student_explorer = AnagramExplorer(get_valid_word_list())
      val = student_explorer.get_all_anagrams(letters2)
      self.assertEqual(val, all_anagrams)
