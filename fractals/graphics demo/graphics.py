import tkinter as tk
#pip3 install tk
#Documentation: https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/canvas.html
import random

def draw_ovals(x):
    canvas.create_text(x+50, 280, text='Ovals', font='Arial 16 bold', fill='black')#center point
    canvas.create_oval(x, 20, x+100, 120, fill='#00FF00', outline='green')#top left, botom right
    canvas.create_oval(x, 130, x+90, 260, outline='#FF0000')

def draw_lines(x):
    canvas.create_text(x+50, 280, text='Lines', font='Arial 16 bold', fill='black')#center point
    canvas.create_line(x, 15, x+90, 5, dash=[2,5])#x1, y1, x2, y2
    canvas.create_line(x, 45, x+90, 35, fill='green')
    canvas.create_line(x, 75, x+90, 85, width=4)
    canvas.create_line(x, 95, x+90, 105, arrow=tk.LAST)
    canvas.create_line(x, 115, x+90, 125, arrow=tk.BOTH)
    canvas.create_line(x, 135, x+90, 155, arrow=tk.FIRST)

def draw_rectangles(x):
    canvas.create_text(x+50, 280, text='Rectangles', font='Arial 16 bold', fill='black')#center point
    canvas.create_rectangle(x, 20, x+90, 110, fill='#00FF00', outline='green')#top left, botom right
    canvas.create_rectangle(x, 120, x+90, 250, outline='#FF0000')

def draw_polygons(x):
    canvas.create_text(x+50, 280, text='Polygons', font='Arial 16 bold', fill='black')#center point
    points = [
        random.randrange(x, x+100), random.randrange(0, 150),
        random.randrange(x, x+100), random.randrange(0, 150),
        random.randrange(x, x+100), random.randrange(0, 150),
        random.randrange(x, x+100), random.randrange(0, 150),
        random.randrange(x, x+100), random.randrange(0, 150)
    ]
    canvas.create_polygon(points,  fill='orange', outline='white')

    points2 = [x+5, 175, x+5, 265, x+95, 265, x+95, 175, x+5, 175]
    canvas.create_line(points2, smooth='true', splinesteps=2)

def draw_images(x):
    global logo #make global b/c Pytho garbage collection
                #https://stackoverflow.com/questions/16424091/why-does-tkinter-image-not-show-up-if-created-in-a-function/63599265#63599265
    logo = tk.PhotoImage(file='hacktrin.png')
    canvas.create_image(x, 150, image=logo, anchor=tk.CENTER)

if __name__ == "__main__":
    appWidth = 650
    appHeight = 350

    app = tk.Tk()
    app.title("Tkinter Python Graphics demo")
    app.geometry(f"{appWidth}x{appHeight}")
    canvas = tk.Canvas(app, bg="#cccccc", width=appWidth-50, height=appHeight-50)
    canvas.pack()


    draw_lines(0)
    draw_rectangles(110)
    draw_ovals(210)
    draw_polygons(310)
    draw_images(510)

    app.mainloop()

