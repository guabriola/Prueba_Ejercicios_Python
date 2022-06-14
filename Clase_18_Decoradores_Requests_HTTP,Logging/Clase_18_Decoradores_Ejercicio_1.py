############################

"""
Ejercicio 1
● Escribir un decorador que se llame ejecutar que reciba un parámetro boleano “activo” y cuando se agrega este
  decorador a una función ejecute o no la función decorada.

"""

def ejecutar(activo):
    def inner_decorator(funcion_original):
        def wrapped(*args):
            if activo == True:
                return funcion_original(*args)

        return wrapped
    return inner_decorator


@ejecutar(activo=True)
def func1():
    print('func1')

@ejecutar(False)
def func2():
    print('func2')

func1()
func2()

############################