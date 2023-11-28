import tkinter

canvas = tkinter.Canvas(width=800, height=400,)
canvas.pack()

x = 20
y = 10
d = 30
polovica = d//2
stvrtina = d//4
tristvrtina = stvrtina * 3 + 2

#Strecha
canvas.create_polygon(x+polovica, y, x+d, y+polovica, x, y+polovica  ,fill='red', outline='black')

#Dom
canvas.create_rectangle(x, y+polovica,x+d,y+d, fill='red', outline='black')


canvas.mainloop()

