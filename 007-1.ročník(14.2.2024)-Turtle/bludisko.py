import tkinter

canvas = tkinter.Canvas(width=720, height=720)
canvas.pack()

def pohyb_hore(event):
    canvas.move(auto, 0, -10)
def pohyb_dole(event):
    canvas.move(auto, 0, 10)
def pohyb_vlavo(event):
    canvas.move(auto, -10, 0)
def pohyb_vpravo(event):
    canvas.move(auto, 10, 0)

canvas.bind_all('<Up>', pohyb_hore)
canvas.bind_all('<w>', pohyb_hore)

canvas.bind_all('<Down>', pohyb_dole)
canvas.bind_all('<s>', pohyb_dole)

canvas.bind_all('<Left>', pohyb_vlavo)
canvas.bind_all('<a>', pohyb_vlavo)

canvas.bind_all('<Right>', pohyb_vpravo)
canvas.bind_all('<d>', pohyb_vpravo)


auto = canvas.create_rectangle(170, 350, 190, 370, outline='red', fill='red')
stena_1 = canvas.create_line(0,300, 500,300, width=10)
stena_2 = canvas.create_line(495,300, 495,400, width=10)

tkinter.mainloop()