def linearSearch(target, numList):
    for i in range(len(numList)):
        if numList[i] == target:
            return i
    return -1

def binarySearch_nonrecursive(target, numList):
    lo, hi = 0, len(numList)-1
    while lo <= hi:
        mid = (lo + hi) // 2
        if numList[mid] < target:
            lo = mid + 1
        elif target < numList[mid]:
            hi = mid - 1
        else:
            return mid
    return -1

def binarySearch_recursive(target, numList, low, high):
    if high >= low:
        mid = (high + low) // 2
        if numList[mid] == target:
            return mid
        elif numList[mid] > target:
            return binarySearch_recursive(target, numList, low, mid - 1)
        else:
            return binarySearch_recursive(target, numList, mid + 1, high)
    else:
        return -1

if __name__ == "__main__":
    list1 = [2, 3, 4, 10, 40]
    list2 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, \
         71, 73, 79, 83, 89, 97]

    target = 37

    #result = linearSearch(target, list2)
    #result = binarySearch_nonrecursive(target, list2)
    result = binarySearch_recursive(target, list2, 0, len(list2) - 1)

    if result != -1:
        print(f"{target} is at index {result} in {list2}")
    else:
        print(f"{target} is not in {list2}")
