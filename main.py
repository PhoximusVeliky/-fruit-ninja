import tkinter as tk
from collections import deque
from array import *
from tkinter import *
import random


 
def redraw():
    if len(q_blade_xy) == 2:
        x, y = q_blade_xy.popleft(), q_blade_xy.popleft()
        while len(q_blade_xy) != ((20+20/4)*2):
            q_blade_xy.append(x)
            q_blade_xy.append(y)
    rad=0
    if 2<= len(q_blade_xy):
        while rad != 20 :
            x,y = q_blade_xy.popleft(),q_blade_xy.popleft()
            rad +=1
            canvas.create_oval(x-rad, y-rad, x+rad, y+rad, fill="red",tags="blade")
            if len(q_blade_xy)<((20+20/4)*2)-2:
                q_blade_xy.append(x)
                q_blade_xy.append(y)

    if rad == 20:
        while rad != 0:
            x,y=q_blade_xy.popleft(), q_blade_xy.popleft()
            rad-=4
            canvas.create_oval(x-rad,y-rad,x+rad,y+rad, fill="red", tags="blade")
            if len(q_blade_xy) < ((20+20/4)*2)-2:
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
    idle_timer = root.after(200, clear_circles) # 1000 мс бездействия для очистки
    delete_fruits_at_cursor(x, y) #ЗДЕСЬ 

def clear_circles():
    canvas.delete("blade")
    q_blade_xy.clear()

def delete_fruits_at_cursor(x, y): # хз чё это 
    items = canvas.find_overlapping(x-50, y-50, x+50, y+50)
    for item in items:
        tags = canvas.gettags(item)
        if "fruit" in tags:
            canvas.delete(item)


def coordinates_fruits():
    global coordinates16_xy, coordinates64_xy, coordinates128_xy
    x = -800
    while x != 801: 
        if -100*2<=x<=100*2 and x*x % 16 == 0:
            coordinates16_xy.extend([x//2,((x*x)//16)//2])
        if -200*2<=x<=200*2 and x*x % 64 == 0:
            coordinates64_xy.extend([x//2,((x*x)//64)//2])
        if -400*2<= x<=400*2 and x*x % 128 == 0:
            coordinates128_xy.extend([x//2,((x*x)//128)//2])
        # if x<=100*2 and x*x % 2 == 0:
        #     coordinates16_xy.extend([x//2,((x*x)//2)//2])
        x+=1

def rand_dot():
    global dotx, doty
    dotx = random.randint(150, height-500)
    doty = random.randint(100, width-300) 

def create_fruit(fruit_type):
    dotx = random.randint(150, width - 150)  # Generate unique x position
    doty = random.randint(150, height - 150)  # Generate unique y position
    img = photo_list[fruit_type]
    fruit_id = canvas.create_image(dotx, doty, image=img, tags=("fruit", f"fruit{fruit_type}"))
    return fruit_id, dotx, doty  # Return initial positions and ID

def fly_fruits():
    global fruit_positions  # Dictionary to track each fruit's position
    fruit_positions = {}
    for fruit_type in range(0, 4):  # For three different fruits
        fruit_id, dotx, doty = create_fruit(fruit_type)
        fruit_positions[fruit_id] = (dotx, doty)
        move_fruit(0, fruit_id, fruit_type, dotx, doty)

def move_fruit(i, fruit_id, fruit_type, dotx, doty):
    if fruit_id not in fruit_positions:
        return  # Exit the function if the fruit_id is no longer valid

    coordinates = [coordinates16_xy, coordinates64_xy, coordinates128_xy][fruit_type - 1]
    if i < len(coordinates) - 1:
        x = coordinates[i] + dotx
        y = coordinates[i+1] + doty
        fruit_x, fruit_y = fruit_positions[fruit_id]
        dx = x - fruit_x
        dy = y - fruit_y
        canvas.move(fruit_id, dx, dy)
        fruit_positions[fruit_id] = (x, y)  # Update position in the dictionary
        root.after(100, lambda: move_fruit(i + 2, fruit_id, fruit_type, dotx, doty))
    else:
        root.after(100, fly_fruits)

def delete_fruits():
    canvas.delete("fruit")  
    root.after(100, fly_fruits)  

root = tk.Tk()
photo_list = [
    tk.PhotoImage(file = "photo/strawberry.png"),
    tk.PhotoImage(file = "photo/coconut.png"),
    tk.PhotoImage(file = "photo/melon.png"),
    tk.PhotoImage(file = "photo/orange.png"),
    tk.PhotoImage(file = "photo/strawberry_past.png"),
    tk.PhotoImage(file = "photo/coconut_past.png"),
    tk.PhotoImage(file = "photo/melon_past.png"),
    tk.PhotoImage(file = "photo/orange_past.png")
]
root.title("Draw Circle on Right Click")
q_blade_xy = deque()
idle_timer = root.after(1000, clear_circles) 
coordinates16_xy,coordinates64_xy,coordinates128_xy= array('i'),array('i'),array('i')
coordinates_fruits()
dotx=0
doty=0
fruit_id = []
fruit_x, fruit_y, rad = 0, 0, 0
rand_pattern = 1
 
width, height = 1366, 768
root.geometry("1366x768")
canvas = tk.Canvas(root, width=width, height=height, bg="white")
canvas.pack()

canvas.bind("<B1-Motion>", draw_circle)
fly_fruits()
root.mainloop()