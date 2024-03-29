import tkinter

def pohyb_hore(event):
    canvas.move(auto, 0, -10)
def pohyb_dole(event):
    canvas.move(auto, 0, 10)
canvas = tkinter.Canvas(width=720, height=720)
canvas.pack()


canvas.bind_all('<Up>', pohyb_hore)
canvas.bind_all('<Down>', pohyb_dole)

auto = canvas.create_rectangle(170, 350, 190, 370)

tkinter.mainloop()