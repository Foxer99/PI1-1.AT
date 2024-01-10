import tkinter
canvas = tkinter.Canvas(width = 1300,height = 1300, background='black')
canvas = tkinter.Canvas()
canvas.pack()

x = 10
y = 10
d = 20
f = 'blue'
canvas.create_rectangle(x, y, x+d, y+d, fill = f)
canvas.create_rectangle(x+d, y+d, x+(2*d), y+(2*d), fill = f)
canvas.create_rectangle(x+(2*d), y+(2*d), x+(d*3), y+(d*3), fill = f)
canvas.create_rectangle(x+(d*3), y+(d*3), x+(d*4), y+(d*4), fill = f)
canvas.create_rectangle(x+(d*4), y+(d*4), x+(d*5), y+(d*5), fill = f)
canvas.create_rectangle(x+(d*4), y, x+(d*5), y+d, fill = f)
canvas.create_rectangle(x+(d*3), y+d, x+(d*4), y+(2*d), fill = f)
canvas.create_rectangle(x+(d*1), y+(d*3), x+(d*2), y+(d*4), fill = f)
canvas.create_rectangle(x, y+(d*4), x+d, y+(d*5), fill = f)


x = 6 * d
y = 10
d = 20
f = 'blue'
canvas.create_rectangle(x, y, x+d, y+d, fill = f)
canvas.create_rectangle(x+d, y+d, x+(2*d), y+(2*d), fill = f)
canvas.create_rectangle(x+(2*d), y+(2*d), x+(d*3), y+(d*3), fill = f)
canvas.create_rectangle(x+(d*3), y+(d*3), x+(d*4), y+(d*4), fill = f)
canvas.create_rectangle(x+(d*4), y+(d*4), x+(d*5), y+(d*5), fill = f)
canvas.create_rectangle(x+(d*4), y, x+(d*5), y+d, fill = f)
canvas.create_rectangle(x+(d*3), y+d, x+(d*4), y+(2*d), fill = f)
canvas.create_rectangle(x+(d*1), y+(d*3), x+(d*2), y+(d*4), fill = f)
canvas.create_rectangle(x, y+(d*4), x+d, y+(d*5), fill = f)

canvas.mainloop()