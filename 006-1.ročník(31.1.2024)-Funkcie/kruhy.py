def kruhy_riadkov(x, y, pocet, r, farba):
    for i in range(pocet):
        kruh(x, y, r, farba)
        x = x + r * 2


def kruhy_stvorec(x, y, pocet, r, farba):
    for i in range(pocet):
        kruhy_riadkov(x, y, pocet, r, farba)
        y - y + r * 2