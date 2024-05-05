# import tkinter as tk

# def motion(event):
    # x, y = event.x, event.y
    # print(f"Курсор находится в точке ({x}, {y})")

# root = tk.Tk()
# root.title("Отслеживание движения курсора")
# root.geometry("800x600")

# frame = tk.Frame(root, width=800, height=600)
# frame.bind("<B1-Motion>", motion)  # ЛКМ имеет код B1
# frame.pack()

# root.mainloop()

# import tkinter as tk
# root = tk.Tk()
# root.title("Fruit Ninja Blade")
# root.geometry("800x600")

# canvas = tk.Canvas(root, bg="white", width=800, height=600)
# canvas.pack()

# def draw_blade(event):
    # x, y = event.x, event.y
    # canvas.delete("blade")
    # canvas.create_line(0, 0, x, y, fill="black", width=5, tags="blade")

# canvas.bind("<B1-Motion>", draw_blade)

# root.mainloop()

import tkinter as tk
from collections import deque

def redraw():
    rad = q_blade_r.popleft()
    x,y = q_blade_xy.popleft(),q_blade_xy.popleft()
    rad -=10
    canvas.create_oval(x-rad, y-rad, x+rad, y+rad, fill="red",tags="blade")
    if rad > 0: #проверка на нулевой радиус
        q_blade_xy.append(x)
        q_blade_xy.append(y)
        q_blade_r.append(rad)
    


def draw_circle(event):
    global i
    canvas.delete("blade")
    x, y = event.x, event.y
    q_blade_xy.append(x)
    q_blade_xy.append(y)
    q_blade_r.append(radius)
    canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill="red",tags="blade")
    if i != 1 :
        redraw()
    i = 0
    

    


root = tk.Tk()
root.title("Draw Circle on Right Click")

q_blade_xy = deque()
q_blade_r = deque()

width, height = 800, 600
radius = 50
i=1

canvas = tk.Canvas(root, width=width, height=height, bg="white")
canvas.pack()
canvas.bind("<Button-1>", draw_circle)  

root.mainloop()