import tkinter

canvas = tkinter.Canvas()
canvas.pack() #spustime canvas

x = 100 #pomocou tejto premennej ovládame miesto na osi x
y = 50 #pomocou tejto premennej ovládame miesto na osi y
dlzka = 20 #pomocou tejto premennej vieme uraviť velkosť
#I pomocou štvorcov
canvas.create_rectangle(x, y, x+dlzka, y+dlzka,)
canvas.create_rectangle(x+dlzka, y, x+(2*dlzka), y+dlzka,)
canvas.create_rectangle(x+(2*dlzka), y, x+(3*dlzka), y+dlzka,)
canvas.create_oval(x+dlzka, y+dlzka, x+(2*dlzka), y+(2*dlzka), fill = 'red')
canvas.create_oval(x+dlzka, y+(2*dlzka), x+(2*dlzka), y+(3*dlzka), fill = 'blue')
canvas.create_rectangle(x+dlzka, y+(3*dlzka), x+(2*dlzka), y+(4*dlzka),)
canvas.create_rectangle(x, y+(3*dlzka), x+dlzka, y+(4*dlzka), )
canvas.create_rectangle(x+(2*dlzka), y+(3*dlzka), x+(3*dlzka), y+(4*dlzka), )

canvas.mainloop() #udržuje nám okno na obrazovke