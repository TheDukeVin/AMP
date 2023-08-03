import math
from TimingProfiler import TimingProfiler

def is_prime(n) -> bool:
    if n<=1: return False
    if n%2 == 0: return n==2
    factor_fold = math.ceil(math.sqrt(n))
    for potential_factor in range(3, factor_fold+1, 2):
        if n%potential_factor == 0: return False
    return True

def cross_off_multiples(i, n, prime) -> None:
    for j in range(i, n+1, i):# All multiples of p -> False
            prime[j] = False

def sieve_of_eratosthenes(n) -> int:
    prime = [True for i in range(n+1)] #assume all numbers <= n to be prime
    count = 0
    i = 2
    while i <= n:
        if (prime[i] == True):# If prime[p] hasn't changed, then it is a prime
            count += 1
            cross_off_multiples(i, n, prime)
        i += 1
    return count

def basic_prime_count(n) -> int:
    count=0
    for i in range(2, n+1):
        if is_prime(i):
            count+=1
    return count

if __name__ == "__main__":
    actual_prime_counts={
      10:3,
      100:25,
      1000:168
    }
    for count in actual_prime_counts:
        assert(basic_prime_count(count) == actual_prime_counts[count], f"basic_prime_count is incorect for n ={count}")
        assert(sieve_of_eratosthenes(count) == actual_prime_counts[count], f"sieve_of_eratosthenes is incorect for n ={count}")
        print(f"\u03C0({count})={actual_prime_counts[count]}... passed")

    algorithms =[basic_prime_count, sieve_of_eratosthenes]
    inputs=[10, 100, 1000, 10000, 100000, 1000000]
    trials = 10

    experiment = TimingProfiler(algorithms, inputs, trials)
    experiment.run_experiments()
    experiment.graph(title="Counting Primes", scale="log")
