"""
Ejercicio 1:
–
    Escribir una funcion, que reciba un archivo y un número n
    e imprima las primeras  n líneas del archivo
"""
linea = input("Ingrese cantidad de lineas: ")
#def leer_archivo(archivo):

archivo = open('nombres.txt', 'r')
for linea in archivo:
    print(archivo.readline())


#print(archivo.read())
#archivo.close()


#leer_archivo(archivo)
















"""
def leer_n_lineas(archivo,n):
    with open(archivo,'r') as archivo:
        for x in range(n):
            print(archivo.readline(),end="")

leer_n_lineas('nombres.txt',3)
"""