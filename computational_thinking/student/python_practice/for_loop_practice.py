"""
This file is meant to give you practice with for loops.
Feel free to play around with it to get a sense of how for loops work!
"""
def for_loop_stop():
    for i in range(5):
        print(i)

def for_loop_start_stop():
    for i in range(5, 10):
        print(i)

def for_loop_start_stop_step():
    for i in range(2, 10, 2):
        print(i)

def for_loop_start_stop_negative_step():
    for i in range(10, 0, -2):
        print(i)


# Exercise
def for_loop_multiples_of_three():
    """
    Fill in this function yourself!
    Use a for loop to print out the first 8 non-negative multiples of 3:
    0
    3
    6
    ...
    21
    """

    # Your code here

    return 0


if __name__ == "__main__":

    # Pro tip: putting a '#' symbol in front of a line of code turns it into a 'comment'
    # Comments are not run when you run the code
    # Uncomment one line at a time below to run one function at a time!

    for_loop_stop()
    # for_loop_start_stop()
    # for_loop_start_stop_step()
    # for_loop_start_stop_negative_step()
    for_loop_multiples_of_three()