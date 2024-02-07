import tkinter
canvas = tkinter.Canvas(width=1280, height=720)
canvas.pack()

premenna = 0
x = 2
y = 2
farba = 'maroon'

velkost_stvorcov = int(input('Zadaj veľkosť štvorcov:\n'))
pocet_v_rade = int(input('Zadaj počet štvorcov v rade:\n'))
pocet_v_stlpci = int(input('Zadaj počet štvorcov s stĺpci:\n'))

for f in range(pocet_v_stlpci):
    for i  in range(pocet_v_rade):
        canvas.create_rectangle(x, y, x + velkost_stvorcov, y + velkost_stvorcov, fill=farba)
        x = x + 3 + velkost_stvorcov
        if premenna == 1:
            farba = 'maroon'
            premenna = 0
        else:
            farba = 'gold'
            premenna = 1
    y = y + 3 + velkost_stvorcov
    x = 2
    
canvas.mainloop()





