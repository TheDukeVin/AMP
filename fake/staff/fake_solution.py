"""The following puzzle is derived from Programming for the Puzzled by Srini Devadas"""

def split_eggs(basket:list[int])-> tuple[list[int], list[int], list[int]]:
    """Splits a basket of eggs into 3 groups of equal size.
       Assumes that the number of eggs in the basket is a power of 3.

        Args:
         basket (list[int]): A list of integer weights for each egg in the basket

        Returns:
         list1: a list of first third of egg weights in the basket
         list2: a list of middle third of egg weights in the basket
         list3: a list of last third of egg weights in the basket

        Example
        -------
        >>>split_eggs([10, 10, 10, 11, 10, 10, 10, 10, 10])
        [10,10,10], [11, 10, 10], [10, 10, 10]
    """
    length = len(basket)

    group1 = basket[0 : length // 3]
    group2 = basket[length // 3 : length // 3 * 2]
    group3 = basket[length // 3 * 2 : length]

    return group1, group2, group3


def compare_egg_groups(left_group:list[int], right_group:list[int])-> str:
    """ Compares the weight of 2 groups like a balance. 
        Calling the compare function counts as 1 weighing.
        
        Args:
         left_group (list[int]): A list of integer weights for the eggs on the left side of the balance
         right_group  (list[int]): A list of integer weights for the eggs on the right side of the balance

        Returns:
         "left", "right", or "equal" depending on which group is heavier

        Example
        -------
        >>>compare_egg_groups([10,10,10], [11, 10, 10])
        "right"
    """
    if sum(left_group) > sum(right_group): return "left"
    elif sum(right_group) > sum(left_group): return "right"
    else: return "equal"

def find_fake_group(left_group:list[int], right_group:list[int], extra_group:list[int])-> tuple[list[int], str]:
    """ Finds the fake egg group, knowing that the fake egg is heavier
   
        Args:
         left_group (list[int]): A list of integer weights for the eggs on the left side of the balance
         right_group  (list[int]): A list of integer weights for the eggs on the right side of the balance
         extra_group  (list[int]): A list of integer weights for the eggs that aren't being weighed

        Returns:
          the group with the fake egg
         "left", "right", or "equal" depending on which side of the scale is heavier

        Example
        -------
        >>>find_fake_group([10,10,10], [11, 10, 10], [10, 10, 10])
        [11, 10, 10]
        "right"
    """
    result = compare_egg_groups(left_group, right_group)

    if result == 'left': return left_group, 'left'
    elif result == 'right': return right_group, 'right'
    elif result =='equal': return extra_group, 'equal'

def find_heavier_egg_nonrecursive(basket:list[int])-> tuple[int, int]:
    """
    Uses a while loop to repeatedly divide the pile into 3 smaller groups of eggs.
    - Number of eggs in the basket will be equal to a power of 3.
    - There will be either exactly 1 or 0 fake eggs
    - Makes use of provided splitEggs(basket) function to divide eggs into three groups
         -To arrive at the same number of weighings as the autograder, use the given definition of the split_eggs function.

    Args:
     basket (list[int]): A list of egg weights

    Returns:
      the location of the fake egg, along with the number of weighings used to find the egg
        - If there is no fake Egg, return -1 for index
        - If the function is called on an empty basket of eggs, return -1, 0
    """
    if len(basket)==0:
        return -1, 0

    num_weighings = 0
    curr_group  = basket[:]#Make a copy of basket to preserve the original list
                         #This will help us find the location of the fake egg at the end

    while len(curr_group) > 1: #Once you're down to one egg in the group you've found the fake
        group1, group2, group3 = split_eggs(curr_group )
        curr_group , result = find_fake_group(group1, group2, group3)
        num_weighings += 1

    if result == 'equal':
        num_weighings=num_weighings+1
        if compare_egg_groups(curr_group , group1) == 'equal':
            return -1, num_weighings

    fake = curr_group [0]  #The fake is the only egg in the list
    return basket.index(fake), num_weighings


def find_heavier_egg_recursive(basket:list[int], num_weighings=0, orgList=[])-> tuple[int, int]:
    """Uses recursion to repeatedly divide the pile into 3 smaller groups of eggs.
       Assumes:
          - Number of eggs in the basket will be equal to a power of 3.
          - There will be exactly 1 or 0 heavier eggs
          - Makes use of provided splitEggs(basket) function to divide eggs into three groups
            -To arrive at the same number of weighings as the autograder, use the given definition of the split_eggs function.
        
        Args:
          basket (list): A list of egg weights with length equal to a power of 3
          numWeighings (int): The current number of egg weighings
          orgList: (list): The original egglist (used to find the position of the fake egg)

        Returns:
          int: The index of the fake egg in the original list
          int: The number of weighings used to find the egg
          - If there is no fake Egg, return -1 for index
          - If the function is called on an empty basket of eggs, return -1, 0
    """
    if len(basket) == 0:
        return -1, 0

    if len(orgList)==0:
        orgList = basket[:]

    group1, group2, group3 = split_eggs(basket)
    basket, res = find_fake_group(group1, group2, group3)
    num_weighings += 1

    if len(basket) == 1:
        if res == "equal":
            extra = compare_egg_groups(group1, group3)
            num_weighings+=1
            if extra  == "equal":
              return -1, num_weighings
            else:
              return orgList.index(group3[0]), num_weighings
        else:
            return orgList.index(basket[0]), num_weighings
    else:
        return find_heavier_egg_recursive(basket, num_weighings, orgList)


def find_fake_heavier_group(left_group:list[int], right_group:list[int], extra_group:list[int])->list[int]:
    '''
    find_lighter_or_heavier_egg helper function
    Finds the fake coin group, knowing that the fake coin is heavier
    '''
    result = compare_egg_groups(left_group, right_group)

    match result:
       case 'left':
         return left_group
       case 'right':
         return right_group
       case 'equal':
         return extra_group
       case '_':
         return []

def find_fake_lighter_group(left_group:list[int], right_group:list[int], extra_group:list[int]):
    '''
    find_lighter_or_heavier_egg helper function
    Finds the fake coin group, knowing that the fake coin is lighter
    '''
    result1and2 = compare_egg_groups(left_group, right_group)

    if result1and2 == 'left':
       return right_group
    elif result1and2 == 'right':
       return left_group
    else:
       return extra_group

def find_fake_group_and_type(group1, group2, group3):
    '''
    find_lighter_or_heavier_egg helper function
    finds out if the fake coin is lighter or heavier and finds out which group it's in
    This requires two weighings or comparisons
    '''
    result1and2 = compare_egg_groups(group1,group2)

    if result1and2 == 'left':
        result1and3 = compare_egg_groups(group1,group3)
        if result1and3 == 'left':
            fakeGroup = group1
            weightComparison = 'heavier'
        elif result1and3 == 'equal':
            fakeGroup = group2
            weightComparison = 'lighter'
    elif result1and2 == 'right':
        result1and3 = compare_egg_groups(group1,group3)
        if result1and3 == 'right':
            fakeGroup = group1
            weightComparison = 'lighter'
        elif result1and3 == 'equal':
            fakeGroup = group2
            weightComparison = 'heavier'
    elif result1and2 == 'equal': #Could just be an else
        result1and3 = compare_egg_groups(group1,group3)
        if result1and3 == 'right':
            fakeGroup = group3
            weightComparison = 'heavier'
        elif result1and3 == 'left':
            fakeGroup = group3
            weightComparison = 'lighter'
        else:
            #There is no fake coin!
            fakeGroup = group2
            weightComparison = 'no fake'
    return fakeGroup, weightComparison

def find_lighter_or_heavier_egg(basket:list[int])-> tuple[str, int]:
    """Determines which egg (if any) is a fake, as well as the type of fake
       
       Assumes:
          - Number of eggs in the basket will be equal to a power of 3.
          - There will be exactly 1 or 0 heavier or lighter eggs
          - Makes use of provided splitEggs(basket) function to divide eggs into three groups

        Args:
          basket (list): A list of egg weights with length equal to a power of 3

        Returns:
          str: a label indicating which type of fake egg has been found: 'heavier', 'lighter', or 'no fake'
          int: The index of the fake egg in the original list
          - If there is no fake Egg, return 'no fake', -1
          - If the function is called on an empty basket of eggs, return 'no fake', -1
    """
    if len(basket)<1:
        return "no fake", -1

    num_weighings = 0
    curr_group  = basket[:]
    while len(curr_group ) > 1:
        group1, group2, group3 = split_eggs(curr_group )
        if num_weighings == 0:
            curr_group , wtype = find_fake_group_and_type(group1, group2, group3)
            num_weighings += 2 #requires 2 weighings
        else:
            #We know that the fake is either heavier or lighter
            if wtype == 'heavier':
                curr_group  = find_fake_heavier_group(group1, group2, group3)
                num_weighings += 1 #requires 1 weighing
            elif wtype == 'lighter':
                curr_group  = find_fake_lighter_group(group1, group2, group3)
                num_weighings += 1 #requires 1 weighing
            else:
                return "no fake", -1

    if wtype=="no fake":
        return "no fake", -1

    fake = curr_group [0]

    return wtype, basket.index(fake)


if __name__ == "__main__":
    basket1 = [10, 10, 10, 11, 10, 10, 10, 10, 10]
    basket2 = [10, 10, 10, 10, 10, 11, 10, 10, 10]

    basket3 = [10, 10, 10, 10, 10, 10, 10, 10, 10,
                10, 10, 10, 10, 10, 10, 10, 10, 10,
                10, 10, 10, 10, 11, 10, 10, 10, 10]

    #index, number_of_weighings = find_heavier_egg_nonrecursive(basket1)
    index, number_of_weighings = find_heavier_egg_nonrecursive([10, 10, 10, 10, 10, 10, 10, 10, 10])
    #type, index = find_lighter_or_heavier_egg(basket1)
    print(f"The fake egg has index of {index} in the basket")
    print(f"Number of weighings: {number_of_weighings}")
    #print(type)

    find_heavier_egg_recursive([10, 10, 10, 10, 10, 11, 10, 10, 10])