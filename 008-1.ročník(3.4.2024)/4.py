veta = input('Napíš vetu:\t')
pocet_samohlasiek = 0

for i in veta:
    if i in 'aAáÁäÄeEéÉiIíÍyYýÝoOóÓuUúÚ':
        pocet_samohlasiek += 1

print(pocet_samohlasiek)
