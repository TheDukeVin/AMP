import tkinter as tk

def RGB_3_loops():
    x = 50
    for y in range(50, 350, 3):  # Red.
        canvas.create_line(x, y, x + 350, y, width=1, fill='#FF0000') #x1, y1, x2, y2

    x = 200
    for y in range(51, 350, 3):  # Green.
        canvas.create_line(x, y, x + 350, y, width=1, fill='#00FF00') #x1, y1, x2, y2

    x = 125
    for y in range(151, 451, 3):  # Blue.
        canvas.create_line(x, y, x + 350, y, width=1, fill='#0000FF') #x1, y1, x2, y2

def RGB_1_loop():
    red_x = 50
    green_x = 200
    blue_x = 125
    for i in range(100):  # Index of line we are currently drawing.
        red_y = 50 + (i * 3)
        green_y = 51 + (i * 3)
        blue_y = 154 + (i * 3)
        canvas.create_line(red_x, red_y, red_x + 350, red_y, width=1, fill='#FF0000') #x1, y1, x2, y2
        canvas.create_line(green_x, green_y, green_x + 350, green_y, width=1, fill='#00FF00') #x1, y1, x2, y2
        canvas.create_line(blue_x, blue_y, blue_x + 350, blue_y, width=1, fill='#0000FF') #x1, y1, x2, y2


def grid():
    width, height = appWidth, appHeight
    color = '#666666'  # Initialize this variable so we can reuse the color for all the lines.
    for i in range(8):
        # Horizontal lines.
        canvas.create_line(0, i * (height / 8), width, i * (height / 8), width=2, fill=color)
        # Vertical lines.
        canvas.create_line(i * width / 8, 0, i * width / 8, height, width=2, fill=color)

        # Downward diagonals.
        canvas.create_line(0, i * (height / 8), (8 - i) * (width / 8), height, width=2, fill=color)
        canvas.create_line(i * width / 8, 0, width, (8 - i) * height / 8, width=2, fill=color)
        # Upward diagonals.
        canvas.create_line(0, i * (height / 8), (i) * (width / 8), 0, width=2, fill=color)
        canvas.create_line(i * (width / 8), height, width, i * (height / 8), width=2, fill=color)
    
# As we increase y, we increase x.
def curve_red():
    num_lines = 10
    step_size = appWidth // num_lines
    for i in range(num_lines):
        canvas.create_line(0, i * step_size, i * step_size, appHeight, width=2, fill='red')

# As we increase x, we decrease y.
def curve_yellow():
    num_lines = 10
    step_size = appWidth // num_lines
    for i in range(num_lines):
        canvas.create_line(0, (num_lines - i) * step_size, i * step_size, 0, width=2, fill='yellow') 

# As we increase x, we increase y.
def curve_green():
    num_lines = 10
    step_size = appWidth // num_lines
    for i in range(10):
        canvas.create_line(i * step_size, 0, appWidth, i * step_size, width=2, fill='green') 

# As we increase y, we decrease x.
def curve_blue():
    num_lines = 10
    step_size = appWidth // num_lines
    for i in range(10):
        canvas.create_line(appWidth, i * step_size, (num_lines - i) * step_size, appHeight, width=2, fill='blue') 

# Generalizes curve functions.
def draw_curve_at(a_x, a_y, b_x, b_y, corner_x, corner_y, color='blue'):
    num_lines = 10
    # a to c and b to c first.
    canvas.create_line(a_x, a_y, corner_x, corner_y, width=2, fill=color)
    canvas.create_line(b_x, b_y, corner_x, corner_y, width=2, fill=color)
    for i in range(num_lines):
        ac_x_diff = corner_x - a_x
        ac_y_diff = corner_y - a_y
        bc_x_diff = corner_x - b_x
        bc_y_diff = corner_y - b_y

        x1 = a_x + (ac_x_diff / num_lines) * i
        y1 = a_y + (ac_y_diff / num_lines) * i
        x2 = b_x + (bc_x_diff / num_lines) * (num_lines - i)  # Complement.
        y2 = b_y + (bc_y_diff / num_lines) * (num_lines - i)
        canvas.create_line(
            x1, y1,
            x2, y2,
            width=2, fill=color
        )

def flower():
    half_width = appWidth / 2  # Note that this produces a float (not an int!)
    half_height = appHeight / 2
    draw_curve_at(half_width, 0, 0, half_height, 0, 0, 'red')
    draw_curve_at(half_width, 0, 0, half_height, half_width, half_height, 'red')
    draw_curve_at(0, half_height, half_width, appHeight, 0, appHeight, 'red')
    draw_curve_at(0, half_height, half_width, appHeight, half_width, half_height, 'red')

    draw_curve_at(half_width, 0, appWidth, half_height, half_width, half_height, 'red')
    draw_curve_at(half_width, 0, appWidth, half_height, appWidth, 0, 'red')
    draw_curve_at(half_width, appHeight, appWidth, half_height, half_width, half_height, 'red')
    draw_curve_at(half_width, appHeight, appWidth, half_height, appWidth, appHeight, 'red')


if __name__ == "__main__":
    appWidth = 600
    appHeight = 500

    app = tk.Tk()
    app.title("Curve Stitching")
    app.geometry(f"{appWidth}x{appHeight}")
    canvas = tk.Canvas(app, bg="#000000", width=appWidth, height=appHeight)
    canvas.pack()

    RGB_3_loops()
    #RGB_1_loop()

    app.mainloop()
