import tkinter, time

canvas = tkinter.Canvas(width=1280, height=720)
canvas.pack()
def a(event):
    canvas.move(mario, -v_mario, 0)
def d(event):
    canvas.move(mario, v_mario, 0)

image_mario = tkinter.PhotoImage(file="stanie_mario.png")
mario = canvas.create_image(100, 540, image=image_mario)
v_mario = 3

canvas.create_rectangle(0, 650, 1280, 720, fill='green', outline='')
canvas.create_rectangle(50, 670, 105, 700, fill='brown', outline='')
canvas.create_rectangle(135, 660, 175, 690, fill='brown', outline='')
canvas.create_rectangle(200, 690, 270, 680, fill='brown', outline='')
'''
canvas.create_rectangle()
canvas.create_rectangle()
canvas.create_rectangle()
canvas.create_rectangle()
'''
canvas.bind_all('<a>', a)
canvas.bind_all('<d>', d)

tkinter.mainloop()