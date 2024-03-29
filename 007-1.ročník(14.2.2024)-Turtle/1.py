import turtle

def stvorec(dlzka):
    for i in range(4):
        t.forward(dlzka)
        t.right(90)

def n_uholnik(n, dlzka):
    for i in range(n):
        t.fd(dlzka)
        t.lt(360/n)

t = turtle.Turtle()
#t.speed(0)
turtle.delay(0)

stvorec(33)
n_uholnik(13, 33)
for i in range(3, 17):
    n_uholnik(n, 50)


turtle.mainloop()