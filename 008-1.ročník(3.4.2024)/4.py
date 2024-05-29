veta = input('Napíš vetu:\t')
pocet_samohlasiek = 0
pocet_spoluhlasiek = 0

for i in veta:
    if i in 'aAáÁäÄeEéÉiIíÍyYýÝoOóÓuUúÚ':
        pocet_samohlasiek += 1

for i in veta:
    if i in 'qQwWrŕRŔtTzžZŽpPsšSŠdďDĎfFgGhHjJkKlĺLĹxXcčCČvVbBnňNŇmM':
        pocet_spoluhlasiek += 1

print('\n',pocet_samohlasiek, pocet_spoluhlasiek)
