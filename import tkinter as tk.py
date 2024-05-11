import tkinter as tk
from collections import deque
import time

def redraw():
    # Удаление старых кругов
    canvas.delete("blade")
    # Рисование новых кругов
    for i in range(len(q_blade_xyt)):
        x, y, _ = q_blade_xyt[i]
        rad = i  # Радиус зависит от позиции в очереди
        canvas.create_oval(x-rad, y-rad, x+rad, y+rad, fill="red", tags="blade")

def draw_circle(event):
    global idle_timer
    x, y = event.x, event.y
    # Добавление нового круга с временем создания
    q_blade_xyt.append((x, y, time.time()))
    redraw()
    # Перезапуск таймера при движении мыши
    root.after_cancel(idle_timer)
    idle_timer = root.after(1000, clear_circles)  # 1000 мс бездействия для очистки

def clear_circles():
    current_time = time.time()
    # Удаление кругов, которые были созданы более 1 секунды назад
    while q_blade_xyt and current_time - q_blade_xyt[0][2] > 1:
        q_blade_xyt.popleft()
    redraw()

root = tk.Tk()
root.title("Draw Circle on Right Click")
q_blade_xyt = deque()  # Очередь для хранения кругов и времени их создания
idle_timer = root.after(1000, clear_circles)  # Инициализация таймера

width, height = 800, 600
root.geometry(f"{width}x{height}")
canvas = tk.Canvas(root, width=width, height=height, bg="white")
canvas.pack()

canvas.bind("<B1-Motion>", draw_circle)

root.mainloop()
