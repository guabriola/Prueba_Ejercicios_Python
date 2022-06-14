"""

Ejercicio 7
Escribir un programa que tome una lista de strings y devuelva la misma lista,
pero en cada string, debe eliminarse la última letra. Usar listas por comprensión.

"""
lista = ['Fresas', 'Peras', 'Naranjas', 'Sandías', 'Manzanas', 'Kiwis', 'plátanos']


def borra_ultima_letra(lista):
    for palabra in lista:
        z = 0
        for letra in lista[z]:
            palabra = palabra[:-1]
        z = z + 1
    return lista


print(borra_ultima_letra(lista))



palabra = "palabraz"
print(palabra[-1])
palabra = palabra[:-1]
print(palabra)
print(palabra[-1])
