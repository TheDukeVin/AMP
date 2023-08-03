#Programming for the Puzzled -- Srini Devadas
#America Has Got Talent
#Given a group of candidates, each with a set of talents and
#given a list of talents that need to be displayed on the show
#choose a minimum weight selection of candidates so they can display the entire
#list of talents on the show.

#Exercise 3: Candidates have weights according to their salaries.
#Dominated candidates are eliminated prior to starting the search.

#This procedure checks a given combination to see if the combination
#fails to cover any of the talents in AllTalents that need to be covered.
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


#Remove candidates whose talents are all covered by some other candidate
def removeDominatedCandidates(cList, cTalents):
    newClist = []
    newTlist = []
    for i in range(len(cList)):
        dominated = False
        for j in range(len(cList)):
            #If candidate i has less weight than candidate j, need to keep i
            if i == j or cList[i][1] < cList[j][1]:
                continue
            #Check if j dominates i, if so don't include i
            iTalent = cTalents[i]
            jTalent = cTalents[j]
            if contained(iTalent, jTalent):
                dominated = True
                print ('Candidate', cList[i], 'dominated by', cList[j])
                #Now that you know what a break statement is, note that we can break here!
                break
        if not dominated:
            newClist.append(cList[i])
            newTlist.append(cTalents[i])

    return newClist, newTlist

#Check if each element of list1 is contained in list2
def contained(list1, list2):
    for elm in list1:
        if elm not in list2:
            return False
    return True

#Compute the weight of the combination
def weight(comb):
    return sum(c[1] for c in comb)

#This procedure finds the combination with the minimum number of candidates
#that cover all the required talents
def Hire4Show(candList, candTalents, talentList):
    candList, candTalents = removeDominatedCandidates(candList, candTalents)
    n = len(candList)
    hire = candList[:]
    for i in range(2**n):
        Combination = []
        num = i
        for j in range(n): 
            if (num % 2 == 1):
                Combination = [candList[n-1-j]] + Combination
            num = num // 2

        if Good(Combination, candList, candTalents, talentList):
            if weight(hire) > weight(Combination):
                hire = Combination
    
    print ('Optimum Solution:', hire)
    print ('Weight is:', weight(hire))


Talents = ['Sing', 'Dance', 'Magic', 'Act', 'Flex', 'Code']
Candidates = [('Aly', 3), ('Bob', 6), ('Cal', 5), ('Don', 3),
              ('Eve', 3), ('Fay', 3)]
CandidateTalents = [ ['Flex', 'Code'], ['Dance', 'Magic'], ['Sing', 'Magic'],
                  ['Sing', 'Dance'], ['Dance', 'Act', 'Code'], ['Act', 'Code'] ]

ShowTalentW = [1, 2, 3, 4, 5, 6, 7, 8, 9]
CandidateListW = [('A', 3), ('B', 2), ('C', 1), ('D', 4),
                  ('E', 5), ('F', 2), ('G', 7)]
CandToTalentsW = [ [1, 5], [1, 2, 8], [2, 3, 6, 9], [4, 6, 8], [2, 3, 9],
                   [7, 8, 9], [1, 3, 5] ]

Hire4Show(Candidates, CandidateTalents, Talents)
Hire4Show(CandidateListW, CandToTalentsW, ShowTalentW)

