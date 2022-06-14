#### Función generadora que devuelve un iterador ###########

def cuenta_regresiva(n):
    print("Comienza cuenta regresiva")
    while n > 0:
        yield n # Retorna n y espera a la siguiente llamada.
        n -= 1

for x in cuenta_regresiva(10):
    print(x)

#########################

