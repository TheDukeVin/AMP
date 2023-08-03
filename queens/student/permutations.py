def permutations1(a):
    # Base Case: the only permutation of an empty list is the empty list
    if (len(a) == 0):
        return [ [] ]
    else:
        # Recursive Case: remove the first element, then find all possible
        # permutations of the remaining elements. For each permutation,
        # insert a into every possible position in that permutation.

        partialPermutations = permutations1(a[1:])
        allPerms = [ ]
        for perm in partialPermutations:
            for i in range(len(perm) + 1):
                allPerms.append(perm[:i] + [ a[0] ] + perm[i:])
        return allPerms

def permutations2(a):
    if (len(a) == 0):
        return [ [] ]
    else:
        allPerms = [ ]
        for i in range(len(a)):
            partialPermutations = permutations2(a[:i] + a[i+1:])
            for perm in partialPermutations:
                allPerms.append([ a[i] ] + perm)
        return allPerms

def powerset(a):
    # Base case: the only possible subset of an empty list is the empty list.
    if (len(a) == 0):
        return [ [] ]
    else:
        # Recursive Case: remove the first element, then find all subsets of the
        # remaining list. Then for each subset, use two versions of that subset:
        # one without the first element, and another one with it.

        partialSubsets = powerset(a[1:])
        allSubsets = [ ]
        for subset in partialSubsets:
            allSubsets.append(subset)
            allSubsets.append([a[0]] + subset)
        return allSubsets

print(powerset([1,2,3]))
print(permutations1([1,2,3]))
print(permutations2([1,2,3]))
