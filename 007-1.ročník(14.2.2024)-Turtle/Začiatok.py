#skratky: forward - fd, left - lt,
import turtle

t = turtle.Turtle()
t.speed(3)

dlzka = 5

'''t.penup()
t.fd(dlzka)
t.lt(90)
t.pendown()
for i in range(3):
    t.fd(dlzka+5)
    t.lt(90)
t.penup()
t.fd(dlzka+10)
t.lt(90)
t.pendown()
for i in range(3):
    t.fd(dlzka+10)
    t.lt(90)
    '''

pocet_stvorcov = int(input('Zadaj počet poschodí pyramídy:\n'))
for j in range(4):
    for i in range(pocet_stvorcov):
        t.penup()
        t.fd(dlzka)
        t.lt(90)
        t.pendown()
        t.fd(dlzka)
        t.lt(90)
        t.fd(dlzka)
        t.lt(90)
        t.penup()
        t.fd(dlzka)
        t.lt(90)
        dlzka = dlzka + 10
    dlzka = 5
    t.lt(180)
turtle.mainloop()



'''
t.fd(100)
t.penup()
t.fd(100)
t.pendown()
t.fd(100)

turtle.mainloop()
'''

'''
def stvorec(dlzka):
    for i in range(4):
        t.fd(dlzka)
        t.lt(90)

t = turtle.Turtle()
t.speed(0)

for f in range(4):
    for i in range(1, 11):
        stvorec(10*i)
    t.lt(90)

turtle.mainloop()
'''

'''
def stvorec():
    for i in range(4):
        t.fd(dlzka_strany)
        t.lt(90)


t = turtle.Turtle()
dlzka_strany = int(input('Zadaj veľkosť strany:\n'))
stvorec()
turtle.mainloop()
'''

'''
print(t.pos())
print(t.heading())
t.forward(100) #pohyb smerom dopredu (smerom ktorým smeruje)
t.left(90)
print(t.pos())
print(t.heading())
t.fd(100)
print(t.pos())
print(t.heading())
turtle.mainloop()
'''

'''
for i in range(4):
    t.fd(100)
    t.lt(90)
turtle.mainloop()
'''

