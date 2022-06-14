def antes_despues(funcion_original): #Nombre del decorador y como parametro la función original.

    def nueva_funcion(*params): #Nueva función interna la cual vamos a devolver
        print("Hola antes de invocar a la función original")
        funcion_original(*params) # ES LA PARTE MÁS IMPORTENTE EN LA DEFINICIÓN DE DECORADOR
        print("Hola despues de invocar a la función original")

    return nueva_funcion


@antes_despues
def imprimir_saludo():
    print("Hola decoradores")

@antes_despues
def imprimir_saludo_en(mensaje):
    print(f"Hi {mensaje}")

imprimir_saludo()
imprimir_saludo_en("Decoretors con parametro")

#################################