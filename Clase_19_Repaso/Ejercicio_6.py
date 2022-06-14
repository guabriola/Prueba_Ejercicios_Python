"""
Ejercicio 6
Se recomienda beber 1 vaso de agua por bebida con alcohol para no tener resaca a la mañana siguiente.
Supongamos que tenemos como entrada los siguiente bebidas en formato string. Devuelva una cadena que
sugiera cuántos vasos de agua debe beber para no tener resaca.
Ejemplos
"1 cerveza" => "1 vaso de agua"
"1 trago, 5 cervezas y 1 copa de vino" => "7 vasos de agua"
Notas
Para simplificar las cosas, consideraremos que cualquier cosa con un número delante es una bebida:
 "1 oso" => "1 vaso de agua" o "1 motosierra y 2 piscinas" => "3 vasos de agua "
El número delante de cada bebida se encuentra en el rango [1; 9]
"""

string = input("escriba cuantos vasos se tomó de cada bebida: ")
vaso_agua = 0

for x in string:
    if x in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
        vaso_agua += int(x)

if vaso_agua == 1:
    print(f"Se tiene que tomar {vaso_agua} vaso de agua")
else:
    print(f"Se tiene que tomar {vaso_agua} vasos de agua")




