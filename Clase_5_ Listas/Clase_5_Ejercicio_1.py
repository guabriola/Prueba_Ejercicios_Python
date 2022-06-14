import math
"""
Ejercicios●Ejercicio 1.
Dada una lista de números enteros, escribir una función que:
–a) Devuelva la sumatoria y el promedio de los valores.
–b) Devuelva una lista con el factorial de cada uno de esos números.
"""

"""
Solucion de clase:

"""
lista_numeros = [5,3,67,36,23,6,824]

def ejercicio1a(entrada):
    suma = 0
    for x in entrada:
        suma += x
    promedio = suma / len(entrada)
    return suma, promedio

def ejercicio1b(entrada):
    lista_factoriales = []
    for x in entrada:
        #lista_factoriales.append(math.factorial(x))
        lista_factoriales += [math.factorial(x)]
    return lista_factoriales

resultado = ejercicio1a(lista_numeros)
print(resultado)



