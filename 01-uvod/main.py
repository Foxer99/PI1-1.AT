print("----------\n|  Ahoj  |\n----------") #print vypisuje text do konzoli (toho dole)

meno = input("AKo sa voláš?\n") #=je príkaz priradenia #príkaz input uloží údaj ktorý napísal do konzoly užívateľ
print(" Ahoj",meno)
#Hocičo v "" je brané ako text #python je netypový jazyk
rok = int(input("Kedy si sa narodil?\n")) #funkcia int() pretypuje text na celé čísla
vek = 2023 - rok
print("Máš", vek, "rokov.")
print("\n\nError :/\n")
#int-integer keď používame čísla
#string - znaky
#""text
#bez ničoho je premenná
#s , kombinujem