import math

def roadtrip_demo():
    roadtrip_destinations = ["Seattle", "Leavenworth", "Mount Rainier", "Seattle"]
    print(roadtrip_destinations)

    num_destinations = len(roadtrip_destinations)
    print(f"I plan to make {num_destinations} stops on my roadtrip.")

    roadtrip_destinations.append("Sequim")
    num_destinations = len(roadtrip_destinations)
    print(f"We added a city to our list. Now I plan to make {num_destinations} stops on my trip.")
    print(f"My new itinerary: {roadtrip_destinations}")

    third_destination = roadtrip_destinations[2]
    print(f"My 3rd destination will be {third_destination}")

    last_destination = roadtrip_destinations[len(roadtrip_destinations)-1]
    print(f"The last destination will be {last_destination}.")

def favorite_numbers_demo():
    my_favorite_numbers = [6, 0, math.pi, -1.5, 1000000]
    for i in range(len(my_favorite_numbers)):
        print(f"I love the number {my_favorite_numbers[i]} ❤️")
        print(f"There are only {i} numbers in the whole world that I love more!")

# This function prints out the first n natural numbers
def natural_numbers(n):
    natural_numbers = []
    for number in range(1, n+1):
        natural_numbers.append(number)
    return natural_numbers

# Exercise
def negative_numbers(n):
    """
    Implement this function with your own code!
    Return a list of the greatest n negative integers
    e.g. negative_numbers(3) would return [-1, -2, -3]
    """

if __name__ == "__main__":
    roadtrip_demo()
    favorite_numbers_demo()

    x = 10
    list_of_natural_numbers = natural_numbers(x)
    print(list_of_natural_numbers)

    y = 10
    list_of_neg_numbers = negative_numbers(y)
    print(list_of_neg_numbers)