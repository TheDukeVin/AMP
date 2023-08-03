import py_compile
import unittest
# from gradescope_utils.autograder_utils.decorators import weight, number
from wordle_wordlist import get_word_list
from wordle_wordlist2 import get_long_word_list
import random
import time

from wordle import get_AI_guess

def get_feedback(guess, secret_word):
    feedback = ["-"]*5
    guess = guess.upper()
    secret = list(secret_word.upper())

    for i in range(5):
        if guess[i] == secret[i]:
            feedback[i] = secret[i]
            secret[i] = '-'

    for i in range(5):
        if guess[i] in secret and feedback[i]=='-':
            feedback[i] = guess[i].lower()
            secret[secret.index(guess[i])] = '-'

    return "".join(feedback)


def play_wordle(secret_word, word_list, get_AI_guess):
    guesses = []
    feedback = []
    game_over = False

    while not game_over:
        guesses.append(get_AI_guess(word_list, guesses, feedback))
        feedback.append(get_feedback(guesses[len(guesses)-1], secret_word))
        if len(guesses)==6 or guesses[len(guesses)-1] == secret_word:
            game_over=True

    return guesses

class TestEx1(unittest.TestCase):
  def test_1(self):
      """get_AI_guess - Basic Requirements"""
      guesses =()
      feedback = ()
      guess = get_AI_guess(get_word_list(), guesses, feedback)
      self.assertEqual(True, isinstance(guess, str))
      print("get_AI_guess is present and returns a string")
      self.assertEqual(len(guess), 5)
      self.assertEqual(guess in get_word_list(), True)
      print("AI guess is a 5-letter word from wordlist")

  def test_2(self):
      """get_AI_guess - Basic Profiler (given wordlist w/ ~2,300 5-letter words)"""
      wins = 0
      skill = 0
      numWords = len(get_word_list())
      random.shuffle(get_word_list())

      for secret_word in get_word_list():
          guesses = play_wordle(secret_word, get_word_list(), get_AI_guess)
          if secret_word==guesses[len(guesses)-1]:
              wins += 1
          skill += len(guesses)

      print(f"Total Games: {numWords}")
      print(f"Wins: {wins}")
      print(f"Accuracy: {(wins/numWords)*100}")
      print(f"Skill: {skill/numWords}")

      self.assertEqual(True, True)

  def test_3(self):
      """get_AI_guess - Advanced Profiler (new wordlist w/ ~13,000 5-letter words)"""
      wins = 0
      skill = 0
      numWords = len(get_long_word_list())

      random.shuffle(get_long_word_list())

      for secret_word in get_long_word_list():
          guesses = play_wordle(secret_word, get_long_word_list(), get_AI_guess)
          if secret_word==guesses[len(guesses)-1]:
              wins += 1
          skill += len(guesses)

      print(f"Total Games: {numWords}")
      print(f"Wins: {wins}")
      print(f"Accuracy: {(wins/numWords)*100}")
      print(f"Skill: {skill/numWords}")

      self.assertEqual(True, True)

start_time = time.time()
hello = TestEx1()
hello.test_2()
end_time = time.time()
print(end_time - start_time)