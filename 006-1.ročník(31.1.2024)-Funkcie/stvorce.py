import tkinter, random
canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()

def rgb (r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'
def stvorce(x, y, pocet_v_rade, velkost, r=255, g=255, b=255):
    for i in range(pocet_v_rade):
        canvas.create_rectangle(x, y, x + velkost, y + velkost, fill=rgb(r ,g, b), outline=rgb(r, g, b))
        x += velkost
        if r > 100:
            r -= 10
        if g > 100:
            g -= 10
        if b > 100:
            b -= 10

random_r = random.randint(0,255)
random_g = random.randint(0,255)
random_b = random.randint(0,255)

x = int(input(f'Zadaj súradnice x:\n'))
y = int(input(f'Zadaj súradnice y:\n'))
pocet_v_rade = int(input(f'Zadaj počet štvorcov v rade:\n'))
velkost = int(input(f'Zadaj veľkosť štvorcov:\n'))
stvorce(x, y, pocet_v_rade, velkost, random_r, random_g, random_b)



canvas.mainloop()