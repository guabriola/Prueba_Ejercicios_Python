import math
num = int(input("Introduce un numero entero: "))

def persistencia(num:int) -> int:
    numero = [int(i) for i in str(num)]
    if len(numero) == 1:
        numero_pers = 0
        return numero_pers

    else:
        numero_pers = 0
        for i in numero:

            numero = math.prod(numero)
            numero_pers += 1

        return numero_pers

print(persistencia(num))

