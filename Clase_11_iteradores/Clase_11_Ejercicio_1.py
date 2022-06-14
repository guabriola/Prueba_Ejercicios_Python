"""
Ejercicio
●Dado una lista de elementos inicial crear un flujo de generadores que:
–Quite los elementos que no sean del tipo int
–Filtrar y retornar con los enteros pares.
–Convertir los enteros a str
–Filtrar y retornar los str que comiencen con 1.

●Entrada = [1,12,124,"1Hola",[1,2,3],True,33]
●Salida–“12”–“124”

"""
entrada = [1, 12, 22, 124, "1Hola", [1, 2, 3], True, 33]

quitar_elemento = (elemento for elemento in entrada if isinstance(elemento, int))
filtrar_pares = (elemento for elemento in quitar_elemento if elemento % 2 == 0)
convertir_str = (str(elemento) for elemento in filtrar_pares)
comiencen_1 = (elemento for elemento in convertir_str if elemento[0] == '1')

for x in quitar_elemento:
    print(x)

for x in filtrar_pares:
    print(x)

for x in convertir_str:
    print(x)

for x in comiencen_1:
    print(x)
    