
"""
Ejercicio
1–Escribir una función que reciba un número n por parámetro e imprima los primeros n números triangulares, junto con su índice.
–Los números triangulares se obtienen mediante la suma de los números naturales desde 1 hasta n. Es decir, si se piden los primeros
5 números triangulares, el programa debe imprimir:
●1 - 1
●2 - 3
●3 - 6
●4 - 10
●5 - 15
"""
n = int (input("Ingrese parámetro: "))

def triangulares(n):
    suma = 0
    for x in range(1,n+1):
        #suma = suma + x
        suma += x
        print(f"{x} - {suma}")

triangulares(n)







