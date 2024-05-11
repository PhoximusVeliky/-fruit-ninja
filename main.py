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
    if len(q_blade_xy) == 2 :
       x,y = q_blade_xy.popleft(),q_blade_xy.popleft()
       while  len(q_blade_xy) != ((20+20/4)*2):
            q_blade_xy.append(x)
            q_blade_xy.append(y)
    rad=0
    print(q_blade_xy)
    if 2<= len(q_blade_xy):
        while rad != 20 :
            x,y = q_blade_xy.popleft(),q_blade_xy.popleft()
            rad +=1
            canvas.create_oval(x-rad, y-rad, x+rad, y+rad, fill="red",tags="blade")
            if len(q_blade_xy)<((20+20/4)*2)-2:
                q_blade_xy.append(x)
                q_blade_xy.append(y)
                
    if rad==20:
        while rad != 0 :
            x,y = q_blade_xy.popleft(),q_blade_xy.popleft()
            rad -=4
            canvas.create_oval(x-rad, y-rad, x+rad, y+rad, fill="red",tags="blade")
            if len(q_blade_xy)<((20+20/4)*2)-2:
                q_blade_xy.append(x)
                q_blade_xy.append(y)  

def delete_circle():

    if 2<= len(q_blade_xy):
        while rad != 20 :
            x,y = q_blade_xy.popleft(),q_blade_xy.popleft()
            rad +=1
            canvas.create_oval(x-rad, y-rad, x+rad, y+rad, fill="red",tags="blade")
            if len(q_blade_xy)<((20+20/4)*2)-2:
                q_blade_xy.append(x)
                q_blade_xy.append(y)
                
    if rad==20:
        while rad != 0 :
            x,y = q_blade_xy.popleft(),q_blade_xy.popleft()
            rad -=4
            canvas.create_oval(x-rad, y-rad, x+rad, y+rad, fill="red",tags="blade")
            if len(q_blade_xy)<((20+20/4)*2)-2:
                q_blade_xy.append(x)
                q_blade_xy.append(y)


def draw_circle(event):
    global idle_timer
    canvas.delete("blade")
    x, y = event.x, event.y
    q_blade_xy.append(x)
    q_blade_xy.append(y)
    redraw()
    root.after_cancel(idle_timer)
    idle_timer = root.after(1000, clear_circles)  # 1000 мс бездействия для очистки

def clear_circles():
    canvas.delete("blade")
    q_blade_xy.clear()


root = tk.Tk()
root.title("Draw Circle on Right Click")
q_blade_xy = deque()
idle_timer = root.after(1000, clear_circles) 

width, height = 800, 600
root.geometry("900x700")
canvas = tk.Canvas(root, width=width, height=height, bg="white")
canvas.pack()

canvas.bind("<B1-Motion>", draw_circle)  

root.mainloop()