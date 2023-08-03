# Organizational
- [Coding Conventions](https://docs.google.com/document/d/10FMccJ0e6ckRC43NO2eJhaZNsi-NHDMMJQ9SqFnkQPI/edit)
- [Debugging and Collaboration Strategies](https://docs.google.com/document/d/1zKwF6bNvUK9bArwBv88twjqLCTAPemCiIhJzoZ3Gdsw/edit)
- [Gradescope Autotests](https://docs.google.com/document/d/1y6JPTUfq_68sLd-kWP8J2l4_bZXTlpxBN5UdS_gPQzI/edit)
- [AMP:CS Overview](https://docs.google.com/presentation/d/16iET69OAirmC0K9P5yXWl77BKYmKGFT5X_i4ljcR8yI/edit#slide=id.p)
- [AMP:CS Curriculum Guide](https://docs.google.com/document/d/1V4dXRPlUW2et8W0A2N7UDvNG7KV0ILqtJzuLMNi-DvU/edit)

# Running Tests Locally
**MAKE SURE gradescope_utils IS INSTALLED!**


To install gradescope utils: `pip install gradescope_utils`


- Make sure you are in the root of the github repository
- Run the command `python run_tests_local.py <module>` (or `py run_tests_local.py <module>` if windows complains about python)
- You may make the output more detailed by setting the verbosity flag:
    - `python run_tests_local.py --verbosity 2 <module_name> <starter|solution>`
        - `py run_tests_local.py --verbosity 2 fake solution`
        - `py run_tests_local.py --verbosity 2 fake starter`
- See help about the script by running `python run_tests_local.py --help`

# Curriculum
## [Computational Thinking](/computational_thinking/README.md)
1. [Instructions](/computational_thinking/README_0.md) (Pre-Activity)
2. [Tangrams](/computational_thinking/README_1.md)
2. [Curve Stitching](/computational_thinking/README_2.md)
3. [Throwing Darts](/computational_thinking/README_3.md)

## [Python Warm-Up](/warm_up/README.md)
1. [Hello NYC (w/ VS Code and Python)](/warm_up/README_1.md)
2. [Hello Unit Testing (w/ Gradescope)](/warm_up/README_2.md)
3. [Python Selection](/warm_up/README_3.md)

## Problem Solving with Python
1. [Prize Envelopes](/envelopes/README.md)
2. [Automathic](/automathic/README.md)
3. [Sixteen Stones](/stones/README.md)

## Iterative Strategies
1. [Prime Timing](/prime/README.md)
2. [You Will All Conform](/conform/README.md)
3. [AnaGame](/anagame/README.md)
4. Guess Who's Coming to Dinner
5. Word Ladder

## Recursive Strategies
1. Find the Fake
2. Drawing Fractals
3. N-Queens
4. Making Change
5. Climbing Stairs
6. Detectives

## Monte Carlo Strategies
1. Monty Hall Problems

## Information Theory
1. Wordle
2. Ghost (TODO)

## Game Theory
1. Boolean Satisfiability (TODO)
3. Quarto
