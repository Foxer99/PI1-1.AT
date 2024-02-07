import tkinter, time, random

canvas_width = 300
canvas_height = 600
santa_x = canvas_width // 2
santa_y = 66
santa_posun = 1

canvas = tkinter.Canvas(width=canvas_width, height=canvas_height)
canvas.pack()

image_santa = tkinter.PhotoImage(file="santa.png")
santa = canvas.create_image(santa_x, santa_y, image=image_santa)

while True:
        canvas.update()
        time.sleep(0.0001)
        canvas.move(santa, 0, santa_posun)
        santa_y = santa_y + santa_posun
        if santa_y == canvas_height - 64:
            canvas.delete(santa)
            santa_y = 66
            santa = canvas.create_image(santa_x, santa_y, image=image_santa)

'''
        canvas.delete(santa)
        santa_y = 66
        santa = canvas.create_image(santa_x, santa_y, image=image_santa)
'''


'''
for i  in range(3):
    for i in range(450):
        canvas.update()
        time.sleep(0.001)
        canvas.move(santa, 0, 1)

    time.sleep(0.01)

    for i in range(450):
        canvas.update()
        time.sleep(0.001)
        canvas.move(santa, 0, -1)

canvas.mainloop()
'''

'''
while True:
    canvas.update()
    time.sleep(0.0001)
    canvas.move(santa, 0, santa_posun)
    santa_y = santa_y + santa_posun
    if santa_y == canvas_height - 64:
        canvas.update()
        time.sleep(0.0001)
        canvas.move(santa, 0, -santa_posun)
        santa_y = santa_y - santa_posun
        
        
možes dokoncit tak aby sa odrázal od dola
'''