
"""
Ejercicio 2–Dada una palabra ingresada por el usuario contar cuantas ocurrencias de la letra “a” tiene.
"""

palabra = (input("Ingrese la palabra a escanear: "))
largo = len(palabra)
cantidad = 0
for i in palabra:
    if (i == "a")or(i == "A"):
        cantidad = cantidad + 1

if cantidad == 0:
    print(f"El texto ingresado tiene {cantidad} lestras (a)")
elif cantidad == 1:
    print(f"El texto que ingresó tiene solo {cantidad} letra (a)")
else:
    print(f"El texto que ingresó tiene {cantidad} de letras (a)")
"""
Otra opción vista en clase:

Se puede utilizar count
cantidad = palabra.count("a")
print /f'Cantidad de letras utilizando count {entrada.count("a")}
"""














