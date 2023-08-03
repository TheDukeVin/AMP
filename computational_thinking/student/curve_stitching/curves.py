import tkinter as tk

def RGB():
    canvas.create_line(50, 50, 400, 50, width=1, fill='#FF0000') #x1, y1, x2, y2
    canvas.create_line(50, 53, 400, 53, width=1, fill='#FF0000') #x1, y1, x2, y2
    canvas.create_line(50, 56, 400, 56, width=1, fill='#FF0000') #x1, y1, x2, y2

    canvas.create_line(200, 51, 550, 51, width=1, fill='#00FF00') #x1, y1, x2, y2
    canvas.create_line(200, 54, 550, 54, width=1, fill='#00FF00') #x1, y1, x2, y2
    canvas.create_line(200, 57, 550, 57, width=1, fill='#00FF00') #x1, y1, x2, y2

def RGB_3_loops():
    # Your code here (exercises 1-3)
    return 0

def RGB_1_loop():
    # Your code here (exercise 4)
    return 0


if __name__ == "__main__":
    appWidth = 600
    appHeight = 500

    app = tk.Tk()
    app.title("Curve Stitching")
    app.geometry(f"{appWidth}x{appHeight}")
    canvas = tk.Canvas(app, bg="#000000", width=appWidth, height=appHeight)
    canvas.pack()

    # Uncomment these to run your functions
    RGB()
    # RGB_3_loops()
    # RGB_1_loop()

    app.mainloop()
