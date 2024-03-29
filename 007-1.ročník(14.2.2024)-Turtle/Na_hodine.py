import turtle,random

dlzka = random.randint(10,100)
def stvorec(dlzka):
    for i in range(4):
        t.fd(dlzka)
        t.lt(90)

t = turtle.Turtle()
t.speed(0)
for i in range(1000):
    t.penup()
    t.setpos(random.randint(-200, 200), random.randint(-200, 200))
    t.setheading(random.randint(0, 359))
    t.pendown()
    t.fillcolor(random.choice(('blue', 'lightblue', 'cyan', 'skyblue', 'cornflowerblue', 'deepskyblue', 'royalblue',
                               'steelblue', 'mediumblue', 'navy', 'red', 'sandybrown', 'salmon',
                               'tomato', 'orange', 'darkorange', 'orangered', 'indianred', 'chocolate',
                               'tan', 'maroon', 'sienna', 'brown', 'saddlebrown', 'pink', 'plum',
                               'violet', 'orchid', 'magenta', 'purple', 'green', 'palegreen',
                               'yellowgreen', 'mediumseagreen', 'lawngreen', 'limegreen', 'forestgreen',
                               'darkgreen', 'yellow', 'khaki', 'gold', 'gray', 'lightgray',
                               'black', 'white')))
    t.begin_fill()
    stvorec(dlzka)
    t.end_fill()


turtle.mainloop()