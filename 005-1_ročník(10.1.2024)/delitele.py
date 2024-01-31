'''print('Pre ukončenie zadaj číslo 0')

while True:
    cislo = int(input('Zadaj číslo\n:'))
    if cislo == 0:
        print('Číslo je nula!!!')
        break
    elif cislo % 2 == 0:
         print('Číslo je párne')

    else:
        print('Číslo je nepárne')'''

'''
cislo = int(input('Zadaj číslo\n:'))
if cislo % 1 == 0
    print ('Číslo je deliteľné 1')
if cislo % 2 == 0
    print('Číslo je deliteľné 2')
if cislo % 3 == 0
    print('Číslo je deliteľné 3')
if cislo % 4 == 0
    print('Číslo je deliteľné 4')
if cislo % 5 == 0
    print('Číslo je deliteľné 5')
if cislo % 6 == 0
    print('Číslo je deliteľné 6')
if cislo % 7 == 0
    print('Číslo je deliteľné 7')
if cislo % 8 == 0
    print('Číslo je deliteľné 8')
if cislo % 9 == 0
    print('Číslo je deliteľné 9')
if cislo % 10 == 0
    print('Číslo je deliteľné 10')
 '''





'''pocet = 0
while True:
    cislo = int(input('Zadaj číslo:\n'))
    print('Delitele:', end= ' ')
    for delitel in range(1, cislo+1):
        if cislo % delitel == 0:
            pocet = pocet + 1
            print(delitel, end=' ')
    print('\nPočet delitelov je ',pocet)
    if cislo == 0:
        pocet = 0
        break'''

'''
pocet = 0
print('Pre zastavenie programu napíš 0')
while True:
    cislo = int(input('Zadaj číslo:\n'))
    for delitel in range(1, cislo+1):
        if cislo % delitel == 0:
            pocet = pocet + 1
    if pocet == 2:
        print('Číslo je prvočíslo')
    pocet = 0
    if cislo == 0:
        break
'''

'''
print('Pre zastavenie programu napíš 0')
while True:
    n = int(input('Zadaj N')
    print('Prvočísla',end=' ')
    for cislo in range(2, n+1):
        if cislo % delitel == 0
            pocet += 1
    if pocet == 2:
        print(cislo,end=' ')
    print()
    if n == 0:
        break'''



'''print('Pre zastavenie programu napíš 0')
while True:
    n = int(input('Zadaj N')
    print('Prvočísla',end=' ')
    for cislo in range(2, n  + 1):
        if cislo % delitel == 0:
            pocet = n + 1
    if pocet == 2:
        print(cislo,end=' ')
    print()
    if n == 0:
        break
'''