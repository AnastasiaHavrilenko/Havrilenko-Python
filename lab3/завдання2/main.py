def povtoru(slovo):
    literu = {}
    spysok = []

    for l in slovo:
        if l in literu:
            literu[l] += 1
        else:
            literu[l] = 1

    for l, kilkist in literu.items():
        if kilkist >= 2:
            spysok.append(l)

    return spysok

slovo = input("Введіть слово: ")
result = povtoru(slovo)

if result:
    print("Повторювані літери в слові:",", ".join(result))
else:
    print("У слові немає повторюваних літер.")
