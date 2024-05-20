import tkinter
import time
window = tkinter.Tk()

#settings
window.title("Traffic lights")
window.geometry("800x1000+50+4")
window.configure(background="#545454")
window.resizable(width=False,height=False)

canvas = tkinter.Canvas(window, bg='#038c75', height=1000, width=1000)
canvas.pack()
 
canvas.create_rectangle(0,0,800,1000,fill="white", outline="#633", width=1)

white_shell = canvas.create_oval((345, 55), (445, 155), fill='#D8D8D8',outline="#494949", width=8)
white_num = canvas.create_text(395,105, text="1",fill="#494949", font=("Open Sand Extra Bold", 65))
white = white_shell, white_num
def moving():
    coords = canvas.coords(white_shell)
    if coords[1] <= 410:
        canvas.move(white_shell, 0, 1)
        canvas.move(white_num, 0, 1)
        canvas.after(10, moving)

moving()
window.mainloop()