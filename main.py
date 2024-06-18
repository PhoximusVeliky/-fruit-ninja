import tkinter as tk
from collections import deque
from array import *
from tkinter import *
import random
import time


 
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
    idle_timer = root.after(200, clear_circles)
    delete_fruits_at_cursor(x, y)

def clear_circles():
    canvas.delete("blade")
    q_blade_xy.clear()

def delete_fruits_at_cursor(x, y):
    global fruit_count_label, score
    items = canvas.find_overlapping(x-50, y-50, x+50, y+50)
    sliced_fruits = 0
    fruit_scores = {0: 50, 1: 10, 2: 20, 3: 10}  # Define scores for each fruit type

    for item in items:
        tags = canvas.gettags(item)
        if "fruit" in tags:
            fruit_type = int(tags[1].replace("fruit", ""))
            canvas.delete(item)
            score += fruit_scores[fruit_type]
            fruit_count_label.config(text=f"Счёт: {score}")
        elif "bomba" in tags:  # Check if the item is a bomb
            canvas.delete(item)
            fruit_count_label.config(text=f"Счёт: {score}")
            remove_heart()
            remove_heart()
            remove_heart()

    fruit_count_label.config(text=f"Счёт: {score + sliced_fruits}")

def coordinates_fruits():
    global coordinates16_xy, coordinates64_xy, coordinates128_xy,fallr,falll
    x = -800
    while x != 801: 
        if  -100*2<=x<=100*2 and x*x % 16 == 0:
            coordinates16_xy.extend([x//2,((x*x)//16)//2])
        if  -200*2<=x<=200*2 and x*x % 64 == 0:
            coordinates64_xy.extend([x//2,((x*x)//64)//2])
        if  -400*2<= x<=400*2 and x*x % 128 == 0:
            coordinates128_xy.extend([x//2,((x*x)//128)//2])
        if   0<=x<=100*2 and x*x % 16 == 0:
            fallr.extend([x//2,((x*x)//16)//2])
        if  -100*2<=x<=0 and x*x % 16 == 0:
            falll.extend([x//2,((x*x)//16)//2])
        x+=1

def rand_dot():
    global dotx, doty
    dotx = random.randint(150, height-500)
    doty = random.randint(100, width-300) 

def create_fruit(fruit_type):
    dotx = random.randint(150, width - 150)  # Generate unique x position
    doty = random.randint(50, height // 2 - 150)  # Generate unique y position
    if random.random() < 0.8:  # 10% chance of creating a bomb
        img = photo_list[4]  # Assuming the bomb image is at index 4 in photo_list
        fruit_id = canvas.create_image(dotx, doty, image=img, tags=("bomba"))
    else:
        img = photo_list[fruit_type]
        fruit_id = canvas.create_image(dotx, doty, image=img, tags=("fruit", f"fruit{fruit_type}"))
    return fruit_id, dotx, doty  # Return initial positions and ID

def fly_fruits():
    global fruit_positions, timestop,stop_fly_fruits
    fruit_positions = {}
    for fruit_type in range(0, 4):
        if stop_fly_fruits:
            break
        fruit_id, dotx, doty = create_fruit(fruit_type)
        fruit_positions[fruit_id] = (dotx, doty)
        move_fruit(0, fruit_id, fruit_type, dotx, doty)

def move_fruit(i, fruit_id, fruit_type, dotx, doty):
    global timestop
    if fruit_id not in fruit_positions:
        return  

    coordinates = [coordinates16_xy, coordinates64_xy, coordinates128_xy][fruit_type - 1]
    if i < len(coordinates) - 1:
        x = coordinates[i] + dotx
        y = coordinates[i+1] + doty
        fruit_x, fruit_y = fruit_positions[fruit_id]
        dx = (x - fruit_x) * timestop 
        dy = (y - fruit_y) * timestop
        canvas.move(fruit_id, dx, dy)
        fruit_positions[fruit_id] = (x, y) 
        root.after(100, lambda: move_fruit(i + 2, fruit_id, fruit_type, dotx, doty))
    else:
        if fruit_id in canvas.find_all():
            if "bomba" not in canvas.gettags(fruit_id):
                remove_heart()
            canvas.delete(fruit_id)
        del fruit_positions[fruit_id]
        root.after(100, fly_fruits) 

def toggle_timestop(event):
    global timestop, last_shift_press_time
    current_time = time.time()
    if current_time - last_shift_press_time >= 5:
        last_shift_press_time = current_time
        if timestop == 1.7:
            timestop = 0.1
            root.after(3000, lambda: change_timestop(1.7))
        else:
            timestop = 1.7
        
def change_timestop(new_value):
    global timestop
    timestop = new_value

def delete_fruits():
    canvas.delete("fruit")  
    root.after(100, fly_fruits)

def create_hearts():
    global heart_ids
    heart_ids = []  # Initialize a list to store heart IDs
    for i in range(3):
        heart_img = photo_list[9]  # Assuming the heart image is at index 9 in photo_list
        heart_id = canvas.create_image(50 + i * 100, 100, image=heart_img, tags=("heart", f"heart{i}"))
        heart_ids.append(heart_id)

def start_game():
    global fruit_count_label, heart_ids, stop_fly_fruits, score, start_time
    stop_fly_fruits = False
    score = 0
    start_time = time.time()
    for widget in root.winfo_children():
        if widget != canvas:
            widget.destroy()
            canvas.delete(id)
    fruit_count_label = tk.Label(root, text="Счёт: 0", font=("Arial", 12, "bold"), fg="black")
    fruit_count_label.place(x=10, y=10) 
    create_hearts()
    fly_fruits()  

def game_over_window():
    global id, stop_fly_fruits
    stop_fly_fruits = True
    game_duration = round(time.time() - start_time)
    rect_width = 250
    rect_height = 250
    x1 = (width - rect_width) // 2
    y1 = (height - rect_height) // 2
    x2 = x1 + rect_width
    y2 = y1 + rect_height
    id=canvas.create_rectangle(x1, y1, x2, y2, fill="white")
    # Assuming `canvas` is the tkinter Canvas object
    score_label = tk.Label(root, text=f"Счёт: {score}", font=("Arial", 12, "bold"), fg="black")
    score_window = canvas.create_window(x1 + 125, y1 + 35, anchor='center', window=score_label, width=230, height=50)
    score_label.config(text=f"Счёт: {score}")
    time_label = tk.Label(root, text=f"Время: {game_duration} секунд", font=("Arial", 12, "bold"), fg="black")
    time_window = canvas.create_window(x1 + 125, y1 + 70, anchor='center', window=time_label, width=230, height=50)
    button = tk.Button(root, text="выйти в меню", command=menu)
    button_window = canvas.create_window(x2-20, y2-10, anchor='se', window=button, width=100, height=50)
    button = tk.Button(root, text="новая игра", command=start_game)
    button_window = canvas.create_window(x1+120, y2-10, anchor='se', window=button, width=100, height=50)

def remove_heart():
    if heart_ids:
        rightmost_heart_id = heart_ids.pop()
        canvas.delete(rightmost_heart_id)
    if len(heart_ids) == 0:
        canvas.delete("all")
        fruit_count_label.destroy() 
        game_over_window()
        root.after_cancel(idle_timer)

def menu ():
    global id
    for widget in root.winfo_children():
        if widget != canvas:
            widget.destroy()
            canvas.delete(id)
    button1 = tk.Button(root, text="начать игру", command=start_game, width=20, height=2)
    button1.place(relx=0.5, rely=0.4, anchor='center')
    button2 = tk.Button(root, text="выход", command=root.destroy, width=20, height=2)
    button2.place(relx=0.5, rely=0.5, anchor='center')
                  
root = tk.Tk()
photo_list = [
    tk.PhotoImage(file = "photo/strawberry.png"),
    tk.PhotoImage(file = "photo/coconut.png"),
    tk.PhotoImage(file = "photo/melon.png"),
    tk.PhotoImage(file = "photo/orange.png"),
    tk.PhotoImage(file = "photo/bomba.png"),
    tk.PhotoImage(file = "photo/strawberry_past.png"),
    tk.PhotoImage(file = "photo/coconut_past.png"),
    tk.PhotoImage(file = "photo/melon_past.png"),
    tk.PhotoImage(file = "photo/orange_past.png"),
    tk.PhotoImage(file = "photo/HP.png"),
    tk.PhotoImage(file = "photo/48377.png"),
]

root.title("Draw Circle on Right Click")
q_blade_xy = deque()
idle_timer = root.after(1000, clear_circles) 
coordinates16_xy,coordinates64_xy,coordinates128_xy= array('i'),array('i'),array('i')
fallr,falll= array('i'),array('i')
coordinates_fruits()
dotx=0
doty=0
fruit_id = []
fruit_x, fruit_y, rad = 0, 0, 0
rand_pattern = 1
timestop = 1.7
stop_fly_fruits = False
score = 0
start_time = None
last_shift_press_time = time.time()

width, height = 1366, 768
root.geometry("1366x768")
canvas = tk.Canvas(root, width=width, height=height, bg="white")
original_image = photo_list[10] #замена
resized_image = original_image.subsample(3, 4)  
canvas.create_image(0, 0, anchor='nw', image=resized_image)
menu ()
canvas.pack()
root.bind("<Shift_L>", toggle_timestop)
canvas.bind("<B1-Motion>", draw_circle)
root.mainloop()