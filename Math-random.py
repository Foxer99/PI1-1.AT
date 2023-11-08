import random
cislo = random.randrange(0, 10)
farba = random.choice(("red", "green", "orange", ""))
print(cislo)
print(farba)

import math
r = int(input("Zadaj číslo polomeru:\n"))
o = 2 * math.pi * r #math je knižnica .(musí byť) pi je z knižnice
print(o)
print(round(o, 2)) #round slúži na zaokrúhlenie číslo (o je čo má zaokrúhliť  2 je na koľko desatnných čisel )
'''
from math import *
o = 2 * pi * r 
'''

'''
import math as matematika (matematika je meno)
o = 2 * matematika.pi * r
'''

