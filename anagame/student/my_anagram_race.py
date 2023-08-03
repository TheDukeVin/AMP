import itertools
from valid_word_list import get_valid_word_list # only words with 2 - 7 letters

def top_level_checks(word1:str, word2:str)->bool:
    ''' needs comments

        Highly-recommended to create this function.
    '''
    if word1 == word2: return False
    words = get_valid_word_list()
    if word1 not in words or word2 not in words: return False
    return True
   
def is_anagram_exhaustive(word1:str, word2:str)->bool:
    '''Generate all possible permutations of the first word until you find one that is the second word.
       If no permutation of the first word equals the second word, the two are not anagrams.

       Args:
        word1: The first word
        word2: The second word

       Returns:
        Returns True if word1 and word2 are anagrams, otherwise returns False
    '''
    # word = "cat"
    word1 = word1.lower()
    word2 = word2.lower()
    if not top_level_checks(word1, word2): return False

    permuations = list(itertools.permutations(word1)) 

    return (tuple(word2) in permuations)

def is_anagram_checkoff(word1:str, word2:str)->bool:
    '''Create a parallel list-based version of the second word (strings are immutable).
       Check off letters in the list as they are found by setting the value to None.

       Args:
        word1: The first word
        word2: The second word

       Returns:
        bool: Returns True if word1 and word2 are anagrams, otherwise returns False
    '''
    word1 = word1.lower()
    word2 = word2.lower()
    if not top_level_checks(word1, word2): return False

    if len(word1) != len(word2): return False

    checklist = list(word2)
    for c in word1:
        if c in checklist:
            i = checklist.index(c)
            checklist[i] = 0
        else:
            return False
    return True


def is_anagram_lettercount(word1:str, word2:str)->bool:
    '''
      Create two lists of length 26 to keep track of letter counts in each word.
          ie. [0] represents the letter a, [1] represents the letter b, and so on…
      Compare final versions of each list to determine if the words are anagrams.
      
      HINT- ASCII conversions will be helpful: ord("A") → 65. char(65)  -> “A”

       Args:
        word1 (str): The first word
        word2 (str): The second word

       Returns:
        bool: Returns True if word1 and word2 are anagrams, otherwise returns False
    '''
    word1 = word1.lower()
    word2 = word2.lower()
    if not top_level_checks(word1, word2): return False

    def toList(word:str):
        count = [0] * 26
        for c in word:
            count[ord(c) - 97] += 1
        return count
    return toList(word1) == toList(word2)


def is_anagram_sort(word1:str, word2:str)->bool:
    '''
      Sort both words, then compare to see if they are exactly the same.

       Args:
        word1 (str): The first word
        word2 (str): The second word

       Returns:
        bool: Returns True if word1 and word2 are anagrams, otherwise returns False
    '''
    word1 = word1.lower()
    word2 = word2.lower()
    if not top_level_checks(word1, word2): return False

    letters1 = list(word1)
    letters2 = list(word2)
    return sorted(letters1) == sorted(letters2)

ch_to_prime = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13,
    'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43,
    'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79,
    'w': 83, 'x': 89, 'y': 97, 'z': 101 }

def is_anagram_prime(word1:str, word2:str)->bool:
    '''
      Create a dictionary of prime numbers (see chToprime above). Use the ascii value of each letter in both
      words to construct a unique numeric representation of the word (called a 'hash').
      Words with the same hash value are anagrams of each other.

       Args:
        word1 (str): The first word
        word2 (str): The second word

       Returns:
        bool: Returns True if word1 and word2 are anagrams, otherwise returns False
    '''
    word1 = word1.lower()
    word2 = word2.lower()
    if not top_level_checks(word1, word2): return False

    def hash(word:str):
        n = 1
        for c in word:
            n *= ch_to_prime[c]
        return n
    return hash(word1) == hash(word2)


if __name__ == "__main__":
    print(f"There are {len(get_valid_word_list())} valid words with between 2 - 7 letters.")

    algorithms=[is_anagram_exhaustive, is_anagram_checkoff, is_anagram_lettercount, is_anagram_sort, is_anagram_prime]
    word_1 = "baset"
    word_2 = "bastee"

    for algorithm in algorithms:
        print(f"{algorithm.__name__}- {word_1}, {word_2}: {algorithm(word_1, word_2)}")
