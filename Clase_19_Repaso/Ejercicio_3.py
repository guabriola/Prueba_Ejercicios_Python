"""
Ejercicio 3
Escribir dos funciones para cifrar/descifrar un string.
La función cifrar recibe un string y retorna el string cifrado.
La función descifrar recibe el string cifrado y lo devuelve descifrado.
El algoritmo para cifrar/descifrar es el siguiente:
Para cifrar y descifrar precisaremos una clave secreta.
La clave secreta es una palabra que debe estar almacenada en un archivo.
Si el caracter a cifrar se encuentra entre las letras de la clave, se sustituye por su posición dentro de la clave.
Si no, simplemente se deja la letra original.

Supongamos que la palabra claves es MURCIELAGO.
ABECEDARIO cifrado 7B535D7249
Trabajar con todas las palabras (tanto clave como string a cifrar/descifrar) en mayúsculas.
Se puede asumir que en la palabra clave no hay caracteres repetidos y su largo no es mayor que 10.
Tener en cuenta las funciones de Python:
upper,
index,
len,
is_digit
"""

def cifrar(palabra):
    palabra = palabra.upper()
    clave_arch = open("Clave.txt")
    clave = clave_arch.readline()
    pal_cifrada = ""
    for x in palabra:
        if x in clave:
            pal_cifrada += str(clave.index(x))
        else:
            pal_cifrada += x

    return pal_cifrada


def descifrar(pal_cifrada):
    clave_arch = open("Clave.txt")
    clave = clave_arch.readline()
    pal_orig = ""
    for x in pal_cifrada:
        if x.isnumeric():
            pal_orig += clave[int(x)]
        else:
            pal_orig += x
    return pal_orig


palabra = str(input(f"Ingrese palabra a cifrar: "))
palabra_cifrada = cifrar(palabra)
print(f"Palabra {palabra.upper()} Cifrada: {cifrar(palabra)}")
print(f"LA palabra descifrada {descifrar(palabra_cifrada)}")