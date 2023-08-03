# Sixteen Stones

[Sixteen Stones presentation](https://docs.google.com/presentation/d/17_TgYHJN8CIdbDUHigWUzh7sA_2F_ASBuuMc2AHRczc/edit#slide=id.g14975c0d44e_1_0)

## Puzzle Description
1. A game of 16 Stones begins with two players and a pile of 16 stones.
2. Players alternate turns taking stones from the pile.
3. A player may each take 1, 2, 3, or 4 stones from the pile.
4. The player who takes the last stone loses the game.


## Problem Solving Strategy
### Transform and Conquer - Instance Simplification
The always win strategy is based on modular arithmetic (and going second).

## Potential Extensions
- Add an AISkill variable:
    - aiSkill of 0 never choose the correct move.
    - aiSKill of 5 chooses the correct move 50% of the time
    - aiSkill of 10 always choses the correct move.

- Allow players to pick the starting number of stones and the set of valid moves before beginning the game. Feel free to disallow scenarios like 18 starting stones to ensure that numStones % (maxGuess + 1) == 1

## General Lesson Format
1. Groups play Sixteen Stones in order to discover the perfect strategy for winning
- Divide students into groups of 2. 
- Each group of 2 should have 16 stones. 
- Groups will slowly build up to the solution:
    - Always leave your opponent with 11
    - Always leave your opponent with 6
    - etc

2. Discuss the perfect strategy, and how to articulate it as a mathematical pattern
- Basically, the perfect strategy is to take 5’s complement: 16 % 5 == 1

3. Assign the Sixteen Stones coding project
    - Use the starter code in stones.py to finish a digital version of the game Sixteen Stones. In the digital version you may choose to play the game against an AI. Most of the code is finished for you, however you will have to implement three functions:

    - `format_pile`: Generates a pretty string version of the pile of stones
    - `is_valid_move`: Checks whether a player has opted to take a legit number of stones
    - `get_ai_guess`: Always picks the perfect move (if possible)

    Implement these three methods, then submit stones.py to Gradescope under the Sixteen Stones assignment. 

    Optional Extensions:
    Add an aiSkill variable such that a skill of 0 never picks the correct number of stones, a skill of 10 always picks the correct number of stones (if possible), and a skill of 5 picks the correct move 50% of the time. 
    Allow players to pick the starting number of stones and the set of valid moves before beginning the game. Feel free to disallow scenarios like 18 starting stones. 


4. Take a look at the starter code with the class
- Look at flow chart of solution components
- Talk about Python membership operators
- Talk about while loops
- Introduce Type hints
- Introduce 
- The main section models the same input, calculations, display results
-  `format_pile` reframes displaying results in a manner that is testable
- `format_pile` and `get_ai_guess` could be reframed as huge extended-if structures, but look for a higher-order pattern instead

## Teacher Notes
- An easier project for students to gain confidence with Python. Students who finish early can work on Project Euler.

- Learning Points
    - Python // and % operators are reinforced in both the AI strategy and the stringification of the pile of stones.
    - Encourages patterns over long extended if statements: AI strategy, ai_skill cutoff
        - It should be emphasized to students that there are better alternatives to long extended if statements 
    - Introduces range as a useful data type
    - Reinforces Python membership operators
    - Gets students up to speed with basic python conventions
    - Makes extensive use of while loops
    - First "big" starter code

- Sixteen Stones is an instance of the classic game Nim.

## TODO
- Create a flow chart to illustrate how big pieces of the starter code fit together
