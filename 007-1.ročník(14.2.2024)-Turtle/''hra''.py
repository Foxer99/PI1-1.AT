import tkinter

canvas = tkinter.Canvas(width=600, height=600)
canvas.pack()

def up(event):
    canvas.move(santa, 0, -v_santa)
def down(event):
    canvas.move(santa, 0, v_santa)
def left(event):
    canvas.move(santa, -v_santa, 0)
def right(event):
    canvas.move(santa, v_santa, 0)
def w(event):
    canvas.move(santa, 0, -v_santa)
def s(event):
    canvas.move(santa, 0, v_santa)
def a(event):
    canvas.move(santa, -v_santa, 0)
def d(event):
    canvas.move(santa, v_santa, 0)

image_santa = tkinter.PhotoImage(file="santa.png")
santa = canvas.create_image(300, 300, image=image_santa)
v_santa = int(input('Speed of Santa:\n'))

canvas.bind_all('<Down>', down)
canvas.bind_all('<Left>', left)
canvas.bind_all('<Up>', up)
canvas.bind_all('<Right>', right)
canvas.bind_all('<s>', down)
canvas.bind_all('<a>', left)
canvas.bind_all('<w>', up)
canvas.bind_all('<d>', right)


tkinter.mainloop()