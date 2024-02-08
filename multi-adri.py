numero = int(input("introduce el número del que quieras ver la tabla: "))

for n in range(11):
    calculo = numero*n
    print(f'{numero} x {n} = {calculo}')
