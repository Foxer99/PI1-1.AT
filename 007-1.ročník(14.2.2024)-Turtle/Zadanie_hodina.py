import turtle, random

t = turtle.Turtle()
t.speed(0)
y = 0

for r in range(8):
    for j in range(8):
        t.fillcolor('blue')
        t.begin_fill()
        for i in range(4):
            t.fd(10)
            t.lt(90)
        t.end_fill()
        t.penup()
        t.fd(10)
        t.pendown()
    t.penup()
    y = y+10
    t.setpos(0, y)
    t.pendown()


turtle.mainloop()