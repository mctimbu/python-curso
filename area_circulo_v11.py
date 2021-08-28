from math import pi
import sys


class Cores:
    W = '\033[0m'   # white (normal)
    R = '\033[31m'  # red
    G = '\033[32m'  # green
    L = '\033[33m'  # laranja
    B = '\033[34m'  # blue
    P = '\033[35m'  # purple


def circulo(raio):
    return pi * float(raio) ** 2


def help():
    return print(Cores.R, """\n\tTem que colocar o numero ai po sem nada n tem jogo.
\tEx: {} 123.123""".format(sys.argv[0][46:]))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        print(Cores.W)
        sys.exit(1)

    elif not sys.argv[1].isnumeric():
        help()
        print(Cores.R, "\tBota um numero brouuu", Cores.W)
        sys.exit(2)

    raio = sys.argv[1]
    area = circulo(raio)
    print(Cores.G, "Área do circulo é igual a:", Cores.W, area)
    print(dir())
