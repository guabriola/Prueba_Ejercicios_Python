###EJEMPLOS DE UTILIZACIÓN DE INDICES###########
palabra = "Python"

#Indices positivos
print("##########INDICES POSITIVOS#############")
print("Primera letra: ",palabra[0])
print("Cuarta letra: ",palabra[3])
print("Última letra",palabra[5])
#Funcion len nos devuelve el largo de la colección.
print("Última letra (len)",palabra[len(palabra) - 1])
#IndexError: string index out of range
#print("Fuera de la colección, ",palabra[8])

#Indices negativos
print("##########INDICES NEGATIVOS#############")
print("Primera letra: ",palabra[-6])
print("Cuarta letra: ",palabra[-3])
print("Última letra",palabra[-1])
#Funcion len nos devuelve el largo de la colección.
print("Primera letra (len)",palabra[-len(palabra)])


###EJEMPLOS DE UTILIZACIÓN DE INDICES CON OPERADOR DE CORTE (SLICE)###########
# OPERADOR DE CORTE [INICIO:FINAL:SALTO]
palabra = "Uruguay"

print("Elementos entre posición 1 a 3 sin incluir:", palabra[1:3])
print("Las primeras tres letras: ",palabra[0:3])
print("Las primeras tres letras: ",palabra[0:3])

print("Elementos en la posición pares: ",palabra[0:len(palabra):2])

print("Primer elemento: ",palabra[0])
print("Ultimo elemento: ",palabra[len(palabra]-1)
print("ultio elemento(Indice negativo)",palabra[-1] )
print("Primer elemento: ", palabra[-len(palabra)])