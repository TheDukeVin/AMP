import py_compile
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number

from AnagramExplorer_solution import AnagramExplorer_solution
from valid_word_list import get_valid_word_list

explorer_solution = AnagramExplorer_solution(get_valid_word_list())

from anagame import calc_stats
from AnagramExplorer import AnagramExplorer
student_explorer = AnagramExplorer(get_valid_word_list())

letters = ["p", "o", "t", "s", "r", "i", "a"]

all_anagrams = explorer_solution.get_all_anagrams(letters)

class TestEx1(unittest.TestCase):
  @weight(1)
  @number("4.1")
  def test_1(self):
       """calc_stats - No valid guesses out of 3 guesses"""
       guesses=list()
       guesses.append(("star","tarts"))
       guesses.append(("far","rat"))
       guesses.append(("top","tip"))
       print(f"Guesses: {guesses}")

       scoreDict = calc_stats(guesses, letters, student_explorer)
       """- score should be 0"""
       self.assertEqual(scoreDict["score"], 0)
       self.assertEqual(len(scoreDict["valid"]), 0)
       self.assertEqual(len(scoreDict["invalid"]), 3)
       self.assertEqual(scoreDict["accuracy"], 0)

       guessed = sorted(["star","tarts","far","rat","top","tip"])
       self.assertEqual(scoreDict["skill"], 0)
       self.assertEqual(len(scoreDict["guessed"]), 0)
       self.assertEqual(scoreDict["not guessed"], all_anagrams)

  @weight(1)
  @number("4.2")
  def test_2(self):
      """calc_stats - All valid guesses with one duplicate anagram stem"""
      guesses=[]
      guesses.append(("art","rat")) 
      guesses.append(("rats","arts"))
      guesses.append(("spit","pits"))
      guesses.append(("spit","tips"))
      guesses.append(("stop","pots"))
      guesses.append(("tip","pit"))
      guesses.append(("top","pot"))
      print(f"Guesses: {guesses}")
      
      #letters = ["p", "o", "t", "s", "r", "i", "a"]
      scoreDict = calc_stats(guesses, letters, student_explorer)
      self.assertEqual(scoreDict["score"], 11)
      self.assertEqual(len(scoreDict["valid"]), 7 )
      self.assertEqual(len(scoreDict["invalid"]), 0)
      self.assertEqual(scoreDict["accuracy"], 100)

      guessed = ["art","rat","rats","arts","spit","pits","tips","stop","pots","tip","pit","top","pot"]
      expectedSkill = 17
      self.assertEqual(scoreDict["skill"], expectedSkill)
      self.assertEqual(len(scoreDict["guessed"]), len(guessed))
      self.assertEqual(len(scoreDict["not guessed"]), len(all_anagrams)-len(guessed))
      self.assertEqual(len(scoreDict["guessed"].union(guessed)), len(guessed))
      all_anagrams2=all_anagrams.copy()
      for word in guessed:
          all_anagrams2.remove(word)
      self.assertEqual(scoreDict["not guessed"], all_anagrams2)

  @weight(1)
  @number("4.3")
  def test_3(self):
      """calc_stats - Some valid and some invalid guesses"""
      guesses=[]
      guesses.append(("star","pair"))
      guesses.append(("fun","rat"))
      guesses.append(("top","tip"))
      guesses.append(("art","rat"))
      guesses.append(("rats","arts"))
      guesses.append(("spit","pits"))
      guesses.append(("pits","tips"))
      guesses.append(("stop","pots"))
      guesses.append(("tip","pit"))
      guesses.append(("top","pot"))
      guesses.append(("ports","sport"))
      guesses.append(("spot", "spit"))
      guesses.append(("sot", "spit"))
      guesses.append(("hiss", "cat"))
      guesses.append(("mouse", "rat"))
      guesses.append(("cat", "dog"))
      print(f"Guesses: {guesses}")
      scoreDict = calc_stats(guesses, letters, student_explorer)
      print(f"Testing score... expecting 14..")
      self.assertEqual(scoreDict["score"], 14)
      print(f"Testing valid words... expecting 8 pairs of valid words")
      self.assertEqual(len(scoreDict["valid"]), 8)
      print(f"Testing invalid words... expecting 8 pairs of iinvalid words")
      self.assertEqual(len(scoreDict["invalid"]), 8)
      print(f"Testing accuracy... expecting an accuracy of 50")
      self.assertEqual(scoreDict["accuracy"], 50)

      guessed = {"art","rat","rats","arts","spit","pits","tips","stop","pots","tip","pit","top","pot", "ports","sport"}
      print(f"Testing unique words guessed... expecting {guessed}")
      self.assertEqual(scoreDict["guessed"], guessed)
      all_anagrams2=all_anagrams.copy()
      for word in guessed:
           all_anagrams2.remove(word)
      print(f"Testing unique words not guessed... expecting {all_anagrams2}")  
      self.assertEqual(scoreDict["not guessed"], all_anagrams2)
      expectedSkill = 20
      print(f"Testing skill... expecting a skill of 20")
      self.assertEqual(scoreDict["skill"], expectedSkill)

  @weight(1)
  @number("4.4")
  def test_4(self):
     """calc_stats - No guesses"""
     guesses=set()
     print(f"Guesses: {guesses}")

     scoreDict = calc_stats(guesses, letters, student_explorer)
     self.assertEqual(scoreDict["score"], 0)
     self.assertEqual(len(scoreDict["valid"]), 0)
     self.assertEqual(len(scoreDict["invalid"]), 0)
     self.assertEqual(scoreDict["accuracy"], 0)
     self.assertEqual(scoreDict["skill"], 0)
     self.assertEqual(len(scoreDict["guessed"]), 0)
     self.assertEqual(len(scoreDict["not guessed"]), len(all_anagrams))

  @weight(1)
  @number("4.5")
  def test_5(self):
       """calc_stats - Scoring with duplicate and invalid guesses"""
       guesses=[]
       guesses.append(("star","tarts")) #INVALID
       guesses.append(("far","rat")) #INVALID
       guesses.append(("rat","art"))
       guesses.append(("rat","art")) #INVALID
       guesses.append(("art","rat")) #INVALID
       #letters = ["p", "o", "t", "s", "r", "i", "a"]

       print(f"Guesses: {guesses}")

       scoreDict = calc_stats(guesses, letters, student_explorer)
       print(f"Testing score... expecting 1..")
       self.assertEqual(scoreDict["score"], 1)
       print(f"Testing valid words... expecting 1 pair of valid words")
       self.assertEqual(len(scoreDict["valid"]), 1)
       print(f"Testing invalid words... expecting 4 pairs of valid words")
       self.assertEqual(len(scoreDict["invalid"]), 4)
       print(f"Testing accuracy... expecting an accuracy of 20")
       self.assertEqual(scoreDict["accuracy"], 20)
       guessed={"art", "rat"}
       print(f"Testing unique words guessed... expecting {guessed}")
       self.assertEqual(len(scoreDict["guessed"]), 2)
       print(f"Testing unique words not guessed... expecting {len(all_anagrams)-2} words not guessed")  
       self.assertEqual(len(scoreDict["not guessed"]), len(all_anagrams)-2)
       print(f"Testing skill... expecting a skill of 2")
       self.assertEqual(scoreDict["skill"], 2)