# Prime Timing

## Puzzle Description
A 10x10 grid is filled with repeating numbers on its diagonals. Calculuate the sum of all the numbers in the table in your head.

## Problem Solving Strategy
### Finding Patterns

## General Lesson Format
1. Number Grid warm-uo
    - Students have time to solve the Number Grid puzzle.
    - Teacher talks about various patterns that could be employed to reduce the total number of overall calculations.
        - Apprach in the presentation
            - Formula for the sum of numbers from 1 - n
            - Recursive relationship of row sums
            - Multiplication is repeated addition
        - Other approaches:
            - Folding along the 10’s diagonal, then adding number pairs to get 20


2. Introduce Project Euler #3: Finding the Largest Prime Factor
    - The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143 ?
    - Practice *Understanding the Problem* by identifying key understandings embedded in the problem description
        - Factor: f is a factor of n if f divides n with no remainder
            - ie. if n % f == 0, then f is a factor of n
        - Prime: A prime number is a number that has no factors other than 1 and itself
            - The example given indicates that 1 should not considered a prime number
        - Prime factor: A prime factor, f, divides a number with no remainder, while having no factors other than 1 and f 
        - Largest: The largest prime factor of n would be bigger than all other prime factors of n
        - Natural Numbers: No need to worry about negatives, 0, or decimals
            - Not explicitly stated, but implied by the nature of the problem

3. Class Exercise: Implement get_factors
    - Given that finding factors and prime go hand-in-hand, let’s warm up by writing code which will find all the positive integer factors of a given natural number.
    - Implement get_factors, a method which takes a natural number n to return a list of the unique positive integer factors of n in sorted order.
    - For instance:
        - get_factors(6) → [1, 2, 3, 6]
        - get_factors(17) -> [1, 17]
        - get_factors(36) -> [1, 2, 3, 4, 6, 9, 12, 18, 36]
        - get_factors(-2) -> []
    - Use the prime_timing.py starter code. Submit to the Prime Timing Gradescope assignment when you feel like you have a complete implementation.
    - Once most students have correctly implemented get_factors, talk about a variety of implementations.
        - Compare Brute Force approach with potential patterns:
            - Once a factor is found, immediately dividing to get the factor pair
            - Stopping at the square root (inclusive) because you've already checked for the smaller side of the factor pairs
        - This activity should ensure students understand the factor pair pattern:
            - all factors come in pairs
            - smallest factor is paired with biggest factor
            - the "factor fold" occurs at the square root of n

4. Talk about various patterns that can speed up is_prime
    -  Start by talking about ways in which get_factors and is_prime are related, yet different problems
    - is_prime patterns:
        - skipping 1 and n
        - breaking after first factor
        - skipping evens after 2
        - stopping at square root (inclusive)

5. Students implement a variety of is_prime algorithms and 2 prime-related PE problems:
- PE #7: Find the 10001st Prime
- PE #10: Summation of Primes
- PE #27: Quadratic Primes
- PE# 35: Circular Primes
- PE# 37: Truncatable Primes
- PE# 41: Pandigital Primes

## Teaching Notes
- Two main themes: 
    - Finding Mathematical Patterns to improve on Brute Force
    - Understanding the Problem
        - Before writing an algorithm to solve a problem, it’s important to fully understand the problem. This can often be accomplished by a careful reading of the problem statement. 
        - Some tips for understanding the problem: 
            - Define important terms, then identify micro coding statements
            - Highlight all words that impact your solution: factor → n % f == 0
            Define all words that have mathematical meaning: below → <
            - Explicitly list any implicit requirements 
                - Problems won’t always state constraints. 
                - For instance, prime numbers are natural numbers. This implies that negative numbers, 0, and decimals should not be considered.
            - Work a smaller example to confront misunderstandings
                - The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143 ?
- Passing functions as variables will most likely be new for many students.
    - This is demonstrated as a local means of verifying correctness
- There is a small part II in the next lesson, where a Timing Profiler is run to experimentally verify that approaches take differing amounts of time (which is why the activity is called Prime Timing)


## Possible Extensions/Continuations
- The [prime counting problem](https://www.quantamagazine.org/mathematicians-will-never-stop-proving-the-prime-number-theorem-20200722/):
How many primes are less than or equal to n? This value is called π(n), where π is the “prime counting function.” For example:
π(10) = 4 since there are four primes less than or equal to 10: 2, 3, 5 and 7
π(100) = 25
π(1,000) = 168
Note: As you calculate π(10) , π(100) , π(1000)  the percentage of primes decreases from 40% to 25% to 16.8%.  

- Implement two versions of prime counting functions: basic counting and sieve of eratosthenes using the counting_pimes.py starter code

- Generate demonstration graphs:
    - The density of prime numbers at or below n decreases as n gets larger
    - The error rate between the actual prime count and the approximation provided by n/ln(n) decreases as n gets larger