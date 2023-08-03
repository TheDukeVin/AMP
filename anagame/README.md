# Anagame

## Puzzle Description
Anagame
1. Pick: seven 30-sided letter dice, or 7 scrabble tiles
    - If there are fewer than 3 vowels/wild, pick/roll again
2. Players have 2 minutes to find as many anagrams or palindromes as they can.
    - Wild rolls/blank tiles can be used as any letter
    - Wild rolls/blank tiles can be used as different letters in different word combinations
    - Letters may not be repeated unless multiple dice display the same letter
3. The player with the highest score at the end of 2 minutes wins!
    - 3 letter anagram pair: 1pt      are, ear
    - 4 letter anagram pair: 2pt      balm, lamb
    - 5 letter anagram pair: 3pt      sneak, snake
    - 6 letter anagram pair: 4pt      actors, costar
    - 7 letter anagram pair: 5pt      allergy, gallery

## Problem Solving Strategy
### Transform and Conquer

## Part 1: Anagram Race- General Lesson Format

1. Student should play 3-4 rounds of Anagame with letter dice or scrabble tiles (student choice)

2. Students work in groups of 2-3 to brainstorm as many different creative approaches to is_anagram(word1, word2) as they can come up with.
    - Groups articulate each approach with brief pseudocode and a diagram on large poster paper
    - Each group resents their collection of approaches to the class
    - Groups should make attempts to compare each approach by understandability, time, and memory
    - Note: These algorithms should be at a high level, independent of whether students could actually code the algorithm at this point
    - Highlight the five approaches from anagram_race.py in the discussion:
        - Exhaustive/Permutations
        - Letter Count
        - Check-Off
        - Sorting
        - Prime Hash

3. Go over helpful hints for anagram_race.py
- Python `dict` - Used for prime hash algorithm (slide in presentations)
- ASCII - used in Letter Count (hint in starter code)
- `sorted` - used in the Sorting approach, introduced in `get_factors` from Prime Timing
- itertools - used to generate all permutations of a word (hint in starter code)
- `get_valid_word_list()` - imported helper functions which contains a set of valid words


4. Assign anagram_race.py which asks students to implement the five is_anagram approaches from above.


5. Optional Project Euler problems for speedy students
- PE #98: Anagramic Squares
- PE #52: Permuted Multiples
- PE #35: Circular Primes
- PE #49: Prime Permutations
- PE #36: Double-base Palindromes
- PE #4: Largest Palindrome Product
- PE #125: Palindromic Sums

### Part 1 - Teacher Notes
- Push students to get as many algorithms as they can before sharing with the class
    - Students should concisely describe the algorithm with English
- `get_valid_word_list()` returns all valid words with between 2 -7 letters (inclusive). 
    - This list of words has been pruned of some potentially offensive English words.
    - Encourage students to help out by saying something if they see a word that is inappropriate/offensive and should be removed. 
- Students will have to iterate over strings, so encourage looking at Automathic or the Python-At-A-Glance sheet
- This activity is a lead in to implementing a digital version of AnaGame that improves upon the table-top version
- Introduces dictionaries, which will be very useful in part 2


## Part 2: Anagram Explorer- General Lesson Format



## Teaching Notes
- Comparing uniform random distributions with weighted random distributions
    - dice vs scrabble tiles
- Introduction to dictionaries


