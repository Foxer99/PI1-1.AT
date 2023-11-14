import tkinter

canvas = tkinter.Canvas()
canvas.pack()

x = 10
y = 5
dlzka = float(input("Zadaj číslo veľkosti mena:\n(číslo nesmie byť väčšie ako 14)"))

if dlzka <= 14 :
    # F
    canvas.create_rectangle(x, y, x + dlzka, y + dlzka, )
    canvas.create_rectangle(x + dlzka, y, x + dlzka * 2, y + dlzka, )
    canvas.create_rectangle(x + dlzka * 2, y, x + dlzka * 3, y + dlzka, )
    canvas.create_rectangle(x + dlzka * 3, y, x + dlzka * 4, y + dlzka, )
    canvas.create_rectangle(x + dlzka * 4, y, x + dlzka * 5, y + dlzka, )

    canvas.create_rectangle(x + dlzka, y + dlzka * 3, x + dlzka * 2, y + dlzka * 4, )
    canvas.create_rectangle(x + dlzka * 2, y + dlzka * 3, x + dlzka * 3, y + dlzka * 4, )
    canvas.create_rectangle(x + dlzka * 3, y + dlzka * 3, x + dlzka * 4, y + dlzka * 4, )

    canvas.create_rectangle(x, y + dlzka, x + dlzka, y + dlzka * 2, )
    canvas.create_rectangle(x, y + dlzka * 2, x + dlzka, y + dlzka * 3, )
    canvas.create_rectangle(x, y + dlzka * 3, x + dlzka, y + dlzka * 4, )
    canvas.create_rectangle(x, y + dlzka * 4, x + dlzka, y + dlzka * 5, )
    canvas.create_rectangle(x, y + dlzka * 5, x + dlzka, y + dlzka * 6, )
    canvas.create_rectangle(x, y + dlzka * 6, x + dlzka, y + dlzka * 7, )

    # I
    canvas.create_rectangle(x + dlzka * 6, y, x + dlzka * 7, y + dlzka, )
    canvas.create_rectangle(x + dlzka * 7, y, x + dlzka * 8, y + dlzka, )
    canvas.create_rectangle(x + dlzka * 8, y, x + dlzka * 9, y + dlzka, )

    canvas.create_rectangle(x + dlzka * 7, y + dlzka, x + dlzka * 8, y + dlzka * 2, )
    canvas.create_rectangle(x + dlzka * 7, y + dlzka * 2, x + dlzka * 8, y + dlzka * 3, )
    canvas.create_rectangle(x + dlzka * 7, y + dlzka * 3, x + dlzka * 8, y + dlzka * 4, )
    canvas.create_rectangle(x + dlzka * 7, y + dlzka * 4, x + dlzka * 8, y + dlzka * 5, )
    canvas.create_rectangle(x + dlzka * 7, y + dlzka * 5, x + dlzka * 8, y + dlzka * 6, )

    canvas.create_rectangle(x + dlzka * 6, y + dlzka * 6, x + dlzka * 7, y + dlzka * 7, )
    canvas.create_rectangle(x + dlzka * 7, y + dlzka * 6, x + dlzka * 8, y + dlzka * 7, )
    canvas.create_rectangle(x + dlzka * 8, y + dlzka * 6, x + dlzka * 9, y + dlzka * 7, )

    # L
    canvas.create_rectangle(x + dlzka * 10, y, x + dlzka * 11, y + dlzka, )
    canvas.create_rectangle(x + dlzka * 10, y + dlzka, x + dlzka * 11, y + dlzka * 2, )
    canvas.create_rectangle(x + dlzka * 10, y + dlzka * 2, x + dlzka * 11, y + dlzka * 3, )
    canvas.create_rectangle(x + dlzka * 10, y + dlzka * 3, x + dlzka * 11, y + dlzka * 4, )
    canvas.create_rectangle(x + dlzka * 10, y + dlzka * 4, x + dlzka * 11, y + dlzka * 5, )
    canvas.create_rectangle(x + dlzka * 10, y + dlzka * 5, x + dlzka * 11, y + dlzka * 6, )

    canvas.create_rectangle(x + dlzka * 10, y + dlzka * 6, x + dlzka * 11, y + dlzka * 7, )
    canvas.create_rectangle(x + dlzka * 11, y + dlzka * 6, x + dlzka * 12, y + dlzka * 7, )
    canvas.create_rectangle(x + dlzka * 12, y + dlzka * 6, x + dlzka * 13, y + dlzka * 7, )
    canvas.create_rectangle(x + dlzka * 13, y + dlzka * 6, x + dlzka * 14, y + dlzka * 7, )
    canvas.create_rectangle(x + dlzka * 14, y + dlzka * 6, x + dlzka * 15, y + dlzka * 7, )

    # I
    canvas.create_rectangle(x + dlzka * 16, y, x + dlzka * 17, y + dlzka, )
    canvas.create_rectangle(x + dlzka * 17, y, x + dlzka * 18, y + dlzka, )
    canvas.create_rectangle(x + dlzka * 18, y, x + dlzka * 19, y + dlzka, )

    canvas.create_rectangle(x + dlzka * 17, y + dlzka, x + dlzka * 18, y + dlzka * 2, )
    canvas.create_rectangle(x + dlzka * 17, y + dlzka * 2, x + dlzka * 18, y + dlzka * 3, )
    canvas.create_rectangle(x + dlzka * 17, y + dlzka * 3, x + dlzka * 18, y + dlzka * 4, )
    canvas.create_rectangle(x + dlzka * 17, y + dlzka * 4, x + dlzka * 18, y + dlzka * 5, )
    canvas.create_rectangle(x + dlzka * 17, y + dlzka * 5, x + dlzka * 18, y + dlzka * 6, )

    canvas.create_rectangle(x + dlzka * 16, y + dlzka * 6, x + dlzka * 17, y + dlzka * 7, )
    canvas.create_rectangle(x + dlzka * 17, y + dlzka * 6, x + dlzka * 18, y + dlzka * 7, )
    canvas.create_rectangle(x + dlzka * 18, y + dlzka * 6, x + dlzka * 19, y + dlzka * 7, )

    # P
    canvas.create_rectangle(x + dlzka * 20, y, x + dlzka * 21, y + dlzka, )
    canvas.create_rectangle(x + dlzka * 21, y, x + dlzka * 22, y + dlzka, )
    canvas.create_rectangle(x + dlzka * 22, y, x + dlzka * 23, y + dlzka, )
    canvas.create_rectangle(x + dlzka * 23, y, x + dlzka * 24, y + dlzka, )

    canvas.create_rectangle(x + dlzka * 20, y + dlzka, x + dlzka * 21, y + dlzka * 2, )
    canvas.create_rectangle(x + dlzka * 20, y + dlzka * 2, x + dlzka * 21, y + dlzka * 3, )
    canvas.create_rectangle(x + dlzka * 20, y + dlzka * 3, x + dlzka * 21, y + dlzka * 4, )
    canvas.create_rectangle(x + dlzka * 20, y + dlzka * 4, x + dlzka * 21, y + dlzka * 5, )
    canvas.create_rectangle(x + dlzka * 20, y + dlzka * 5, x + dlzka * 21, y + dlzka * 6, )
    canvas.create_rectangle(x + dlzka * 20, y + dlzka * 6, x + dlzka * 21, y + dlzka * 7, )

    canvas.create_rectangle(x + dlzka * 21, y + dlzka * 3, x + dlzka * 22, y + dlzka * 4, )
    canvas.create_rectangle(x + dlzka * 22, y + dlzka * 3, x + dlzka * 23, y + dlzka * 4, )
    canvas.create_rectangle(x + dlzka * 23, y + dlzka * 3, x + dlzka * 24, y + dlzka * 4, )

    canvas.create_rectangle(x + dlzka * 24, y + dlzka, x + dlzka * 25, y + dlzka * 2)
    canvas.create_rectangle(x + dlzka * 24, y + dlzka * 2, x + dlzka * 25, y + dlzka * 3)

    canvas.mainloop()
else:
    print('Chyba!\n(číslo je moc veľké)')
