"""The following puzzle is derived from Programming for the Puzzled by Srini Devadas"""

def make_change(bills, target):
    """
    Find the different ways to make change treating bills of the same denomination
    as identical. This time, its ok (in fact we want) to have repeat solutions!

    Example:
    >>> make_smart_change([1, 2, 5], 6))
    [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 2], [1, 1, 1, 2, 1], [1, 1, 2, 1, 1], \
        [1, 1, 2, 2], [1, 2, 1, 1, 1], [1, 2, 1, 2], [1, 2, 2, 1], [1, 5], \
        [2, 1, 1, 1, 1], [2, 1, 1, 2], [2, 1, 2, 1], [2, 2, 1, 1], [2, 2, 2], [5, 1]]
    """

    def helper(bills, target, sol, all_sols):
        #Recursion base case -- reached the target
        if sum(sol) == target:
            all_sols.append(sol)
            return

        #Recursion base case -- exceeded the target
        if sum(sol) > target:
            return

        #Recursive calls: explore adding each bill denomination
        for bill in bills:
            newSol = sol[:]
            newSol.append(bill)
            helper(bills, target, newSol, all_sols)
    
    # Initialize the list to store all solutions
    all_solutions = []
    
    # Call the helper function
    helper(bills, target, [], all_solutions)
    
    return all_solutions

def make_smart_change_best(money, target, highest, sol=[], bestSol=[]):
    """
    Find the different ways to make change treating
    bills of the same denomination as identical, while respecting a limit to 
    coin usage.
    
    For example, money = [(1, 3), (2, 3), (5, 1)] means that there are 3 $1 bills,
    3 $2 bills, and 1 $5 bill. These limits need to respected during solution generation

    Return exactly one solution corresponding to the fewest number of
    bills used. Store only one solution -- the current best solution found.

    >>> make_smart_change_best([(1, 3), (2, 3), (5, 1)], 6, 1)
    [1,5]
    """


    #Recursion base case -- reached the target
    if sum(sol) == target:
        if len(bestSol) == 0:
            bestSol = sol
        elif len(bestSol) > len(sol):
            bestSol = sol
        else:
            pass
        return bestSol

    #Recursion base case -- exceeded the target
    if sum(sol) > target:
        return bestSol

    #Recursive calls: explore adding each bill denomination
    #Money is a list of 2-tuples, the first item is the denomination,
    #the second is the count
    for (bill, count) in money:
        #Add bill only if bill denomination is high enough
        #and if there are enough bills available
        bcount = 0
        for b in sol:
            if b == bill:
                bcount += 1
        if bill >= highest and bcount < count:
            newSol = sol[:]
            newSol.append(bill)
            bestSol = make_smart_change_best(money, target, bill, newSol, bestSol)

    return bestSol


def count_change(money, length, target): 
    """
    Recursive code that counts the number of solutions without enumerating solutions.

    Example:
    >>> count_change(money, len(money), 6) 
    5
    >>> count_change(bills2, len(bills2), 16)
    25

    """

    # Recursion base case -- reached the target
    if target == 0:
        return 1

    # Recursion base case -- no solution exists
    if target < 0:
        return 0

    # Recursion base case -- no solution exists
    # don't have the bills to pay
    if length <= 0 and target > 0:
        return 0

    # Recursive calls: explore adding each bill denomination
    skip = count_change(money, length-1, target)
    pick = count_change(money, length, target - money[length-1])

    return skip + pick

if __name__ == "__main__":
    '''
    
    bills = [1, 2, 3, 4, 5]
    # Sort the inner lists
    sorted_inner_lst = [sorted(x) for x in make_change(bills, 10)]

    # Convert sorted lists to tuples
    tuple_lst = [tuple(x) for x in sorted_inner_lst]

    # Remove duplicates
    unique_sorted_tuples = list(set(tuple_lst))

    # Sort the list of unique tuples
    final_sorted_unique_tuples = sorted(unique_sorted_tuples)

    # print the final list
    print(final_sorted_unique_tuples)
    '''
    print(make_smart_change_best([(1, 11), (2, 7), (5, 9), (10, 10), (20, 4)], 9,1))
 