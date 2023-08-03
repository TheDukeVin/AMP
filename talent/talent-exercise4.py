#Programming for the Puzzled -- Srini Devadas
#America Has Got Talent
#Given a group of candidates, each with a set of talents and
#given a list of talents that need to be displayed on the show
#choose a minimum number of candidates so they can display the entire
#list of talents on the show.

#Exercise 4: Determine candidates who are essential to any show, because
#they have a talent that is not covered by any other candidate.
#Remove such essential candidates and make the problem smaller.
#Solve the problem, and add in the essential candidates.
#Do this for the weighted problem.

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


def findEssentialCandidates(candList, candTalents, talentList):

    eCand = []
    cList = []
    cTalents = []
    tList = []
    covered = [0] * len(talentList)
    candidate = [None] * len(talentList)

    #Look for essential candidates by looking at talents that are covered only
    #by one candidate
    for i in range(len(candTalents)):
        for t in candTalents[i]:
            covered[talentList.index(t)] += 1
            candidate[talentList.index(t)] = candList[i]

    #Essential candidates are discovered by looking at talents
    #covered by a single candidate
    for i in range(len(covered)):
        if covered[i] == 1:
            #append essential candidates to this list (will be returned)
            eCand.append(candidate[i])

    for i in range(len(candList)):
        if not candList[i] in eCand:
            #Build the new table's candidate list and candidate to talent list
            cList.append(candList[i])
            #Note that the removed talents will still appear in candidate's talents
            cTalents.append(candTalents[i])
            
    #Need to remove talents covered by essential candidates from talent list
    for t in talentList:
        need = True
        for e in eCand:
            if t in candTalents[candList.index(e)]:
                need = False
                break
        if need:
            tList.append(t)

    return eCand, cList, cTalents, tList


#Compute the weight of the combination
def weight(comb):
    return sum(c[1] for c in comb)   

#This procedure finds the combination with the minimum number of candidates
#that cover all the required talents
def Hire4Show(candList, candTalents, talentList):
    #Remove essential candidates and update entire table
    essenCand, candList, candTalents, talentList \
               = findEssentialCandidates(candList, candTalents, talentList)
    print ('Essential candidates are:', essenCand)
    print ('New candidates are:', candList)
    print ('New candidate talents are:', candTalents)
    print ('New talent list is:', talentList)

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

    #Add in the essential candidates
    hire += essenCand
        
    print ('Optimum Solution:', hire)
    print ('Weight is:', weight(hire))


Talents = ['Sing', 'Dance', 'Magic', 'Act', 'Flex', 'Code']
Candidates = [('Aly', 3), ('Bob', 6), ('Cal', 5), ('Don', 3),
              ('Eve', 3), ('Fay', 3)]
CandidateTalents = [ ['Flex', 'Code'], ['Dance', 'Magic'], ['Sing', 'Magic'],
                  ['Sing', 'Dance'], ['Dance', 'Act', 'Code'], ['Act', 'Code'] ]

ShowTalent2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
CandidateList2 = [('A', 3), ('B', 2), ('C', 1), ('D', 4),
                  ('E', 5), ('F', 2), ('G', 7)]
CandToTalents2 = [ [1, 5], [1, 2, 8], [2, 3, 6, 9], [4, 6, 8], [2, 3, 9],
                   [7, 8, 9], [1, 3, 5] ]

Hire4Show(Candidates, CandidateTalents, Talents)
Hire4Show(CandidateList2, CandToTalents2, ShowTalent2)

