import py_compile
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number

from AnagramExplorer_solution import AnagramExplorer_solution
from valid_word_list import get_valid_word_list

explorer_solution = AnagramExplorer_solution(get_valid_word_list())

from AnagramExplorer import AnagramExplorer

class TestEx1(unittest.TestCase):
  @weight(1)
  @number("7.1")
  def test_1(self):
      """explorer.get_most_anagrams -  One anagram family that is the longest"""
      wordList= ["abed", "mouse", "bead", "baled", "abled", "rat", "blade"]
      print(f"wordList: {wordList}")
      letters = ["a","b","e","d","l"]
      print(f"letters: {letters}")
      correct_choices = ["baled", "abled", "blade"]
      student_explorer = AnagramExplorer(wordList)
      val = student_explorer.get_most_anagrams(letters)

      self.assertEqual(val in correct_choices, True)

  @weight(1)
  @number("7.2")
  def test_2(self):
       """explorer.get_most_anagrams -  Two anagram families that are the longest"""
       wordList= ["abed", "mouse", "bead", "baled", "rat", "blade"]
       print(f"wordList: {wordList}")
       letters = ["a","b","e","d","l"]
       print(f"letters: {letters}")
       correct_choices = ["abed","bead","baled","blade"]
       student_explorer = AnagramExplorer(wordList)
       val = student_explorer.get_most_anagrams(letters)
       self.assertEqual(val in correct_choices, True)


  @weight(1)
  @number("7.3")
  def test_3(self):
      """explorer.get_most_anagrams - default letter choices in actual wordlist from get_valid_word_list()"""
      letters = ["p", "o", "t", "s", "r", "i", "a"]
      correct_choices = explorer_solution.get_most_anagrams_all(letters)
      student_explorer = AnagramExplorer(get_valid_word_list())
      val = student_explorer.get_most_anagrams(letters)
      self.assertEqual(val in correct_choices, True)
