"""
Ejercicio 2. Dominó.

a) Escribir una función que indique si dos fichas de dominó encajan o no.
Las fichas son recibidas en dos tuplas, por ejemplo: (3,4) y (5,4).b)
Escribir una función que indique si dos fichas de dominó encajan o no.
Las fichas son recibidas en una cadena, por ejemplo: 3-4 2-5. Nota: utilizar
la función split de las cadenas.
"""
from collections import namedtuple
ficha_domino = namedtuple("Ficha", ["izquierdo", "derecho"])

def encajan_fichas(ficha1,ficha2):
    if ficha1.izquierdo == ficha2.izquierdo or ficha1.izquierdo == ficha2.derecho:
        return True
    if ficha1.derecho == ficha2.izquierdo or ficha1.derecho == ficha2.derecho:
        return True
    return False

def encajan_fichas_b(ficha1,ficha2):
    ficha1_tupla = ficha_domino(ficha1.split("-")[0],ficha1.split("-")[1])
    ficha2_tupla = ficha_domino(ficha2.split("-")[0],ficha2.split("-")[1])
    return encajan_fichas(ficha1_tupla,ficha2_tupla)

ficha_1 = ficha_domino(2, 3)
ficha_2 = ficha_domino(3, 4)
ficha_3 = ficha_domino(5, 4)
ficha_4 = ficha_domino(5, 2)

ficha_1 = "2-3"
ficha_2 = "3-4"
ficha_3 = "5-4"
ficha_4 = "5-2"

print(encajan_fichas(ficha_1,ficha_2))
print(encajan_fichas(ficha_1,ficha_3))
print(encajan_fichas(ficha_1,ficha_4))



"""
Hola,


Les paso la solución completa al ejercicio que estuvimos viendo hoy y dado que me corrían del salón no pudimos ver cuál era el problema.


Básicamente, nos faltaba invocar la nueva función que habíamos creado.


rint(encajan_fichas_b(ficha_1,ficha_2))
print(encajan_fichas_b(ficha_1,ficha_3))
print(encajan_fichas_b(ficha_1,ficha_4))

??Va en el adjunto la solución completa, en formato txt para que el correo no bloquee el adjunto.


Cualquier consulta a las órdenes,


Saludos,
"""