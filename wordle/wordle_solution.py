'''
Wordle- Guess a five-letter secret word in at most six attempts.
'''
import random
from colorama import Fore, Back, Style, init
init(autoreset=True) #Ends color formatting after each print statement
from  wordle_wordlist import getWordList


def picksecretWord(wordList):
    ''' Picks a secret word from the list of allowable words

        Returns:
            str: a single word from the list of allowable words
    '''
    #return random.choice(wordList)
    return "MOTTO"

def getPlayerGuess(wordList):
    '''Prompts for and returns a player guess until the player enters a guess that:
        - is exactly five letters
        - exists in the list of Wordle words
        Args:
            wordList (list): A list of allowable words
        Returns:
            str: a string guess that is exactly 5 uppercase letters.
    '''
    guess = input("Enter guess: ")
    while len(guess) != 5: #or guess.upper() not in wordList:
        guess = input("Enter a valid guess: ")

    return guess.upper()

def getAIGuess(wordList, guesses, feedback):
    '''Analyzes feedback from previous guesses (if any) to make a new guess
        Args:
            wordList (list): A list of potential Wordle words
            guesses (list): A list of string guesses
            feedback (list): A list of feedback strings
        Returns:
         str: a valid guess that is exactly 5 uppercase letters
    '''

    match len(guesses):
        case 0:
            return "MOTTO"
        case 1:
            return "MOMMY"
        case 2:
            return "CATER"
        case 3:
            return "REACT"
        case 4:
            return "CRATE"
        case 5:
            return "TRACE"
        case _:
            return "TOOTH"

def getFeedback(guess, secretWord):
    '''Generates a feedback string based on comparing a 5-letter guess with the secret word. 
       The feedback string uses the following schema: 
        - Correct letter, correct spot: uppercase letter ('A'- 'Z')
        - Correct letter, wrong spot: lowercase letter ('a' - 'z')
        - Letter not in the word: '-'

       For example:
        - getFeedback("lever", "EATEN") --> "-e-E-"
        - getFeedback("LEVER", "LOWER") --> "L--ER"
        - getFeedback("MOMMY", "MADAM") --> "M-m--"
        - getFeedback("ARGUE", "MOTTO") --> "-----"

        Args:
            guess (str): The guessed word
            secretWord (str): The secret word
        Returns:
            str: Feedback string, based on comparing guess with the secret word
    '''

    feedback = ["-"]*5
    guess = guess.upper()
    secret = list(secretWord.upper())
    for i in range(5):
        if guess[i] == secret[i]:
            feedback[i] = secret[i]
            secret[i] = '-'

    for i in range(5):
        if guess[i] in secret and feedback[i]=='-':
            feedback[i] = guess[i].lower()
            secret[secret.index(guess[i])] = '-'

    return "".join(feedback)

def printFeedback(guesses, feedback):
    '''Uses the colorama library to display both a list of guesses and a
       "keyboard" representation of the entire alphabet.
        - Green/White: Correct letter in the correct spot
        - Yellow/White: Correct letter in the incorrect spot
        - Black/White: Guessed letters not in the word
        - White/Black: Unguessed letters in keyboard

        For example, if you guess "LEVER" when the secret word is "EATEN":
         - The first E turns Yellow because it is in the word but in the wrong spot.
         - The second E turns Green because it is in the word, and in the correct spot.
         - The other letters (L, V, R) will turn Black because they are not in the secret word.

        If you guess two of the same letter in a word, and only one of the letters turn Yellow
        or Green, then there is only one copy of that letter in the secret word.
        Args:
            guesses (tuple): A tuple of guessed words
            feedback (tuple): A tuple of feedback strings
    '''
    print(Back.WHITE+Fore.WHITE + "       ")
    for i in range(len(guesses)):
        colorString = Back.WHITE+Fore.WHITE + " "
        for j in range(5):
            if feedback[i][j]=="-":
                colorString+=Back.BLACK+Fore.WHITE + guesses[i][j]
            elif ord(feedback[i][j]) < 97:
                colorString+=Back.GREEN+Fore.WHITE + feedback[i][j]
            else:
                colorString+=Back.YELLOW+Fore.WHITE + feedback[i][j].upper()
        colorString += Back.WHITE+Fore.WHITE + " "
        print(colorString)
    print(Back.WHITE+Fore.WHITE + "       ")

def playWordle(secretWord, wordList, mode="HUMAN"):
    '''Plays a complete game of Wordle. The game ends when:
        - a player has guessed the secret word
        - a player has not guessed the secret word in six guesses

        if mode == "AI", the AI should make guesses.
        if mode == "HUMAN", a human should make guesses.

        Args:
            secretWord (str): The secret word
            wordList (list): A list of allowable words
            mode (str): The mode (HUMAN or AI) of play
        Returns:
         list: a tuple of all valid player guesses
    '''
    guesses=[]
    feedback=[]
    gameOver = False

    while not gameOver:
        if mode=="HUMAN": guesses.append(getPlayerGuess(wordList))
        elif mode=="AI": guesses.append(getAIGuess(wordList, guesses, feedback))

        feedback.append(getFeedback(guesses[len(guesses)-1], secretWord))
        printFeedback(guesses, feedback)
        if len(guesses)==6 or guesses[len(guesses)-1] == secretWord:
            gameOver=True

    return guesses

if __name__ == "__main__":
    secretWord = picksecretWord(getWordList()) #sometimes secret_word will be easy, sometimes will be hard
    guesses = playWordle(secretWord, getWordList(), "HUMAN") #steps 0 - 3

    if secretWord!=guesses[len(guesses)-1]:
        print("You lost.")
        print("The correct word was:"+secretWord)
    else:
        print("You won in "+str(len(guesses))+ " guesses!")
