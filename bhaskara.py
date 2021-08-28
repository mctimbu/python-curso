import math
a = float(input('Entre com o valor de a: '))
b = float(input('Entre com o valor de b: '))
c = float(input('Entre com o valor de c: '))

delta = (b ** 2) - 4 * a * c
if a == 0:
    print("O valor de a, deve ser diferente de 0")
elif delta < 0:
    print("Delta deve ser positivo")
else:
    x1 = (-b + math.sqrt(delta)) / 2 * a
    x2 = (-b - math.sqrt(delta)) / 2 * a
    print(x1)
    print(x2)
