import itertools
from valid_word_list import get_valid_word_list # only words with 2 - 7 letters
#from TimingProfiler2 import TimingProfiler


def top_level_checks(word1:str, word2:str)-> tuple[bool, str, str]:

    '''
        This function implements top-level checks common to each is_anagram approach
        Highly-recommended to create this function.

        Could return bool, though a more streamlined process would also return lowercase versions of each word along with a boolean
    '''

    
   
def is_anagram_exhaustive(word1:str, word2:str)->bool:
    '''Generate all possible permutations of the first word until you find one that is the second word.
       If no permutation of the first word equals the second word, the two are not anagrams.

       Args:
        word1: The first word
        word2: The second word

       Returns:
        Returns True if word1 and word2 are anagrams, otherwise returns False
    '''
    return False

def is_anagram_checkoff(word1:str, word2:str)->bool:
    '''Create a parallel list-based version of the second word (strings are immutable).
       Check off letters in the list as they are found by setting the value to None.

       Args:
        word1: The first word
        word2: The second word

       Returns:
        bool: Returns True if word1 and word2 are anagrams, otherwise returns False
    '''
    return False


def is_anagram_lettercount(word1:str, word2:str)->bool:
    '''Two approaches:
      Approach 1) Create two lists of length 26 to keep track of letter counts in each word.
                    ie. [0] represents the letter a, [1] represents the letter b, and so on…
                  HINT- ASCII conversions will be helpful: ord("A") → 65. chr(65)  -> “A”
 
      Approach 2) Create two dictionaries  to keep track of letter counts in each word.

      Compare final versions of each list to determine if the words are anagrams.
      
       Args:
        word1 (str): The first word
        word2 (str): The second word

       Returns:
        bool: Returns True if word1 and word2 are anagrams, otherwise returns False
    '''
    return False


def is_anagram_sort(word1:str, word2:str)->bool:
    '''
      Sort both words, then compare to see if they are exactly the same.

       Args:
        word1 (str): The first word
        word2 (str): The second word

       Returns:
        bool: Returns True if word1 and word2 are anagrams, otherwise returns False
    '''
    return False

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
    return False


if __name__ == "__main__":
    print(f"There are {len(get_valid_word_list())} valid words with between 2 - 7 letters.")
    algorithms = [is_anagram_exhaustive, is_anagram_checkoff, is_anagram_lettercount, is_anagram_sort, is_anagram_prime]
    word1 = "beast"
    word2 = "baste"

    for algorithm in algorithms:
        print(f"{algorithm.__name__}- {word1}, {word2}: {algorithm(word1, word2)}")
    
    '''
    inputs=[("eat","ate"), ("tale", "late"), ("sneak", "snake"), ("actors", "costar"), ("allergy", "gallery"), ("calipers", "replicas"), ("cautioned", "education"), ("percussion", "supersonic"), ("calligraphy", "graphically")]
    trials = 10

    experiment = TimingProfiler(algorithms, inputs, trials)
    experiment.run_experiments()
    # print(experiment.results)
    experiment.graph(title="is_anagrams Timings", scale="linear")
    '''
