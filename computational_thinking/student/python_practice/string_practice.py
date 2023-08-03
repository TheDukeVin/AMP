"""
This file is meant to give you practice with Python strings.
"""
def iterate_through_string(some_string: str) -> None:
    for letter in some_string:
        print(letter + "...")

def welcome_to_NYC():  # Demos f-strings, indexing, and len.
    print("Welcome to 🗽!!")
    user_name = input("What's your name? ")
    print(f"Hello {user_name}!")
    print(f"Did you know that '{user_name}' has {len(user_name)} characters?")
    print(f"'{user_name[0]}' is the first letter of your name. '{user_name[-1]}' is the last letter of your name.")

# Complete the following function. You may need to add parameter(s).
"""
Takes a list of N places someone wants to visit
and returns their itinerary in the following format: 
city1 -> city2 -> …. -> cityN

    Parameters: ????

    Return: ????

    Example
    ------
    >>>create_itinerary(['NYC', 'London', 'Shanghai'])
    'NYC -> London -> Shanghai'
"""
def create_itinerary():
    pass

if __name__ == "__main__":
   iterate_through_string("1989")
   iterate_through_string("shake it off")
   welcome_to_NYC()