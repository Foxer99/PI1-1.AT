import tkinter
import random

canvas = tkinter.Canvas(width=500,height=500)
canvas.pack()

meno = 'Ján'
priezvisko = 'Mrkvička'
vek = 255

print('Volám sa',meno,'',priezvisko, 'a mám', vek, 'rokov.',)
print(f'Volám sa {meno} {priezvisko} a  mám {vek:02} rokov.')
                                       #vypisuje na 2 cifry
print(f'Volám sa {meno} {priezvisko} a  mám {vek:03} rokov.')
                                        #vypisuje na 3 cifry
print(f'Volám sa {meno} {priezvisko} a  mám {vek:02x} rokov.')
                                        # zmení číslo na 16 sustavu
polomer = 20
for i in range(20):
    x = random.randint(2,480)
    y = random.randint(2,480)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    farba = f"#{r:02x}{g:02x}{b:02x}"
    canvas.create_rectangle(x,y,x+30,y+30, fill = farba)
    canvas.create_oval(x-polomer,y-polomer,x+-polomer,y+polomer, fill = farba)




    canvas.mainloop()
