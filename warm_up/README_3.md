# Warm-Up 3: Hello Python Selection
Consider the following Python code:
```Python
def get_side_lengths():
    side_1 = float(input("Side 1: "))
    side_2 = float(input("Side 2: "))
    side_3 = float(input("Side 3: "))
    return side_1, side_2, side_3

def is_valid_triangle(side_1, side_2, side_3):
  
  if side_1 <= 0 or side_2 <= 0 or side_3 <= 0:  #all side lengths must be positive
    return False
  
  #sum of smaller two side lengths must exceed larger side length
  if side_1 >= side_2 and side_1 >= side_3 and side_2 + side_3 <= side_1: 
    return False
  elif side_2 >= side_1 and side_2 >= side_3 and side_1 + side_3 <= side_2:
    return False
  elif side_3 >= side_1 and side_3 >= side_2 and side_1 + side_2 <= side_3:
    return False
  else:
    return True
    
if __name__ == "__main__":
    side_1, side_2, side_3 = get_side_lengths()

    if is_valid_triangle(side_1, side_2, side_3): 
        print(f"Side lengths {side_1}, {side_2}, and {side_3} DO form a valid triangle.")
    else:
        print(f"Side lengths {side_1}, {side_2}, and {side_3} DO NOT form a valid triangle.")
```
This code verifies whether three given side lengths can be used to create a valid triangle. 

There are two major red flags to look out for in regards to determining whether three given side lengths can form a valid triangle:
- are all three side lengths positive?
- is the sum of the smaller two sides greater than the largest side?

## Boolean Data Type
The `bool` data type has two potential values: `True` or `False`

## Boolean Expressions
A Boolean expression is any expression that evaluates to either `True` or `False`

### Boolean Operators: `<`, `>`, `<=`, `>=`, `!=`, `==`

### Logical Operators: `not`, `and`, `or`
Simple boolean expressions can be combined into more complex boolean expressions with logical operators:
| Precedence| Operation    | Operator |  Example  |  Result  |
| -------- | -------- | ------- | -------- | ------- |
| 1 | Logical NOT  | `not` | `not 5 > 6`| `True` |
| 2 | Logical AND  | `and` | `not 5 > 6 and -2 > 0` | `False` |
| 3 | Logical OR  | `or` | `not 5 > 6 or -2 < 0` | `True`  |

Two important considerations with logical operators:
- Logical operators have different precedence in the order of operations… and will be evaluate before or in a complex boolean expression combining both operators
- Many other programming languages use ~, &&, and || to represent the same logical operators. It’s an easy mistake to forget that Python uses English-based logical operators.


## Selection Statements
`if` statements create branching paths in the execution of code based on whether a Boolean expression evaluates to `True` or `False`
- The `:` symbol is used to indicate the body of an if statement.
- Unlike in other languages, Boolean expressions within an if statement do not need to be enclosed in `()`s

### if Statements
if statements create a possible path, one that is only taken if a Boolean expression evaluates to `True`:
```python
if side_1 <= 0 or side_2 <= 0 or side_3 <= 0:  #all side lengths must be positive
    return False
```
If one of the given side lengths is negative, the `is_valid_triangle` function immediately returns `False`. No further code in the function is executed.

However, it's possible that none of the given side lengths are negative. In that case, the code inside of the body of the if statement is skipped.

### if-else Statements
if-else statements create two mutually-exclusive branches:
```python
if is_valid_triangle(side_1, side_2, side_3): 
    print(f"Side lengths {side_1}, {side_2}, and {side_3} DO form a valid triangle.")
else:
    print(f"Side lengths {side_1}, {side_2}, and {side_3} DO NOT form a valid triangle.")
```
In an if-else statement one of the two paths must be followed. The body of the `else` section is sometimes called the *default*.

*Mutually-exclusive* for two alternatives means one, or the other, but not both. 

### Extended if Statements
An extended if statement creates multiple mutually-exclusive branches:
```python
if side_1 >= side_2 and side_1 >= side_3 and side_2 + side_3 <= side_1: 
    return False
elif side_2 >= side_1 and side_2 >= side_3 and side_1 + side_3 <= side_2:
    return False
elif side_3 >= side_1 and side_3 >= side_2 and side_1 + side_2 <= side_3:
    return False
else:
    return True
```
*Mutually-exclusive* in this case means one, but not more than one. The inclusion of an `else` means that at least one of the branching paths must be followed.

Pro Tip: For this particular scenario, the `elif` isn't strictly necessary. If a given Boolean expression were to be `True`, the function would return and immediately stop executing. Even though these are all mutually-exclusive conditions, all `elif` statements could be replaced with `if` to achieve the same results. In the same vein, the `else` could also be removed given that the function would necessarily have to return `True` when all the Boolean expressions evaluate to `False`. 

## Exercises
1. Implement the `classify_triangle` function in `warm_up_3.py`.
    - Right Triangles: the sum of the squares of the two smaller sides equals the square of the largest side
    - Obtuse Triangles: the sum of the squares of the two smaller sides is less than the square of the largest side
    - Acute Triangles: the sum of the squares of the two smaller sides is greater than the square of the largest side
2. Run tests included in function documentation locally with doctest.
3. If the two local tests pass, submit `warm_up_3.py` to Gradescope to run the full suite of tests.  