import tkinter
import random

canvas = tkinter.Canvas(width=600, height=500)
canvas.pack()

x = 3
y = 10
d = 30

pocet_x = 598 // d    # // slúži na celočíselné delenie (7/2 = 3)
pocet_y = 498 // d

for i in range(pocet_x):
    farba = random.choice(('green', 'red', 'blue', 'orange', 'purple',))
    canvas.create_rectangle(x,y,x+d,y+d, fill= farba)
    canvas.create_line(x,y,x+d,y+d)
    canvas.create_line(x+d,y,x,y+d)
    x = x + d

for i in range(pocet_y):
    farba = random.choice(('green', 'red', 'blue', 'orange', 'purple',))
    canvas.create_rectangle(x,y,x+d,y+d, fill= farba)
    canvas.create_line(x,y,x+d,y+d)
    canvas.create_line(x+d,y,x,y+d)
    y = y + d

canvas.mainloop()

# ctrl + x