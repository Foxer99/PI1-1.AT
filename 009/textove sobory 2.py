fmena = open('mena.txt', 'r',encoding='utf-8')
fpriezviska = open('priezviska.txt', 'r', encoding='utf-8')
fmena_priezviska = open('mena__priezviska.txt', 'w',encoding='utf-8') # 'w' otvorí súbor na zápis ak neexistuje ,tak sa vytvori a ak existuje tak sa zmaže jeho obsah

'''for riadok in fmena:
    print(riadok.strip())
'''

for meno in fmena:
    priezvisko = fpriezviska.readline()
    print(f'{meno.strip()} {priezvisko.strip()}', file=fmena_priezviska) # file= zapisuje do subora ktorý je za nim zadani (konktrétne teraz premenna fmena_priezviska)
    #fmena_priezviska.write(f'{meno.strip()} {priezvisko.strip()}\n')    #toto je druhý spôsob ktorým to môžme zapisovať

fmena.close()
fpriezviska.close()
fmena_priezviska.close()