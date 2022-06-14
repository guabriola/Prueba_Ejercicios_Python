"""Ejercicio 2
–Escribir un decorador “timer” que se pueda incluir a cualquier función y que registre cuanto tiempo
demoro en ejecutar la función.
–Utilizar para registrar el tiempo la función default_timer()
●from timeit import default_time

"""

###ACLARAR Duda! de como hacerlo para una función pre-establecida###############
from math import factorial
from timeit import default_timer


def decorador(funcion_original):
    def wrapped(*args):
        hora_comienzo = default_timer()
        funcion_original(*args)
        hora_fin = default_timer()
        print(f"Tiempo de ejecucion de Factorial {hora_fin - hora_comienzo}")
    return wrapped


#hora_comienzo = default_timer()
@decorador
def calculo_factorial(x):
    resultado_factorial = factorial(x)


x = 1000000
calculo_factorial(x)

#hora_fin = default_timer()
#print(f"Tiempo de ejecucion de Factorial {hora_fin - hora_comienzo}")