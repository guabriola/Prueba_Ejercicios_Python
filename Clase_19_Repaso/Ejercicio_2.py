"""

Ejercicio 2
Crear un método is_uppercase(string) que verifica si el string que se pasó por parámetro esta escrito todo en mayúscula.
is_uppercase("c") == False
is_uppercase("C") == True
is_uppercase("hello I AM DONALD") == False
is_uppercase("HELLO I AM DONALD") == True
is_uppercase("ACSKLDFJSgSKLDFJSKLDFJ") == False
is_uppercase("ACSKLDFJSGSKLDFJSKLDFJ") == True

"""


def is_uppercase(string):
    return string.isupper()

def is_uppercase_2(string: str) ->str:
    #Se hace la palabra en mayusculas
    #se hacer return palabra == palabra en mayusculas
    pass
palabra = input("ingrse palabra: ")
print(is_uppercase(palabra))