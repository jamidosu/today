from tkinter import *
import random


def rand_choice():
    r_img = random.choice(img_list)
    Canvas.itemconfig(canvas_img, image=r_img)

window = Tk()
window.title("astrology")


Canvas = Canvas(window, height=950, width=950, bg="ivory")
Canvas.pack()

img_main = PhotoImage(file="asas.png")
canvas_img = Canvas.create_image(475, 475, image=img_main)
Canvas.create_text(475, 30, text="소원을 말해봐", fill="brown",
                   font=("나눔바른펜", 30, "bold"))

img_list = []
for i in range(10):
    img = PhotoImage(file=f"images/img{i}.png")
    img_list.append(img)

button = Button(window, text="Click", bg="white", fg="hot pink",
                font=("나눔바른펜", 20, "bold"),
                command=rand_choice)
button.place(x=885, y=0)


window.mainloop()