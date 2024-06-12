import tkinter

canvas = tkinter.Canvas()
canvas.pack

fbody = open('zadanie.txt', 'r')
for riadok in fbody:

    medzera = riadok.find(' ')
    tvar = riadok[:medzera]
    riadok = riadok[medzera+1:]

    medzera = riadok.find(' ')
    x = int(riadok[:medzera])
    riadok = riadok[medzera+1:]

    medzera = riadok.find(' ')
    y = int(riadok[:medzera])
    riadok = riadok[medzera + 1:]

    medzera = riadok.find(' ')
    r = riadok[:medzera]
    riadok = riadok[medzera + 1:]

    medzera = riadok.find(' ')
    g = riadok[:medzera]
    riadok = riadok[medzera + 1:]

    medzera = riadok.find(' ')
    b = riadok[:medzera]
    riadok = riadok[medzera + 1:]

    print(tvar, x, y, r, g, b)
    if tvar == 'r':
        canvas.create_rectangle(x, y, x+100, y+100, )
    else:
        canvas.create_oval(x, y, x + 100, y + 100, )

tkinter.mainloop()