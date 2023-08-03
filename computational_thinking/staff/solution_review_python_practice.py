def fizz_buzz(n: int) -> list:
    """Returns a list of n natural numbers, except multiples of 3
    are replaced with the string "fizz", multiples of 5
    are replaced with "buzz", and multiples of 15 are 
    replaced with "fizzbuzz"

    Example:
    --------
    >>> fizz_buzz(15)
    [1, 2, "fizz", 4, "buzz", "fizz", 7, 8, "fizz", "buzz", 11, "fizz", 13, 14, "fizzbuzz"]
    
    Args:
        n (int): The number of elements in the returned list

    Returns:
        list: a list including natural numbers, "fizz", "buzz", and "fizzbuzz"
    """
    result = []
    for i in range(1, n+1):
        msg = ""
        if i % 3 == 0:
            msg += "fizz"
        if i % 5 == 0:
            msg += "buzz"
        if msg == "":
            msg = i 
        result.append(msg)
    return result

def alternating(n: int) -> list[int]:
    """Generate the first n natural numbers, except the list alternates
    between positive and negative values 

    Example:
    --------
    >>> alternating(10)
    [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]

    Args:
        n (int): The length of the output list

    Returns:
        list[int]: a list of integers that alternates its sign
    """
    result = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            result.append(i * -1)
        else:
            result.append(i)
    return result

def xor(val1: bool, val2: bool) -> bool:
    """Returns True if exactly one of val1 and val2 is True

    Example:
    --------
    >>> xor(True, True)
    False
    >>> xor(False, False)
    False
    >>> xor(True, False)
    True
    >>> xor(False, True)
    True

    Args:
        val1 (bool): A boolean value
        val2 (bool): A second boolean value

    Returns:
        bool: The result of XORing val1 and val2
    """
    return (val1 or val2) and not (val1 and val2)

def alphabetize(nums: list[int]) -> str:
    """Turns a list of integers into a string.

    value -> letter
    ---------
    0 -> 'a'
    1 -> 'b'
    2 -> 'c'
    ...
    24 -> 'y'
    25 -> 'z'

    Example:
    >>> alphabetize([0, 12, 15])
    "amp"
    

    Args:
        nums (list[int]): A list of integers representing the indexes of alphabet letters

    Returns:
        str: A string containing the message decoded from the list nums
    """
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    result = ""
    for letter_index in nums:
        result += alphabet[letter_index]
    return result

def reverse(value: str) -> str:
    """Takes in a string and returns the reverse of the string

    Example:
    ---------
    >>> reverse("Jane Street")
    "teertS enaJ"
    >>> reverse("AMP 2023")
    "3202 PMA"

    Args:
        value (str): The string to be reversed

    Returns:
        str: The reversed version of the string
    """
    result = ""
    for i in range(len(value)):
        # -1 on index because python is 0 indexed
        reversed_index = len(value) - i - 1
        result += value[reversed_index]
    return result

if __name__ == '__main__':
    n = 10
    string = "Hello AMP"
    print(fizz_buzz(n))
    print(alternating(n))
    print(xor(True, False))
    print(alphabetize([2,18,14,13,4]))
    print(reverse(string))
