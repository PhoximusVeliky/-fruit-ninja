import tkinter as tk

def motion(event):
    x, y = event.x, event.y
    print(f"Курсор находится в точке ({x}, {y})")

root = tk.Tk()
root.title("Отслеживание движения курсора")
root.geometry("800x600")

frame = tk.Frame(root, width=800, height=600)
frame.bind("<B1-Motion>", motion)  # ЛКМ имеет код B1
frame.pack()

root.mainloop()