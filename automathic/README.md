# Automathic

[Automathic presentation](https://docs.google.com/presentation/d/1WlzwlulKRjxCzkyJfFoBONQQ0a3M9JAWEV0xNhPAWuQ/edit#slide=id.g14975c0d44e_1_0)

## Puzzle Description
### Project Euler #1: Multiples of 3 or 5
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

## Problem Solving Strategy
### Finding Patterns
Students solve the problem by understanding that some multiples of 3 and 15 are shared.

## General Lesson Format
0. Ask about Warm-Up activity. Quickly highlight important points:
- VSCode: Running, Editing, Terminal, Problems
- Differences between Python and other coding languages (student-led discussion)
   - No explicit data types with variable declarations
   - Required indentation consistency
   - Designed to be closer to English:
      - and, or, not
      - Reduced syntax requirements: no ;, if statement (), {}
   - New keywords/symbols: def, elif, **
   - Familiar keywords/symbols: if, return, else, =, *

1. Opening Statements: 
- *Coding* is providing instructions for a machine to complete some task.
- *Problem Solving* is the process of understanding which instructions to give to a computer. 
- The set of instructions for completing some task is called an *algorithm*.
- AMP:CS is about problem solving as much as it is about coding.

2. Introduce [Project Euler](https://projecteuler.net/) as a repository of math problems curated for computational solutions.
- We will assign some specific Project Euler problems over the summer. However, students are encouraged to explore Project Euler on their own. Problems can be solved in any order.

3. Class discussion: How would you solve PE #1?
- Students discuss with a partner, then write their collaborative solution on a white board (in English)
- In the discussion, make sure to discuss “Understanding the Problem'' as the first step. In this case, students should identify a few keywords in the problem description before attempting to solve the problem: 
   - sum
   - below 1000
   - natural numbers
   - multiples
   - or
- Distinguish writing a set of instructions for solving a problem from actually solving the problem
- Compare approaches: multiple loops vs. one loop

4. In order for students to solve the problem, they'll need to learn about Python for loops. 
- Introduce Python for loops:
For Loops
```python
for i in range(10):
   print(i)       # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

for i in range(2, 10, 2):
   print(i)       # 2, 4, 6, 8

for i in range(10, 0, -2):
   print(i)       # 10, 8, 6, 4, 2
```

5. Allow student time to solve PE #1.
   - Students should raise their hand to let the teacher know when they have successfully submitted their answer to Project Euler
   - Students who finish early can read ahead in the slides to start on the project

6. Intro duce list basics and list comprehensions
Lists
```python
nums = [2, 4, 6, 8]

for i in range(len(nums)):             # every index, element in the nums list
  print(i, nums[i])

for i in range(len(nums)-1, -1, -1):   # every index, element in the nums list (reverse order)
  print(i, nums[i])

for n in nums:                         # every element in the nums list
   print(n)

for i, n in enumerate(nums):           # every index, element in the nums list
   print(i, n)s

len(nums)        # number of items in the list
nums.append(10)  # insert 10 to the end of the list
```
List Comprehensions
```python
nums = [2*i for i in range(0, 5)]            # [0, 2, 4, 6, 8]
nums = [i for i in range(0, 10, 2)]          # [0, 2, 4, 6, 8]
nums = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
```

7. Assign Automathic:

## Exercise
### Automathic
Menu-driven starter code asking students to implement a collection of functions which generate lists with n terms from the following sequences:
 - positive odd integers 
 - positive integer multples 
 - square numbers
 - triangular numbers
 - arithmetic sequence
 - fibonacci sequence (iterative approach)

## Teacher Notes
Fibonacci sequence will come up again in multiple Project Euler problems, dynamic programming, and recursion discussions

Consider requiring the output of the sum of arithmetic and geometric sequences….. 

No type hints in starter code yet, that comes with the next project


## TODO