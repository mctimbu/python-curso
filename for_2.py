class Cores:
    W = '\033[0m'   # white (normal)
    G = '\033[32m'  # green


produto = {'Nome': 'Celular X', 'Preço': 777, 'Importado': True, 'Estoque': 80}

for keys in produto:
    print(keys)

for value in produto.values():
    print(value)

for keys, values in produto.items():
    print(Cores.G, keys, '=', values, Cores.W)
