# Warm-Up 2: Hello Unit Testing (w/ Gradescope)
Consider the following Python code:
```python
import math

def get_radius():
    radius = input("Enter the radius of a circle (mm): ")
    return float(radius)

def calculate_circumference(radius):
    return 2*math.pi*radius

if __name__ == "__main__":
    radius = get_radius()
    circumference = calculate_circumference(radius)
    print(f"A circle with radius {radius}mm has a circumference of {round(circumference, 3)}mm")
```
- What problem is being solved by this code? 
- What do you think will happen when you run this code?

## Problem Solving with Code
At a top level, problem solving with code can be described by three steps:
1. Gather necessary input.
2. Perform some calculation using the input.
3. Display results.

The `"__main__"` section of the above code splits the process of finding the circumference of a circle into similar steps:
1. Get a circle radius from the user.
2. Calculate the circumference of a circle using the given radius.
3. Display the resulting circumference to the user.

## Step 1: Get a circle radius from the user.
```python
radius = get_radius()
```
`get_radius()` redirects program execution to the `get_radius` function definition. Once `get_radius` finishes executing, returned data is stored in a variable called `radius`.

### Defining Functions
`get_radius` is a function which is defined toward the top of the file:
```python
def get_radius():
    radius = input("Enter the radius of a circle (mm): ")
    return float(radius)
```
When defining a function:
- The keyword `def` is used to begin the function definition.
- The `:` symbol is used to begin the *body* of the function.
- Consistent indentation indicates which lines of code should be considered part of the function definition.
- `return` immediately ends the function by sending data back to  where `get_radius` was invoked. 
- Function names follow the same rules as variable naming:
   - must start with a letter or the underscore character, and contain only `A-z`, `0-9`, or `_`
   - case-sensitive
   - self-documenting
- Function definitions must come before the function is used

### Data Types
Understanding data types is an important first step in code-based problem solving. The radius and circumference of a circle are both numeric values. However, the `input` function only returns string (ie. text-based) data. This requires 
working with two data different types:
- `float` - Floating-point numbers (decimals)
- `str` - Single-letters, and text-based words

*Type conversion* describes the process of converting data into a different data type.

The last line of `get_radius` converts the original string data of `radius` into numeric data by using the built-in `float` function:
```python
return float(radius)
```
Python has several built-in data types which will be important this summer:
- Numeric Data Types: `int`, `float`
- Text Data Type: `str`
- Boolean Data Type: `bool`
- Sequence Data Types: `list`, `tuple`, `range`
- Mapping Data Type: `dict`
- Set Data Type: `set`

## Step 2: Calculate the circumference of a circle with the given radius.
```python
circumference = calculate_circumference(radius)
```
### Function Parameters
`calculate_circumference` is a programmer-defined function one required parameter:
```python
def calculate_circumference(radius):
    return 2*radius*math.pi
```
Even though the formula to calculate the circumference of a circle is essentially a 1-line calculation, creating a stand-alone function for `calculate_circumference` allows us to test the function in isolation.

### Python Arithmetic and the Order of Operations
`calculate_circumference` makes use of the `*` operator for multiplication. 

Python has the following built-in arithmetic operators:
| Precedence| Operation    | Operator |  Example  |  Result  |
| -------- | -------- | ------- | -------- | ------- |
| 1 | Exponent  | `**`    | 2**4 | 16 |
| 2 | Multiplication  | `*`    | 2*4 | 8 |
| 2 | Division  | `/`   | 2/4 | 0.5 |
| 2 | Floor Division  | `//`    | -2//4 | -1 |
| 2 | Remainder  | `%`   | 2%4 | 2  |
| 3 | Subtraction  | `-`   | 2-4 | -2  |
| 3 | Addition  | `+ `  | 2+4 | 6  |

### The `math` Library
The first line of code in this example imports the `math` library:
```python
import math
```
This allows us to use `math.pi` as a reliable approximation for $\pi$.

The `math` library contains many useful functions/constants:
- constants: `math.pi`, `math.e`, etc.
- functions: `math.sqrt`, `math.floor`, `math,ceil`, `math.log`, etc.

`math` library functions and constants aren't available without first importing the `math` library.

## Step 3: Display results to the user.
```python
print(f"A circle with radius {radius}mm has a circumference of {round(circumference, 3)}mm")
```
This output prioritizes *understandability* by stating the original problem, user input, and the numeric result in a concise manner. Further, units are included to provide a context for numeric data.

### Built-in math function: `round`
To help make results more readable, the built-in `round` function is used to indicate that only 3 decimals from  `circumference` data should be displayed.

## Exercises
1. Submit `warm_up_2.py` to Gradescope without changing anything in the file.
    - Gradescope makes several calls to `calculate_circumference` using different values for the `radius` parameter. 
    - Gradescope compares expected values with actual values returned by the `calculate_circumference` function to determine whether a particular test has failed.

2. Introduce a mistake in the definition of `calculate_circumference` in `warm_up_2.py`:
    ```python
    def calculate_circumference(radius):
        return radius*math.pi      # should be 2*radius*math.pi 
    ```
    Save your changes, then resubmit this modified version of `warm_up_2.py` to Gradescope. What feedback do you receive?

3. Correct the implementation of `calculate_area` in `warm_up_2.py`, then submit `warm_up_2.py` to Gradescope.

4. Correct the implementation of `calculate_distance` in `warm_up_2.py`, then submit `warm_up_2.py` to Gradescope.