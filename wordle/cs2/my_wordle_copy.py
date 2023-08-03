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

def get_AI_guess_raw(word_list: list[str], guesses: list[str], feedback: list[str]) -> str:
    # find current options
    options = []
    for word in word_list:
        matches = True
        for i in range(0, len(guesses)):
            if get_feedback(guesses[i], word) != feedback[i]:
                matches = False
                break
        if matches:
            options.append(word)
    assert len(options) > 0
    # If only one option, return it
    if len(options) == 1:
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
    # print(best_size)
    return best_guess

def get_first_guess(word_list):
    return "RAISE"
    # return get_AI_guess_raw(word_list, [], [])

def get_second_guess_lookup(word_list, first_guess):
    return {'-a---': 'CLOUT', '-a-SE': 'BUTCH', '-a--E': 'PLANT', '-a--e': 'CLEAT', 'ra---': 'CROWD', '-aI-E': 'ANKLE', '-a-S-': 'SHALT', 'rai--': 'GLAND', '-ai--': 'UNTIL', 'ra--E': 'TRACK', 'raI-E': 'AFIRE', 'ra--e': 'BLEAT', '-aI--': 'AGONY', 'rai-e': 'AIDER', '-aisE': 'AISLE', '-aI-e': 'ALIEN', '-aIS-': 'AMISS', 'raISE': 'ARISE', 'ra-SE': 'ABACK', 'ra-s-': 'SPLAT', 'ra-S-': 'BATCH', '-a-s-': 'PLANT', '-a-se': 'KNELT', '-aIsE': 'ASIDE', '-A---': 'COUNT', '-A--E': 'GULCH', '-A--e': 'NOTCH', 'rA--e': 'EMPTY', 'rA--E': 'ABACK', 'rA---': 'CLOTH', '-A-s-': 'TONAL', '-Ais-': 'ANTIC', '-A-sE': 'BUTCH', '-a-Se': 'LEFTY', '----e': 'BETEL', '--i-e': 'LIPID', '--I-e': 'DEPTH', '--i-E': 'LINGO', '----E': 'COULD', 'r---e': 'DETER', '---se': 'SPELT', '--i--': 'PILOT', 'r-i--': 'GROUT', '--is-': 'SHOUT', '---Se': 'CLOTH', '--I--': 'BLUNT', '--IS-': 'FORTH', '-----': 'MULCH', 'r----': 'COUNT', '---S-': 'FLOSS', '---s-': 'PLUNK', 'r---E': 'PRONG', 'raI--': 'ABLED', 'r-I-E': 'DUMPY', 'r-I--': 'CRYPT', 'r-I-e': 'DRAFT', 'r-IS-': 'ABACK', 'r--S-': 'COUNT', '-Ai--': 'CLEFT', 'rAI--': 'CHAFE', '-A-SE': 'AMPLE', '--I-E': 'CLOTH', '---SE': 'CLOTH', 'r-i-e': 
'VINYL', 'r--Se': 'BOTCH', 'r--SE': 'COUNT', '-AI--': 'ADAPT', '-AIS-': 'ABATE', 'r-i-E': 'ABIDE', '-A-se': 'EASEL', '-ai-e': 'ABLED', '---sE': 'MONTH', 'r--se': 'SHEEP', '--ISe': 'ABHOR', 'r-iS-': 'FIRST', '-A-S-': 'SLEPT', '--iS-': 'EMPTY', '--ISE': 'ACORN', 'rA-S-': 'ADMIN', '-ai-E': 'ACORN', 'rai-E': 'IRATE', '--ise': 'ADEPT', '--isE': 'AGENT', '-AI-E': 'ADMIN', 'r-ise': 'ADMIN', 'rAi--': 'ABATE', 'rA-SE': 'PARSE', '-aiS-': 'QUASI', 'RAi--': 'BLOND', 'RA--e': 'CARVE', 'RA---': 'DELAY', 'RAI--': 'RAINY', 'RAISE': 'RAISE', 'RA--E': 'RANGE', 'RA-s-': 'RASPY', 'Ra--e': 'LYMPH', 'R---e': 'COULD', 'R--se': 'ABACK', 'R-i-e': 'CAPER', 'R-I-e': 'REIGN', 'R-ise': 'ADMIN', 'R--SE': 'ABBOT', 'R---E': 'ABOUT', 'R-I--': 'RHINO', 'R-i-E': 'ABIDE', 'R-i--': 'ABBOT', 'R-iSE': 'RINSE', 'R-is-': 'RISKY', 'Rai--': 'RIVAL', 'Ra---': 'ABHOR', 'Ra-S-': 'ROAST', 'R----': 'OUTDO', 'R--S-': 'ROOST', 'R--s-': 'RUSTY', 'rA-se': 'ACORN', '-AIs-': 'SAINT', 'rA-s-': 'ABATE', '-a-sE': 'STUCK', 'ra-sE': 'CHANT', '--Is-': 'KNELT', 'r--sE': 'PERCH', 'r--s-': 'COUNT', '--IsE': 'PLANT', '-aise': 'SEPIA', 'ra-se': 'CHAMP', '--Ise': 'ADAPT', 'r-IsE': 'ABHOR', 'r-Is-': 'CHALK', '-ais-': 'ENACT', 'r-Ise': 'SKIER', 'r-is-': 'ABOUT', 'rais-': 'STAIR'}
    # lookup = {}
    # for word in word_list:
    #     f = get_feedback(first_guess, word)
    #     if f not in lookup:
    #         second = get_AI_guess_raw(word_list, [first_guess], [f])
    #         lookup[f] = second
    # return lookup

first_guess = ""
second_guess_lookup = {}
remaining = {}

def get_remaining(word_list):
    global first_guess, second_guess_lookup
    poss = {}
    for word in word_list:
        f = get_feedback(first_guess, word)
        if f not in poss:
            poss[f] = set()
        poss[f].add(word)
    poss2 = {}
    for f, p in poss.items():
        if f not in second_guess_lookup:
            poss2[f] = {key : "" for key in poss[f]}
            continue
        poss2[f] = {}
        for word in p:
            f2 = get_feedback(second_guess_lookup[f], word)
            if f2 not in poss2[f]:
                poss2[f][f2] = {}
            poss2[f][f2][word] = ""
    return poss2

def get_AI_guess(word_list: list[str], guesses: list[str], feedback: list[str]) -> str:
    '''Analyzes feedback from previous guesses (if any) to make a new guess
        Args:
            word_list (list): A list of potential Wordle words
            guesses (list): A list of string guesses, could be empty
            feedback (list): A list of feedback strings, could be empty
        Returns:
         str: a valid guess that is exactly 5 uppercase letters
    '''
    # precompute first and second guess
    global first_guess, second_guess_lookup, remaining
    if first_guess == "":
        first_guess = get_first_guess(word_list)
        second_guess_lookup = get_second_guess_lookup(word_list, first_guess)
        remaining = get_remaining(word_list)
    if len(guesses) == 0:
        return first_guess
    if len(guesses) == 1 and feedback[0] in second_guess_lookup:
        return second_guess_lookup[feedback[0]]
    if feedback[0] in second_guess_lookup:
        poss = remaining[feedback[0]][feedback[1]]
    else:
        poss = remaining[feedback[0]]
    if len(poss) <= 2:
        for word in poss:
            matches = True
            for i in range(0, len(guesses)):
                if get_feedback(guesses[i], word) != feedback[i]:
                    matches = False
                    break
            if matches:
                return word
    elif poss[]

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