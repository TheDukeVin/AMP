def get_side_lengths():
    """Prompts the user to enter three side lengths of a triangle.

    Returns:
      Three float values reprsenting the side lengths of the triangle
    """
    side_1 = float(input("Side 1: "))
    side_2 = float(input("Side 2: "))
    side_3 = float(input("Side 3: "))
    return side_1, side_2, side_3

def classify_triangle(side_1, side_2, side_3):
    """Given three sides of a triangle, classifies a triangle into 1 of 4 categories: "does not exist", "acute", "obtuse", or "right"
      
        HINT:
        - Right Triangles: the sum of the squares of the two smaller sides equals the square of the largest side
        - Obtuse Triangles: the sum of the squares of the two smaller sides is less than the square of the largest side
        - Acute Triangles: the sum of the squares of the two smaller sides is greater than the square of the largest side
        - Does Not Exist: the sum of the smaller two sides doesn't exceed the length of the largest side

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
    #your code goes here
    return "TODO"

if __name__ == "__main__":
    side1, side2, side3 = get_side_lengths()
    print(classify_triangle(side1, side2, side3))
