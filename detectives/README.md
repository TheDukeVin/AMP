# Prize Envelopes

[Prize Envelopes presentation](https://docs.google.com/presentation/d/1zd7fIaylFjKLdWjTJYygZ8gwrFBgFIbTzapop6Zs4Ps/edit#slide=id.g14975c0d44e_1_0)

## Puzzle
A gameshow has up to $1000 to give away to a single contestant. However, contestants can earn any amount from $1 - $1000 based on their performance solving a collection of puzzles. To help facilitate awarding the correct prize amount during a  live stream of the game show, the game show host suggests that the $1000 should be divided into 10 envelopes before the show goes live. The game show producers get confused. Is there a way to split up $1000 between 10 envelopes such that the game show host can quickly award the correct amount of prize money without opening any envelopes?

## Problem Solving Strategy
### Transform and Conquer - Representation Change
10: 489
9: 2^8
8: 2^7
...
2: 2^1
1: 2^0

## General Lesson Format
1. Introduce puzzle
2. Students solve the puzzle
    - Maybe rotate through a couple different partners?
3. Teachers give tip: Binary
    -Walk though converting binary to decimal and decimal to binary
4. Introduce full list of Python Order of Operations
    - Point out interesting operators
        - **
        - -3//2  vs int(-3/2)
        - -10%3
        - Differing precedence of the logical operators
        - absence of ++/--
5. Exercise: Find and fix several mistakes envelope.py, which contains a variety of to_binary algorithms:
    - Built-in: bin
    - Built-in: format
    - Division by 2
    - Subtracting powers of 2
    - Bitwise Operators (Challenge for stronger students)
 
## Teacher Notes
This is a short lesson. The main goal is to introduce students to the general class format:
    - 1. Puzzle
    - 2. Understand solution to the puzzle
    - 3. Talk about translating the solution into code
    - 4. Implement modifications to the coding solution

Generating binary comes up again as combinations example in Guess Who’s Coming to Dinner puzzle

There’s more time to talk about The Warm-Up exercises on Day 2. 

The exercise is more about careful reading than writing. It’s an opportunity for students to see:
- Common Python mistakes
- Repetition with while
- Selection with if and else/if
- Programmer-defined functions
- Intro to String slicing

No type hints or doc strings in envelope.py…. they’ll come in the next two projects

## TODO
-
