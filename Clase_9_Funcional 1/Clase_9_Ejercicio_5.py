"""
En una biblioteca tenemos la siguiente información acerca de órdenes de compra.
    id      Titulo  y   Autor               Cantidad     Precio
["34587", "Learning Python, Mark Lutz",         4,      40.95],
["98762", "Programming Python, Mark Lutz",      5,      56.80],
["77226", "Head First Python, Paul Barry",      3,      32.95]]


Escribir un programa que retorne una lista con tuplas de 2 elementos.

Cada tupla consiste en el id de la orden (primer elemento) y el precio (de acuerdo a la cantidad).

El precio final debe tener un descuento de 10% en caso de que la orden supere los 100. La información relativa a las ordenes está representada como una lista de listas:


"""
orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95],["98762", "Programming Python, Mark Lutz", 5, 56.80],["77226", "Head First Python, Paul Barry", 3,32.95]]

orden = ["34587", "Learning Python, Mark Lutz", 4, 40.95]

def read_order(orden):
    for i in orden:
        if i[3] < 100:
            precio = i[3] * i[4]
    return precio

print(read_order(orders))







def Tup_Id_Precio():
    pass