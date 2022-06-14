"""
Escribir una función que reciba dos números (ingresados por el usuario) y
a partir de las operaciones especificadas en un archivo (cuyo nombre deberá ser provisto como parámetro),
realice los cálculos y devuelva el resultado final de cada línea (resultado que se obtiene operando los dos números recibidos).
El archivo contendrá por línea una operación aritmética sencilla; por ej:+/**Nota: investigar la función de Python llamada eval.
En caso de producirse un error durante la lectura de una línea del archivo,
se debe lanzar una excepción propia que informe número de línea, operación problemática y motivo del error.
"""
import sys
class Mi_Error(Exception):
    def __init__(self, valor, mensaje):
        self.valor = valor
        self.mensaje = mensaje


    def __str__(self):
        exception_type, exception_object, exception_traceback = sys.exc_info()
        filename = exception_traceback.tb_frame.f_code.co_filename
        line_number = exception_traceback.tb_lineno

        return f"{self.mensaje}({self.valor}) en el archivo {filename} no es válido.\nEl error ocurre en la linea {line_number}" \
               f"\nSe debe ingresar \, +, - ó *"
        #ejemplo

        #print(f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}: {e}")
        #return (repr(self.valor))

def evaluar_operacion(a, b, archivo):
    for i in archivo:
        try:
            operador = i.replace("\n", "")#Acá sacamos el salto de line
            if operador == '+':
                print(f"Resultado de : {a} {operador} {b}  ")
                print(eval(f"{a}{operador}{b}"))
            elif operador == '-':
                print(f"Resultado de : {a} {operador} {b}  ")
                print(eval(f"{a}{operador}{b}"))
            elif operador == '/':
                print(f"Resultado de : {a} {operador} {b}  ")
                print(eval(f"{a}{operador}{b}"))
            elif operador == '*':
                print(f"Resultado de : {a} {operador} {b}  ")
                print(eval(f"{a}{operador}{b}"))
            else:
                print(f"Resultado de : {a} {operador} {b}  ")
                raise Mi_Error(operador, "El operador ")

        except Mi_Error as e:
            print(e)




archivo = open("Archivo_clase_13.txt", "r")
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

evaluar_operacion(a, b, archivo)

####Solucion del Profesor #####
##LA letra no la entendí había que decir cual era la linea del archivo
# y no era encesario que siga procesando.
#En mi solución Tengo que sacar lo del sys y poner un contador para que cuente linea e imprima la linea del archivo

"""
class MiError(Exception):
    def __init__(self,linea,operacion,motivo):
        self.nro_linea = linea
        self.operacion = operacion
        self.motivo = motivo

    def __str__(self):
        return f"Operacion: {self.operacion}, {self.motivo} - linea: {self.nro_linea}"

def evaluar_operacion(x,y,archivo):
    with open(archivo,"r") as archivo_origen:
        #Mostramos como funciona el eval
        eval("print('Ejecutando el eval')")
        nro_linea = 1
        for linea in archivo_origen:
            #Quitamos el salto de linea
            operacion = linea[:-1]
            operacion2 = linea.replace("\n","")
            try:
                print(eval(f"{x}{operacion}{y}"))
            except:
                raise MiError(nro_linea,operacion,"Operacion no valida")
            nro_linea += 1


if __name__ == '__main__':
    print("Ejecutando Excepciones")
    x = input("Ingrese el primer numero: ")
    y = input("Ingrese el segundo numero: ")
    try:
        evaluar_operacion(x,y,"operaciones.txt")
    except MiError as e:
        print(e)
"""