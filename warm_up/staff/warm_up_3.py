def get_side_lengths()-> list:
    """Prompts the user to enter three side lengths of a triangle.

    Returns:
      Three float values reprsenting the side lengths of the triangle
    """
    side_1 = float(input("Side 1: "))
    side_2 = float(input("Side 2: "))
    side_3 = float(input("Side 3: "))
    return side_1, side_2, side_3

def classify_triangle(side_1:float, side_2:float, side_3:float)-> str:
    """Given three sides of a triangle, classifies a triangle into 1 of 4 categories:
        - "does not exist", "acute", "obtuse", or "right"

        Args:
          side_1: The measurement of one side of the triangle
          side_2: The measurement of one side of the triangle
          side_3: The measurement of one side of the triangle

        Returns:
          A single string label- "does not exist", "acute", "obtuse", or "right"

        Examples
        --------
        >>>classify_triangle(2, 2, 4)
        "does not exist"

        >>>classify_triangle(3, 5, 4)
        "right"
    """
    if side_1 >= side_2 and side_1 >= side_3:
        c = side_1
        a, b = side_2, side_3
    elif side_2 >= side_1 and side_2 >= side_3:
        c = side_2
        a, b = side_1, side_3
    else:
        c = side_3
        a, b = side_1, side_2

    if a <= 0 or a + b <= c: return "does not exist"
    if a**2 + b**2 == c**2: return "right"
    if a**2 + b**2 < c**2: return "obtuse"
    return "acute"

if __name__ == "__main__":
    side1, side2, side3 = get_side_lengths()
    print(classify_triangle(side1, side2, side3))