"""
Manejo de contraseñas
●a) Escribir un programa que contenga una contraseña inventada y que se la pregunte al usuario.
    No permitirá continuar hasta que haya ingresado correctamente.
●b) Modificar el programa anterior para que solamente permita una cantidad fija de intentos.
●c) Modificar el programa anterior para que después de cada intento agregue una pausa cada vez mayor,
    utilizando la función sleep del módulo time.
    –import time
    –time.sleep(secs)
"""
import time
pass_correcta = "password"
intentos = 0

while intentos < 3:
    pass_usuario = input("Ingrese la contraseña: ")
    if pass_correcta == pass_usuario:
        print("Contraseña correcta!")
        intentos = intentos + 1
        break
    else:
        print("Contraseña incorrecta")
        intentos = intentos + 1
        time.sleep(5)
        print(f"Va {intentos} intentos")
        if intentos ==3:
            print("Ud. Superó los tres intentos.")



