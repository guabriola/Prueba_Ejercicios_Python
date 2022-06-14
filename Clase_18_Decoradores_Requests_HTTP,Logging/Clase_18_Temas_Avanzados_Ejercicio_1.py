"""
Ejercicio
Escribir la función potencia_2 que, dado un número natural n como  entrada,
devuelva  una  lista  con  los  números  de  1  a  n elevados al cuadrado.
    ●Definir la función utilizando los Types Hint
    ●Realizar los siguientes casos de prueba:
        *potencia_2(0) == []
        *potencia_2(1) == [1]
        potencia_2(10) == [1, 4, 9, 16, 25, 36, 49, 64, 81]
"""
from unittest import TestCase,main

def potencia_2(n: int) -> list:
    return [elem ** 2 for elem in range(1, n + 1)]

class CasosPrueba(TestCase):

    def test_0(self):
        self.assertEqual(potencia_2(0),[],"Se esperaba []")

    def test_1(self):
        self.assertEqual(potencia_2(1),[1],"Se esperaba [1]")

    def test_10(self):
        self.assertEqual(potencia_2(10),[1, 4, 9, 16, 25, 36, 49, 64, 81],"Se esperaba [1, 4, 9, 16, 25, 36, 49, 64, 81,100]")

if __name__ == '__main__':
    main()






