def sucet (cislo_a, cislo_b):
    return cislo_a + cislo_b
def parne (cislo):
    if cislo % 2 == 0:
        return 'párne'
    else:
        return 'nepárne'

def prvocislo(cislo):
    prvoc1slo = True
    for i in range(2, cislo):
        if cislo % i  == 0:
            prvoc1slo = False
    return prvoc1slo

a = int(input('Zadaj číslo a\n'))
b = int(input('Zadaj číslo b\n'))
sucet = sucet(a,b)

print(f'Súčet čísel {a} a {b} je {sucet}.')
print(f'Číslo {a} je {parne(a)}.')
print(f'Číslo {b} je {parne(b)}.')
if prvocislo(a) == True:
    print(f'Číšlo {a} je prvočíslo')
else:
    print(f'Číslo {a} nie je prvočíslo')
if  prvocislo(b) == True:
    print(f'Číslo {b} je prvočíslo')
else:
    print(f'Číslo {b} nie je prvočíslo')