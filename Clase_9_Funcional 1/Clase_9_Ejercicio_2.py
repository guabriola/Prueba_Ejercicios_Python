'''
Ejercicio 2:
Utilizando la función map, escribir una función que dada una lista de palabras retorne una lista de
tuplas donde cada tupla tenga este formato: (palabra, largo de la palabra)
'''
import functools

lista = ['perro', 'gato', 'catalogo', 'chiche', 'abe', 'ace']


def fun_tup(palabra):
    largo_palabra = len(palabra)
    tupla = palabra, largo_palabra
    return tupla


lista_tuplas = list(map(fun_tup, lista))
print(lista_tuplas)


########Solucion Profe##########
"""
lista_palabra = ['hola','como','andannnnn','todos','a']

def tupla_palabra(palabra):
    return (palabra,len(palabra))

 
print(list(map(tupla_palabra,lista_palabra)))
"""