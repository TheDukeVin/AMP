import tkinter as tk
import random
import math

def distance(x1, y1, x2, y2):
    # Return the distance between the points (x1, y1) and (x2, y2).
    return -1

def is_dart_in_square(
        dart_x, dart_y, square_left_x, square_left_y, square_right_x, square_right_y):
    """
    Return the boolean True if the coordinate (dart_x, dart_y) lies within the square
    whose upper left vertex is at (square_left_x, square_left_y) and lower right
    vertex is at (square_right_x, square_right_y), and False otherwise.
    """
    return False

def is_dart_in_circle(dart_x, dart_y, circle_center_x, circle_center_y, circle_radius):
    """
    Return the boolean True if the coordinate (dart_x, dart_y) lies within the circle
    of radius length circle_radius whose center is at (circle_center_x, circle_center_y),
    and False otherwise.
    """
    return False

# Returns x-coordinate less than the window width.
def get_dart_x(window_width):
    return random.randrange(0, window_width) 

# Returns y-coordinate less than the window height.
def get_dart_y(window_height):
    return random.randrange(0, window_height) 

# Displays a "dart" circle (with radius 2) on the canvas for visualization purposes.
def visualize_dart(dart_x, dart_y):
    canvas.create_oval(dart_x - 2, dart_y - 2, dart_x + 2, dart_y + 2, fill='black')


if __name__ == "__main__":
    appWidth = 375
    appHeight = 250

    app = tk.Tk()
    app.title("Estimating Pi")
    app.geometry(f"{appWidth}x{appHeight}")
    canvas = tk.Canvas(app, bg="#cccccc", width=appWidth, height=appHeight)
    canvas.pack()

    radius = 100

    square_left_x, square_right_x = 25, 25 + radius
    square_left_y, square_right_y = 75, 75 + radius
    canvas.create_rectangle(square_left_x, square_left_y, square_right_x, square_right_y, outline='green') #top left, bottom right

    circle_left_x, circle_right_x = 150, 150 + 2 * radius
    circle_left_y, circle_right_y = 25, 25 + 2 * radius
    circle_center_x = (circle_right_x - circle_left_x) // 2 + circle_left_x
    circle_center_y = (circle_right_y - circle_left_y) // 2 + circle_left_y
    canvas.create_oval(circle_left_x, circle_left_y, circle_right_x, circle_right_y , outline='red')

    app.mainloop()