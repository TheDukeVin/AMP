import math
#from TimingProfiler import TimingProfiler

def get_factors(n:int)->list[int]:
    '''
    Generates a sorted list of unique integer factors for a given integer

    Args:
    n (int): The integer which should be factored

    Returns:
    list: a list of unique integer factors in sorted order
    '''
    factors=[]
    for potential_factor in range(1, n+1):
        if n%potential_factor==0:
            factors.append(potential_factor)
    return sorted(factors)

def is_prime_exhaustive(n) -> bool:
    if n<=1: return False
    prime = True
    for potential_factor in range(2, n):
        if n%potential_factor == 0:
            prime = False
    return prime

def is_prime_exhaustive_escape(n) -> bool:
    if n<=1: return False
    for potential_factor in range(2, n):
        if n%potential_factor == 0: return False
    return True

def is_prime_skip_evens(n) -> bool:
    if n<=1: return False
    if n%2 == 0: return n==2
    for potential_factor in range(3, n, 2):
        if n%potential_factor == 0: return False
    return True

def is_prime_skip_impossible_factors(n) -> bool:
    if n<=1: return False
    if n%2 == 0: return n==2
    factor_fold = math.ceil(math.sqrt(n))
    for potential_factor in range(3, factor_fold+1, 2):
        if n%potential_factor == 0: return False
    return True

if __name__ == "__main__":
    n = int(input("Enter a positive integer"))

    factors = get_factors(n)
    print(f"The factors of {n} are {factors}")
    if len(factors) == 2:
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")

    algorithms =[ is_prime_exhaustive_escape, is_prime_skip_evens, is_prime_skip_impossible_factors]
    inputs=[11, 101, 1009, 10007, 100003, 1000003, 10000019]
    trials = 10

    experiment = TimingProfiler(algorithms, inputs, trials)
    experiment.run_experiments()
    print(experiment.results)
    experiment.graph(title="is_prime Timings", scale="log")
