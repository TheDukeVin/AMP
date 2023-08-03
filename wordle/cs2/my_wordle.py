'''
[CS2] Wordle- Guess a five-letter secret word in at most six attempts.
'''
import random
import math
# To install colorama, run the following command in your VS Code terminal:
# py -m pip install colorama
from colorama import Fore, Back, Style, init
init(autoreset=True) #Ends color formatting after each print statement
from wordle_wordlist import get_word_list

def get_feedback(guess: str, secret_word: str) -> str:
    '''Generates a feedback string based on comparing a 5-letter guess with the secret word. 
       The feedback string uses the following schema: 
        - Correct letter, correct spot: uppercase letter ('A'-'Z')
        - Correct letter, wrong spot: lowercase letter ('a'-'z')
        - Letter not in the word: '-'

       For example:
        - get_feedback("lever", "EATEN") --> "-e-E-"
        - get_feedback("LEVER", "LOWER") --> "L--ER"
        - get_feedback("MOMMY", "MADAM") --> "M-m--"
        - get_feedback("ARGUE", "MOTTO") --> "-----"

        Args:
            guess (str): The guessed word
            secret_word (str): The secret word
        Returns:
            str: Feedback string, based on comparing guess with the secret word
    '''
    guess = list(guess.lower())
    secret_word = secret_word.lower()
    checkoff = secret_word
    feedback = ['-']*5
    for i in range(5):
        if guess[i] == checkoff[i]:
            feedback[i] = guess[i].upper()
            checkoff = checkoff.replace(guess[i], '-', 1)
            guess[i] = '-'

    for i in range(5):
        if guess[i] != '-' and guess[i] in checkoff:
            feedback[i] = guess[i]
            checkoff = checkoff.replace(guess[i], '-', 1)
    return ''.join(feedback)

def get_size(partition):
    # return max(partition)
    return sum([x * math.log(x) for x in partition])

guess_lookup = {}
options_lookup = {}

def get_AI_guess(word_list: list[str], guesses: list[str], feedback: list[str]) -> str:
    f_key = tuple(feedback)
    if f_key in guess_lookup:
        return guess_lookup[f_key]
    # find current options
    if len(feedback) == 0:
        options_lookup[f_key] = list(word_list)
    options = options_lookup[f_key]
    assert len(options) > 0
    # If only one option, return it
    if len(options) <= 2:
        guess_lookup[f_key] = options[0]
        if len(options) == 2:
            options_lookup[tuple(feedback + [get_feedback(options[0], options[1])])] = [options[1]]
        return options[0]
    # For each guess, group together possible feedback
    # minimize expected log of size
    best_guess = ""
    best_size = len(options)**2
    for guess in word_list:
        possible_feedback = {}
        for option in options:
            f = get_feedback(guess, option)
            if f not in possible_feedback:
                possible_feedback[f] = 0
            possible_feedback[f] += 1
        size = get_size(possible_feedback.values())
        if size < best_size:
            best_guess = guess
            best_size = size
    guess_lookup[f] = best_guess

    return best_guess


# TODO: Define and implement your own functions!


if __name__ == "__main__":
    # TODO: Write your own code to call your functions here

    # word_list = get_word_list()
    # first_guess = get_first_guess(word_list)
    # print(get_second_guess_lookup(word_list, first_guess))

    # Simulate on all words

    num_guesses = [0]*10
    word_list = get_word_list()
    N = len(word_list)
    for secret in word_list:
        guesses = []
        feedback = []
        for j in range(10):
            # print(guesses)
            # print(feedback)
            guess = get_AI_guess(word_list, guesses, feedback)
            f = get_feedback(guess, secret)
            guesses.append(guess)
            feedback.append(f)
            if guess.lower() == secret.lower():
                break
        num_guesses[j] += 1
    print(num_guesses)


    # Run the game
    # word_list = get_word_list()
    # guesses = []
    # feedback = []
    # while True:
    #     guess = get_AI_guess(word_list, guesses, feedback)
    #     print(guess)
    #     f = str(input("Feedback: "))
    #     guesses.append(guess)
    #     feedback.append(f)
    #     if f == "r":
    #         print("Restart")
    #         guesses = []
    #         feedback = []
    #     if f == "q":
    #         print("Quit")
    #         break