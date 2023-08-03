"""
Welcome To AMP! Let's make friends!

In this assignment we're going to be reasoning about people and their friends.

~~~ PEOPLE ~~~~~

Each person will be represented by a string (aka `str`).
We'll represent the list of people in our Universe as a list of names, for example,
If the only people in our universe are 
    Joshua, Sebastian, Sam, David, 
    Dylan, Angela, Sai, Dean, Jiayi,
    Eckhart, and Jesus

We represent this using a list of names. You may assume that names are unique and 
that the lists of names have no duplicates
    ["Joshua", "Sebastian", "Sam", "David", "Dylan", 
    "Angela", "Sai", "Dean", "Jiayi", "Echkart", "Jesus"]

In the rest of this assignment, the list of people (which may represent any number of people, 
not just the ones above) will be referred to as the argument `people`

~~~ LIKES ~~~

We represent a relationship `likes` as a list of the names of two people.

If a pair of people (a,b) is in the list `likes` then a likes b.

For instance for instance if "Bill" and "Ted" like each other then the likes list is
    [("Bill", "Ted"), ("Ted", "Bill")]


If we want to indicate that "Bill" likes "Ted" but not vice versa, the list is
    [("Bill", "Ted")]

Excellent.

~~~ Python Loops ~~~

To solve the problems in this homework, you will need to use loops in python.

I strongly recommend that you use for loops. Generally in python you want to use 
for-loops instead of while loops whenever you can to avoid the possibility of an infinite loop

Python has some pretty cool features that makes looping over lists very ergonomic.
For example, loop over a list of pairs, such as `likes`, and print out each element,
you can write the following code

    for (liker, likee) in likes:
        print (liker, "likes", likee)
    
If you run this on the Bill and Ted mutual-liking list you'll get the following output

    Bill likes Ted
    Ted Likes Bill

~~~~ List Comprehensions ~~~~

You may also find list comprehensions useful, though you do not need them. 
List comprehensions provide a way to loop over a list without writing them down.
If you know "set builder" notation in mathematics, its a similar idea.

To compute the list of people who like "Bill", simply write the command

    likes_bill = [liker for (liker, likee) in likes if liker == "Bill"]

This is equivalent to, but more succinct than, the following for-loop

    likes_bill = []
    for (liker, likee) in likes:
        if likee == "Bill":
            likes_bill.append(liker)
"""


def no_imaginary(people: list[str], likes: list[tuple[str, str]]) -> bool:
    """
    Imaginary friends get us through childhood. 
    If we have them as adults, others may get concerned.

    Make sure that noone likes anyone "imaginary" i.e. not in the list of people

    >>> no_imaginary(["Ted", "Bill"], [("Ted", "Bill"), ("Bill", "Ted")])
    True

    >>> no_imaginary(["Ted"], [("Ted","Acathla the Friendly Demon")])
    False

    Also make sure that noone is liked by anyone imaginary i.e. not in the people set

    >>> no_imaginary(["Bill"], [("Buffo the Clown","Bill")])
    False
    """
    # TODO Implement Me!
    return False

def friends(likes: list[tuple[str, str]]) -> bool:
    """
    Friendship is mutual liking. 
    Okay theres more to it than than.. You have to take them out for coffee, chat about deep personal trauma..
    But I don't know how to code emotional support...
    so consider a and b to be friends iff a likes b and b likes a.

    Return True if everyone who likes someone is liked by that person, and false otherwise

    >>> friends([("Bill","Ted"),("Ted","Bill")])
    True

    >>> friends(["Bill","Ted"])
    False
    """
    # TODO Implement Me!
    return False

def self_love(likes: list[tuple[str, str]]) -> list[tuple[str, str]]:
    """
    Love yourself, but don't like your own posts
    Make sure we only represent external liking relationships by removing self-likes.

    >>> self_love([("me","me")])
    []

    >>> self_love([("you", "me"), ("me","you"), ("you", "you")])
    [("you", "me"), ("me", "you")]
    """
    # TODO Implement Me!
    return []

def antisocial_social_club(people: list[str], likes: list[tuple[str, str]]) -> list[str]:
    """
    Misanthropes are a special breed.
    Let's put them in a room together so they can bond over their hatred of other people.

    You may find it helpful to write a subroutine that checks whether anyone likes a person.

    return a list of all of the people who like noone.

    >>> antisocial_social_club(["Jen", "Amy", "Ms. Anthrope", "Isa Lated"], [("Jen","Amy"), ("Amy", "Jen")])
    ["Ms. Anthrope", "Isa Lated"]

    Note that being a misanthrope doesn't mean you aren't well liked, just that you like noone.
    Indeed misanthropes can be the most popular:

    >>> antisocial_social_club(["Jen", "Amy", "Ms. Anthrope"], [("Jen","Ms. Anthrope"), ("Amy", "Ms. Anthrope")])
    ["Ms. Anthrope"]
    
    """
    return []

def count_friends(people: list[str], likes: list[tuple[str, str]]):
    """
    Return a list whose ith index corresponds to the number of people who are friends
    assume that no_imaginary_friends(people, likes) and friends(likes) both hold

    You may find it convenient to write a helper function that counts the number of friends for a single person

    Be very careful not to double-count!

    Extra credit: Think about how you can restructure the data in `likes` so that this is more efficient.
    Write a function that converts likes to your new data structure and implements the count_friends function
    on this more efficient data structure. Hint: think about how you can use `dict`s or `set`s. 
    If you don't know what those are, feel free to google them!

    >>> count_friends(["Bill","Ted","Ana"], [("Bill","Ted"), ("Ted", "Bill"), ("Ana", "Ted"), ("Ted", "Ana")])
    [1, 2, 1]

    >>> count_friends(["Bill", "Ted", "Ana"], [])
    [0, 0, 0]
    """
    return []


if __name__ == "__main__":
    """
    Only code written in this if-block is executed.
    Use this section to write tests for your code.
    Make liberal use of the the `print` and `assert` commands!

    Remember that in Python, you can print most things!
    """
    # Test for no_imaginary
    

    # Test for friends
    


    # Test for self_love
    
    

    # Test for antisocial_social_club
    
    

    # Test for count_friends


    assert True