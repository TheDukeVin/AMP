from itertools import combinations

class AnagramExplorer_solution:
    def __init__(self, all_words:list[str]):
       self.__corpus = all_words
       self.anagram_lookup = self.get_sorted_hash_dict() #only calculated once, when the object is created

    @property
    def corpus(self):
      return self.__corpus

    def is_valid_anagram_pair(self, pair:tuple[str], letters:list[str])-> bool:
       '''Checks whether a pair of words:
            -are both included in the allowable word list (self.corpus)
            -consist entirely of letters chosen at the beginning of the game
            -form a valid anagram pair

            Args:
                pair: A tuple of two strings
                letters: The letters from which the anagrams should be created

            Returns:
                bool: Returns True if the word pair fulfills all validation requirements, otherwise returns False
       '''
       if len(pair[0]) != len(pair[1]): return False

       w1, w2 = pair[0].lower(), pair[1].lower()
       if w1 == w2: return False

       if w1 not in self.corpus: return False
       if w2 not in self.corpus: return False
       
       if sorted(w1) != sorted(w2): return False

       letters_copy = letters[:]
       for letter in w1:
         if letter not in letters_copy:
            return False
         else:
            letters_copy.remove(letter)

       return True
        
    def get_sorted_hash_dict(self)-> dict:
        '''needs comments'''
        lookup = {}
        for word in self.corpus:
            word = word.lower()
            sorted_key = tuple(sorted(word))
            if sorted_key not in lookup:
                lookup[sorted_key] = [word]
            else:
                lookup[sorted_key].append(word)
        return lookup

    def get_all_anagrams(self, letters:list[str])->set:
        '''Creates a set of all unique words that could have been used to form an anagram pair.
           Words which can't create any anagram pairs should not be included in the set.

           Ex)
            corpus: ["abed","mouse", "bead", "baled", "abled", "rat", "blade"]
            allAnagrams = {"abed",  "abled", "baled", "bead", "blade"}

           Args:
              letters (list): A list of letters from which the anagrams should be created

           Returns:
              set: all unique words in wordlist which form at least 1 anagram pair
        '''
        all_anagrams=set()

        combos=[]
        for i in range(3, len(letters)+1):
          combos += list(combinations(letters, i))

        for combo in combos:
          anagram_key = tuple(sorted(combo))
          if anagram_key in self.anagram_lookup and len(self.anagram_lookup[anagram_key])>1:
            for word in self.anagram_lookup[anagram_key]:
                all_anagrams.add(word)

        return all_anagrams

    def get_most_anagrams(self, letters:list[str])-> str:
        '''returns a word from the largest list of anagrams that can be formed using the given letters'''
        mostAnagrams=[]
        most = 0

        for i in range(3, len(letters)+1):
         combos = list(combinations(letters, i))

         for combo in combos:
             hash_key=tuple(sorted(combo))
             if hash_key in self.anagram_lookup and len(self.anagram_lookup[hash_key])>1:
                anagram_list = self.anagram_lookup[hash_key]
                if len(anagram_list) > most:
                    most = len(anagram_list)
                    mostAnagrams= anagram_list
                elif len(anagram_list) == most:
                    mostAnagrams += anagram_list

        return mostAnagrams[0]

if __name__ == "__main__":
  print("Running AnagramExplorer for testing")
  words1 = ["abed","abet","abets","abut","acme","acre","acres","actors","actress","airmen","alert","alerted","ales","aligned","allergy","alter","altered","amen","anew","angel","angle","antler","apt",
    "bade","baste","bead","beast","beat","beats","beta","betas","came","care","cares","casters","castor","costar","dealing","gallery","glean","largely","later","leading","learnt","leas","mace","mane",
    "marine","mean","name","pat","race","races","recasts","regally","related","remain","rental","sale","scare","seal","tabu","tap","treadle","tuba","wane","wean"]

  words2 = ["rat", "mouse", "tar", "art", "chicken", "stop", "pots", "tops" ]

  letters = ["l", "o", "t", "s", "r", "i", "a"]

  my_explorer = AnagramExplorer_solution(words2)

  print(my_explorer.is_valid_anagram_pair(("rat", "tar"), letters))
  print(my_explorer.is_valid_anagram_pair(("stop", "pots"), letters))
  print(my_explorer.get_most_anagrams(letters))
  print(my_explorer.get_all_anagrams(letters))
