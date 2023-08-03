def find_dislikes(friends: dict) -> set[tuple]:
    """Given a dictionary-based adjacency list of String-based nodes,
       returns a set of all edges in the graph (ie. dislikes who can't be invited together).

       An edge should only appear once in the list.
       Each edge should list node connections in alphabetical order.

       Example
       -------
       >>>friends = {
           'Alice':['Bob'],
           'Bob':['Alice', 'Eve'],
           'Eve':['Bob']
       }
       >>>find_dislikes(friends)
       {('Alice','Bob'),('Bob','Eve')}

    """
    dislikes = set()
    for edge in friends.items():
        for node in edge[1]:
            new_edge = tuple(sorted([edge[0], node]))
            dislikes.add(new_edge)

    return dislikes

def lagest_invite_list(invites:list[str], all_friends:list[str], dislike_pairs:set[tuple], Sol:list[str]):
    """
    Input: invites is a (possibly empty) list of guests chosen so far.
           all_friends is a (possibly empty) list of elements yet to consider.
           dinnerCheck(invites, x, dislikes) return True if it is OK to append x to invites.
           Sol is list of all largest Sol found so far.
    Return list of all largest Sol found.
    """
    if len(all_friends) == 0:
        if Sol == [] or len(invites) > len(Sol):
            Sol = invites
        return Sol
    if no_beefs(invites + [all_friends[0]], dislike_pairs):
        Sol = lagest_invite_list(invites + [all_friends[0]], all_friends[1:], dislike_pairs, Sol)
    return lagest_invite_list(invites, all_friends[1:], dislike_pairs, Sol)


def no_beefs(invite_list:list[str], dislike_pairs:set[tuple])->bool:
    '''Validates an invite list for no dislike pairs

       Args:
         invite_list (list[str]): a list of string names of friends who are invited to the party
         dislike_pairs (set[tuple]): a set of tuple-based dislike pairs

       Returns:
         True/False based on whether invite_list contains no dislike pairs
    '''
    good = True
    for j in dislike_pairs:
        if j[0] in invite_list and j[1] in invite_list:
            good = False
    return good

if __name__ == "__main__":
    
    graph={
        'A': [],
        'B': ['C'],
        'C': ['B', 'D'],
        'D': ['C', 'E'],
        'E': ['D'],
        'F': ['G', 'H', 'I'],
        'G': ['F', 'H'],
        'H': ['F', 'G'],
        'I': ['F']
    }

    dislike_pairs=find_dislikes(graph)
    guest_list = list(graph.keys())

    best_guest_list = lagest_invite_list([], guest_list, dislike_pairs, [])
    print(best_guest_list)
