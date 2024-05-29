fmena = open('Mená.txt', 'r',encoding='utf-8') #otvorí súbor Mená.txt na čítanie (r-čítanie, w-zápis)
#fmena = open('C:/dokumenty/Mená.txt','r')

'''for i in range(4): #nedokážeme vypísať veštky mená bez úpravy
    riadok = fmena.readline()
    print(riadok[:-1]) # [.-1] = vypíše všetky znaky od nultého po predposledný (posledný je \n ktorý nechceme)
'''

while True:
    riadok = fmena.readline()
    if riadok == '':
        break
    print(riadok[:-1])

fmena.close() #zatvoriť súbor je dôležité hlavne pri zápise