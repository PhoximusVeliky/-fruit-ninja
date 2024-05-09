import tkinter
import math
import time
 
root = tkinter.Tk()
 
canv = tkinter.Canvas(root, width=500, height=500, bg="white")
canv.create_line(30, 350, 500, 350, width=2, arrow=tkinter.LAST)  # x
canv.create_line(60, 60, 60, 600, width=2, arrow=tkinter.BOTH)  # y
 
g = 9.8
v0 = 20
p = 3.14
a = 50
b = p * a / 180
u = v0 * math.cos(b)
w = v0 * math.sin(b)
x = 0
y = 0
 
# Траекториясы сызу
for i in range(0, 10000):
    x = 0.03 * i
    y = w * x / u - g * x ** 2 / (2 * u ** 2)
    canv.create_line(60 + 10 * x, 350 - 10 * y, 60 + 10 * x + 1, 350 - 10 * y + 1, fill='red')
# Доптың қозғалсы
x_t = 60 + 1 * x
y_t = 350 - 1 * y
ball1 = canv.create_oval(60, 350, 60 + 10, 350 - 10, fill='red', width=1)
 
for i in range(0, 50):
    canv.move(ball1, 0, 5)
    root.update()
    time.sleep(0.05)
 
canv.pack()
root.mainloop()