#šírka medzi čiarami = smc
#veľkosť plochy = vp
#miesto čiari = mc
#farba = f

import tkinter
import random

vp = int(input('Zadaj veľkosť plochy.\n:'))
x = 0
y = 0
mc = 0
f = random.choice(['blue', 'lightblue', 'cyan', 'skyblue', 'cornflowerblue', 'deepskyblue', 'royalblue', 'mediumblue',
                    'red', 'sandybrown', 'salmon', 'tomato', 'orange', 'darkorange', 'orangered', 'indianred', 'chocolate',
                    'tan', 'maroon', 'sienna', 'brown', 'saddlebrown', 'pink', 'plum', 'violet', 'orchid', 'magenta',
                    'purple', 'green', 'palegreen', 'yellowgreen', 'mediumseagreen', 'lawngreen', 'limegreen', 'forestgreen',
                    'darkgreen', 'yellow', 'khaki', 'gold', 'gray', 'lightgray', 'black', 'white', 'navy'])

canvas = tkinter.Canvas(width=vp, height=vp)
canvas.pack()

smc = int(input('Zadaj veľkosť medzi čiarami.\n:'))

while mc < vp:
    canvas.create_line(x, y, x+smc, vp, fill=f)
    x = x + smc
    mc = mc + smc

canvas.mainloop()