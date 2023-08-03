from valid_word_list import get_valid_word_list

def get_letter_masks(word:str)->list[str]:
    '''Generates a list of letter masks using '*' as a wildcard
        
        Args:
            word (str): the word to convert into a collection of masks

        Returns:
            A list of all the wildcard masks that can be made from the word

        Examples
        --------
        >>>letter_masks("cat")
        ["*at","c*t","ca*"]
    '''
    masks = []
    word = word.lower()
    for i in range(len(word)):
        masks.append(word[:i]+"*"+word[i+1:])
    return masks

def filter_word_list(full_corpus:list[str], word_length:int)->list[str]:
    '''Filters a corpus by word length
        
        Args:
            full_corpus: every potential valid word
            word_length: the length of the words in the word ladder game

        Returns:
            A list of all words from the corpus with length of word_length

        Examples
        --------
        >>>filter_word_list(["cat", "dog", "tiger","giraffe","eel","bird"], 3)
        ["cat", "dog", "eel"]
    '''
    return [w for w in full_corpus if len(w) == word_length]

def build_ladder_graph(word_list:list)->dict:
    '''Creates a dictionary mapping wildcard key letter masks to a set of all possible words 
        that could be formed from this mask.
        Note that, since all words which can be formed from the same mask share an edge, 
        all pairs of words in each set share an edge.

        Args:
            word_list: list of words, all of the same length

        Returns:    
            a dictionary with wildcard keys returning a set of all the 
            words from word_list which fit the wildcard pattern 

        Example
        ------
        >>>word_list=['hope', 'mope', 'nope', 'pipe', 'pole', 'pope', 'rope']
        >>>build_ladder_graph(word_list)
        {
            '*ope': {'nope', 'hope', 'mope', 'pope', 'rope'}, 
            'p*pe': {'pope', 'pipe'},
            'po*e': {'pole', 'pope'},
            'pop*': {'pope'},
            ...
            'nop*': {'nope'}      
        }
    '''
    graph = {}
    for word in word_list:
        for mask in get_letter_masks(word):
            if mask not in graph:
                graph[mask]=set()
            graph[mask].add(word.lower())
    return graph

def shortest_ladder(graph:dict, start:str, target:str, word_list:list[str])->list:
    '''Returns a word ladder with the fewest number of rungs connecting start word with target word

        Args:
            graph: dictionary-based adjacency list of 
            start: the first word on the ladder
            target: the last word on the ladder
            word_list: a list of words where every word is the same length as start and target
        
        Return:
            a list of words forming a complete word ladder with start as teh first element and target as the last element
    '''
    start=start.lower()
    target=target.lower()
    if target not in word_list or start not in word_list: return []
    if start == target: return []

    #explored = set()
    queue = [[start]] # a list of paths explored so far

    while queue:
        old_ladder = queue.pop(0)
        last_rung = old_ladder[-1] #last stop in the path

        for mask in get_letter_masks(last_rung):
            for neighbour in graph[mask]:
                if neighbour not in old_ladder:
                    new_ladder = list(old_ladder) #makes deep copy
                    new_ladder.append(neighbour) #extends path by 1 word
                    queue.append(new_ladder) # puts the path back on the stack to explore

                    if neighbour == target:
                        return new_ladder #first one found -> shortest ladder

    return [] #if this happens there are no solutions

def all_shortest_ladders(graph:dict, start:str, target:str, word_list:list[str])->set[tuple[str]]:
    '''Returns all word ladders with the fewest number of rungs connecting start word with target word

        Args:
            graph: dictionary-based adjacency list of 
            start: the first word on the ladder
            target: the last word on the ladder
            word_list: a list of words where every word is the same length as start and target
        
        Return:
            a set of word ladder tuples, all of which form a complete word ladder from start word to target word in the fewest number of rungs
    ''' 
    start=start.lower()
    target=target.lower()   
    if target not in word_list or start not in word_list: return set()
    if start == target: return set()

    min_length = len(shortest_ladder(graph, start, target, word_list))
    if min_length > 7:
        return set() #5 rungs max for game

    all_min = set()
    queue = [[start]] # a list of paths explored so far

    while queue:
           old_ladder = queue.pop(0)
           last_rung = old_ladder[-1] #last stop in the path

           # If we have already seen one of the shortest ladders:
           # If the current ladder so far (before the target word), plus the
           # the target word, is longer than the known shortest ladder length,
           # we have already seen all the ladders of shortest length, so stop
           # searching.
           if len(old_ladder) + 1 > min_length:
               return all_min

           for mask in get_letter_masks(last_rung):
               for neighbour in graph[mask]:
                   if neighbour not in old_ladder:
                       new_ladder = list(old_ladder) # makes copy
                       new_ladder.append(neighbour) # extends path by 1 word

                       if len(new_ladder) <= min_length:
                         queue.append(new_ladder) # puts the path back on the stack to explore
                       
                       if neighbour == target:
                           if len(new_ladder) == min_length:
                               all_min.add(tuple(new_ladder))
                       
    return all_min


def all_ladders(graph:dict, start:str, target:str, word_list:list[str], max_rungs:int)->set[tuple[str]]:
    '''Returns all word ladders with max_rungs or fewer rungs connecting start word with target word

        Args:
            graph: dictionary-based adjacency list of 
            start: the first word on the ladder
            target: the last word on the ladder
            word_list: a list of words where every word is the same length as start and target
            max_rungs: an in t indicating how many words can be used to connect start word with target word
        
        Return:
            a list of word ladders, all of which form a complete word ladder from start word to target word in the max_rungs or fewer rungs
              If a given pair of words cannot be connected with max_rungs or fewer rungs, then get_all_ladders  returns an empty set.
    ''' 
    start=start.lower()
    target=target.lower()   
    if target not in word_list or start not in word_list: return set()
    if start == target: return set()

    all_ladders = set()
    queue = [[start]] # a list of paths explored so far

    while queue:
        old_ladder = queue.pop(0)
        last_rung = old_ladder[-1] #last stop in the path

        for mask in get_letter_masks(last_rung):
            for neighbour in graph[mask]:
                if neighbour not in old_ladder:
                    new_ladder = list(old_ladder) # makes copy
                    new_ladder.append(neighbour) # extends path by 1 word

                    if neighbour == target:
                        if len(new_ladder) <= max_rungs+2:
                            all_ladders.add(tuple(new_ladder))
                    else:
                        if len(new_ladder) <= max_rungs+1:
                            queue.append(new_ladder) # puts the path back on the stack to explore
                        elif len(new_ladder) > max_rungs+2:
                            # Return because we have started to see longer paths than we want.
                            return all_ladders
                    
    return all_ladders

if __name__ == "__main__":
  #graph = {0: [1, 2, 3], 1: [0, 2], 2: [0, 1, 4], 3: [0], 4:[2]}
  #bfs(graph, 0)
  
  w1="goat"
  w2="raft"
  print(f"\n_____Running on {w1}/{w2}_____")
  word_length = len(w1)
  word_list = filter_word_list(get_valid_word_list(), word_length)
  graph = build_ladder_graph(word_list)
  print(shortest_ladder(graph, w1, w2, word_list))
  print(all_shortest_ladders(graph, w1, w2, word_list))
#   print(all_ladders(graph, w1, w2, word_list, 5))