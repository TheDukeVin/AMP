# Graphs Warmup

Graphs are a fundamental aspect of computer science, letting us reason about all kinds of binary relationships between entities, for example, friendship, coauthorship, collaboration.


## Project Description

In this project, students must perform a few basic warm up tasks to get them used to thinking about graphs.

Given a very simple graph representation, a list of vertices and a list of nodes, students will write a few warm up functions to get them familiar with the abstractions


## Problem Solving Strategy
### Nested loops and problem decomposition

- for each edge we must check that each edge is between vertices in the list of vertices
- check that no repeat edges occur

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

3. Class discussion: How would you solve PE #1?
- Students discuss with a partner, then write their collaborative solution on a white board (in English)
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

6. Introduce list basics and list comprehensions
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



## TODO