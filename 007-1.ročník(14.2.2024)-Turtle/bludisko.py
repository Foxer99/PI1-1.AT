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
canvas.bind_all('<Down>', pohyb_dole)
canvas.bind_all('<Left>', pohyb_vlavo)
canvas.bind_all('<Right>', pohyb_vpravo)

auto = canvas.create_rectangle(170, 350, 190, 370)
stena = canvas.create_line(0,300, 500,300)


tkinter.mainloop()