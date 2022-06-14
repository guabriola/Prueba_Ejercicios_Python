#### Ejemplos de Diccionario ######

mi_diccionario = {"nombre":"Rodrigo",
                  "edad":34,
                  "gustos":["Futbol","Pasear"],
                  4134512:"Cedula"
                  }

print(mi_diccionario)
print(f"Edad: { mi_diccionario['edad'] }")
mi_diccionario["edad"] = 35
print(f"Edad: { mi_diccionario['edad'] }")
mi_diccionario['nacionalidad'] = "Uruguaya"
print(f"Nacionalidad: {mi_diccionario['nacionalidad']}")

print(f"Todas las claves: {mi_diccionario.keys()}")
print(f"Todas los objetos: {mi_diccionario.values()}")
print(f"Lista de clave,valor: {list(mi_diccionario.items())}")