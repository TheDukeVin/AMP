"""The following puzzle is derived from Programming for the Puzzled by Srini Devadas"""

def find_dislikes(friends: dict)->set[tuple]:
    """Given a dictionary-based adjacency list of String-based nodes,
       returns a set of all edges in the graph (ie. dislikes who can't be invited together).

       An edge should only appear once in the list.

       Example
       -------
       >>>friends={
           'Alice':['Bob'],
           'Bob':['Alice', 'Eve'],
           'Eve':['Bob']
       }
       >>>find_dislikes(friends)
       [['Alice','Bob'],['Bob','Eve']]

    """
    edges = set()
    for edge in friends.items():
        for node in edge[1]:
            new_edge=tuple(sorted([edge[0], node]))
            edges.add(tuple(sorted(new_edge)))

    return edges

def generate_all_subsets(friends: list[str])->list[str]:
    '''Converts each number from 0 to 2^n - 1 into binary and uses the binary representation
       to determine the combination of guests and returns all possible combinations
       TODO: Needs comments
    '''
    friend_list = list(friends.keys())
    n = len(friends)
    
    all_subsets = []

    for i in range(2**n):
        num = i  #convert each number in the range to a binary string
        new_subset = []
        for j in range(n): # to_binary_division approach
            if (num % 2 == 1): # 1 indicates the guest is included
                new_subset = [friend_list[n-1-j]] + new_subset 
            num = num // 2
        all_subsets.append(new_subset)

    return all_subsets


def filter_bad_invites(all_subsets:list, friends:dict)-> list:
    '''Removes subsets from all_subsets that contain any pair of friends who
       are in a dislike relationship

       Example
       -------
       >>>all_subsets = [[], ['Eve'], ['Bob'], ['Bob', 'Eve'], ['Alice'], ['Alice', 'Eve'], ['Alice', 'Bob'], ['Alice', 'Bob', 'Eve']]
       >>>friends={
        'Alice':['Bob'],
        'Bob':['Alice'],
        'Eve':[]
       }  
       >>>filter_bad_invites(all_subsets, friends)
       [[], ['Eve'], ['Bob'], ['Bob', 'Eve'], ['Alice'], ['Alice', 'Eve']]
    '''
    good_invites = []

    dislike_pairs = find_dislikes(friends)

    for subset in all_subsets:
        good = True
        for dislike in dislike_pairs:
            if dislike[0] in subset and dislike[1] in subset:
                good = False
        if good:
            good_invites.append(subset)

    return good_invites

def filter_no_dislikes(friends:dict)->tuple[list, dict]:
    '''Removes friends who are not in any dislikes relationships.
       Also returns a reduced friends graph without the removed friends
        
       Examples
       -------
       >>>friends={
        'Alice':['Bob'],
        'Bob':['Alice'],
        'Eve':[]
       }  
       >>>filter_no_dislikes(friends)
       ['Eve']
       {
        'Alice':['Bob'],
        'Bob':['Alice']
       }  
    '''
    no_dislikes = []
    new_friends = {}

    dislike_pairs = find_dislikes(friends)
    guest_list = list(friends.keys())

    for guest in guest_list:
        stay = False
        for pair in dislike_pairs:
            if guest in pair:
                stay = True
        if stay == True:
            new_friends[guest] = friends[guest]
        else:
            no_dislikes.append(guest)

    return no_dislikes, new_friends


def invite_to_dinner(friends: dict):
    '''Finds the invite combo with the maximum number of guests
       TODO: Needs comments
    '''
    definite_invites, problem_friends = filter_no_dislikes(friends)
    all_subsets = generate_all_subsets(problem_friends)
    good_subsets = filter_bad_invites(all_subsets, problem_friends)

    #find the subset which maximizes number of invites
    invite_list = []
    for i in good_subsets:
        if len(i) > len(invite_list):
            invite_list = i

    #recombine with definite invites
    invite_list += definite_invites

    return invite_list

def invite_to_dinner_optimized(friends:dict)->list:
    '''Finds the combination with the maximum number of guests without storing all combinations
       TODO: Needs comments
    '''
    invite_list = []

    guest_list = list(friends.keys())
    n = len(guest_list)
    dislike_pairs = find_dislikes(friends)
    
    for i in range(2**n):
        potential_invite_list = []
        num = i
        for j in range(n):
            if (num % 2 == 1):
                potential_invite_list = [guest_list[n-1-j]] + potential_invite_list
            num = num // 2
        #Check that it is a good combination
        good = True
        for j in dislike_pairs:
            #Check that each element of j is in i
            if j[0] in potential_invite_list and j[1] in potential_invite_list:
                good = False
        if good:
            #Check if it is the best combination so far
            if len(potential_invite_list) > len(invite_list):
                invite_list = potential_invite_list

    return invite_list

if __name__ == "__main__":
    friends={
        'Alice':['Bob'],
        'Bob':['Alice', 'Eve'],
        'Cleo':[],
        'Don':[],
        'Eve':['Bob']
    }
    print(find_dislikes(friends))
    print(invite_to_dinner(friends))
    print(invite_to_dinner_optimized(friends))

    friends_2={
        'Alice':['Bob'],
        'Bob':['Alice', 'Eve'],
        'Eve':['Bob']
    }
    print(find_dislikes(friends_2))

    #print(invite_to_dinner(friends_2))
    #print(invite_to_dinner_optimized(friends_2))

    friends_3={
        'Asa':[], 
        'Bear':['Cate'],
        'Cate':['Bear', 'Dave'],
        'Dave':['Cate','Eve'], 
        'Eve':['Dave'], 
        'Finn':['Ginny', 'Haruki', 'Ivan'], 
        'Ginny':['Finn','Haruki'], 
        'Haruki':['Ginny'], 
        'Ivan':['Finn']
    }
    print(find_dislikes(friends_3))

    #print(invite_to_dinner(friends_3))
    #print(invite_to_dinner_optimized(friends_3))
    friends_4={
        'Alice':['Bob'],
        'Bob':['Alice'],
        'Eve':[]
    }

    s=generate_all_subsets(friends_2)
    print(s)
    print(filter_bad_invites(s, friends_2))
    print(invite_to_dinner(friends_4))
    print(invite_to_dinner_optimized(friends_4))