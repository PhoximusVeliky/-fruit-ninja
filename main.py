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
from array import *
import random

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

def coordinates_fruits():
    global coordinates1_xy,coordinates4_xy,coordinates16_xy
    x=-800
    while x != 801: # иначе не хватает одного
        if -100*2<=x<=100*2 and x*x % 16 == 0:
            coordinates16_xy.extend([x//2,((x*x)//16)//2])
        if -200*2<=x<=200*2 and x*x % 64 == 0:
            coordinates64_xy.extend([x//2,((x*x)//64)//2])
        if -400*2<=x<=400*2 and x*x % 128 == 0:
            coordinates128_xy.extend([x//2,((x*x)//128)//2])
        x+=1

def fly_fruits():
    for i in range(0,202,2):
        x=coordinates16_xy[i]+300
        y=coordinates16_xy[i+1]+100
        rad= 50
        canvas.create_oval(x-rad, y-rad, x+rad, y+rad, fill="chartreuse",tags="fruit")
    for i in range(0,202,2):
        x=coordinates64_xy[i]+500
        y=coordinates64_xy[i+1]+100
        rad= 50
        canvas.create_oval(x-rad, y-rad, x+rad, y+rad, fill="red",tags="fruit")
    for i in range(0,202,2):
        x=coordinates128_xy[i]+600
        y=coordinates128_xy[i+1]+100
        rad= 50
        canvas.create_oval(x-rad, y-rad, x+rad, y+rad, fill="darkred",tags="fruit")

    
def rand_dot():
    w = root.winfo_screenwidth()
    number = random.randint(0, w)
    



root = tk.Tk()
root.title("Draw Circle on Right Click")
q_blade_xy = deque()
idle_timer = root.after(1000, clear_circles) 
coordinates16_xy,coordinates64_xy,coordinates128_xy= array('i'),array('i'),array('i')
coordinates_fruits() 

print(len(coordinates16_xy))
print(len(coordinates64_xy))
print(len(coordinates128_xy))

width, height = 1366, 768
root.geometry("1366x768")
canvas = tk.Canvas(root, width=width, height=height, bg="white")
canvas.pack()

canvas.bind("<B1-Motion>", draw_circle)  
fly_fruits()
root.mainloop()