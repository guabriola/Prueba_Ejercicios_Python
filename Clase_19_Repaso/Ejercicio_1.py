"""
Ejercicio 1
Escribir una función que dada una cadena de caracteres divida la cadena en pares.
Si la cadena contiene un número impar de caracteres, debería reemplazar el segundo
carácter faltante del par final con un guión bajo ('_').

Ejemplo:
pares('abc')
retorna ['ab', 'c_']
pares('abcdef')
retorna ['ab', 'cd', 'ef' ]
!!!!!!!!!!!!!!en clase se pide hacerlo con type hints!!!!!!!!!!!
"""


def de_a_par(palabra):
    lista_letras = []
    nueva_palabra = palabra if len(palabra) % 2 == 0 else palabra + "_"
    for i in range(0, len(nueva_palabra), 2):
        lista_letras.append(nueva_palabra[i:i+2])
    return lista_letras


palabra = str(input("Ingrese la palabra a dividir:  "))
print(f"La palabra dividida es: {de_a_par(palabra)}")


#Con type hints
#Hint lo que hace es es recomendar un type - es mas para documentacion del código
# Se ve que se indica que tiene que ingresar str y sale list.

def de_a_par(palabra: str) -> list:
    lista_letras = []
    nueva_palabra = palabra if len(palabra) % 2 == 0 else palabra + "_"
    for i in range(0, len(nueva_palabra), 2):
        lista_letras.append(nueva_palabra[i:i+2])
    return lista_letras


palabra = str(input("Ingrese la palabra a dividir:  "))
print(f"La palabra dividida es: {de_a_par(palabra)}")
