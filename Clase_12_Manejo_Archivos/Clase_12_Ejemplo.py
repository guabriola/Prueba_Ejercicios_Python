####### Picklear objetos #####

import pickle

mi_diccionario = {'bin': 'sis_bin', 'oct': 'sis_oct', 'nombre': 'Rodrigo', 0: 567}
mi_diccionario2 = {'algo': 'mas'}

print(mi_diccionario['bin'])
print(mi_diccionario[0])

with open('data.save', 'wb') as archivo:
    pickle.dump(mi_diccionario, archivo)
    pickle.dump(mi_diccionario2, archivo)

########################

#####Desplickear objetos ########
import pickle

with open('data.save', 'rb') as archivo:
    mi_diccionario = pickle.load(archivo)
    mi_diccionario2 = pickle.load(archivo)
    print(mi_diccionario['bin'])
    print(mi_diccionario[0])
    print(mi_diccionario2['algo'])

########################