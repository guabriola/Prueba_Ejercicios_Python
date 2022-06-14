#Utilizando listas por comprensión, generar una lista de
# los primeros 10 números naturales elevados al cuadrado

#Usando una Lista pre definida(hice yo)
Lista = [1,2,3,4,5,6,7,8,9,10]
Lista_R = [x*x for x in Lista]#Lo que esta bien es hacerlo con Range y x**2
print(Lista_R)

#La solucion dada por el prof.
print(list(range(10)))
print([x**2 for x in range(10)])






