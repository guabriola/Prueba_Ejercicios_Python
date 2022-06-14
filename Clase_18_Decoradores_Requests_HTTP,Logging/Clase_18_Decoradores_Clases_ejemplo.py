#################################
##########EJEMPLO DE @property ########

class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

    @property
    def nombre(self):
        print("Utilizando el getter de @property")
        return self._nombre

    @nombre.setter
    def nombre(self,valor):
        if valor == "":
            raise ValueError("Nombre vacio")

        self._nombre = valor

nueva_persona = Persona("Rodrigo","Perez")

print(nueva_persona.nombre)
nueva_persona.nombre = "Gonzalo"
print(nueva_persona.nombre)

nueva_persona.nombre = "Rodrigo"
print(nueva_persona.nombre)
#nueva_persona.nombre = ""

############################