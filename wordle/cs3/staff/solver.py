#!/usr/bin/env python3

from wordle import GameManager, Player
from wordlist import WordList
from information import patterns
from random import choice
from scipy.stats import entropy

class Prob():

    def __init__(self, word_list):
        assert (len(word_list) > 0)
        self.word_list = word_list
        self.length = len(self.word_list)

    def of_pattern(self, guess, pat):
        count = sum(1 for _ in self.word_list.matching(pat, guess))
        return count / float(self.length)

    def expected_entropy(self, guess):
        eta = entropy([self.of_pattern(guess, pat) for pat in patterns()], base=2)
        return (guess, eta)

def max_entropy_word(word_list, num_words):
    """the word in word_list with the maximum """
    goat = None
    goat_entropy = None
    prob = Prob(word_list)
    # for word in ProgressBar(word_list):
    for word in word_list:
        _, new_entropy = prob.expected_entropy(word)
        if goat is None or new_entropy > goat_entropy:
            goat = word
            goat_entropy = new_entropy
    return goat, goat_entropy

class Solver(Player):

    def __init__(self, first_guess = "raise"): # "raise", "slate", "sores", "salet"
        self.word_list = WordList()
        self.num_guesses = 0
        self.first_guess = first_guess
        self.dumb = False

    def make_guess(self):
        if self.dumb:
            guess = choice(self.word_list.words)
        elif self.first_guess is None:
            num_words = len(self.word_list)
            guess, eta = max_entropy_word(self.word_list, num_words)
        else:
            guess = self.first_guess
            self.first_guess = None
        assert guess is not None
        self.num_guesses += 1
        return guess


    def update_knowledge(self, info):
        print(info)
        self.word_list.refine(info)
        assert(len(self.word_list) > 0)


def main():
    num_guesses = GameManager(Solver()).play_game()
    print("you found the word in", num_guesses, "guesses")


if __name__ == "__main__": main()
