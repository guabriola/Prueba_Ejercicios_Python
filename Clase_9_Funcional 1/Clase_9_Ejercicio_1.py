'''
Ejercicio 1:

Utilizando la función reduce, escribir una función que tenga como entrada una lista de palabras y retorne la palabra mas larga.
Ídem pero que retorne la menor alfabéticamente
'''

import functools

lista = ['perro', 'gato', 'catalogo', 'chiche', 'abe', 'ace']


def mas_larga(pal_1, pal_2):
    if len(pal_1) > len(pal_2):
        pal_larga = pal_1
    else:
        pal_larga = pal_2
    return pal_larga


def alfa_order(pal_1, pal_2):
    return pal_1 if pal_1 < pal_2 else pal_2


print('La lista completa es: ', lista)
print("La palabra mas larga es: ", functools.reduce(mas_larga, lista))
print("La primer palabra alfabeticamente: ", functools.reduce(alfa_order, lista))
