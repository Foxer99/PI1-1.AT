max_bodov = int(input('Zadaj plný počet bodov:\n'))
pocet_bodov = int(input('Zadaj počet bodov\n'))
percenta = (pocet_bodov / max_bodov) * 100
print(f'\n\n\n\nZískal si {round(percenta, 2)} %')

#if percenta >= 90:
#    print('Výborný')
#else:
#    if percenta >= 75:
#       print('Chválitebný')
#    else:
#        if percenta >= 50:
#           print('Dobrý')
#   else:
#         if percenta >= 30:
#              print('Dostatočný')
#           else:
#               print('Nedostatočný')

if percenta >= 90:
        print('Výborný')
elif 75 <= percenta:
        print('Chválitebný')
elif 50 <= percenta:
    print('Dobrý')
elif 30 <= percenta:
    print('Dostatočný')
else:
    print('Nedostatočný')