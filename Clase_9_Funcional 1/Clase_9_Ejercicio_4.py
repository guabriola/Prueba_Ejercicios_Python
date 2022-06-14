"""
Usar filter para que, dado un string, se devuelva una lista con todas las vocales contenidas en él
"""
import functools

palabra = input(str("Ingrese la palabra para contar vocales: "))


def encuentra_vocales(letra):
    if letra in "aeiou":
        return letra


print(list(filter(encuentra_vocales, palabra)))


"""
*******solucion del profesor**********
def esVocal(letra):
    return letra.lower() in "aeiou"


print(list(filter(esVocal, palabra)))
**************************************
"""


