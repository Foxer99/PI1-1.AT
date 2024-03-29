import turtle,random

t = turtle.Turtle()
turtle.delay(0)
def obluk(d):
    for i in range(9):
        t.fd(d)
        t.lt(10)
def rgb (r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'
def lupen(d):
    for i in range(2):
        obluk(d)
        t.lt(90)

def kvet(n, d):
    for i in range(n):
        t.fillcolor(rgb(255,random.randint(0 ,100),random.randint(0,100)))
        t.begin_fill()
        lupen(d)
        t.end_fill()
        t.lt(360/n)
kvet(33, 33)

turtle.mainloop()