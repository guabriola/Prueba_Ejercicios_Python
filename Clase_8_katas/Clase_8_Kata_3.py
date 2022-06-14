import random
#random.randint(inicial, final)#incluye el final
#random.randrange(inicial, final)#no incluye el final

lista = []
i = 1

while i <= 10000:
        num = random.randint(1, 6)
        i = i + 1
        lista.append(num)

print(lista)

"""
Ejercicios de compañeros
-----------------------
Juan Curto

import random
lista=[]
cuenta=[0,0,0,0,0,0]
for i in range(10000):
    lista.append(random.randint(1,6))
    cuenta[lista[i]-1]+=1
print (cuenta)
promedio=0
for i in range(6):
    promedio+=cuenta[i]*(i+1)

promedio=promedio/10000
print(promedio)

-------------------------------------

Paulo
import random
aleatorios = []
sum = 0
for i in range(0, 10000):
    rnd = random.randint(1, 6)
    aleatorios.append(rnd)
    sum += rnd

for j in range(1, 7):
    print(f"La cantidad de {j} es {aleatorios.count(j)}")

print(f"El promedio es {sum/10000}")

-----------------------------
Santiago
import random
lista=[]
for x in range(0,10000):
    y=random.randint(1,6)
    lista.append(y)
print(lista)
for x in range(1,7):
    print(f"La ocurrencia de {x} en la lista es {lista.count(x)}")
suma=0
for x in lista:
    suma+=x
print(f"El promedio es: {suma/10000}")

----
Federico
import random

def random_frec_list(n):
    list = []
    # Lista de 10000 aleatorios entre 1 y 6
    for i in range (0,n):
        list.append(random.randrange(1,7))

    count = 0
    # Cuento ocurrencias de los números
    for i in range (1,7):
        count = list.count(i)
        print("Nro", i, "Ocurrencias", count)
    
    # Calculo Promedio
    avg = sum(list)/n
    print ("Promedio", avg)

random_frec_list(10000)
"""