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
import tkinter as tk

def draw_circle(event):
    x, y = event.x, event.y
    canvas.create_oval(x-radius, y-radius, x+radius, y+radius, fill="red")

root = tk.Tk()
root.title("Draw Circle on Right Click")

width, height = 800, 600
radius = 50

canvas = tk.Canvas(root, width=width, height=height, bg="white")
canvas.pack()

canvas.bind("<Button-1>", draw_circle)  # Привязываем событие правой кнопки мыши к функции рисования круга

root.mainloop()