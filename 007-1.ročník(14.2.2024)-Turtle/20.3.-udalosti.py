#napíše slovo ktoré napíšem
'''import tkinter
import random

Text = input('Napíš text:\n')

def vypis():
    text = Text
    x = random.randrange(50, 330)
    y = random.randrange(20, 240)
    canvas.create_text(x, y, text=text, font='arial 20')

def zmaz():
    canvas.delete('all')

canvas = tkinter.Canvas()
canvas.pack()
tkinter.Button(text='Vypíš text', command=vypis).pack()
tkinter.Button(text='Zmaž plochu', command=zmaz).pack()

vstup = tkinter.Entry(width=10)
vstup.pack()

tkinter.mainloop()'''





#nakreslí čiaru s bodmi
'''import tkinter

xx = yy = None

def klik(event):
    global xx, yy
    x, y = event.x, event.y
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill='red')
    if xx != None:
        canvas.create_line(xx, yy, x, y)
    xx, yy = x, y

canvas = tkinter.Canvas()
canvas.pack()
canvas.bind('<ButtonPress>', klik)

tkinter.mainloop()'''

#kreslí kruhy za myšou
'''import tkinter

canvas = tkinter.Canvas()
canvas.pack()

def tahaj(event):
    x, y = event.x, event.y
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill='red')

canvas.bind('<Motion>', tahaj)

tkinter.mainloop()'''

#Pri posúvaní myši sa kreslia malé modré kruhy, pri kliknutí sa nakreslí jeden väčší červený kruh
'''import tkinter

def klik(event):
    x, y = event.x, event.y
    canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill='red')

def tahaj(event):
    x, y = event.x, event.y
    canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill='blue')

canvas = tkinter.Canvas()
canvas.pack()
canvas.bind('<ButtonPress>', klik)
canvas.bind('<Motion>', tahaj)

tkinter.mainloop()'''
