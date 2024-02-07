import tkinter,random
canvas = tkinter.Canvas(width=600, height=600)
canvas.pack()

pocet_stvorcov = int(input('Zadaj počet štvorcov:\n'))

for i in range(pocet_stvorcov):
    random_x = random.randint(2, 498)
    random_y = random.randint(2, 498)
    canvas.create_rectangle(random_x, random_y, random_x+100, random_y+40)
    canvas.create_text(random_x+50, random_y+20, text='Python',font='arial 14')

canvas.mainloop()