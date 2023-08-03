"""The following puzzle is derived from Programming for the Puzzled by Srini Devadas"""

def make_change(bills, target):

  def change_helper(bills, target, sol, all_sols):
    if sum(sol) == target:
       all_sols.append(sol)
       return

    if sum(sol) <= target:
       for bill in bills:
         new_sol = sol[:]
         new_sol.append(bill)
         change_helper(bills, target, new_sol, all_sols)
  
  all_sols = []
  change_helper(bills, target, [], all_sols)
  return all_sols

def make_unique_change(bills, target, highest, sol = []):
   if sum(sol) == target:
       print (sol)
       return

   if sum(sol) < target:
       for bill in bills:
           #Add bill only if bill is large enough
           if bill >= highest:
               new_sol = sol[:]
               new_sol.append(bill)
               make_unique_change(bills, target, bill, new_sol)
   return

def make_unique_change_limited_bills(money:list[tuple[int,int]], target:int, highest:int, sol:list[int] = []):
    '''The number of bills of each denomination is limited.
        For example, money = [(1, 3), (2, 3), (5, 1)] means that there are 3 $1 bills, 3 $2 bills, and 1 $5 bill.
        These limits need to respected during solution generation.

        Args:
          money: a list of 2-tuples where the first item is the denomination, the second is the count
          target: the integer target that should be represetned with change
          highest: the highest bill considered so far
          sol: a list of integers represetning the current solution configuration
    '''

    if sum(sol) == target:
        print (sol)
        return

    if sum(sol) > target:
        return

    for (bill, count) in money:
        #Add bill only if bill denomination is high enough
        #and if there are enough bills available
        bcount = 0
        for b in sol:
            if b == bill:
                bcount += 1
        if bill >= highest and bcount < count:
            new_sol = sol[:]
            new_sol.append(bill)
            make_unique_change_limited_bills(money, target, bill, new_sol)

    return


def make_unique_change_fewest_bills(money:list[tuple[int,int]], target:int, highest:int, sol:list[int] = [], best_sol:list[int]=[]):
    '''Return exactly one solution corresponding to the fewest number of bills used. 
       Store only one solution -- the current best solution found.
    '''
    #Recursion base case -- reached the target
    if sum(sol) == target:
        if len(best_sol) == 0:
            best_sol = sol
        elif len(best_sol) > len(sol):
            best_sol = sol
        else:
            pass
        return best_sol

    #Recursion base case -- exceeded the target
    if sum(sol) > target:
        return best_sol

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
            new_sol = sol[:]
            new_sol.append(bill)
            best_sol = make_unique_change_fewest_bills(money, target, bill, new_sol, best_sol)

    return best_sol


def make_unique_change_memoized(money, target, highest, memo):
    '''Restructure the code to add memoization.
        The primary change is to have the target value shrink so you can store the intermediate solutions and memoize.
    '''
    if target == 0:
        return []

    #Recursive calls: explore adding each bill denomination
    bestSol = []
    for bill in money:
        #Add bill only if bill denomination is high enough
        if bill >= highest:
            new_sol = [bill]
            if target - bill < 0:
                continue
            #Check memo table prior to recursive call
            if (target - bill) in memo:
                currSol = memo[target - bill]
            else:
                currSol = make_unique_change_memoized(money, target - bill, bill, memo)
            if sum(new_sol) + sum(currSol) == target:
                if bestSol == [] or len(new_sol) + len(currSol) < len(bestSol):
                    bestSol = new_sol + currSol

    memo[target] = bestSol
    return bestSol

def count_change(money, length, target, memo):

    if target == 0:
        return 1

    if target < 0:
        return 0

    return 0

if __name__=="__main__":
    '''
    bills = [1, 2, 5]
    print("----Making Change: $6----")
    print(make_change(bills, 6))
    
    print("-----Making Change: $16----")
    make_unique_change(bills, 16, 1)

    
    bills3 = [1, 2, 5, 10]
    make_unique_change(bills3, 16, 1)
    yourMoney1 =  [7, 59, 71, 97]
    make_unique_change(yourMoney1, 1305, 1)
    #exercise 2
 
    money = [(1, 3), (2, 3), (5, 1)]
    make_unique_change_limited_bills(money, 6, 1)
    #yourMoney2 =  [(1, 11), (2, 7), (5, 9), (10, 10), (20, 4)]
    #make_unique_change_limited_bills(yourMoney2, 16, 1)
    '''
    #exercise 3
    money = [(1, 3), (2, 3), (5, 1)]
    print(make_unique_change_limited_bills(money, 6, 1))
    yourMoney =  [(1, 11), (2, 7), (5, 9), (10, 10), (20, 4)]
    print(make_unique_change_limited_bills(yourMoney, 16, 1))
    '''
    #exercise 4
    money = [1, 2, 5]
    print(make_unique_change_memoized(money, 6, 1, memo={}))
    yourMoney =  [1, 2, 5, 10, 20]
    print(make_unique_change_memoized(yourMoney, 296, 1, memo={}))
    yourMoney =  [7, 59, 71, 97]
    print(make_unique_change_memoized(yourMoney, 1305, 1, memo={}))
    #exercise 5
    money = [1, 2, 5]
    print(count_change(money, len(money), 6, memo={}))
    bills2 = [1, 2, 5, 10]
    print(count_change(bills2, len(bills2), 16, memo={}))
    yourMoney =  [7, 59, 71, 97]
    print(count_change(yourMoney, len(yourMoney), 1305, memo={}))
    '''