"""
Ejercicio 3:
Utilizando la función filter, escribir una función que tenga como entrada una lista de
palabras y un entero n y que retorne una lista con las palabras de largo mayor a n.
"""
import functools

lista_original = ['perro', 'gato', 'catalogo', 'chiche', 'abe', 'ace']
n = int(input("Ingrese un número: "))

def largo_palabra(palabra):
    if len(palabra) > n:
        return palabra


lista_final = list(filter(largo_palabra, lista_original))
print(lista_final)

