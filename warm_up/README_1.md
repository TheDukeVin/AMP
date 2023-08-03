# Warm-Up 1: Hello NYC with VSCode and Python
`warm_up_1.py` contains the following Python code:
```python
if __name__ == "__main__":
    print("Welcome to 🗽 for AMP 2023!!")
    user_name = input("What's your name? ")
    print(f"Hello {user_name}!")
    print(f"Did you know that '{user_name}' has {len(user_name)} characters?")
    print(f"'{user_name[0]}' is the first letter of your name. '{user_name[-1]}' is the last letter of your name.")
```
What do you think will happen when you run this code?

## Line #1 provides a starting point for the Python interpreter:
```python
if __name__ == "__main__":
```
- While not strictly necessary, including this in your Python program provides an explicit context for the Python interpreter
   - `"__main__"` essentially means this file is being run as a stand-alone program
- In later exercises you'll include function definitions which precede this line. However, code in this section will be executed first.
- There are other important considerations for including this line in your Python files, some of which we'll explore later in the summer.

### Indentation is very important in Python.
- Lines 2 - 5 are consistently indented to indicate that they are part of this section. 
- The Python interpreter will throw an error if you aren't consistent with your indentation.


## Line #2 outputs a text-based message to the Terminal:
```python
print("Welcome to 🗽 for AMP 2023!!")
```
### `print` is a built-in Python function used to display output to the terminal.
- In this example, the `print` function takes a single string literal as a parameter.

### Python string literals can be delimited several different ways:
```python
"This is a string."

'This is also a string.'

"""
  This is 
  a multi-line string.
"""

'''
  This is also
  a multi-line string.
'''
```

## Line #3 prompts the user to enter their name, then stores the data in a variable:
```python
user_name = input("What's your name? ")
```
### `input` is a built-in Python function used to gather input from the terminal
- An optional string parameter is shown as a prompt to the user
- Data entered by the user is returned as a string

### Variables store a reference to data for future access
- Python variable names:
   - must start with a letter or the underscore character, and contain only alpha-numeric characters and underscores: `A-z`, `0-9`, and `_`
   - are case-sensitive
   - should be self-documenting
- *snake_case* is a variable naming convention using lowercase letters and `_` to separate words 
   - AMP projects will use snake_case for most variale/function names

## Line #4 uses *f-string* notation to interweave the `user_name` variable into a string literal:
```python
print(f"Hello {user_name}!")
```
There are many ways to include variables in Python output. For consistency, AMP projects will use Python *f-strings*.
- Placing an 'f' just before a Python string literal indicates that *f-string* notation will be used.
- *f-string* notation uses `{}`'s to indicate that the name of the variable should be replaced by the data referenced by the variable.

## Line #5 creates a string literal with double-quotes, while also using single-quotes inside of the string with no error:
```python
print(f"Did you know that '{user_name}' has {len(user_name)} characters?")
```
### The `len` function is used to determine the length of a string. 
- Notice how f-string notation permits function calls.
- The `len` function can also be used to determine the length of a list.

## Line #6: String Indexing
Line #6 uses index notation to reference individual letters in a string variable:
```python
print(f"{user_name[0]} is the first letter of your name. {user_name[-1]} is the last letter of your name.")
```
### String indexing is similar to array/list indexing
- `[]`s are used to indicate a specific index
- Notice how string indexing uses `0` to refer to the first letter of a string. 
- Python permits negative indexing, which subtracts from the length of the string/list.

## Exercises
1. Use the VSCode editor to run `warm_up_1.py`
   1. Open VSCode
   2. Open `warm_up_1.py` in VSCode
   3. Run the Python code in `warm_up_1.py`

2. Change the last line of `warm_up_1.py` to break the indentation pattern: 
   ```python
   if __name__ == "__main__":
       print("Welcome to 🗽 for AMP 2023!!")
       user_name = input("What's your name? ")
       print(f"Hello {user_name}!")
       print(f"Did you know that '{user_name}' has {len(user_name)} characters?")
      print(f"'{user_name[0]}' is the first letter of your name. '{user_name[-1]}' is the last letter of your name.")
   ```
   Save your changes, then run the code. What feedback does the Python interpretter give you?

3. Undo your changes from #2, then extend the original code in `warm_up_1.py`:
   - Ask the user where they're traveling from. 
   - Store their response in an appropriately named variable.
   - Output to the terminal: `"Don't get homesick for ____________ while you're living in NYC for the summer!"`#