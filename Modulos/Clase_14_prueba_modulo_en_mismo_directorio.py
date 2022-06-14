##Una manera de hacerlo##
"""
import mis_funciones_matematicas as Mate #Se le pone =as= para crearle un Alias.

Mate.sumar(7, 5)
Mate.resta(5, 2)
Mate.multi(3, 2)
"""
###Con esto no es necesario llamar al modulo cada vez que se usa###

from mis_funciones_matematicas import sumar, resta, multi #Se puede poner un * y ahi importa  todo
sumar(7, 5)
resta(5, 2)
multi(3, 2)
