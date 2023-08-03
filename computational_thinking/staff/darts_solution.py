import tkinter as tk
import random
import math
import matplotlib.pyplot as plt

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def is_dart_in_square(
        dart_x, dart_y, square_left_x, square_left_y, square_right_x, square_right_y):
    if (dart_x > square_left_x and dart_x < square_right_x 
        and dart_y > square_left_y and dart_y < square_right_y):
        return True
    return False

def is_dart_in_circle(dart_x, dart_y, circle_center_x, circle_center_y, circle_radius):
    if distance(dart_x, dart_y, circle_center_x, circle_center_y) < circle_radius:
        return True
    else:
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

    num_darts_per_trial = range(10, 1000, 10)
    approx_pi_per_trial = []

    for num_darts in num_darts_per_trial:
        num_in_circle = 0
        num_in_square = 0.1  # Prevents division by 0, in case 0 points land in the square!
        # Randomly throw num_darts darts at the board.
        for _ in range(num_darts):
            dart_x = get_dart_x(appWidth)
            dart_y = get_dart_y(appHeight)
            # Comment back in for visualization: visualize_dart(dart_x, dart_y)
            # Check where the dart landed.
            if is_dart_in_circle(dart_x, dart_y, circle_center_x, circle_center_y, radius):
                num_in_circle += 1
            elif is_dart_in_square(dart_x, dart_y, square_left_x, square_left_y, square_right_x, square_right_y):
                num_in_square += 1
        approx_pi_per_trial.append(num_in_circle / num_in_square)

    plt.xlabel('Trials')
    plt.ylabel(f'PI')
    plt.title("Estimating Pi")
    plt.axhline(y = 3.14, color = 'red', linestyle = '-')
    plt.plot(num_darts_per_trial, approx_pi_per_trial)
    plt.show()
    app.mainloop()