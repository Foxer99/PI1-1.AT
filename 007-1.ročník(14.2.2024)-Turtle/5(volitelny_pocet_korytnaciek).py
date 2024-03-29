import turtle

pocet = 3
#pocet = int(input('Zadaj počet korytnačiek'))
turtles = []       #list (respektíve pole korytnačiek)

for i in range(pocet):
    t = turtle.Turtle()
    t.pu()
    t.setpos(i*100, 0)
    t.pd()
    turtles.append(t)

for i in range(4):
     for t in turtles:
         t.forward(50)
         t.rt(90)

'''
for t in turtles:
    for i in range(4):
        t.forward(50)
        t.rt(90)
'''
turtle.mainloop()