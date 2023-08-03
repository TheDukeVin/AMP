import math

def get_radius():
    radius = input("Enter the radius of a circle (mm): ")
    return float(radius)

def calculate_circumference(radius):
    return 2*radius*math.pi

if __name__ == "__main__":
    radius = get_radius()
    circumference = calculate_circumference(radius)
    print(f"A circle with radius {radius}mm has a circumference of {round(circumference, 3)}mm")