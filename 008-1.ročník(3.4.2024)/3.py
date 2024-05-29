#sifrovanie cezarovou sifrov
retazec = input('Zadaj retazec:\n')
posun = int(input('Zadaj o koľko sa má posunúť šifra:\n'))
sifra = ''

for i in range(len(retazec)):
    print(i, retazec[i])

for i in range(len(retazec)):
    print(i, ord(retazec[i]))

for i in range(len(retazec)):
    print(retazec[i],':',ord(retazec[i]))

for i in range(len(retazec)):
    print(f'{retazec[i]}:{chr(ord(retazec[i]) + posun)}')
    sifra += chr(ord(retazec[i]) + posun)

print(f'Zaodovaný retazec:{sifra}')
