import tkinter, math

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
def dotyk():
    if canvas.coords(auto) == canvas.coords(stena_1):
        print('STOP', color= 'red')

canvas.bind_all('<Up>', pohyb_hore)
canvas.bind_all('<w>', pohyb_hore)

canvas.bind_all('<Down>', pohyb_dole)
canvas.bind_all('<s>', pohyb_dole)

canvas.bind_all('<Left>', pohyb_vlavo)
canvas.bind_all('<a>', pohyb_vlavo)

canvas.bind_all('<Right>', pohyb_vpravo)
canvas.bind_all('<d>', pohyb_vpravo)


auto = canvas.create_rectangle(170, 350, 190, 370)
stena_1 = canvas.create_line(0,300, 500,300, width=10)
stena_2 = canvas.create_line(495,300, 495,400, width=10)





#spraviť ale s kruhmi (netusim fakt)
def circle_collision(center1, radius1, center2, radius2):
    distance = math.sqrt((center1[0] - center2[0])**2 + (center1[1] - center2[1])**2)
    return distance <= radius1 + radius2

tkinter.mainloop()