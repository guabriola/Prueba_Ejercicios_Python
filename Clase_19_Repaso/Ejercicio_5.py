"""
Ejercicio 5
Implementar una clase que se llame DefaultList y tenga dos atributos: una lista y un valor predeterminado.
La lista será la lista que corresponde a ese objeto y el valor predeterminado se devolverá cada vez que se llame a un índice de la lista fuera de rango.
En una lista común, cuando queremos acceder a un índice fuera de rango (es decir, i > len (lista) - 1 o i <-len (lista)), se lanza una excepción.
Esta clase debe extender list y para lograr el comportamiento deseado es necesario sobreescribir el método __getitem__(self,index)

"""

#repasar funciones de sobrecarga
# DefaultList
class DefaultList(list):#clase lista es el padre
    def __init__(self, lst, default): #los atributos se declaran en el constructor
        super().__init__(lst)#llama al constructor de la calse padre - en este caso no aporta nada
        self.lst = lst

    self.default = default


def __getitem__(self, index):
    if index < len(self.lst) and index >= -len(self.lst):
        return self.lst[index]
    else:
        return self.default


l = ["hola", 3]
dl = DefaultList(l, -1)

print(dl[0])  # hola
print(dl[2])  # -1


