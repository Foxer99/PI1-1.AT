
#premenná i je počítadlo pre cyklus
#range nám vráti postupnosť od 0 do N - 1 (N je zadané číslo)
#range môže mať viac parametrov (prvý je odkiaĽ má začat, druhý parameter je kedy má skončiť,
#tretí parameter je po koľkých násobkoch ide)
#napríklad : range(2, 11, 2) tak vypíše : 2,4,6,8,10
'''
for i in range(20, 31, 2):
    #rovnaké ako 0 , 1 , 2 , 3 , 4
    print(i, "Ahoj")
    print("-------------")
'''
"""
#program na súčet prvých čísiel
n = int(input("Zadaj číslo:\n"))
sucet = 0
for i in range(1, n+1):
    print(i)
    sucet = sucet + i
print("Súčet čísel od 1 do", n, "je:", sucet)
"""

""""
#program na výpočet faktoriálu
n = int(input("Zadaj číslo:\n"))
faktorial = 1
for i in range(1, n+1):
    print(i)
    faktorial = faktorial * i
print("Faktoriál čísla", n, "je:", faktorial)
"""

#program na výpočet ciferného súčtu
