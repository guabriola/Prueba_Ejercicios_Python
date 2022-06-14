## Como funciona el slice
## [inicial,final,salto] -- elementos entre inidice inicial hasta el final, sin incluirlo y con salto definido.

entrada = "PYTHON"

print(entrada)
print(entrada[2:4])
print(entrada[2:])
print(entrada[:4])
print(entrada[:]) ## Una nueva colección
print(entrada[2:5:2]) ## Salto de 2.
print(entrada[::-1]) ## Devuelve la colección a la inversa
print(entrada[-2:-4:-1])
print(entrada[:-1])
print(entrada[-1])


#Con type hints
#Hint lo que hace es es recomendar un type - es mas para documentacion del código
# Se ve que se indica que tiene que ingresar str y sale list.

#   def de_a_par(palabra: str) -> list:



"""

Utilizando el modulo datetime y la función datetime.datetime.now(), escribir una función que reciba dos parámetros:

un nombre de archivo (con su ruta relativa incluida) ●un texto.

La función abre el archivo de log indicado por parámetro y guarda en el archivo una línea con un texto indicado por parámetro, incluyendo la hora actual.

Cierra el archivo de log.

"""

from datetime import datetime


def guardar_log(archivo: str, texto:str) -> str:
    with open(archivo,"a") as archivo_log:
        """el 'a' (append) ya crea el archivo"""
        archivo_log.write(f"{texto} - time: {datetime.now()} \n")


guardar_log("archivo.log","Primera Linea")
guardar_log("archivo.log","Error 500")
guardar_log("archivo.log","Fin de ejecución")

