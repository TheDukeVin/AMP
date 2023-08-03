import tkinter as tk

def create_window(window_width, window_height):
  '''Creates the main window of the graphics app'''
  window = tk.Tk()
  window.title("Fractal Lab")
  window.geometry(f'{window_width}x{window_height}')
  return window

def create_canvas(window, canvas_width, canvas_height):
  '''Creates a canvas for drawing shapes, and adds it to window'''
  canvas = tk.Canvas(window, bg="#cccccc", width=canvas_width, height=canvas_height)
  canvas.configure(bg="#FFFFFF")
  canvas.pack()
  return canvas

def concentricCircles(center_x, center_y, radius, color):
    canvas.create_oval(center_x-radius, center_y-radius, center_x+radius, center_y+radius, outline=color)#top left, botom right

    if radius > 2:
      concentricCircles(center_x, center_y, radius*0.85, color);

if __name__ == "__main__":
    app_width = 800
    app_height = 800
    canvas_width = app_width-50
    canvas_height = app_height-50
    window = create_window(app_width, app_height)
    canvas = create_canvas(window, canvas_width, canvas_height)

    play  = True
    print("Welcome to the Fractal Generator!")
    while play:
        print("(0) - Concentric Circles")
        print("(1) - Circle Tree")
        print("(2) - Circle Tiles")
        print("(3) - Cantor Set")
        print("(4) - Ruler Tick Marks")
        print("(5) - Sierpinski Carpet")
        print("(6) - Sierpinski Triangle")
        print("(7) - H-Tree")
        print("(8) - Koch Curve")
        print("(9) - Koch Snowflake")
        print("(E)xit")
        choice = input("Enter your fractal of choice:")
        canvas.create_rectangle(0, 0, canvas_width, canvas_height, fill='#FFFFFF')

        match choice:
            case '0':
              concentricCircles(canvas_width/2, canvas_height/2, canvas_width/2, 'black')
            case _:
              play = False

        window.update()
