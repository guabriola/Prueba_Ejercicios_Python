"""
- Definir una clase perro que contenga un atributo de clase que especifique el tipo de animal: “Mamifero” y dos atributos del objeto
  que especifique el nombre y la edad.
– Definir el metodo str para que cuando se haga el print de un perro muestre el nombre y la edad del perro.
– Definir el metodo ladrar que imprime el texto correspondiente al ladrido de su perro, pasado por parámetro
– Crear 3 instancias de tipo perro con edades diferentes y retornar el mayor de esos. Para comparar la edad de los perros se debe utilizar los
  operadores > y >=
– Investigar cuál metodo habría que definir en una clase para que cuando se pregunte por el largo (len) de un perro devuelve su edad

"""

class Perro:

    tipo_animal = "Mamifero"

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"El perro se llama  {self.nombre} y tiene  {self.edad} años"

    def ladrar(self, sonido):
        return print(str(sonido))


Perro1 = Perro("Oliver", 2)
Perro2 = Perro("Toto", 5)
Perro3 = Perro("Cata", 8)





################################################################
                ##Solución Profesor ##
################################################################




"""

class Perro:
    tipo_animal = "Mamifero"

    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.nombre} tiene {self.edad} años"

    def ladrar(self,ladrido):
        print(f"{self.nombre} esta ladrando y diciendo {ladrido}")

    def __gt__(self, other):
        return self.edad > other.edad

    def __ge__(self,other):
        return self.edad >= other.edad



lucky = Perro("Lucky",7)
firulais = Perro("Firulais",11)
rambo = Perro("Rambo",4)

if lucky >= firulais:
    print(f"{lucky} es mayor igual que {firulais}")
else:
    print(f"{firulais} es mayor igual que {lucky}")

if lucky > rambo:
    print(f"El mayor es: {lucky}")
else:
    print(f"El mayor es: {firulais}")

print(len(lucky)) # --> 7
print(len(rambo)) # --> 4
print(len(firulais)) # --> 11

######################################

"""


