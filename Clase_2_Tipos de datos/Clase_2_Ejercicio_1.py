"""
Ejercicio 1. Escribir un programa que pregunte al usuario:
    a) su nombre, y luego lo salude.
    b) dos números y luego muestre el producto.
"""

nombre = input("Ingrese su nombre: ")
print("Hola", nombre, ". Ya puede ingresar los números a sumar:")
num_1 = int(input("Ingrese primer número:"))
num_2 = int(input("Ingrese segundo número:"))

resultado = num_1 + num_2
print("La suma es: ", resultado)


