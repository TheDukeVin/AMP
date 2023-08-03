#Puzzle 10: A Profusion of Queens

#Exercise 4: Write a recursive talent search (Puzzle 9)

def smallestSol(chosen, elts, candL, candT, allT, Sol):
    """
    Input: chosen is a (possibly empty) list of elements chosen so far.
           elts is a (possibly empty) list of elements yet to consider.
           talentCheck(chosen, x, ) return True if all the talents are
           covered.
           Sol is smallest solution found so far that covers all the talents.
    """
    if len(elts) == 0:
        if Good(chosen, candL, candT, allT):
            if Sol == [] or len(chosen) < len(Sol):
                Sol = chosen
        return Sol
    Sol = smallestSol(chosen + [elts[0]], elts[1:], candL, candT, allT, Sol)
    return smallestSol(chosen, elts[1:], candL, candT, allT, Sol)

#This procedure checks a given combination to see if the combination
#fails to cover any of the talents in AllTalents that need to be covered.
#Same as in Puzzle 9.
def Good(Comb, candList, candTalents, AllTalents):
    for tal in AllTalents:
        cover = False
        for cand in Comb:
            candTal = candTalents[candList.index(cand)]
            if tal in candTal:
                cover = True
        if not cover:
            return False 
    return True 
    
def Hire4Show(candList, candTalents, talentList):
    """
    Print an optimum (smallest) team for given input.
    """
    Sol = smallestSol([], candList, candList, candTalents,\
                      talentList, [])
    print("Optimum solution:", Sol, "\n")


Talents = ['Sing', 'Dance', 'Magic', 'Act', 'Flex', 'Code']
Candidates = ['Aly', 'Bob', 'Cal', 'Don', 'Eve', 'Fay']
CandidateTalents = [ ['Flex', 'Code'], ['Dance', 'Magic'], ['Sing', 'Magic'],
                  ['Sing', 'Dance'], ['Dance', 'Act', 'Code'], ['Act', 'Code'] ]

ShowTalent2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
CandidateList2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
CandToTalents2 = [ [4, 5, 7], [1, 2, 8], [2, 4, 6, 9], [3, 6, 9], [2, 3, 9],
                   [7, 8, 9], [1, 3, 7] ]

Hire4Show(Candidates, CandidateTalents, Talents)
Hire4Show(CandidateList2, CandToTalents2, ShowTalent2)
