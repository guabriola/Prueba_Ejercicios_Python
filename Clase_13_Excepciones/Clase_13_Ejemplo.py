####### EJEMPLO DE EXCEPCION #################
class MiError(Exception):
    def __init__(self, valor, mensaje):
        self.valor_error = valor
        self.mensaje_error = mensaje

    def __str__(self):
        return f"MiError: {self.valor_error} - {self.mensaje_error}"


try:
    entrada = int(input("Ingrese un numero entre 1 y 10: "))
    if entrada > 10:
        raise MiError(entrada, "El número es mayor a 10")
    elif entrada < 1:
        raise MiError(entrada, "El número es menor a 1")
    else:
        print("El numero ingresado es correcto: ", entrada)
except MiError as e:
    # print(f"Error en la entrada. El numero ingresado {e.valor_error} es incorrecto" )
    # print(f"Mensaje de error: {e.mensaje_error}")
    print(e)

#############################################
