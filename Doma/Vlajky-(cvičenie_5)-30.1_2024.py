import tkinter

canvas = tkinter.Canvas(width=315,height=220)
canvas.pack()
#Nemecko
canvas.create_rectangle(15, 15, 150, 45, fill='black', outline='')
canvas.create_rectangle(15, 45, 150, 75, fill='red', outline='')
canvas.create_rectangle(15, 75, 150, 105, fill='yellow', outline='')
canvas.create_rectangle(15, 15, 150, 105)
#Taliansko
canvas.create_rectangle(165, 15, 210, 105, fill='green', outline='')
canvas.create_rectangle(210, 15, 255, 105, fill='white', outline='')
canvas.create_rectangle(255, 15, 300, 105, fill='red', outline='')
canvas.create_rectangle(165, 15, 300, 105)
#Francúzsko
canvas.create_rectangle(15, 120, 60, 210, fill='blue', outline='')
canvas.create_rectangle(60, 120, 105, 210, fill='white', outline='')
canvas.create_rectangle(105, 120, 150, 210, fill='red',  outline='')
canvas.create_rectangle(15, 120, 150, 210)
#Ukrajina
canvas.create_rectangle(165, 120, 300, 165, fill='blue', outline='')
canvas.create_rectangle(165, 165, 300, 210, fill='yellow', outline='')
canvas.create_rectangle(165, 120, 300, 210)

canvas.mainloop()