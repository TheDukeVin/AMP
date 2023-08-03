def get_menu_choice()->list:
    """Prompts the use to enter a valid menu choice to indicate which sequence should be generated.
       Also prompts the user to enter how many terms they would like to see.
    """
    print("Enter your choice:")
    print("-----------------")
    print("  (O)dd Integers (positive)")
    print("  (M)ultiples (positive integer)")
    print("  (S)quare numbers")
    print("  (T)riangular numbers")
    print("  (A)rithmetic Sequence")
    print("  (F)ibonacci Sequence")
    choice = input("Which sequence would you like to generate?\n")

    while choice.lower() not in ["o", "m", "s", "t", "a", "f"]:
        choice = input("Which sequence would you like to generate?\n")

    n = int(input("How many terms would you like to see?\n"))

    return [n, choice.lower()]


def positive_odds(n):
    """Returns a list of the first n positive odd integers.

        Example
        --------
        >>>positive_odds(4)
        [1, 3, 5, 7]
    """
    if n <= 0: return []
    return [num for num in range(1, 2*n, 2)]



def positive_multiples(n, m):
    """Returns a list of the first n positive integer multiples of m.

        Example
        --------
        >>>positive_multiples(4, 6)
        [6, 12, 18, 24]
    """
    if n <= 0 or m <= 0: return []
    return [m*num for num in range(1, n+1)]

def square_numbers(n):
    """Returns a list of the first n non-negative square numbers.

        Example
        --------
        >>>square_numbers(4)
        [0, 1, 4, 9]
    """
    if n <= 0: return []
    return [num*num for num in range(n)]

def triangle_numbers(n):
    """Returns a list of the first n triangle numbers.

        Example
        --------
        >>>triangle_numbers(6)
        [1, 3, 6, 10, 15, 21]
    """
    if n <= 0: return []
    diff = 2
    terms=[1]
    for i in range(1, n):
        last_term = terms[len(terms)-1]
        terms.append(last_term+diff)
        diff +=1
    return terms

def arithmetic_sequence(n, t1, t2):
    """Returns a list of the first n terms of the arithmetic sequence defined by t1 and t2.

        Example
        --------
        >>>arithmetic_sequence(4, 3, 7)
        [3, 7, 11, 15]
    """
    if n <= 0:
        return []
    terms = []
    term = t1
    diff = t2 - t1
    for i in range(n):
        terms.append(term)
        term += diff
    return terms


def fibonacci_sequence(n):
    """Returns a list of the first n terms of the fibonacci sequence.

        Example
        --------
        >>>fibonacci_sequence(5)
        [1, 1, 2, 3, 5]
    """
    if n <= 0:
        return []
    if n == 1:
        return [1]
    
    terms = [1, 1]

    t1 = 1
    t2 = 1
    for i in range(2, n):
        next_term = t1 + t2
        terms.append(next_term)
        t2 = t1
        t1 = next_term

    return terms

if __name__ == "__main__":
    n, choice = get_menu_choice()

    match choice:
        case "o":
            seq = positive_odds(n)
        case "m":
            multiple = input("Which multiple would you like to use?")
            seq = positive_multiples(n, multiple)
        case "s":
            seq = square_numbers(n)
        case "t":
            seq = triangle_numbers(n)
        case "a":
            term_1 = input("What is the first term of the arithmetic sequence?")
            term_2 = input("What is the second term of the arithmetic sequence?")
            seq = arithmetic_sequence(n, term_1, term_2)
        case  "f":
            seq = fibonacci_sequence(n)
        case _:
            seq = "Invalid input"

    print(seq)