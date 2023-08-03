"""The following puzzle is derived from Programming for the Puzzled by Srini Devadas"""

def find_dislikes(friends: dict)->set[tuple]:
    """Given a dictionary-based adjacency list of String-based nodes,
       returns a set of all edges in the graph (ie. dislikes who can't be invited together).

       An edge should only appear once in the list.
       Each edge should list node connections in alphabetical order.

       Example
       -------
       >>>friends={
           'Alice':['Bob'],
           'Bob':['Alice', 'Eve'],
           'Eve':['Bob']
       }
       >>>find_dislikes(friends)
       [('Alice','Bob'),('Bob','Eve')]

    """
    dislikes = set()

    for key, adj in friends.items():
        for other in adj:
            dislikes.add((key, other) if key < other else (other, key))
   
    return dislikes

def generate_all_subsets(friends: list[str])->list[str]:
    '''Converts each number from 0 to 2^n - 1 into binary and uses the binary representation
       to determine the combination of guests and returns all possible combinations

       Example
       -------
       >>>friends={
           'Alice':['Bob'],
           'Bob':['Alice', 'Eve'],
           'Eve':['Bob']
       }
       >>>generate_all_subsets(friends)
       [[], ['Eve'], ['Bob'], ['Bob', 'Eve'], ['Alice'], ['Alice', 'Eve'], ['Alice', 'Bob'], ['Alice', 'Bob', 'Eve']]
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
    '''Checks the given combinations to see if the combination contains any pair of guests
       who dislike each other and removes the combination if that is the case

       Example
       -------
       >>>friends={
           'Alice':['Bob'],
           'Bob':['Alice', 'Eve'],
           'Eve':['Bob']
       }
       >>>filter_bad_invites(generate_all_subsets(friends), friends)
       [[], ['Eve'], ['Bob'], ['Alice'], ['Alice', 'Eve']]
    '''
    good_invites = []

    for subset in all_subsets:
        valid = True
        for key, adj in friends.items():
            for other in adj:
                if key in subset and other in subset:
                    valid = False
        if valid:
            good_invites.append(subset)

    return good_invites

def filter_no_dislikes(friends:dict)->tuple[list, dict]:
    '''An optimization that removes friends who are not in any dislikes relationships,
       prior to generating combinations and add them to the invite list.

       Parameters:
           friends: dictionary-based adjacency matrix representing friend relations
       
       Returns tuple containing:
           list of friends not in dislike relations AND 
           resulting dictionary with these friends removed

       Example
       -------
       >>>friends={
           'Alice':['Bob'],
           'Bob':['Alice', 'Eve'],
           'Cleo':[],
           'Don':[],
           'Eve':['Bob']
       }
       >>>filter_no_dislikes(friends)
       (['Cleo', 'Don'], {'Alice': ['Bob'], 'Bob': ['Alice', 'Eve'], 'Eve': ['Bob']})
    '''
    no_dislikes = []
    new_friends = {}

    for key, adj in friends.items():
        if len(adj) == 0:
            no_dislikes.append(key)
        else:
            new_friends[key] = adj

    return no_dislikes, new_friends


def invite_to_dinner(friends: dict):
    '''Finds the invite combo with the maximum number of guests

       Example
       -------
       >>>friends={
           'Alice':['Bob'],
           'Bob':['Alice', 'Eve'],
           'Cleo':[],
           'Don':[],
           'Eve':['Bob']
       }
       >>>invite_to_dinner(friends)
       ['Alice', 'Eve', 'Cleo', 'Don']
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

       Functions the same as invite_to_dinner without storing all subsets
       i.e. invite_to_dinner stores the variable all_subsets
    '''
    invite_list = []

    return invite_list

if __name__ == "__main__":
    friends={
        'Alice':['Bob'],
        'Bob':['Alice', 'Eve'],
        'Cleo':[],
        'Don':[],
        'Eve':['Bob']
    }
    print(filter_no_dislikes(friends))
    print(invite_to_dinner(friends))
    print(invite_to_dinner_optimized(friends))

    friends_2={
        'Alice':['Bob'],
        'Bob':['Alice', 'Eve'],
        'Eve':['Bob']
    }
    print("YO")
    print(invite_to_dinner(friends_2))
    print(invite_to_dinner_optimized(friends_2))

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
    print(invite_to_dinner(friends_3))
    print(invite_to_dinner_optimized(friends_3))