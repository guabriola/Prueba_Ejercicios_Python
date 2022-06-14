"""
Ejercicio 4

Escriba una función que tome cualquier lista y la invierta.
Pero ATENCIÓN. No debe devolver una lista nueva sino modificar la que se le pasa por parámetro
¡La lista se debe invertir en su lugar! (no se debe devolver) .
Revisar las funciones de la clase lista que trabajan mismo sobre el objeto.
No se puede utilizar la función reverse de la clase lista ni reversed.
"""


def list_reverse(list):
    largo_lista = len(list)
    while largo_lista > 0:
        list.append(list[largo_lista - 1])
        list.remove(list[largo_lista - 1])
        largo_lista -= 1

#pruebas
list_par = [2, "x", "B", "p"]
print(f"list_par Original: {list_par}")
list_reverse(list_par)
print(f"list_par Invertida: {list_par}")

list_impar = [5, "o", 6, 8, "H"]
print(f"list_impar Original: {list_impar}")
list_reverse(list_impar)
print(f"list_impar Invertida: {list_impar}")

##########Solucion del profe###############
"""
El método pop() elimina y retorna un elemento de una lista.
Hay un parámetro opcional, el índice a ser eliminado de la lista, 
si no se especifica ningún índice, a.pop() elimina y retorna el último elemento de la lista.
"""

print("Solucion del profesor ---->")
def invierte(lista):
    for x in range(0, len(lista)):
        ultimo = lista.pop()
        lista.insert(x, ultimo)
    return lista


print(invierte([1, 2, 3, 4]))