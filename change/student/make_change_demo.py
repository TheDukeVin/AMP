def make_change(bills:list[int], target:int, sol:list[int] = []):
    if sum(sol) == target:
        print(sol)
        return

    if sum(sol) < target:
        for bill in bills:
            new_sol = sol[:]
            new_sol.append(bill)
            make_change(bills, target, new_sol)
    
    return

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

if __name__=="__main__":
    bills2 = [1, 2, 5]
    make_unique_change(bills2, 6, 1)