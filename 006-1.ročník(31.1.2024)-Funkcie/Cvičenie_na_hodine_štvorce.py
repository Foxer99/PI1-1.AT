import tkinter, random
canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()

def rgb (r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

def stvorce(x, y, pocet_v_rade, velkost, r=255, g=255, b=255):
    for pocet_opakovany_stvorcov in range()
        for i in range(pocet_v_rade):
            canvas.create_rectangle(x, y, x + velkost, y + velkost)
            x += velkost

x = int(input(f'Zadaj súradnice x:\n'))
y = int(input(f'Zadaj súradnice y:\n'))
pocet_v_rade = int(input(f'Zadaj počet štvorcov v rade:\n'))
velkost = int(input(f'Zadaj veľkosť štvorcov:\n'))
stvorce(x, y, pocet_v_rade, velkost, r, g, b)



canvas.mainloop()

