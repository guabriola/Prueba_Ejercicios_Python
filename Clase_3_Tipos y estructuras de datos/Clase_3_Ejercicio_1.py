"""
Ejercicio 1
    – Imprimir todos los números pares y su cuadrado del 0 al 100.
"""
#Primer manera de hacerlo
for x in range(0,101):
    if x % 2 == 0:
        print(x,x**2)
#Segunda manera de hacerlo
for x in range(0,101,2):
    print(x,x**2)
#La segunda manera pero usando fstring
for x in range(0, 101, 2):
    print(f"Valor: {x} y su cuadrado: {x**2}")