#Good explanation: https://www.codeproject.com/Tips/1275693/Recursive-Permutations-in-Python

#Article discussing replacing recursion with implementation: https://stackoverflow.com/questions/159590/way-to-go-from-recursion-to-iteration/159777#159777
def dfs_permutations(nums, perm, tabCount):
    global dfs_count
    dfs_count+=1
    print(f"{' '*tabCount}({dfs_count}): dfs({nums}, {perm})")
    if not nums:#no more elements in nums
        all_perms.append(perm) #add perm to list of all permutations
        print(f"{' '*2*tabCount}{perm} added to all_perms")

    for element in nums:
        sub_list = list(nums) #make a deep copy to avoid changing nums
        sub_list.remove(element)
        dfs(sub_list, perm +[element], tabCount+2)

def iterativePermutations(word):
    stack = list(word)
    results = stack.pop()  #remove last element from the list
    while len(stack) != 0:
        c = stack.pop()
        new_results = []
        for w in results:
            for i in range(len(w)+1):
                new_results.append(w[:i] + c + w[i:])
        results = new_results
    return results

def permute(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 1:
            return [nums]
        if len(nums) == 2:
            return [nums,nums[::-1]]
        
        output = []
        for i in range(len(nums)):  #for each element 
            
            nums[0],nums[i] = nums[i],nums[0]
            
            for sub_permutation in self.permute(nums[1:]): 
                output.append([nums[0]]+sub_permutation)
        
        return output

if __name__ == '__main__':
    permutations = recursivePermutations("12345")
    print(permutations)
    permutations = iterativePermutations("12345")
    print(permutations)
    
    dfs_count=0
    all_perms=[]
    dfs([1, 2, 3], [], 0)
    print(all_perms)
