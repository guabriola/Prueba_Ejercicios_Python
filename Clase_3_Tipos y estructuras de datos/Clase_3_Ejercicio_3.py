"""
Ejercicio 3–Dada una cadena de caracteres:●Imprima dicha cadena cada dos caracteres.
Ej.: ’recta’ debería imprimir ’rca’
"""

palabra = input("Ingrese la palabra a recortar: ")
print(f"Palabra recortada es: {palabra[::2]}")

"""
##Otra manera vista en clase##
for x in range(0, len(entrada),2)
    print(palabra[x], end = "")
"""