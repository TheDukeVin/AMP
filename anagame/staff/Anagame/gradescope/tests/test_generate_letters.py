import py_compile
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number

from anagame import generate_letters

from AnagramExplorer_solution import AnagramExplorer_solution
from valid_word_list import get_valid_word_list

explorer_solution = AnagramExplorer_solution(get_valid_word_list())

def check_if_fun_factor_is_met(letters, factor):
    return len(explorer_solution.get_all_anagrams(letters)) >= factor

class TestEx1(unittest.TestCase):
  @weight(1)
  @number("8.1")
  def test_1(self):
      """generate_letters - Produces 7 Letters"""
      letters = generate_letters(1, 'scrabble', explorer_solution)
      self.assertTrue(len(letters) == 7)

  @weight(1)
  @number("8.2")
  def test_2(self):
      """generate_letters - Scrabble Fun Factor of 50"""
      fun_factor = 50
      letters = generate_letters(fun_factor, 'scrabble', explorer_solution)
      result = check_if_fun_factor_is_met(letters, fun_factor)
      self.assertTrue(result)

  @weight(1)
  @number("8.3")
  def test_3(self):
    """generate_letters - Letters Generated Randomly"""
    # Run generate_letters 50 times and check that not all 50 sets of letters are the same.
    seen_letters = set()
    for _ in range(50):
        letters = generate_letters(5, 'scrabble', explorer_solution)
        seen_letters.add(tuple(letters))
    # Make sure we did not only see 1 set of letters generated.  
    self.assertTrue(len(seen_letters) > 1)