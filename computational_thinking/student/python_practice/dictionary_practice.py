"""
Practice with python dictionaries
"""

def room_assignment_demo():
    room_assignments = {"Alice": 302, "Bob": 212, "Chelsea": 721, "Dylan": 318, "Eileen": 519}
    # NOTE: dictionaries don't keep track of what order you put the items in
    print(f"The following people live in this building: {list(room_assignments.keys())}")
    print(f"The following rooms are occupied: {list(room_assignments.values())}")
    for resident in room_assignments:
        print(f"{resident} lives in room {room_assignments[resident]}.")

def tally_votes(votes:list[str])->dict:
    '''Takes a list of votes and returns a dictionary of how many votes each option got

        Args:
          votes (list): A list of all votes

        Returns:
          dict: A dictionary mapping each unique option to how many votes it got

        Examples
      ----------
      >>>tally_votes(["pizza", "pasta", "pasta", "salad", "pizza", "pizza"])
      {"pizza": 3, "pasta": 2, "salad": 1}
    '''
    tallies = {} # empty dictionary
    for vote in votes:
        if vote in tallies:
            tallies[vote] += 1
        else:
            tallies[vote] = 1
    return tallies

# EXERCISE
def words_by_length(words:list[str])->dict:
    '''Organizes a list of words by length of word (in letters)

        Args:
          words (list): A list of words

        Returns:
          dict[int, list[str]]: A dictionary mapping word length to a list of words of that length

        Examples
      ----------
      >>>words_by_length(["cat", "porcupine", "pun", "king", "jump", "trek"])
      {2: ["cat", "pun"], 9: ["porcupine"], 4: ["king", "jump", "trek"]}
    '''
    # Your code here!


if __name__ == "__main__":
    room_assignment_demo()
    print(tally_votes(["pizza", "pasta", "pasta", "salad", "pizza", "pizza"]))
    print(words_by_length(["cat", "porcupine", "pun", "king", "jump", "trek"]))