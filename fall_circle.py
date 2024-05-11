import tkinter as tk
import random

# Функция для движения круга по параболе с случайным смещением
def move_circle(circle, x, y, move_func):
    # Случайные смещения для x и y
    x_offset = random.randint(-2, 2)
    y_offset = random.randint(3, 7)
    canvas.move(circle, x + x_offset, y + y_offset)
    # Получаем координаты круга
    coords = canvas.coords(circle)
    # Проверяем, не вышел ли круг за нижнюю границу холста
    if coords[3] < 600:  # 600 - это высота холста
        window.after(10, move_func, circle, x + x_offset, y + y_offset, move_func)

# Функция для запуска движения круга
def start_movement(move_func):
    for i in range(3):  # Создаем три круга для примера
        # Случайные начальные координаты для кругов
        start_x = random.randint(50, 750)
        start_y = random.randint(50, 550)
        circle = canvas.create_oval(start_x, start_y, start_x + 100, start_y + 100, fill="blue")
        move_func(circle, 0, 0, move_func)

# Создание окна
window = tk.Tk()
window.title("Круги летящие по параболам")

# Создание холста
canvas = tk.Canvas(window, width=800, height=600)
canvas.pack()

# Создание кнопки для запуска движения
start_button = tk.Button(window, text="Начать движение", command=lambda: start_movement(move_circle))
start_button.pack()

window.mainloop()