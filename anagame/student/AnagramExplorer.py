from itertools import combinations

class AnagramExplorer:
    def __init__(self, all_words: list[str]):
       self.__corpus = all_words
       self.anagram_lookup = self.get_lookup_dict() # Only calculated once, when the object is created

    @property
    def corpus(self):
      return self.__corpus

    def is_valid_anagram_pair(self, pair:tuple[str], letters:list[str]) -> bool:
       '''Checks whether a pair of words:
            -are both included in the allowable word list (self.corpus)
            -are both at least 3 letters long
            -consist entirely of letters chosen at the beginning of the game
            -form a valid anagram pair

            Args:
                pair: A tuple of two strings
                letters: The letters from which the anagrams should be created

            Returns:
                bool: Returns True if the word pair fulfills all validation requirements, otherwise returns False
       '''
    
       return True
        
    def get_lookup_dict(self) -> dict:
        '''Creates a fast dictionary look-up (via prime hash or sorted tuple) of all anagrams in a word corpus.
       
        Args:
            corpus (list): A list of words which should be considered

        Returns:
            dict: Returns a dictionary with  keys that return sorted lists of all anagrams of the key (per the corpus)
        '''
        lookup = {}
        
        return lookup

    def get_all_anagrams(self, letters: list[str]) -> set:
        '''Creates a set of all unique words that could have been used to form an anagram pair.
           Words which can't create any anagram pairs should not be included in the set.

           Ex)
            corpus: ["abed", "mouse", "bead", "baled", "abled", "rat", "blade"]
            all_anagrams: {"abed",  "abled", "baled", "bead", "blade"}

           Args:
              letters (list): A list of letters from which the anagrams should be created

           Returns:
              set: all unique words in corpus which form at least 1 anagram pair
        '''
        all_anagrams = set()

        return all_anagrams

    def get_most_anagrams(self, letters:list[str]) -> str:
        '''Returns a word from one of the largest lists of anagrams that can be formed using the given letters.'''
        most_anagrams = []
      
        return most_anagrams[0]

if __name__ == "__main__":
  print("Running AnagramExplorer for testing")
  words1 = [
     "abed","abet","abets","abut","acme","acre","acres","actors","actress","airmen","alert","alerted","ales","aligned","allergy","alter","altered","amen","anew","angel","angle","antler","apt",
     "bade","baste","bead","beast","beat","beats","beta","betas","came","care","cares","casters","castor","costar","dealing","gallery","glean","largely","later","leading","learnt","leas","mace","mane",
     "marine","mean","name","pat","race","races","recasts","regally","related","remain","rental","sale","scare","seal","tabu","tap","treadle","tuba","wane","wean"
  ]

  words2 = ["rat", "mouse", "tar", "art", "chicken", "stop", "pots", "tops" ]

  letters = ["l", "o", "t", "s", "r", "i", "a"]

  my_explorer = AnagramExplorer(words2)

  print(my_explorer.is_valid_anagram_pair(("rat", "tar"), letters))
  print(my_explorer.is_valid_anagram_pair(("stop", "pots"), letters))
  print(my_explorer.get_most_anagrams(letters))
  print(my_explorer.get_all_anagrams(letters))