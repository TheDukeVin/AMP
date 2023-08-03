import math

def tristate_area_demo():
    tristate_area = ("New York", "New Jersey", "Connecticut")
    num_states = len(tristate_area)
    print(f"There are {num_states} states in the tristate area")
    for state in tristate_area:
        print(f"{state} is in the tristate area")
    
def introduce_yourself_demo():
    # each person is a tuple of (name, age, hometown)
    alice = ("Alice", 20, "Phoenix")
    bob = ("Bob", 19, "Montgomery")
    for person in [alice, bob]:
        print(f"Hi, I'm {person[0]}. I'm {person[1]} years old, and I'm from {person[2]}.")

def mutating_tuple_demo():
    fruits = ("apple", "banana", "canteloupe")
    fruits[0] = "apricot" # trying to change the first fruit to "apricot"

def sphere_volume_and_surface_area(radius):
    '''
    Computes the volume and surface area of a sphere of given radius

      Args:
      radius: float (decimal) radius of sphere (in meters)

      Return:
      (volume, surface area): tuple of two floats (decimals) 
      (the volume in meters^3, then the surface area in meters^2)
    '''
    volume = 4.0 / 3.0 * math.pi * radius**3
    surface_area = 4.0 * math.pi * radius**2
    return (volume, surface_area)
    # Note the above is the same as the following line:
    # return volume, surface_area

def changed_major(student_information):
    '''
    Given a student's information,
    determines whether the student changed their intended major after attending AMP

      Args:
      student_information: tuple containing (name, age, major before AMP, major after AMP)

      Return:
      True if this student changed their major, False otherwise 
    '''
    # Fill in your code here!
    return False

if __name__ == "__main__":
    tristate_area_demo()
    introduce_yourself_demo()
    # Uncomment the line below to try mutating a tuple
    # mutating_tuple_demo()

    r = 5.0
    sphere_vol, sphere_surf_area = sphere_volume_and_surface_area(r)
    print(f"A sphere with radius {r} has volume {sphere_vol} and surface area {sphere_surf_area}")

    # Uncomment the code below to test your implementation of changed_major
    # carlos_major_before = "Architecture"
    # carlos_major_after = "Computer science"
    # carlos_student_info = ("Carlos", 18, carlos_major_before, carlos_major_after)
    # carlos_changed = changed_major(carlos_student_info)
    # print(f"Before, Carlos wanted to major in {carlos_major_before}, and now he's majoring in {carlos_major_after}.")
    # if carlos_changed:
    #     print("Carlos DID change his major while at AMP.")
    # else:
    #     print("Carlos did NOT change his major while at AMP.")
