from random import randint


def sortear_dado():
    return randint(1, 6)


for x in range(1, 7):
    if x % 2 == 1:
        continue

    if sortear_dado() == x:
        print(f"Acertou  x eh: {x}")
        break
else:
    print(f'''Não acertou o número. x eh: {x}''')
