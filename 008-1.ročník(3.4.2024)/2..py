retazec = input('Napis slovo:\n')

#tento sluzi na vypisanie od 0 do nekonecno
for i in range(len(retazec)):
    print(i, retazec[i])

#tieto dva sluzia na vypisanie od 0 do -nekonecno
for i in range(1, len(retazec) + 1):
    print(-i, retazec[-i])

for i in range(-1, -len(retazec)-1, -1):
    print(i, retazec[i])