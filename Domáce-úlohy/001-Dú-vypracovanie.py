import  tkinter
import random

canvas = tkinter.Canvas(width=600, height=500)
canvas.pack()

x = 10
y = 10
pocet_x = 600 // 12
pocet_y = 500 // 5

for i in range(pocet_x):
    canvas.create_rectangle(x+20,y+20,x+30,y+30, fill = 'yellow', outline=  'black')
    canvas.create_polygon(x+19,y+20,x+25,y+15,x+31,y+20,fill = 'red' ,outline ='black')
    canvas.create_rectangle(x+22.5,y+22.5,x+27,y+27,fill = 'light blue')
    x = x + 11

for i in range(pocet_y):
    canvas.create_rectangle(x + 20, y + 20, x + 30, y + 30, fill='yellow', outline='black')
    canvas.create_polygon(x + 19, y + 20, x + 25, y + 15, x + 31, y + 20, fill='red', outline='black')
    canvas.create_rectangle(x + 22.5, y + 22.5, x + 27, y + 27, fill='light blue')
    y = y + 11

canvas.mainloop()