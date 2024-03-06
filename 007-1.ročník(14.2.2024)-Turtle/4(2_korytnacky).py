import turtle

t1 = turtle.Turtle()
t1.pu()
t1.setpos(-150, 0)
t1.pd()
t1.speed(0)

t2 = turtle.Turtle()
t2.pu()
t2.setpos(150, 0)
t2.pd()
t2.speed(0)

t3 = turtle.Turtle()
t3.pu()
t3.setpos(0,150)
t3.pd()
t3.speed(0)

t4 = turtle.Turtle()
t4.pu()
t4.setpos(0,-150)
t4.pd()
t4.speed(0)

n = int(input('Napíš počet štvorcov:\n'))

for j in range(n):
    for i in range(4):
        t1.fd(50)
        t1.rt(90)
    t1.rt(360/n)

    for i in range(4):
        t2.fd(50)
        t2.rt(90)
    t2.rt(360/n)

    for i in range(4):
        t3.fd(50)
        t3.rt(90)
    t3.rt(360/n)

    for i in range(4):
        t4.fd(50)
        t4.rt(90)
    t4.rt(360/n)


turtle.mainloop()