import tkinter
import random

canvas = tkinter.Canvas(width=600, height=500)
canvas.pack()

x = 5
y = 15
dlzka = 10
color_1 =  random.choice(['yellow', 'purple', 'green', 'pink', 'blue'])
color_2 =  random.choice(['yellow', 'purple', 'green', 'pink', 'blue'])
color_3 =  random.choice(['yellow', 'purple', 'green', 'pink', 'blue'])
color_4 =  random.choice(['yellow', 'purple', 'green', 'pink', 'blue'])
color_5 =  random.choice(['yellow', 'purple', 'green', 'pink', 'blue'])


    #F
    canvas.create_rectangle(x, y, x + dlzka, y + dlzka,fill = 'color_1')
    canvas.create_rectangle(x + dlzka, y, x + dlzka * 2, y + dlzka,fill = 'color_1'
    canvas.create_rectangle(x + dlzka * 2, y, x + dlzka * 3, y + dlzka,fill = 'color_1')
    canvas.create_rectangle(x + dlzka * 3, y, x + dlzka * 4, y + dlzka,fill = 'color_1'
    canvas.create_rectangle(x + dlzka * 4, y, x + dlzka * 5, y + dlzka,fill = 'color_1'

    canvas.create_rectangle(x + dlzka, y + dlzka * 3, x + dlzka * 2, y + dlzka * 4,fill = 'color_1')
    canvas.create_rectangle(x + dlzka * 2, y + dlzka * 3, x + dlzka * 3, y + dlzka * 4,fill = 'color_1')
    canvas.create_rectangle(x + dlzka * 3, y + dlzka * 3, x + dlzka * 4, y + dlzka * 4,fill = 'color_1')

    canvas.create_rectangle(x, y + dlzka, x + dlzka, y + dlzka * 2,fill = 'color_1'  )
    canvas.create_rectangle(x, y + dlzka * 2, x + dlzka, y + dlzka * 3,fill = 'color_1'  )
    canvas.create_rectangle(x, y + dlzka * 3, x + dlzka, y + dlzka * 4,fill = 'color_1'  )
    canvas.create_rectangle(x, y + dlzka * 4, x + dlzka, y + dlzka * 5,fill = 'color_1'  )
    canvas.create_rectangle(x, y + dlzka * 5, x + dlzka, y + dlzka * 6,fill = 'color_1'  )
    canvas.create_rectangle(x, y + dlzka * 6, x + dlzka, y + dlzka * 7,fill = 'color_1'  )

    # I
    canvas.create_rectangle(x + dlzka * 6, y, x + dlzka * 7, y + dlzka,fill = 'color_2' )
    canvas.create_rectangle(x + dlzka * 7, y, x + dlzka * 8, y + dlzka,fill = 'color_2' )
    canvas.create_rectangle(x + dlzka * 8, y, x + dlzka * 9, y + dlzka,fill = 'color_2' )

    canvas.create_rectangle(x + dlzka * 7, y + dlzka, x + dlzka * 8, y + dlzka * 2,fill = 'color_2' )
    canvas.create_rectangle(x + dlzka * 7, y + dlzka * 2, x + dlzka * 8, y + dlzka * 3,fill = 'color_2' )
    canvas.create_rectangle(x + dlzka * 7, y + dlzka * 3, x + dlzka * 8, y + dlzka * 4,fill = 'color_2' )
    canvas.create_rectangle(x + dlzka * 7, y + dlzka * 4, x + dlzka * 8, y + dlzka * 5,fill = 'color_2' )
    canvas.create_rectangle(x + dlzka * 7, y + dlzka * 5, x + dlzka * 8, y + dlzka * 6,fill = 'color_2' )

    canvas.create_rectangle(x + dlzka * 6, y + dlzka * 6, x + dlzka * 7, y + dlzka * 7,fill = 'color_2' )
    canvas.create_rectangle(x + dlzka * 7, y + dlzka * 6, x + dlzka * 8, y + dlzka * 7,fill = 'color_2' )
    canvas.create_rectangle(x + dlzka * 8, y + dlzka * 6, x + dlzka * 9, y + dlzka * 7,fill = 'color_2' )

    #L
    canvas.create_rectangle(x + dlzka * 10, y, x + dlzka * 11, y + dlzka,fill = 'color_3' )
    canvas.create_rectangle(x + dlzka * 10, y + dlzka, x + dlzka * 11, y + dlzka * 2,fill = 'color_3' )
    canvas.create_rectangle(x + dlzka * 10, y + dlzka * 2, x + dlzka * 11, y + dlzka * 3,fill = 'color_3' )
    canvas.create_rectangle(x + dlzka * 10, y + dlzka * 3, x + dlzka * 11, y + dlzka * 4,fill = 'color_3' )
    canvas.create_rectangle(x + dlzka * 10, y + dlzka * 4, x + dlzka * 11, y + dlzka * 5,fill = 'color_3' )
    canvas.create_rectangle(x + dlzka * 10, y + dlzka * 5, x + dlzka * 11, y + dlzka * 6,fill = 'color_3' )

    canvas.create_rectangle(x + dlzka * 10, y + dlzka * 6, x + dlzka * 11, y + dlzka * 7,fill = 'color_3' )
    canvas.create_rectangle(x + dlzka * 11, y + dlzka * 6, x + dlzka * 12, y + dlzka * 7,fill = 'color_3' )
    canvas.create_rectangle(x + dlzka * 12, y + dlzka * 6, x + dlzka * 13, y + dlzka * 7,fill = 'color_3' )
    canvas.create_rectangle(x + dlzka * 13, y + dlzka * 6, x + dlzka * 14, y + dlzka * 7,fill = 'color_3' )
    canvas.create_rectangle(x + dlzka * 14, y + dlzka * 6, x + dlzka * 15, y + dlzka * 7,fill = 'color_3' )

    #I
    canvas.create_rectangle(x + dlzka * 16, y, x + dlzka * 17, y + dlzka,fill = 'color_4' )
    canvas.create_rectangle(x + dlzka * 17, y, x + dlzka * 18, y + dlzka,fill = 'color_4' )
    canvas.create_rectangle(x + dlzka * 18, y, x + dlzka * 19, y + dlzka,fill = 'color_4' )

    canvas.create_rectangle(x + dlzka * 17, y + dlzka, x + dlzka * 18, y + dlzka * 2,fill = 'color_4' )
    canvas.create_rectangle(x + dlzka * 17, y + dlzka * 2, x + dlzka * 18, y + dlzka * 3,fill = 'color_4' )
    canvas.create_rectangle(x + dlzka * 17, y + dlzka * 3, x + dlzka * 18, y + dlzka * 4,fill = 'color_4' )
    canvas.create_rectangle(x + dlzka * 17, y + dlzka * 4, x + dlzka * 18, y + dlzka * 5,fill = 'color_4' )
    canvas.create_rectangle(x + dlzka * 17, y + dlzka * 5, x + dlzka * 18, y + dlzka * 6,fill = 'color_4' )
    canvas.create_rectangle(x + dlzka * 16, y + dlzka * 6, x + dlzka * 17, y + dlzka * 7,fill = 'color_4' )
    canvas.create_rectangle(x + dlzka * 17, y + dlzka * 6, x + dlzka * 18, y + dlzka * 7,fill = 'color_4' )
    canvas.create_rectangle(x + dlzka * 18, y + dlzka * 6, x + dlzka * 19, y + dlzka * 7,fill = 'color_4' )

    #P
    canvas.create_rectangle(x + dlzka * 20, y, x + dlzka * 21, y + dlzka,fill 'clolor_5' )
    canvas.create_rectangle(x + dlzka * 21, y, x + dlzka * 22, y + dlzka,fill 'clolor_5' )
    canvas.create_rectangle(x + dlzka * 22, y, x + dlzka * 23, y + dlzka,fill 'clolor_5' )
    canvas.create_rectangle(x + dlzka * 23, y, x + dlzka * 24, y + dlzka,fill 'clolor_5' )

    canvas.create_rectangle(x + dlzka * 20, y + dlzka, x + dlzka * 21, y + dlzka * 2,fill 'clolor_5' )
    canvas.create_rectangle(x + dlzka * 20, y + dlzka * 2, x + dlzka * 21, y + dlzka * 3,fill 'clolor_5' )
    canvas.create_rectangle(x + dlzka * 20, y + dlzka * 3, x + dlzka * 21, y + dlzka * 4,fill 'clolor_5' )
    canvas.create_rectangle(x + dlzka * 20, y + dlzka * 4, x + dlzka * 21, y + dlzka * 5,fill 'clolor_5' )
    canvas.create_rectangle(x + dlzka * 20, y + dlzka * 5, x + dlzka * 21, y + dlzka * 6,fill 'clolor_5' )
    canvas.create_rectangle(x + dlzka * 20, y + dlzka * 6, x + dlzka * 21, y + dlzka * 7,fill 'clolor_5' )

    canvas.create_rectangle(x + dlzka * 21, y + dlzka * 3, x + dlzka * 22, y + dlzka * 4,fill 'clolor_5' )
    canvas.create_rectangle(x + dlzka * 22, y + dlzka * 3, x + dlzka * 23, y + dlzka * 4,fill 'clolor_5' )
    canvas.create_rectangle(x + dlzka * 23, y + dlzka * 3, x + dlzka * 24, y + dlzka * 4,fill 'clolor_5' )

    canvas.create_rectangle(x + dlzka * 24, y + dlzka, x + dlzka * 25, y + dlzka * 2,fill 'clolor_5')
    canvas.create_rectangle(x + dlzka * 24, y + dlzka * 2, x + dlzka * 25, y + dlzka * 3,fill 'clolor_5')

    x = x+ 300

canvas.mainloop()