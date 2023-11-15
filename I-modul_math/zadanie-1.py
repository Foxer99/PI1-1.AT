import tkinter
import random

canvas = tkinter.Canvas(width=600, height=500)
canvas.pack()

x = 3
xx = x
y = 10
d = 30

pocet_x = 598 // d    # // slúži na celočíselné delenie (7/2 = 3)
pocet_y = 498 // d

for i in range(pocet_y):
    for i in range(pocet_x):
        farba1 = random.choice(('white', 'orange', 'black',))
        farba2 = random.choice(('white', 'orange', 'black',))
        farba3 = random.choice(('white', 'orange', 'black',))
        canvas.create_rectangle(x,y,x+d,y+d, fill= farba1)
        canvas.create_line(x,y,x+d,y+d,fill = farba2)
        canvas.create_line(x+d,y,x,y+d,fill = farba3)
        x = x + d
    y = y + d
    x = xx

canvas.mainloop()

# ctrl + x