class Punto:

    diminension = 2
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def __add__(self, otro_punto):
        return Punto(self.x + otro_punto.x,self.y + otro_punto.y)


mi_punto0 = Punto(2,5)
mi_punto1 = Punto(5,10)

#Es lo mismo, la sobrecarga del operador + hace que llame internamente a la función __add__
resultado_suma = mi_punto0 + mi_punto1
resultado_suma2 = mi_punto0.__add__(mi_punto1)

print(mi_punto0,mi_punto1)

print(resultado_suma)