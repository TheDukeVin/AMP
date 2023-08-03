import itertools
from valid_word_list import get_valid_word_list # only words with 2 - 7 letters
#from TimingProfiler2 import TimingProfiler

def top_level_checks(word1:str, word2:str)->bool:
    if len(word1) != len(word2): return False, None, None
    w1 = word1.lower()
    w2 = word2.lower()
    if w1 == w2: return False, None, None
    # Line below commented out because get_valid_word_list() only
    # returns words up to 7 characters.
    # if w1 not in get_valid_word_list() or  w2 not in get_valid_word_list(): return False, None, None
    return True, w1, w2

def is_anagram_exhaustive(word1:str, word2:str)->bool:
    '''Generate all possible permutations of the first word until you find one that is the second word.
       If no permutation of the first word equals the second word, the two are not anagrams.

       Args:
        word1: The first word
        word2: The second word

       Returns:
        Returns True if word1 and word2 are anagrams, otherwise returns False
    '''
    result, w1, w2 = top_level_checks(word1, word2)
    if result == False: return False

    permutations = list(itertools.permutations(w1))
    w2Tuple = tuple(w2)
    return w2Tuple in permutations

def is_anagram_checkoff(word1:str, word2:str)->bool:
    '''Create a parallel list-based version of the second word (strings are immutable).
       Check off letters in the list as they are found by setting the value to None.

       Args:
        word1: The first word
        word2: The second word

       Returns:
        bool: Returns True if word1 and word2 are anagrams, otherwise returns False
    '''
    result, w1, w2 = top_level_checks(word1, word2)
    if result == False: return False

    checkoff = list(w2)
    for letter in w1: 
        if letter in checkoff:
            w2_index = checkoff.index(letter)
            checkoff[w2_index] = None
        else:
            return False
            
    return True

def is_anagram_lettercount(word1:str, word2:str)->bool:
    '''
      Approach 1) Create two lists of length 26 to keep track of letter counts in each word.
                    ie. [0] represents the letter a, [1] represents the letter b, and so on…
                  HINT- ASCII conversions will be helpful: ord("A") → 65. char(65)  -> “A”
 
      Approach 2) Create two dictionaries  to keep track of letter counts in each word.

      Compare final versions of each list to determine if the words are anagrams.
      
       Args:
        word1 (str): The first word
        word2 (str): The second word

       Returns:
        bool: Returns True if word1 and word2 are anagrams, otherwise returns False
    '''
    result, w1, w2 = top_level_checks(word1, word2)
    if result == False: return False

    letterCount_w1 = [0]*26
    letterCount_w2 = [0]*26
    for i, letter in enumerate(w1):
        letterCount_w1[ord(w1[i]) - 97] += 1
        letterCount_w2[ord(w2[i]) - 97] += 1

    return letterCount_w1 == letterCount_w2

def is_anagram_sort(word1:str, word2:str)->bool:
    '''
      Sort both words, then compare to see if they are exactly the same.

       Args:
        word1 (str): The first word
        word2 (str): The second word

       Returns:
        bool: Returns True if word1 and word2 are anagrams, otherwise returns False
    '''
    result, w1, w2 = top_level_checks(word1, word2)
    if result == False: return False

    return sorted(w1)==sorted(w2)

chToprime = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13,
    'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43,
    'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79,
    'w': 83, 'x': 89, 'y': 97, 'z': 101 }

def prime_hash(str):
    if len(str) == 0:
        return 1
    else:
        return chToprime[str[0]] * prime_hash(str[1:])

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
    #print(chToprime['e']*chToprime['a']*chToprime['t']) -> 11*2*71
    result, w1, w2 = top_level_checks(word1, word2)
    if result == False: return False

    primeW1=1
    primeW2=1
    for i in range(len(w1)):
        letterW1 = w1[i]
        primeW1 = primeW1 * chToprime[letterW1]
        letterW2 = w2[i]
        primeW2 = primeW2 * chToprime[letterW2]

    return primeW1 == primeW2

if __name__ == "__main__":
    print(f"There are {len(get_valid_word_list())} valid words with between 2 - 7 letters.")
    # algorithms=[ is_anagram_exhaustive,is_anagram_checkoff, is_anagram_lettercount, is_anagram_sort, is_anagram_prime]
    algorithms=[is_anagram_checkoff, is_anagram_lettercount, is_anagram_sort, is_anagram_prime]

    word1 = "beast"
    word2 = "baste"

    for algorithm in algorithms:
        print(f"{algorithm.__name__}- {word1}, {word2}: {algorithm(word1, word2)}")

    inputs=[("eat","ate"), ("tale", "late"), ("sneak", "snake"), ("actors", "costar"), ("allergy", "gallery"), ("calipers", "replicas"), ("cautioned", "education"), ("percussion", "supersonic"), ("calligraphy", "graphically"), ("conversationalists", "conservationalists")]
    trials = 10

    experiment = TimingProfiler(algorithms, inputs, trials)
    experiment.run_experiments()
    # print(experiment.results)
    experiment.graph(title="is_anagrams Timings", scale="linear")
