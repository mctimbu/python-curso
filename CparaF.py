a = str(input('Farenheit para Celsius ou o contrario? Y or N: '))
if a == "N":
    c = int(input('Entre com o valor de c: '))
    F = ((c * 9/5) + 32)
    print(F)
else:
    j = int(input('Entre com o valor de F: '))
    h = (j - 32) * 5/9
    print(h)
