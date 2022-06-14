"""
Ejercicio 3
–Escribir la función tribonacci. Funciona igual que la función conocida Fibonacci
pero en vez de sumar sus dos números anteriores suma de a tres.
–Entonces si la secuencia comienza con [1, 1, 1] la función sigue: [1, 1 ,1, 3, 5, 9, 17, 31, ...]
–Si comenzamos con [0, 0, 1] entonces sigue con [0, 0, 1, 1, 2, 4, 7, 13, 24, ...]
–Escribir la función tribonacci que tome la secuencia de los primeros tres números de entrada como lista y la cantidad de elementos a mostrar.
–Ejemplo:
●Tribonacci([1, 1, 1], 10))–[1, 1, 1, 3, 5, 9, 17, 31, 57, 105])
●Tribonacci([0, 0, 1], 10)–[0, 0, 1, 1, 2, 4, 7, 13, 24
●Tribonacci([1, 1, 1], 1)) –[1]
●Tribonacci([300, 200, 100], 0))
●[]

"""
#solucion profesor
def tribonacci(entrada: list,n: int) -> list:
    lista_resultado = entrada

    for x in range(n):
        nuevo_numero = entrada[-1] + entrada[-2] + entrada[-3]
        #lista_resultado += [nuevo_numero]
        lista_resultado.append(nuevo_numero)

    return lista_resultado[:n]


print(tribonacci([1, 1, 1], 10))
print(tribonacci([0, 0, 1], 10))
print(tribonacci([1, 1, 1], 1))
print(tribonacci([300, 200, 100], 0))








