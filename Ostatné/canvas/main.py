import tkinter as tk

window = tk.Tk()
window.geometry('800x700')
window.title('Canvas')

canvas = tk.Canvas(window, bg = 'white')
canvas.create_text(100,200, text='Filip Roman Michel')

window.mainloop()
