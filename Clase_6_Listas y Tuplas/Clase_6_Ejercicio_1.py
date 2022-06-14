"""
Ejercicio 1. Escribir una función que reciba una tupla de elementos e indique
si se encuentran ordenados de menor a mayor o no
"""

def ordanado_tupla_v1(entrada):
    if entrada == () or len(entrada) == 1:
        return True
    for indice in range(0,len(entrada)-1): #len(entrada) 3 --> [0,1,2]
        if entrada[indice] > entrada[indice+1]:
            return False
    return True

def ordanado_tupla(entrada):
    return entrada == tuple(sorted(entrada))

mi_tupla1 = (6,10,99)
mi_tupla2 = (6,10,1)
mi_tupla3 = ("a","b","z")
mi_tupla3 = ("a","b","z")
mi_tupla4 = ("a")
mi_tupla5 = ()

print(ordanado_tupla(mi_tupla1))
print(ordanado_tupla(mi_tupla2))
print(ordanado_tupla(mi_tupla3))
print(ordanado_tupla(mi_tupla4))
print(ordanado_tupla(mi_tupla5))