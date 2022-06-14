"""
Ejercicio 2:
– Escribir un programa, que copie todo el contenido de un archivo a otro, de modo que queden exactamente igual.
"""


def copia_archivo(origen,destino):
    with open(origen,'r') as archivo_origen:
        contenido = archivo_origen.read()
        with open(destino,'w') as archivo_destino:
            archivo_destino.write(contenido)

copia_archivo('nombres.txt','nobre_bck.txt')