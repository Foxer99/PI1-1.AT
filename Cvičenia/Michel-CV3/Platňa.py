import tkinter,random
canvas = tkinter.Canvas(width=300, height=300)
canvas.pack()

pocet_kruhov = int(input('Zadaj počet kruhov:\n'))

for i in range(pocet_kruhov):
    random_x = random.randint(2, 298)
    random_y = random.randint(2, 298)
    canvas.create_oval(random_x,random_y,random_x+10, random_y+10)

canvas.mainloop()