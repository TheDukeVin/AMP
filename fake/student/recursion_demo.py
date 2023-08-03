def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

def wordPlay(word):
    print(word)
    if len(word)>1:
      wordPlay(word[1:])
    print(word)

chToprime = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13,
    'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43,
    'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79,
    'w': 83, 'x': 89, 'y': 97, 'z': 101 }

def primeHash(str):
    if len(str) == 0:
        return 1
    else:
        return chToprime[str[0]] * primeHash(str[1:])

def isPalindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0].lower() == s[-1].lower() and isPalindrome(s[1:-1])

def to_binary_recursion(n):
    if n<=1:
      return str(n % 2)
    
    return to_binary_recursion(n//2)+str(n % 2)    


if __name__ == "__main__":
    print(factorial(8))
    print(wordPlay("hello"))
    print(primeHash("hello"))
    print(isPalindrome("racecar"))
    
    for i in range(16):
      print(to_binary_recursion(i))
