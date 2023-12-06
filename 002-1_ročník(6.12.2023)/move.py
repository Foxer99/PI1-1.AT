import tkinter, time, random

canvas = tkinter.Canvas()
canvas.pack()

stvorec1 = canvas.create_rectangle(10, 10, 110, 110, fill='red')
for i in range(1000):
    for i in range(130):
        canvas.update()
        time.sleep(0.001)
        canvas.move(stvorec1, 2, 1)    #stvorec1 je objekt, ktorý sa bude posúvať, 100 je o koľko sa posúva na x osi, 0 je o koľko na y osi
        farba1 = random.choice(('blue', 'lightblue', 'cyan', 'skyblue', 'cornflowerblue', 'deepskyblue', 'royalblue',
                               'steelblue', 'mediumblue', 'navy', 'red', 'sandybrown', 'salmon',
                               'tomato', 'orange', 'darkorange', 'orangered', 'indianred', 'chocolate',
                               'tan', 'maroon', 'sienna', 'brown', 'saddlebrown', 'pink', 'plum',
                               'violet', 'orchid', 'magenta', 'purple', 'green', 'palegreen',
                               'yellowgreen', 'mediumseagreen', 'lawngreen', 'limegreen', 'forestgreen',
                               'darkgreen', 'yellow', 'khaki', 'gold', 'gray', 'lightgray',
                               'black', 'white'))
        canvas.itemconfig(stvorec1, fill=farba1)
    time.sleep(0.01)
    for i in range(130):
        canvas.update()
        time.sleep(0.001)
        canvas.move(stvorec1, -2, -1)
        farba1 = random.choice(('blue', 'lightblue', 'cyan', 'skyblue', 'cornflowerblue', 'deepskyblue', 'royalblue',
                               'steelblue', 'mediumblue', 'navy', 'red', 'sandybrown', 'salmon',
                               'tomato', 'orange', 'darkorange', 'orangered', 'indianred', 'chocolate',
                               'tan', 'maroon', 'sienna', 'brown', 'saddlebrown', 'pink', 'plum',
                               'violet', 'orchid', 'magenta', 'purple', 'green', 'palegreen',
                               'yellowgreen', 'mediumseagreen', 'lawngreen', 'limegreen', 'forestgreen',
                               'darkgreen', 'yellow', 'khaki', 'gold', 'gray', 'lightgray',
                               'black', 'white'))
        canvas.itemconfig(stvorec1, fill=farba1)

canvas.mainloop()
