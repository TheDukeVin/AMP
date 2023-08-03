import time
import random
from valid_word_list import get_valid_word_list
from AnagramExplorer import AnagramExplorer

def generate_letters(fun_factor:int, distribution:str="scrabble")->list:
   '''Generates a list of 7 randomly-chosen lowercase letters which can form at least 
      fun_factor unique anagramable words

         Args:
          fun_factor (int): minimum number of unique anagram words offered by the chosen letters
          distribution (str): The type of distribution to use in order to choose letters
            "uniform" - chooses letters based on a uniform distribution
            "scrabble" - chooses letters based on a scrabble distribution

         Returns:
             A set of lowercase letters with length numLetters
   '''
   #start with a predefined list of letters for testing
   result = False
   while(not result):
       letters = []
       #1 choose some random letters
       if distribution == "uniform":
           for i in range(7):
                letters.append(chr(random.randint(97, 122)))
       elif distribution == "scrabble":
           # E-12, A-9, I-9, O-8, N-6, R-6, T-6, D-4, L-4, S-4, U-4,G-3, B-2, C-2, F-2, H-2, M-2, P-2, V-2, W-2, Y-2, J-1, K-1, Q-1, X-1, Z-1
           freq={
             12:["E"],
             9:["A", "I"],
             8:["O"],
             6:["N", "R", "T"],
             4:["D", "L", "S", "U"],
             3:["G"],
             2:["B", "C", "F", "H", "M", "P", "V", "W", "Y"],
             1:["J", "K", "Q", "X", "Z"]
           }
           dist = []
           for key in freq:
               for letter in freq[key]:
                   dist +=list(letter)*key

           for i in range(7):
                 choice = random.choice(dist)
                 dist.remove(choice)
                 letters.append(choice.lower())
       #2 check how many unique anagram words can be formed from those letters
       possibleWords = explorer.get_all_anagrams(letters)

       #3 decide if there are enough possible words
       if len(possibleWords)>=fun_factor:
           result = True

   #for testing letters = ["p", "o", "t", "s", "r", "i", "a"]

   return letters

def parse_guess(guess:str) -> tuple:
   '''Splits an entered guess into a two word tuple with all white space removed

          Args:
           guess: A single string reprsenting the player guess

          Returns:
           A tuple of two words. ("", "") in case of invalid input.

          Examples
          --------
          >>>parse_guess("eat, tea")
          ("eat", "tea")

          >>>parse_guess("eat , tea")
          ("eat", "tea")

          >>>parse_guess("eat,tea")
          ("eat", "tea")

          >>>parse_guess("eat tea")
          ("", "")
   '''
   guess = guess.replace(" ", "")
   commaPos = guess.find(",")
   if commaPos == -1:
       return ("", "")
   for i in range(0, len(guess)):
       if i != commaPos and not guess[i].isalpha():
           return ("", "")

   return (guess[:commaPos], guess[commaPos+1:])

def play_game(time_limit: int, letters: list)->set:
    '''Plays a single game of AnaGame

       Args:
         time_limit: Time limit in seconds
         letters: A list of valid letters form which the player can create an anagram

       Returns:
          A set of tuples reprsenting all player guesses
          The set data type ensures that a player can't make the same guess multiple times
   '''
    guesses= set() #Sets keep track of unique values. No duplicates allowed
    quit = False

    start = time.perf_counter() #start the stopwatch (sec)
    stop = start + time_limit

    while time.perf_counter() < stop and not quit:
        guess = input('')
        if guess.strip() == "quit":
            quit=True
        elif guess.strip() == "hint":
            print(f"Try working with: {explorer.get_most_anagrams(letters)}")
        else:
          tuple_guess = parse_guess(guess)
          if len(tuple_guess[0])>1:
            guesses.add(tuple_guess)
          else:
            print("Invalid input")

        print(f"{letters} {round(stop - time.perf_counter(),2)} seconds left")

    print("Thanks for playing Anagame!")

    return guesses

def calc_stats(guesses: list, letters: list, explorer) -> dict:
    '''Aggregates several statistics into a single dictionary:
        "invalid" -
        "score" -
        "accuracy" - a percentage representing the total number of guessed words from
                     the list of all anagramable words
        "skill" - a percentage representing the total number of valid guesses out of all possible anagrams
        "guessed" - a list of unique words guessed
        "not guessed" -

     Args:
      guesses (set): A set of tuples representing all word pairs guesses by the user

     Returns:
      dict: Returns a dictionary with seven keys: "valid", "invalid", "score", "accuracy", "skill", "guessed", "not guessed"
    '''
    uniqueAnagrams = []
    uniqueWords = set()
    score = 0
    valid = []
    invalid = []
    for guess in guesses:
        swapGuess = (guess[0], guess[1])
        if guess not in uniqueAnagrams and swapGuess not in uniqueAnagrams:
            uniqueAnagrams.append(guess)
            score += 1
            valid.append(guess)
            uniqueWords.add(guess[0])
            uniqueWords.add(guess[1])
        else:
            invalid.append(guess)
    stats = {}
    stats["score"] = score    #total score
    stats["valid"] = valid   #list of tuples: (valid_word1, valid_word2)
    stats["invalid"] = invalid #list of tuples: (invalid_word1, invalid_word2)
    stats["accuracy"] = 0 if guesses == {} else len(valid)/len(guesses) #percentage representing valid guesses out of all guesses
    stats["skill"] = len(uniqueWords)/len(get_valid_word_list())    #percentage representing unique guessed words out of all possible unique guesses
    stats["guessed"] = uniqueWords #unique valid guessed words
    stats["not guessed"] = AnagramExplorer.get_all_anagrams() - uniqueWords #unique words the player could have guessed, but didn’t


    return stats

def display_stats(stats):
    '''Prints a string representation of the game results'''

    print("------------")
    print(f"Final Score: {stats['score']}")
    print("------------")
    print(f"Accuracy: {round(stats['accuracy'], 2)}%")
    print(f" valid guesses ({len(stats['valid'])}):", end=" ")
    for guess in stats['valid']:
        print(f"  {guess[0]},{guess[1]}", end=" ")
    print(f"\n invalid guesses ({len(stats['invalid'])}):", end=" ")
    for guess in stats['invalid']:
        print(f"  {guess[0]},{guess[1]}", end=" ")
    print("\n------------")
    print(f"Skill: {round(stats['skill'], 2)}%")
    print(f" unique words you could have guessed ({len(explorer.get_all_anagrams(letters)) - len(stats['guessed'])}):")
    for guess in stats['not guessed']:
        print(f"  {guess}", end=" ")


if __name__ == "__main__":
  time_limit= 30

  explorer = AnagramExplorer(get_valid_word_list())
  letters= generate_letters(0, "uniform")

  print("\nWelcome to Anagame!\n")
  print("Please enter your anagrams separated by a comma: eat,tea")
  print("Enter 'quit' to end the game early, or 'hint' to get a useful word\n")
  print(f"You have {time_limit} seconds to guess as many anagrams as possible!")
  print(f"{letters}")

  guesses = play_game(time_limit, letters)
  stats_dict = calc_stats(guesses, letters, explorer)
  display_stats(stats_dict)