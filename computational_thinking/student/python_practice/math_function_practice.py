import math

def get_radius():
    radius = input("Enter the radius of a circle (mm): ")
    return float(radius)

def calculate_circumference(radius):
    return 2*radius*math.pi

# In-class Exercise
def calculate_area(radius):
    """
    Fill in this function yourself!
    Hint: refer to slides for how to do exponents in python
    """
    return -1  #intentionally incorrect... -1 is not a valid area


if __name__ == "__main__":
    user_radius = get_radius()

    circumference = calculate_circumference(user_radius)
    print(f"A circle with radius {user_radius}mm has a circumference of {round(circumference, 3)}mm")
 
    area = calculate_area(user_radius)
    print(f"A circle with radius {user_radius}mm has an area of {round(area, 3)}mm\u00b2")
