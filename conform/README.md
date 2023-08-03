# You Will All Conform

## Puzzle Description
There’s a bunch of people waiting in line for a baseball game… but some are wearing their caps forward, while others are wearing their caps backward. As the gatekeeper you can only let groups of fans into the stadium who are wearing their caps the same way –either all forward or all backward. You can’t tell a group whether to make their hats forward or backward, but you can tell people in the group to flip their caps. Luckily, everyone in the group knows their position in line. You could say things like:
-Person in position i, please flip your cap
-People in positions i through j (inclusive), please flip your caps
What you really want to do is minimize the number of times you have to shout. Afterall, there are a lot of groups coming to see the ball game. How can you give the minimum number of shouts (for any possible configuration of hats)? 

## Problem Solving Strategy
### Transform and Conquer: Instance Simplification

## General Lesson Format

0. Prime Timing- Part 2: Introduce an empirical method for comparing algorithms prime_timing.py
    - Comparing algorithms:
        - Time- How much time does it take to complete the algorithm?
        - Memory- How much memory does it take to complete the algorithm?
        - Understandability- How easy is it for a human to understand the algorithm?
        - Purpose- Do the algorithms accomplish the same thing?
    - Stopwatch-style Experiment to compare algorithms via time
    - Teacher runs TimingProfiler class
        - First time: is_prime_exhaustive ruins the graph
        - Second time: Delete is_prime_exhaustive from the array of algorithms
        - Discussion points: 
            - Brief overview of TimingProfiler class
            - bigger n -> more time
            - smaller n → little difference between algorithms
            - choice of testing n’s ie all primes, no evens, etc

1. Lead students through solving the conform problem:
- There’s a bunch of people waiting in line for a baseball game… but some are wearing their caps forward, while others are wearing their caps backward. As the gatekeeper you can only let groups of fans into the stadium who are wearing their caps the same way –either all forward or all backward. You can’t tell a group whether to make their hats forward or backward, but you can tell people in the group to flip their caps. Luckily, everyone in the group knows their position in line. You could say things like:
-Person in position i, please flip your cap
-People in positions i through j (inclusive), please flip your caps
What you really want to do is minimize the number of times you have to shout. Afterall, there are a lot of groups coming to see 
the ball game. How can you give the minimum number of shouts (for any possible configuration of hats)? 
- Finish by summarizing Key Observations with students
    - One interval ends, and another begins, when we see a change in hat direction.
    - First interval has a starting position of 0.
    - We should pick the direction to flip based on which collection of intervals is smaller.
    - Some edge cases given n people:
    - if n is even there will be n/2 forward and n/2 backward intervals
    - If n is odd, there is 1 more forward interval vs backward interval (or vice versa)

2. Ask students to write an algorithm in English, on paper
- Something like:
    1. Determine intervals where hats face the same direction
    2. Intervals begin/end with a change in hat direction
    3. Decide a flip direction based on the hat direction with the least number of intervals
    4. Go through all the intervals to flip intervals that match the flip direction

3. Look at please_flip_original.py
    - Talk about how to important data is modeled with data structures
    - Compare and contrast Python lists, strings, tuples
        - Immutable vs mutable
        - Sequence slicing
    - Walk through Guiding Questions:
        - What keeps track of the count of intervals?
        - Why is some code repeated? Could we eliminate the repeated code?
            - Adding an extra symbol to the end of the list is the suggested approach, though this does modify the actual list… 
            - Create a new list: my_caps = caps +[“END”] with a sentinel value
            - Trade-off between modifying data structures and modifying algorithms
            - A challenge would be to eliminate the redundency 

        - What determines the beginning/end of intervals?
        - Why use tuples to keep track of intervals?
        - What is the actual list of tuples that is generated?
        - Why would this code crash on an empty list?
        - Could we simplify the approach?
        - What is the least amount of work that we need to do?
        - Is there any part of the code that seems clunky or convoluted?

4. Assign the conform exercises
    - `please_flip_oriiginal`: Fix the output of pleaseConformOpt so that it is grammatically correct, even for intervals with only 1 person:
    - `please_flip_streamlined`: Redundant post-loop if statement is removed
    - please_flip_bare: Suppose there are bareheaded people in the line. We’ll represent them with the 'H' character. So for example we might have: cap3= ['F','F','B','H','B','F','B','B','B','F','H','F','F']  We don’t want to confuse the bareheaded people by telling them to flip their non-existent caps and perhaps cause one of them to try to steal a cap from the person ahead in line. Therefore, we want to skip over all the 'H' positions.
    - `please_flip_one_pass`: What if you could only see the group come in one at a time? Implement a one-poss solution to process the list with a single loop. You may assume that everyone in the group is wearing a hat that is either forwards or backwards.
    - Optional Challenge- `run_length_encode`, `run_length_decode`: Write a program that performs simple run-length encoding, which converts a given string. For example, BFFFFFBFFFF, to the shorter 1B5F1B4F, and run-length decoding, which converts the compressed string back to the original. You should be able to compress and decompress in one pass through the string. 


## Teaching Notes
- Introduces Data Modeling ie. deliberately choosing a data structure to model a given scenario
- Encourages one-pass algorithms over two-pass algorithms
- Translates a more complicated problem solving algorithm into code
- Compares and contrasts Python sequence data types: strings, lists, and tuples
- Introduces the idea of sentinel values
    - Trade-off between modifying data structures vs modifying algorithms
- Autotests are all the same for original, streamlined and one-pass. These functions need manual inspection to verify that students fulfilled the intent of the exercise.


