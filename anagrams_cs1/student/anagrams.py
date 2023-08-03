import itertools
from valid_word_list import get_valid_word_list # only words with 2 - 7 letters
#from TimingProfiler2 import TimingProfiler


def top_level_checks(word1:str, word2:str) -> tuple[bool, str, str]:
    """
    This function implements top-level checks common to each is_anagram approach.
    Returns the boolean False if this pair is definitely NOT a valid pair,
    along with lowercase versions of each word.
    """
    pass

def is_anagram_lettercount(word1: str, word2: str) -> bool:
    """
    Create two dictionaries to keep track of letter counts in each word.

    Compare final versions of each list to determine if the words are anagrams.
    
    Args:
        word1 (str): The first word
        word2 (str): The second word

    Returns:
        bool: Returns True if word1 and word2 are anagrams, otherwise returns False
    """
    return False

ch_to_prime = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13,
    'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43,
    'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79,
    'w': 83, 'x': 89, 'y': 97, 'z': 101 }

def is_anagram_prime(word1: str, word2: str) -> bool:
    """
    Create a dictionary of prime numbers (see ch_to_prime below). Use the ascii value of each letter in both
    words to construct a unique numeric representation of the word (called a 'hash').
    Words with the same hash value are anagrams of each other.

    Args:
        word1 (str): The first word
        word2 (str): The second word

    Returns:
        bool: Returns True if word1 and word2 are anagrams, otherwise returns False
    """
    return False

def is_anagram_exhaustive(word1: str, word2: str) -> bool:
    """
    Generate all possible permutations of the first word until you find one that is the second word.
    If no permutation of the first word equals the second word, the two are not anagrams.

    Args:
        word1: The first word
        word2: The second word

    Returns:
        Returns True if word1 and word2 are anagrams, otherwise returns False
    """
    return False

def is_anagram_checkoff(word1: str, word2: str) -> bool:
    """
    Create a parallel list-based version of the second word (strings are immutable).
    Check off letters in the list as they are found by setting the value to None.

    Args:
        word1: The first word
        word2: The second word

    Returns:
        bool: Returns True if word1 and word2 are anagrams, otherwise returns False
    """
    return False

def is_anagram_sort(word1: str, word2: str) -> bool:
    """
    Sort both words, then compare to see if they are exactly the same.

    Args:
        word1 (str): The first word
        word2 (str): The second word

    Returns:
        bool: Returns True if word1 and word2 are anagrams, otherwise returns False
    """
    return False

prime_map = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13,
    'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43,
    'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79,
    'w': 83, 'x': 89, 'y': 97, 'z': 101 }

def prime_hash(str):
  hash_value = 1
  for letter in str:
     hash_value *= prime_map[letter]
  return hash_value

def get_prime_hash_dict(corpus):
    """
    Creates a fast dictionary look-up of all anagrams in a word corpus.
    Keys: Prime hash values (ie. each letter mapped to a prime number, then multiplied together)
    Values: alphabetized list of words from the corpus which are all anagrams of each other

    Args:
        corpus (list): A list of words which should be considered

    Returns:
        dict: Returns a dictionary with prime hash keys that return sorted lists of all anagrams of the key (per the corpus)

    Examples
    ----------
    >>>get_prime_hash_dict(["abed", "abled", "bade", "baled", "bead", "blade"])
    {
        462: ["abed", "bade", "bead"],
        17094: ["abled", "baled", "blade"]
    }
    """
    lookup_dict = {}
    return lookup_dict

def find_anagrammiest_word(corpus: list[str]) -> str:
    """
    Finds any one of the words in the corpus that has the MOST valid anagrams.

    Args:
        corpus (list): A list of words which should be considered

    Returns:
        str: The alphabetically first word from the anagram group with the most anagrams.
        If there are multiple groups, can return any one of their first words.

    Examples
    ----------
    >>>get_most_anagrams(["pat", "mouse", "tap", "chicken", "stop", "pots", "tops" ])
    'pots'
       
    """
    
if __name__ == "__main__":
    print(f"There are {len(get_valid_word_list())} valid words with between 2 - 7 letters.")
    algorithms = [is_anagram_exhaustive, is_anagram_checkoff, is_anagram_lettercount, is_anagram_sort, is_anagram_prime]
    word1 = "beast"
    word2 = "baste"

    for algorithm in algorithms:
        print(f"{algorithm.__name__}- {word1}, {word2}: {algorithm(word1, word2)}")
    
    # Comment in the code below to run a timed experiment comparing the different algorithms.
    """
    inputs=[("eat","ate"), ("tale", "late"), ("sneak", "snake"), ("actors", "costar"), ("allergy", "gallery"), ("calipers", "replicas"), ("cautioned", "education"), ("percussion", "supersonic"), ("calligraphy", "graphically")]
    trials = 10

    experiment = TimingProfiler(algorithms, inputs, trials)
    experiment.run_experiments()
    # print(experiment.results)
    experiment.graph(title="is_anagrams Timings", scale="linear")
    """
    print()
    print()

    big_words = ["abed","abet","abets","abut","acme","acre","acres","actors","actress","airmen","alert","alerted","ales","aligned","allergy","alter","altered","amen","anew","angel","angle","antler","apt",
    "bade","baste","bead","beast","beat","beats","beta","betas","came","care","cares","casters","castor","costar","dealing","gallery","glean","largely","later","leading","learnt","leas","mace","mane",
    "marine","mean","name","pat","race","races","recasts","regally","related","remain","rental","sale","scare","seal","tabu","tap","treadle","tuba","wane","wean"]
    baby_words = ["pat", "mouse", "tap", "chicken", "stop", "pots", "tops"]
    print(f"Prime hash lookup dictionary: {get_prime_hash_dict(baby_words)}")
    print()
    most_anagrams = find_anagrammiest_word(big_words)
    print(f"Most anagrams in big_words: {most_anagrams}")
    print()
    most_anagrams = find_anagrammiest_word(baby_words)
    print(f"Most anagrams in baby_words: {most_anagrams}")
