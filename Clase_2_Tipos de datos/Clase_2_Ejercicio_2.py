
"""
Ejercicio 2. Hacer un programa que:
    a) Calcule el perímetro y área de un rectángulo dado su base y su altura.
    b) Calcule el perímetro y área de un círculo dado su radio (Se puede utilizar math.pi)
"""
import math

###Parte (a)###
"""
#Perímetro
base = int(input("Ingrese la base del rectángulo:"))
altura = int(input("ingrese la altura del rectángulo: "))
perimetro = (base + altura) * 2
print("El perímtro del rectángulo es: ", perimetro)

#Area
area = base * altura
print("El área del rectángulo es: ", area)
"""
###Parte (b)###

#Perímetro
radio = int(input("Ingrese el radio del circulo: "))
per_circulo = 2 * math.pi * radio
print("El perímetro del círculo es: ", per_circulo)

#Area
area_circulo = math.pi * pow(radio,2)
print("El área del circulo es: " , area_circulo)


