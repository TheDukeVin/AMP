"""The following puzzle is derived from Programming for the Puzzled by Srini Devadas"""

def make_change(bills, target):
    '''Finds the different ways to make change treating bills of the same denomination
       as identical. It repeats some ways.
    '''
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

def make_smart_change(bills, target, highest, sol = []):
    '''Finds the different ways to make change treating
        bills of the same denomination as identical
    '''

    # Recursion base case -- reached the target
    if sum(sol) == target:
        return [sol]

    # Recursion base case -- exceeded the target
    if sum(sol) > target:
        return []

    # Recursive calls: explore adding each bill denomination
    all_solutions = []
    for bill in bills:
        # Add bill only if bill is large enough
        if bill >= highest:
            newSol = sol[:]
            newSol.append(bill)
            all_solutions.extend(make_smart_change(bills, target, bill, newSol))

    return all_solutions

#Exercise 2: The number of bills of each denomination is limited.
#For example, money = [(1, 3), (2, 3), (5, 1)] means that there are 3 $1 bills,
# 3 $2 bills, and 1 $5 bill. These limits need to respected during
#solution generation.

def make_smart_change_limited_bills(money, target, highest, sol = []):
    '''Finds the different ways to make change treating
        bills of the same denomination as identical, and each bill as unique
    '''

    #Recursion base case -- reached the target
    if sum(sol) == target:
        return [sol]

    #Recursion base case -- exceeded the target
    if sum(sol) > target:
	    return []

    #Initialize solutions list
    all_solutions = []

    #Recursive calls: explore adding each bill denomination
    #Money is a list of 2-tuples, the first item is the denomination,
    #the second is the count    
    for (bill, count) in money:
        #Add bill only if bill denomination is high enough
        #and if there are enough bills available
        bcount = sol.count(bill)
        if bill >= highest and bcount < count:
            newSol = sol[:]
            newSol.append(bill)
            all_solutions.extend(make_smart_change_limited_bills(money, target, bill, newSol))

    return all_solutions

#Exercise 3: Return exactly one solution corresponding to the fewest number of
#bills used. Store only one solution -- the current best solution found.
def make_smart_change_best(money, target, highest, sol=[], bestSol=[]):

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

#Exercise 4: Restructure the code to add memoization.
#The primary change is to have the target value shrink so you can store
#the intermediate solutions and memoize.
def make_smart_change_memoized(money, target, highest, memo):

    #Recursion base case -- reached the target
    if target == 0:
        return []

    #Recursive calls: explore adding each bill denomination
    bestSol = []
    for bill in money:
        #Add bill only if bill denomination is high enough
        if bill >= highest:
            newSol = [bill]
            if target - bill < 0:
                continue
            #Check memo table prior to recursive call
            if (target - bill) in memo:
                currSol = memo[target - bill]
            else:
                currSol = make_smart_change_memoized(money, target - bill, bill, memo)
            if sum(newSol) + sum(currSol) == target:
                if bestSol == [] or len(newSol) + len(currSol) < len(bestSol):
                    bestSol = newSol + currSol

    memo[target] = bestSol
    return bestSol

#Exercise 1: Count the number of solutions rather than printing them all with a global variable
#Exercise 5: Recursive code that counts the number of solutions
#without enumerating solutions.


def count_change(money, length, target, memo):

    #Recursion base case -- reached the target
    if target == 0:
        return 1

    #Recursion base case -- no solution exists
    if target < 0:
        return 0

    #Recursion base case -- no solution exists
    #don't have the bills to pay
    if length <= 0 and target > 0:
        return 0

    #Recursive calls: explore adding each bill denomination
    if (length-1, target) in memo:
        skip = memo[(length-1, target)]
    else:
        skip = count_change(money, length-1, target, memo)
    if (length, target - money[length-1]) in memo:
        pick = memo[(length, target - money[length-1])]
    else:
        pick = count_change(money, length, target - money[length-1], memo)

    return skip + pick


if __name__== "__main__":
    '''
    print('--------MAKE CHANGE TESTS--------')
    bills = [1, 2, 5]
    print(sorted(make_change(bills, 6)))
    print('break')
    
    print('--------SMART CHANGE TESTS--------')
    bills2 = [1, 2, 5]
    print(sorted(make_smart_change(bills2, 6, 1)))
    print('break')
    bills3 = [1, 2, 5, 10]
    print(sorted(make_smart_change(bills3, 16, 1)))
    #yourMoney1 =  [7, 59, 71, 97]
    #print(sorted(make_smart_change(yourMoney1, 1305, 1)))

    #exercise 2
    
    
    print('--------SMART CHANGE LIMITED TESTS--------')
    money = [(1, 3), (2, 3), (5, 1)]
    print(sorted(make_smart_change_limited_bills(money, 6, 1)))
    yourMoney2 =  [(1, 11), (2, 7), (5, 9), (10, 10), (20, 4)]
    print(sorted(make_smart_change_limited_bills(yourMoney2, 16, 1)))
    
    
    #exercise 3
    print('--------SMART CHANGE BEST TESTS--------')
    money = [(1, 3), (2, 3), (5, 1)]
    print(sorted(make_smart_change_best(money, 6, 1)))
    yourMoney =  [(1, 11), (2, 7), (5, 9), (10, 10), (20, 4)]
    print(sorted(make_smart_change_best(yourMoney, 16, 1)))
    
    #exercise 4
    print('--------SMART CHANGE MEMOIZED TESTS--------')
    money = [1, 2, 5]
    print(sorted(make_smart_change_memoized(money, 6, 1, memo={})))
    yourMoney =  [1, 2, 5, 10, 20]
    print(sorted(make_smart_change_memoized(yourMoney, 296, 1, memo={})))
    yourMoney =  [7, 59, 71, 97]
    print(sorted(make_smart_change_memoized(yourMoney, 1305, 1, memo={})))
    '''
    #exercise 5
    print('--------COUNT-CHANGE--------')
    money = [1, 2, 5]
    print((count_change(money, len(money), 6)))
    bills2 = [1, 2, 5, 10]
    print((count_change(bills2, len(bills2), 16)))
    yourMoney =  [7, 59, 71, 97]
    print((count_change(yourMoney, len(yourMoney), 1305)))
