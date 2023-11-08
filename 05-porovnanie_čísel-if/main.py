""" #velký komentár
a = int(input("Zadaj číslo a:\n"))
b = int(input("Zadaj číslo b:\n"))
c = int(input("Zadaj číslo c:\n"))
if a == b == c:
 print("Všetky čísla sa rovnajú")
else:
    if (a>b):
        if (a>c):
            print("Najväčšie číslo je:", a)
        else:
            print("Najväčšie číslo je:", c)
    else:
        if (b>c):
            print("Najväčšie číslo je:", b)
        else:
            print("Najväčšie číslo je:", c)
"""
a = int(input("Zadaj číslo a:\n"))
b = int(input("Zadaj číslo b:\n"))
c = int(input("Zadaj číslo c:\n"))
d = int(input("Zadaj číslo d:\n"))
e = int(input("Zadaj číslo e:\n"))

max = a
if  max < b:
     max = b
if  max < c:
     max = c
if max < d:
     max = d
if max < e:
     max = e
print("Najväčšie číslo je:", max)
