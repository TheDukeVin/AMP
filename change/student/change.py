def make_unique_change(bills:list[int], target:int):
    """Generates the unique ways to make change treating bills of the same denomination as identical.
       This function should be refactored to include a helper function which accomplishes the rucrusion

       Args:
          bills: a list of 2-tuples where the first item is the denomination, the second is the count
          target: the integer target that should be represetned with change
          sol: a list of integers represetning the current solution configuration

       Returns:
        a list of sorted solutions which make change for a target amount using only denominations 
          found in the bills list
          Note: [1,2,1] and [2,1,1] should be considered the same way to make change for 4.
                [1,1,2] should be the unique solution included in the list

        Example
        -------
        >>> make_unique_change([1, 2, 5], 6))
        [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 2], [1, 1, 2, 2], [1, 5], [2, 2, 2]]
    """
    return []

def make_unique_change_limited_bills(money:list[int], target:int)->list[list[int]]:
    """Find all the ways to make change for a target amount, while respecting a limit to 
       bill usage. For example, money = [(1, 3), (2, 3), (5, 1)] means that there are 3 $1 bills,
       3 $2 bills, and 1 $5 bill. These limits need to respected during solution generation

        Hint: Use a helper function based on your solution to make_unique_change for your recursion.

        Args:
            money: a list of 2-tuples where the first item is the denomination, the second is the count
            target: the integer target that should be represented with change

        Returns:
            a list of sorted lists representing all of the ways to make change for a target amount given 
              a list of bill denominations and counts

        >>> money = [(1, 3), (2, 3), (5, 1)]
        >>> make_unique_change_limited_bills(money, 6)
        [[1, 1, 2, 2], [1, 5], [2, 2, 2]]
    """
    return []

def make_change_fewest_bills(money, target):
    """Find the minimal way to make change for a target amount, while respecting a limit to 
       bill usage.For example, money = [(1, 3), (2, 3), (5, 1)] means that there are 3 $1 bills,
       3 $2 bills, and 1 $5 bill. These limits need to respected during solution generation

        Hint: Use a helper function based on your solution to make_unique_change_limited_bills for your recursion.

        Args:
            money: a list of 2-tuples where the first item is the denomination, the second is the count
            target: the integer target that should be represented with change

        Returns:
            a sorted list representing exactly one solution corresponding to the fewest number of bills 
            needed to make change for a target amount. 

        >>> make_change_fewest_bills([(1, 3), (2, 3), (5, 1)], 6, 1)
        [1,5]
    """
    return []

if __name__=="__main__":
    
    target = 6
    print(f"Making Change for ${target}!")
    infinite_cash = [1, 2, 5]
    make_unique_change(infinite_cash, target)

    limited_cash = [(1, 3), (2, 3), (5, 1)]
    print(make_unique_change_limited_bills(limited_cash, target))
    print(make_change_fewest_bills(limited_cash, target))

    target = 16
    print(f"Making Change for ${target}!")
    limted_cash2=[(1, 11), (2, 7), (5, 9), (10, 10), (20, 4)]
    print(make_unique_change_limited_bills(limited_cash, target))
    print(make_change_fewest_bills(limited_cash, target))